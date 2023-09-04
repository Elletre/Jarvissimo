import os
import random
import schedule
import time
from datetime import datetime, timedelta
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, Updater
import pytz

BOT_TOKEN = 'YOUR_BOT_TOKEN'
IMAGE_FOLDER = '~/content/'
TIMEZONE = 'Europe/Moscow'
DEFAULT_POSTS_PER_DAY = 1

bot = Bot(token=BOT_TOKEN)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я бот для постинга изображений. "
                              "Используй /set_settings для настройки параметров.")

def set_settings(update: Update, context: CallbackContext):
    update.message.reply_text("Установите параметры для постинга изображений. "
                              "Используйте команду /set_posts для установки количества постов в день.")

def set_posts(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        update.message.reply_text("Пожалуйста, укажите количество постов в день.")
        return

    try:
        new_posts_per_day = int(context.args[0])
        context.user_data['posts_per_day'] = new_posts_per_day
        update.message.reply_text(f"Количество постов в день установлено на {new_posts_per_day}.")

        # Запланировать посты на случайное время
        schedule_posts(new_posts_per_day)
    except ValueError:
        update.message.reply_text("Неверный формат количества постов. Пожалуйста, укажите целое число.")

def post_image(update: Update):
    image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith('.jpg') or f.endswith('.png')]
    if not image_files:
        print("В папке с изображениями нет файлов.")
        return

    random.shuffle(image_files)
    image_file = image_files[0]

    try:
        bot.send_photo(chat_id=update.message.chat_id, photo=open(os.path.join(IMAGE_FOLDER, image_file), 'rb'))
        print(f"Отправлено изображение: {image_file}")

        new_name = f"posted_{image_file}"
        os.rename(os.path.join(IMAGE_FOLDER, image_file), os.path.join(IMAGE_FOLDER, new_name))
    except Exception as e:
        print(f"Ошибка при отправке изображения: {str(e)}")

def schedule_posts(posts_per_day, update):
    for i in range(posts_per_day):
        tz = pytz.timezone(TIMEZONE)
        now = datetime.now(tz)
        start_time = now.replace(hour=8, minute=0, second=0, microsecond=0)
        end_time = now.replace(hour=20, minute=0, second=0, microsecond=0)
        random_time = None

        while True:
            random_hour = random.randint(start_time.hour, end_time.hour)
            random_minute = random.randint(0, 59)
            random_time = now.replace(hour=random_hour, minute=random_minute, second=0, microsecond=0)

            if start_time <= random_time <= end_time:
                break

        # Запланировать пост на указанное время
        schedule.every().day.at(random_time.strftime('%H:%M')).do(post_image, update)

if __name__ == '__main__':
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('set_settings', set_settings))
    dispatcher.add_handler(CommandHandler('set_posts', set_posts, pass_args=True, pass_user_data=True))

    updater.start_polling()

    while True:
        schedule.run_pending()
        time.sleep(1)
