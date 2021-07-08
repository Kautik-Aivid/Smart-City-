#!/bin/bash
echo "Welcome To Aivid Script"
echo
echo "Select an option:"
echo "   1) Install App "
echo "   2) Troubleshoot"
echo "   3) Remove App"
echo "   4) Check Docker Images Availability"
echo "   5) Docker Pull from server"
read -p "Option: " option
until [[ "$option" =~ ^[1-5]$ ]]; do
    echo "$option: invalid selection."
    read -p "Option: " option
done
case "$option" in
    1)
        echo
            echo "Select an option:"
            echo "   1) Docker "
            echo "   2) Kubernetes"
            echo "   3) Python"
            echo "   4) Jenkins"
        exit
    ;;
    2)
            echo
            echo "Select an option:"
            echo "   1) Docker Fix "
            echo "   2) Kubernetes Fix"
            exit
    ;;
    3)
            echo
            echo "Select an option:"
            echo "   1) Kubernetes "
            echo "   2) Docker"
            echo "   3) Jenkins"
            exit
    ;;
    4)
            echo
            echo "Select an option:"
            echo "   1) Docker Verify "
            exit
    ;;
    5)
            echo
            echo "Select an option:"
            echo "   1) Docker Pull "
            exit
    ;;
esac
