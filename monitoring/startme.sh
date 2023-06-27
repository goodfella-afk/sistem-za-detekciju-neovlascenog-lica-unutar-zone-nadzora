#!/bin/bash

killall python3
python3 /opt/frtsys/main/recognition.py &
python3 /opt/frtsys/main/orchestration.py &