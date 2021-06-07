#!/bin/bash
printf "\n\n\nPrerequisite checking....."
sudo apt-get update && apt-get install -y \
  apt-transport-https ca-certificates curl wget tar software-properties-common gnupg2 -y


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
#kubelet installation
echo "kubernetes installation started............"
sleep 3
sudo apt remove firewalld -y
sudo apt-get update && sudo apt-get install -y 
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
sudo apt-get update
sudo apt-get install -qy -y kubelet=1.19.1-00 kubeadm=1.19.1-00 kubectl=1.19.1-00
sudo apt-mark hold kubelet kubeadm kubect
sudo swapoff -a
sudo sed -i.bak '/ swap / s/^\(.*\)$/#\1/g' /etc/fsta
sudo systemctl daemon-reload
sudo systemctl restart kubelet
sudo systemctl enable docker kubelet
echo "successfully verified Prerequisite"
sleep 5

echo "----------------------------------Java installation started---------------------------"
apt update
apt install openjdk-8-jre -y
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > \
    /etc/apt/sources.list.d/jenkins.list'

mkdir -p /root/jenkins/
sudo cp -rp jenkins/agent.jar /root/jenkins/
