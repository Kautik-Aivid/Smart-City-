#/bin/bash

cd smart-city-yamls/
echo "---------------------Deploying sensor-info-----------------"
kubectl create configmap sensor-info --from-file=sensor-info.json

echo "----------------------Deploying secrets--------------------"
kubectl create secret generic self-signed-certificate --from-file=./certificate/self.crt --from-file=./certificate/self.key


echo "----------------------Deploying master node yamls----------------------"
kubectl apply -f yaml/PV-PVC/
kubectl apply -f yaml/master/
kubectl apply -f yaml/worker/

cd ../
