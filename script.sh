# https://www.howtogeek.com/121241/how-to-make-your-linux-pc-wake-from-sleep-automatically/
#sudo rtcwake -m no -s 30
#sudo rtcwake -m mem --date 202206032302
sudo rtcwake -m mem -l -t "$(date -d 'tomorrow 05:45' '+%s')"
#sudo rtcwake -m no -l -t $(date +%s -d 'tomorrow 10:00')
#!/usr/bin/expect
sleep 10s

python3 automation.py
