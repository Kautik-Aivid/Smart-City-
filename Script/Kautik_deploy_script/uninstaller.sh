systemctl stop jenkins 
yes | kubeadm reset
yes | sudo apt-get purge kubeadm kubectl kubelet kubernetes-cni kube*   
yes | sudo apt-get autoremove  
sudo rm -rf ~/.kube
yes | sudo apt-get purge -y docker-engine docker docker.io docker-ce  
yes | sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce  
yes | sudo rm -rf /var/lib/docker /etc/docker
sudo rm /etc/apparmor.d/docker
sudo groupdel docker
sudo rm -rf /var/run/docker.sock
yes | apt update
yes | sudo apt-get purge oracle-java8-installer 
yes | sudo apt-get purge  openjdk-8-jre 
yes | sudo apt-get purge  jenkins
sudo rm -rf /var/lib/jenkin 
sudo rm -rf   /etc/default/jenkins 
docker stop $(docker ps -q)
docker kill $(docker ps -q)
docker rm  $(docker ps -a -q)
docker rmi  $(docker images -q) 
yes | sudo apt-get autoremove 
sudo rm -rf /var/lib/docker /etc/docker 
sudo rm /etc/apparmor.d/docker 
sudo rm /etc/apparmor.d/docker 
sudo rm -rf /var/run/docker.sock 
sudo groupdel docker 
yes | sudo apt-get purge -y docker-engine docker docker.io docker-ce
yes | sudo apt-get autoremove
yes | sudo apt-get  update
echo !!
