#!/bin/bash

# @reboot ~/crackhead-bot/start_crackhead_bot.sh >> ~/crackhead-bot/logs.txt 2>&1
#* * * * *  /bin/sh -c 'cd ~/crackhead-bot; git pull -q' >> ~/crackhead-bot/logs.txt 2>&1

sleep 10
cd ~/crackhead-bot/
source ~/crackhead-bot/venv/bin/activate
python main.py

