#!/bin/bash
# Purpose: Demonstrate usage of select and case with toggleable flags to indicate choices
# 2013-05-10 - Dennis Williamson
ip=$(ip route get 8.8.8.8 | awk -F"src " 'NR==1{split($2,a," ");print a[1]}')
ip1=$(ip addr show enp0s3 | grep "inet\b" | awk '{print $2}' | cut -d. -f1,2,3)
ip2=$(ip addr show enp0s3 | grep "inet\b" | awk '{print $2}' | cut -d/ -f2)
ip_final=($ip1.0/$ip2)
# echo $ip_final
choice () {
    local choice=$1
    if [[ ${opts[choice]} ]] # toggle
    then
        opts[choice]=
    else
        opts[choice]=+
    fi
}

PS3='Please enter your choice: '
while :
do
    clear
    options=(
        "Prerequisite Installation.......................... ${opts[1]}"
        "Hardware Information .......................... ${opts[2]}" 
        "Scan Ip.......................... ${opts[3]}" 
        "Camera Port Scanning...................... ${opts[4]}" 
        "System Port Scanning...................... ${opts[5]}" 
        "Network Port Scanning..................... ${opts[6]}"
        "Aivid-Box Scan............................${opts[7]}"
        "System Kubernetes Vulnerability Scan................. ${opts[8]}" 
        "Network Kubernetes Vulnerability Scan........................... ${opts[9]}" 
        "System Vulnerability Scan....................... ${opts[10]}" 
        "System Cleanup....................... ${opts[11]}" 
        "Done")
    select opt in "${options[@]}"
    do
        case $opt in
            "Prerequisite Installation.......................... ${opts[1]}")
                choice 1
                break
                ;;
            "Hardware Information .......................... ${opts[2]}")
                choice 2
                break
                ;;
            "Scan Ip.......................... ${opts[3]}")
                choice 3
                break
                ;;
            "Camera Port Scanning...................... ${opts[4]}")
                choice 4
                break
                ;;
            "System Port Scanning...................... ${opts[5]}")
                choice 5
                break
                ;;
            "Network Port Scanning..................... ${opts[6]}")
                choice 6
                break
                ;;
            "Aivid-Box Scan............................${opts[7]}")
                choice 7
                break
                ;;
            "System Kubernetes Vulnerability Scan................. ${opts[8]}")
                choice 8
                break
                ;;
            "Network Kubernetes Vulnerability Scan........................... ${opts[9]}")
                choice 9
                break
                ;;
            "System Vulnerability Scan....................... ${opts[10]}")
                choice 10
                break
                ;;
            "System Cleanup....................... ${opts[11]}")
                choice  11
                break
                ;;
            "Done")
                break 2
                ;;
            *) printf '%s\n' 'invalid option';;
        esac
    done
done

