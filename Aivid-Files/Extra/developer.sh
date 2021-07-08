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
        "Docker Install.......................... ${opts[1]}" 
        "Kubernetes Install...................... ${opts[2]}" 
        "Docker Scan and Fix..................... ${opts[3]}"
        "Kubernetes Scan and Fix................. ${opts[4]}" 
        "Docker Remove........................... ${opts[5]}" 
        "Kubernetes Remove....................... ${opts[6]}" 
        "Aivid-Docker Images Scan................ ${opts[7]}" 
        "Aivid-Dcoker Images Pull................ ${opts[8]}" 
        "Aivid-Full Uninstall.................... ${opts[9]}" 
        "Aivid-Full Install...................... ${opts[10]}" 
        "Aivid-Full Reinstall.................... ${opts[11]}" 
        "Done")
    select opt in "${options[@]}"
    do
        case $opt in
            "Docker Install.......................... ${opts[1]}")
                choice 1
                break
                ;;
            "Kubernetes Install...................... ${opts[2]}")
                choice 2
                break
                ;;
            "Docker Scan and Fix..................... ${opts[3]}")
                choice 3
                break
                ;;
            "Kubernetes Scan and Fix................. ${opts[4]}")
                choice 4
                break
                ;;
            "Docker Remove........................... ${opts[5]}")
                choice 5
                break
                ;;
            "Kubernetes Remove....................... ${opts[6]}")
                choice 6
                break
                ;;
            "Aivid-Docker Images Scan................ ${opts[7]}")
                choice 7
                break
                ;;
            "Aivid-Dcoker Images Pull................ ${opts[8]}")
                choice 8
                break
                ;;
            "Aivid-Full Uninstall.................... ${opts[9]}")
                choice 9
                break
                ;;
            "Aivid-Full Install...................... ${opts[10]}")
                choice 10
                break
                ;;
            "Aivid-Full Reinstall.................... ${opts[11]}")
                choice 11
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
        printf '%s\n' "-------------------Option 1  - Docker Installing---------------------"
        printf '%s\n'
        printf '%s\n'
sudo apt-get update && apt-get install -y \
  apt-transport-https ca-certificates curl wget tar software-properties-common gnupg2 bridge-utils -y


dpkg -s docker-ce | grep '1.19.1-00'
if [ $? -ne 0 ]; then
    echo "docker package is not installed installing it now....."
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

    sudo add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) \
      stable"

    sudo apt-get update && apt-get install -y \
      docker-ce=5:19.03.11~3-0~ubuntu-$(lsb_release -cs) \
      docker-ce-cli=5:19.03.11~3-0~ubuntu-$(lsb_release -cs) --allow-downgrades
    sudo mkdir -p /etc/systemd/system/docker.service.d

fi
echo "Docker has been installed successfully..........."
sleep 3
sudo cat > /etc/docker/daemon.json <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker


