# New Deployment Steps

- Clone this repo on master and worker nodes.
- Run `aivid-customer-operations-master.sh` on `master` and `aivid-customer-operations-worker.sh` on worker, If workers are more than one, then do same for all worker nodes.
- Once `aivid-customer-operations-master.sh` executed successfully, visit http://<ip-of-master>:8080/ for accessing jenkins.
- Use credentials provided separately to access jenkins.
- In jenkins go to Manage Jenkins--> Configure System--> Scroll down to Jenkins Location and update jenkins URL with your actual IP: http://<ip-of-master>:8080/
- Now Go to Worker node and verify `aivid-customer-operations-worker.sh` exucted successfully or not ?
- If yes then hit Jenkins URL http://<ip-of-master>:8080/ and go to Manage Jenkins--> Manage Nodes and Clouds--> Click on worker01 --> Configure--> Replace name of whatever you want to give --> scroll down and update labels with same name--> Scroll down to Node properties and Updated PATH in Environment Variables with the actual path or your worker node. by runnin `echo $PATH`. --> Once done save.
- Now it will be populated with one long command along with Jenkins URL and secret token, Copy that command and open terminal in `worker` node and go to cd `/root/jenkins/` and paste that command also append `&` in last of that command, and enter to execute that command.
- It will connect this `worker` node with jenkins `master`, Once command successfully executed it will show status **connected** on jenkins master `http://<ip-of-master>:8080/computer/<node-name>/` 
- Now `master` and `worker` node are connected, So let's exeucte pipeline to join that node to `kubernetes` master.
- Import Postman collection from this repo path `jenkins/Jenkins.postman_collection.json` to postman.
- Go to Jenkins dashboard and click on `k8s-join-node` or hit URL:`http://<ip-of-master>:8080/job/k8s-join-node/` to check logs of running job.
- Hit POST from postman collection with `k8s-join-node` name, by replacing your `node-name`(which should be exact label name you give in jenkins), `jenkins-URL` and other details.
- Once you hit POST you will able to see job running on `http://<ip-of-master>:8080/job/k8s-join-node/` check logs by clicking on progress bar in corner.
- Once it's succeeded, You will able to see new node joined to cluster by running `kubectl get nodes` the once without `master` is your `worker-node`.
- Now next part it after successful execution of `k8s-join-node` , We will install/deploy `aivid-worker-components` to cluster.
- Go to Postman Collection and open request `Install-aivid-worker-components` replace required details as per your environment like `ip` and `node` name, **Note that** here you must have to give `ip` address of worker node where you want to install `aivid-worker-components`, but `node` name you can give anything not compulsory to give same name you have used in `jenkins` but recommanded to give same name everywhere.
- Hit the Postman URL and you will able to see Job will start executing on Jenkins URL `http://<ip-of-master>:8080/job/Install-aivid-worker-components/` once it's successful you will able to see `aivid-worker-components` would be installed successfully.
- To verify you can run `kubectl get pods` and `kubectl get pods -n ui` from terminal of `master` node.
- That's it, Cheers. feel free to ping.


# Deployment Scripts
Basic Structure\
+---jenkins\
|&emsp;&emsp;&emsp;    +---install\
|&emsp;&emsp;&emsp;   +---jenkinsfile\
|&emsp;&emsp;&emsp;   +---jenkins_workspace\
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;       +---jenkins\
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;           +--- Custom workspace files\
+---kubernetes\
|&emsp;&emsp;&emsp;   +---app\
|&emsp;&emsp;&emsp;   +---central_location\
|&emsp;&emsp;&emsp;   +---common\
|&emsp;&emsp;&emsp;   +---office_location_master\
|&emsp;&emsp;&emsp;   +---office_location_worker\
|&emsp;&emsp;&emsp;   +---storage\
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;       +---app\
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;       \---volumes\
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;           +---pv\
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;           +---pvc\
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;           \---storageclass\
+---load_balancer\
|&emsp;&emsp;&emsp;   +---install.sh\
|&emsp;&emsp;&emsp;   +---nginx.conf\
+---setup.sh
## Platform Overview


![alt text](https://github.com/AIVID-TECHVISION/deployment_script/blob/main/platform.png?raw=true)


## Jenkins Build Process


![alt text](https://github.com/AIVID-TECHVISION/deployment_script/blob/main/jenkins/Jenkins_Build_Process.png?raw=true)


## Jenkins API Endpoints 


http://<Jenkins_IP/DNS>:<Jenkins_Port>/job/<Job_Name>/build   ---    Initate a build process   ---    Returns the queue number\
http://<Jenkins_IP/DNS>:<Jenkins_Port>/job/<Job_Name>/lastBuild/api/json   ---   Get Information regarding last build happened\
http://<Jenkins_IP/DNS>:<Jenkins_Port>/queue/item/<Queue_Number>/api/json?pretty=true    ---   Get the Build number to check the bulid process status   --- Returns the Build Number\
http://<Jenkins_IP/DNS>:<Jenkins_Port>/job/<Job_Name>/<Build_Number>/api/json   ---   Returns the Staus and information regarding the Build\
http://<Jenkins_IP/DNS>:<Jenkins_Port>/job/<Job_Name>/<Build_Number>/consoleText   --- Returns Actual Console OutPut of the build using the Build Number\


