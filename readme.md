Telegram Image Posting Bot
This Telegram bot is designed to automatically post images from a specified folder on your disk at random times during the day. The bot can also be configured to set the number of posts per day and avoid posting during the night hours, taking into account your specified timezone.

Features
Post images from a designated folder to your Telegram chat.
Set the number of posts per day.
Avoid posting during night hours based on your timezone.
Choose a random time for each post.
Rename files to prevent reposts.
Requirements
Python 3.x
python-telegram-bot library
schedule library
pytz library
You can install the required libraries using pip:

```bash
pip install python-telegram-bot schedule pytz
```

Setup
Clone this repository:
```bash
git clone https://github.com/Elletre/Jarvissimo.git
```

Replace 'YOUR_BOT_TOKEN' with your Telegram bot token in the Python script.

Configure the IMAGE_FOLDER variable to specify the path to the folder containing your images.

Run the bot:

```bash
python Jarvissimo.py
```

Usage
Start a chat with your bot and send the /start command.

Use the /set_posts command followed by the desired number of posts per day to configure the bot. For example:

```
/set_posts 3
```

The bot will schedule posts at random times during the day, avoiding night hours based on your timezone.

The bot will rename posted images to prevent reposts.

Customization
You can customize the bot further by modifying the Python script. For example, you can change the default timezone, time range, or other settings according to your preferences.

Contributing
If you have suggestions or improvements for this bot, feel free to fork the repository and submit a pull request. Your contributions are welcome!





