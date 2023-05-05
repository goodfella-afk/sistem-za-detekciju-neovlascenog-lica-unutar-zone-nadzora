ps -aux | grep -v grep | grep recognition.py | tee /home/bigfella/Desktop/v4/monitoring/recognition;
ps -aux | grep -v grep | grep orchestration.py | tee /home/bigfella/Desktop/v4/monitoring/logalert;
python3 /home/bigfella/Desktop/v4/monitoring/kameratest.py
