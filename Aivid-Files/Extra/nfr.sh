#!/bin/bash
# Purpose: Demonstrate usage of select and case with toggleable flags to indicate choices
# 2013-05-10 - Dennis Williamson

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
        "Health Check Up.......................... ${opts[1]}" 
        "Check System Vulnerability...................... ${opts[2]}" 
        "Check Kubernetes Vulnerbility..................... ${opts[3]}"
        "Check Database And Operatonal Port................. ${opts[4]}" 
        "Check System health Score (0/10)........................... ${opts[5]}" 
        "Improve System Health....................... ${opts[6]}"  
        "Done")
    select opt in "${options[@]}"
    do
        case $opt in
            "Health Check Up.......................... ${opts[1]}")
                choice 1
                break
                ;;
            "Check System Vulnerability...................... ${opts[2]}")
                choice 2
                break
                ;;
            "Check Kubernetes Vulnerbility..................... ${opts[3]}")
                choice 3
                break
                ;;
            "Check Database And Operatonal Port................. ${opts[4]}")
                choice 4
                break
                ;;
            "Check System health Score (0/10)........................... ${opts[5]}")
                choice 5
                break
                ;;
            "Improve System Health....................... ${opts[6]}")
                choice 6
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
for opt in "${!opts[1,2,3,4,5,6,7]}"
do
    if [[ ${opts[1]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "-------------------Option 1  - Health Check Up---------------------"
        printf '%s\n'
        printf '%s\n'
yes | sudo apt-get install neofetch
neofetch  
sudo fdisk -l | grep /dev/sd
hwinfo --short --cpu 
hwinfo --short --netcard
hwinfo --short --storage
sudo hwinfo --short --usb --cpu --block

    fi

        if [[ ${opts[2]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "-------------------Option 2 - Check System Vulnerability-------------------"
        printf '%s\n'
        printf '%s\n'
docker run -it projectdiscovery/naabu -nmap 192.168.1.1 > aivid.txt
    fi

        if [[ ${opts[3]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "------------------Option 3 - Check Kubernetes Vulnerbility-------------------"
        printf '%s\n'
        printf '%s\n'
    fi
        if [[ ${opts[4]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "----------------Option 4 - Check Database And Operatonal Port-----------------"
        printf '%s\n'
        printf '%s\n'
    fi
        if [[ ${opts[5]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "---------------------Option 5 - Check System health Score (0/10)---------------------"
        printf '%s\n'
        printf '%s\n'
    fi
        if [[ ${opts[6]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "-----------------Option 6 - Improve System Health---------------------"
        printf '%s\n'
        printf '%s\n'
    fi
done

