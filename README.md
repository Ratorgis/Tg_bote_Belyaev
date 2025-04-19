# Tg-bote-Belyaev
Creating a telegram bot in python using the aiogram library to create an interactive biography of a historical figure

## Quickstart
1. It is necessary to install all modules from requirements for correct launch
```shell
pip install -r requirements.txt
```
2. We write the token to the .env file, which will be read thanks to the already installed dotenv module. The token is needed to connect to the Telegram API, you can get it from the official bot [@BotFather](https://t.me/BotFather)
```shell
touch .env
echo 'Token = '<token>'' > .env
```
3. Direct launch of the bot
```shell
python3 ./Bote/main.py
```

