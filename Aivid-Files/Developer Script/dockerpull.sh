#bin/bash
ip=$(ip route get 8.8.8.8 | awk -F"src " 'NR==1{split($2,a," ");print a[1]}')
ssh-keygen -f "/root/.ssh/known_hosts" -R "192.168.1.95"
sshpass -p 123456  ssh -y -o "StrictHostKeyChecking no"  root@192.168.1.95 "bash /home/aivid/dockerpush.sh  $ip  $1"
