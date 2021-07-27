#!/bin/bash

# @reboot ~/crackhead-bot/start_crackhead_bot.sh >> ~/crackhead-bot/logs.txt 2>&1

cd ~/crackhead-bot/
source ~/crackhead-bot/venv/bin/activate
python main.py