printf '%s\n' 'Options chosen:'
for opt in "${!opts[1,2,3,4,5,6,7,8,9,10,11,12]}"
do

        if [[ ${opts[1]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "-------------------Option 1  - Prerequisite Installation ---------------------"
        printf '%s\n'
        printf '%s\n'
yes | sudo apt-get install neofetch
yes | sudo apt-get install inxi
yes | apt-get install lynis
docker run --rm -v `pwd`:/host aquasec/kube-bench install
 
    fi

        if [[ ${opts[2]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "-------------------Option 2  - Hardware Information ---------------------"
        printf '%s\n'
        printf '%s\n'
# ip=$(ip route get 8.8.8.8 | awk -F"src " 'NR==1{split($2,a," ");print a[1]}')
echo "Your Node IP.................................. : $ip"  
echo "$now"      
# yes | sudo apt-get install neofetch
# yes | sudo apt-get install inxi
neofetch 
inxi -F
# sudo fdisk -l | grep /dev/sd
# hwinfo --short --cpu 
# hwinfo --short --netcard
# hwinfo --short --storage
# sudo hwinfo --short --usb --cpu --block
    fi

        if [[ ${opts[3]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "-------------------Option 3 - Scan Ip-------------------"
        printf '%s\n'
        printf '%s\n'
echo "$now"
# for ip in $(seq 1 254); do ping -c 1 -W 1 $ip1.$ip | grep "ttl" | awk '{print $4}' | cut -d: -f1; done > aivid-ip.txt
# for ip in $(seq 1 254); do ping -c 1 -W 1 $ip1.$ip | grep "ttl" | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' ;  done > aivid-ip.txt
for i in {1..254} ;do (ping $ip1.$i -c 1 -w 5  >/dev/null && echo "$ip1.$i" &) ;done > aivid-ip.txt
cat aivid-ip.txt
    fi

        if [[ ${opts[4]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "-------------------Option 4 - Camera Port Scanning-------------------"
        printf '%s\n'
        printf '%s\n'
echo "$now"
# yes | sudo apt-get install nmap 
# nmap -O  $ip
# nmap -sA $ip
# nmap -A $ip

for i in $(cat aivid-ip.txt); do nmap -p 554 $i | awk 'NR%8{printf "%s,",$0;next}{print;}' | grep "open\|filtered" | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'   ; done

        printf '%s\n'
# masscan -p554  $ip1.0/24
# for ip in $(seq 1 254); do ping -c 1 -W 1 $ip1.$ip | grep "ttl" | awk '{print $4}' | cut -d: -f1; done > aivid-ip.txt
# for i in $(cat aivid-ip.txt); do nmap -p 554 $i | awk 'NR%8{printf "%s,",$0;next}{print;}' | grep open\|filtered  | awk '{print $14}' | cut -d, -f1 ; done 
# for i in $(cat aivid-ip.txt); do nmap -p T:85,554 $i | awk 'NR%8{printf "%s,",$0;next}{print;}' | grep open  | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' ; done
# for i in $(cat aivid-ip.txt); do nmap -p T:554  $i | awk 'NR%8{printf "%s,",$0;next}{print;}' | grep open | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' ; done 
# for i in $(cat port.txt); do  grep 554  | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' ; done
# for i in $(cat ip.txt); do nmap -p T:554 $i; done > listport.txt
# for i in $(cat aivid-ip.txt); do nmap -p 554 $i | awk 'NR%8{printf "%s,",$0;next}{print;}' | grep open  | awk '{print $14}' | cut -d, -f1; done 
# for i in $(cat listport.txt); do echo $i | awk '{ printf("%s ", $0) }';  done > port.txt 
        printf '%s\n'

#  for i in $(cat openport.txt); do echo $i | awk '{ printf("%s ", $0) }' ;  done
# for i in $(cat ip.txt); do nmap -p T:554 $i; done
# for i in $(cat openport.txt); do echo $i | awk '{ printf("%s ", $0) }';  done
#  nmap -p T:554,85 $ip_final

    fi
        if [[ ${opts[5]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "-------------------Option 5  - System Port Scanning. ---------------------"
        printf '%s\n'
        printf '%s\n'
echo "$now"
    fi
        if [[ ${opts[6]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "------------------Option 6 - Network Port Scanning-------------------"
        printf '%s\n'
        printf '%s\n'
echo "$now"
for i in $(cat aivid-ip.txt); do  nmap  $i | grep open  | awk '{print $1}' | awk 'NR%8{printf "%s,",$0;next}{print;}';  echo $i ; done 
# for i in $(cat aivid-ip.txt); do nmap  $i ; done
# for i in $(cat ip.txt); do echo $i; done
# for ip in $(seq 1 254); do  ping -c 1 -W 1 $ip1.$ip | grep "ttl" | awk '{print $4}' | cut -d: -f1; done //ip list
#  for ip in $(seq 1 254); do nmap -p T:554,85 $(ping -c 1 -W 1 $ip1.$ip | grep "ttl" | awk '{print $4}' | cut -d: -f1); done

        
# nmap -sP $ip_final
        if [[ ${opts[7]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "-------------------Option 7  - Aivid-Box Scan---------------------"
        printf '%s\n'
        printf '%s\n'
echo "$now"
printf '%s\n' "----------------Master Node-----------------"
for i in $(cat aivid-ip.txt); do nmap -p 6443 $i | awk 'NR%8{printf "%s,",$0;next}{print;}' | grep open | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'   ; done 
printf '%s\n' "----------------Worker Node-----------------"
for i in $(cat aivid-ip.txt); do nmap -p 10250 $i | awk 'NR%8{printf "%s,",$0;next}{print;}' | grep open | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'   ; done
printf '%s\n' "----------------Scanning-----------------"

    fi
    fi
        if [[ ${opts[8]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "----------------Option 8 - Kubernetes Node  Scanning-----------------"
        printf '%s\n'
        printf '%s\n'
echo "$now"
# for i in $(cat aivid-ip.txt); do nmap -p 10250 $i | awk 'NR%8{printf "%s,",$0;next}{print;}' | grep open  | awk '{print $14}' | cut -d, -f1 ; done
printf '%s\n' "----------------Master Node-----------------"
for i in $(cat aivid-ip.txt); do nmap -p 6443 $i | awk 'NR%8{printf "%s,",$0;next}{print;}' | grep open | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'   ; done 
printf '%s\n' "----------------Worker Node-----------------"
for i in $(cat aivid-ip.txt); do nmap -p 10250 $i | awk 'NR%8{printf "%s,",$0;next}{print;}' | grep open | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'   ; done
printf '%s\n' "----------------Scanning-----------------"
# docker run --rm -v `pwd`:/host aquasec/kube-bench install
./kube-bench
    fi
        if [[ ${opts[9]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "---------------------Option 9 - Network Kubernetes Vulnerability Scan---------------------"
# docker run --rm aquasec/kube-hunter --cidr $ip1.0/24
echo "$now"
docker run -it --rm --network host aquasec/kube-hunter
        printf '%s\n'
        printf '%s\n'
    fi
        if [[ ${opts[10]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "-----------------Option 10 - System Vulnerability Scan---------------------"
        printf '%s\n'
        printf '%s\n'
echo "$now"
# yes | apt-get install lynis
lynis audit system
    fi
        if [[ ${opts[11]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "-------------------Option 11 - System Full Cleanup ---------------------"
        printf '%s\n'
        printf '%s\n'
echo "$now"
    fi
done