sudo cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sudo sysctl --system
sudo swapoff -a
sudo sed -i.bak '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab

    fi

        if [[ ${opts[2]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "-------------------Option 2 - Kubernetes Installing-------------------"
        printf '%s\n'
        printf '%s\n'
sleep 3
yes | sudo apt-get  update
sudo apt remove firewalld -y
sudo apt-get update && sudo apt-get install -y 
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
sudo apt-get update
sudo apt-get install -qy -y kubelet=1.19.1-00 kubeadm=1.19.1-00 kubectl=1.19.1-00
sudo apt-mark hold kubelet kubeadm kubectl
sudo swapoff -a
sudo sed -i.bak '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
sudo systemctl daemon-reload
sudo systemctl restart kubelet
sudo systemctl enable docker kubelet
echo "successfully verified Prerequisite"
sleep 10


echo "--------------------------------------------initialize master---------------------------"
kill $(lsof -t -i:10259)
ip link set cni0 down
brctl delbr cni0
yes | kubeadm reset 
rm -rf $HOME/.kube
rm -rf $HOME/.kube/config   /etc/cni/net.d
kubeadm init --pod-network-cidr=10.244.0.0/16 
sudo mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
kubectl apply -f https://github.com/coreos/flannel/raw/master/Documentation/kube-flannel.yml
kubectl taint nodes --all node-role.kubernetes.io/master-
    fi

        if [[ ${opts[3]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "------------------Option 3 - Docker Scan and Fixing-------------------"
        printf '%s\n'
        printf '%s\n'
# systemctl status docker 
while true; do
    read -r -p "Do you wish to remove docker from the system? (Y/N): " answer
    case $answer in
        [Yy]* ) 
        docker stop -f  $(docker ps -q)
        docker kill -f $(docker ps -q)
        docker rm  -f $(docker ps -a -q)
        docker rmi -f $(docker images -q); break;;
        [Nn]* ) exit;;
        * ) echo "Please answer Y or N.";;
    esac
done

    fi
        if [[ ${opts[4]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "----------------Option 4 - Kubernetes Scan and Fixing-----------------"
        printf '%s\n'
        printf '%s\n'
ip link delete cni0
yes | kubeadm reset 
rm -rf $HOME/.kube
rm -rf $HOME/.kube/config   /etc/cni/net.d
kubeadm init --pod-network-cidr=10.244.0.0/16 
sudo mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
kubectl apply -f https://github.com/coreos/flannel/raw/master/Documentation/kube-flannel.yml
kubectl taint nodes --all node-role.kubernetes.io/master-

    fi
        if [[ ${opts[5]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "---------------------Option 5 - Docker Removeing---------------------"
        printf '%s\n'
        printf '%s\n'
yes | sudo apt-get purge -y docker-engine docker docker.io docker-ce
yes | sudo apt-get autoremove
sudo rm /etc/apparmor.d/docker
sudo groupdel docker
sudo rm -rf /var/lib/docker /etc/docker 
sudo rm -rf /var/run/docker.sock
yes | sudo apt-get  update 

    fi
        if [[ ${opts[6]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "-----------------Option 6 - Kubernetes Removeing---------------------"
        printf '%s\n'
        printf '%s\n'
yes | kubeadm reset
yes | sudo apt-get purge kubeadm kubectl kubelet kubernetes-cni kube*   
yes | sudo apt-get autoremove  
sudo rm -rf ~/.kube
yes | sudo apt-get  update
    fi
        if [[ ${opts[7]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "----------------Option 7 - Aivid-Docker Images Scaning----------------"
        printf '%s\n'
        printf '%s\n'
    fi
        if [[ ${opts[8]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "----------------Option 8- Aivid-Dcoker Images Pulling----------------"
        printf '%s\n'
        printf '%s\n'
    fi   
        if [[ ${opts[9]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "----------------Option 9- Aivid-Full Uninstall----------------"
        printf '%s\n'
        printf '%s\n'
yes | kubeadm reset
yes | sudo apt-get purge kubeadm kubectl kubelet kubernetes-cni kube*   
yes | sudo apt-get autoremove  
sudo rm -rf ~/.kube
yes | sudo apt-get  update
yes | sudo apt-get purge -y docker-engine docker docker.io docker-ce
yes | sudo apt-get autoremove
sudo rm /etc/apparmor.d/docker
sudo groupdel docker
sudo rm -rf /var/lib/docker /etc/docker 
sudo rm -rf /var/run/docker.sock
yes | sudo apt-get  update 
    fi
        if [[ ${opts[10]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "----------------Option 10- Aivid-Full Install----------------"
        printf '%s\n'
        printf '%s\n'
sudo apt-get update && apt-get install -y \
  apt-transport-https ca-certificates curl wget tar software-properties-common gnupg2 bridge-utils -y


dpkg -s docker-ce | grep '1.19.1-00'
if [ $? -ne 0 ]; then
    echo "docker package is not installed installing it now....."
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

    sudo add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) \
      stable"

    sudo apt-get update && apt-get install -y \
      docker-ce=5:19.03.11~3-0~ubuntu-$(lsb_release -cs) \
      docker-ce-cli=5:19.03.11~3-0~ubuntu-$(lsb_release -cs) --allow-downgrades
    sudo mkdir -p /etc/systemd/system/docker.service.d

fi
echo "Docker has been installed successfully..........."
sleep 3
sudo cat > /etc/docker/daemon.json <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker


sudo cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sudo sysctl --system
sudo swapoff -a
sudo sed -i.bak '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
sleep 3
yes | sudo apt-get  update
sudo apt remove firewalld -y
sudo apt-get update && sudo apt-get install -y 
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
sudo apt-get update
sudo apt-get install -qy -y kubelet=1.19.1-00 kubeadm=1.19.1-00 kubectl=1.19.1-00
sudo apt-mark hold kubelet kubeadm kubectl
sudo swapoff -a
sudo sed -i.bak '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
sudo systemctl daemon-reload
sudo systemctl restart kubelet
sudo systemctl enable docker kubelet
echo "successfully verified Prerequisite"
sleep 10


echo "--------------------------------------------initialize master---------------------------"
kill $(lsof -t -i:10259)
ip link set cni0 down
brctl delbr cni0
yes | kubeadm reset 
rm -rf $HOME/.kube
rm -rf $HOME/.kube/config   /etc/cni/net.d
kubeadm init --pod-network-cidr=10.244.0.0/16 
sudo mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
kubectl apply -f https://github.com/coreos/flannel/raw/master/Documentation/kube-flannel.yml
kubectl taint nodes --all node-role.kubernetes.io/master-

    fi 
        if [[ ${opts[11]} ]]
    then
        printf '%s\n'
        printf '%s\n'
        printf '%s\n' "----------------Option 11- Aivid-Full Reinstall----------------"
        printf '%s\n'
        printf '%s\n'
yes | kubeadm reset
yes | sudo apt-get purge kubeadm kubectl kubelet kubernetes-cni kube*   
yes | sudo apt-get autoremove  
sudo rm -rf ~/.kube
yes | sudo apt-get  update
yes | sudo apt-get purge -y docker-engine docker docker.io docker-ce
yes | sudo apt-get autoremove
sudo rm /etc/apparmor.d/docker
sudo groupdel docker
sudo rm -rf /var/lib/docker /etc/docker 
sudo rm -rf /var/run/docker.sock
yes | sudo apt-get  update 
sudo apt-get update && apt-get install -y \
  apt-transport-https ca-certificates curl wget tar software-properties-common gnupg2 bridge-utils -y


dpkg -s docker-ce | grep '1.19.1-00'
if [ $? -ne 0 ]; then
    echo "docker package is not installed installing it now....."
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

    sudo add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) \
      stable"

    sudo apt-get update && apt-get install -y \
      docker-ce=5:19.03.11~3-0~ubuntu-$(lsb_release -cs) \
      docker-ce-cli=5:19.03.11~3-0~ubuntu-$(lsb_release -cs) --allow-downgrades
    sudo mkdir -p /etc/systemd/system/docker.service.d

fi
echo "Docker has been installed successfully..........."
sleep 3
sudo cat > /etc/docker/daemon.json <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker


sudo cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sudo sysctl --system
sudo swapoff -a
sudo sed -i.bak '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
sleep 3
yes | sudo apt-get  update
sudo apt remove firewalld -y
sudo apt-get update && sudo apt-get install -y 
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
sudo apt-get update
sudo apt-get install -qy -y kubelet=1.19.1-00 kubeadm=1.19.1-00 kubectl=1.19.1-00
sudo apt-mark hold kubelet kubeadm kubectl
sudo swapoff -a
sudo sed -i.bak '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
sudo systemctl daemon-reload
sudo systemctl restart kubelet
sudo systemctl enable docker kubelet
echo "successfully verified Prerequisite"
sleep 10


echo "--------------------------------------------initialize master---------------------------"
kill $(lsof -t -i:10259)
ip link set cni0 down
brctl delbr cni0
yes | kubeadm reset 
rm -rf $HOME/.kube
rm -rf $HOME/.kube/config   /etc/cni/net.d
kubeadm init --pod-network-cidr=10.244.0.0/16 
sudo mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
kubectl apply -f https://github.com/coreos/flannel/raw/master/Documentation/kube-flannel.yml
kubectl taint nodes --all node-role.kubernetes.io/master-
    fi 
done
