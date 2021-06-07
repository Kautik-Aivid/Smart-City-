#!/bin/bash
# printf "\n\n\nPrerequisite checking....."

# chattr -i /etc/gshadow
# chattr -i /etc/group
# chattr -ai /etc/shadow
# chattr -ai /etc/passwd

# sudo apt-get update && apt-get install -y \
#   apt-transport-https ca-certificates curl wget tar software-properties-common gnupg2 -y


# dpkg -s docker-ce | grep '1.19.1-00'
# if [ $? -ne 0 ]; then
#     echo "docker package is not installed installing it now....."
#     curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

#     sudo add-apt-repository \
#       "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
#       $(lsb_release -cs) \
#       stable"

#     sudo apt-get update && apt-get install -y \
#       docker-ce=5:19.03.11~3-0~ubuntu-$(lsb_release -cs) \
#       docker-ce-cli=5:19.03.11~3-0~ubuntu-$(lsb_release -cs) --allow-downgrades
#     sudo mkdir -p /etc/systemd/system/docker.service.d

# fi
# echo "Docker has been installed successfully..........."
# sleep 3
# sudo cat > /etc/docker/daemon.json <<EOF
# {
#   "exec-opts": ["native.cgroupdriver=systemd"],
#   "log-driver": "json-file",
#   "log-opts": {
#     "max-size": "100m"
#   },
#   "storage-driver": "overlay2"
# }
# EOF
# sudo systemctl daemon-reload
# sudo systemctl restart docker


# sudo cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
# net.bridge.bridge-nf-call-ip6tables = 1
# net.bridge.bridge-nf-call-iptables = 1
# EOF
# sudo sysctl --system
# sudo swapoff -a
# sudo sed -i.bak '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
# #kubelet installation
# echo "kubernetes installation started............"
# sleep 3

# sudo apt remove firewalld -y
# sudo apt-get update && sudo apt-get install -y 
# curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
# sudo cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
# deb https://apt.kubernetes.io/ kubernetes-xenial main
# EOF
# sudo apt-get update
# sudo apt-get install -qy -y kubelet=1.19.1-00 kubeadm=1.19.1-00 kubectl=1.19.1-00
# sudo apt-mark hold kubelet kubeadm kubectl
# sudo swapoff -a
# sudo sed -i.bak '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
# sudo systemctl daemon-reload
# sudo systemctl restart kubelet
# sudo systemctl enable docker kubelet
# echo "successfully verified Prerequisite"
# sleep 5

echo "--------------------------------------------initialize master---------------------------"

printf "\n\n\nThe Master is being configured, Kindly wait...   " &sleep 10 &
PID=$!
i=1
sp="/-\|"
echo -n ' '
while [ -d /proc/$PID ]
do
  printf "\b${sp:i++%${#sp}:1}"
done
yes | kubeadm reset
iptables -F && iptables -t nat -F && iptables -t mangle -F && iptables -X
kubeadm init --pod-network-cidr=10.244.0.0/16
printf "\n\n\n The Master is being ready, Kindly wait...   " &sleep 5 &
PID=$!
i=1
sp="/-\|"
echo -n ' '
while [ -d /proc/$PID ]
do
  printf "\b${sp:i++%${#sp}:1}"
done
rm -rf $HOME/.kube
sudo mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
printf "\n\n\nThe Master is being ready, Kindly wait...   " &sleep 5 &
PID=$!
i=1
sp="/-\|"
echo -n ' '
while [ -d /proc/$PID ]
do
  printf "\b${sp:i++%${#sp}:1}"
done
# kubectl apply -f kubernetes/system/kube-flannel.yml
kubectl apply -f https://github.com/coreos/flannel/raw/master/Documentation/kube-flannel.yml
kubectl taint nodes --all node-role.kubernetes.io/master-
printf "\n\n\nThe Master is being ready, Kindly wait...   " &sleep 60 &
PID=$!
i=1
sp="/-\|"
echo -n ' '
while [ -d /proc/$PID ]
do
  printf "\b${sp:i++%${#sp}:1}"
done



master_node=`kubectl get nodes | grep master | awk '{print $1}'`
kubectl label nodes $master_node workload=master


echo "------------------------Installation of aivid master components--------------------------"
# kubectl create ns ui
# kubectl apply -f kubernetes/db/ -n ui
# kubectl create cm kube-config --from-file=$HOME/.kube/config -n ui
#kubectl delete secret aividtechvision
kubectl create secret docker-registry aividtechvision  --docker-username=aividtechvision --docker-password=aivid123vision --docker-email=geo.antony@aividtechvision.com
# kubectl apply -f kubernetes/portal -n ui
#kubectl apply -f kubernetes/app/master/
bash smart-city-yamls/deploy-smart-city.sh
sleep 10
# kubectl get pods -n ui
kubectl get pods

# echo "----------------------------------Jenkins installation started---------------------------"
# apt update
# apt install openjdk-8-jre -y
# wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
# sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > \
#     /etc/apt/sources.list.d/jenkins.list'
# sudo apt-get update
# sudo apt-get install jenkins -y
# sudo systemctl stop jenkins
# sudo cp jenkins/jenkins  /etc/default/jenkins
# sudo rm -rf /var/lib/jenkins
# sudo cp -r jenkins/jenkins_workspace/jenkins /var/lib/jenkins
# systemctl restart jenkins