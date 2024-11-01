@echo on

call %~dp0parse_bot_try_1\venv\Scripts\activate

cd %~dp0parse_bot_try_1

set TOKEN=YourToken

python tg_bot.py

pause