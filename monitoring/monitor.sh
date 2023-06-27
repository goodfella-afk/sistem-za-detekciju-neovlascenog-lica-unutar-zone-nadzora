#!/bin/bash

ps -aux | grep -v grep | grep recognition.py | tee /opt/frtsys/monitoring/recognitionlog;
ps -aux | grep -v grep | grep orchestration.py | tee /opt/frtsys/monitoring/orchlog;
python3 /opt/frtsys/monitoring/kameratest.py
