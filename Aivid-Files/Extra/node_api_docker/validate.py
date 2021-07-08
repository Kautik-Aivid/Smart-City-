from flask import Flask,request, jsonify
from onvif import ONVIFCamera
from getmac import get_mac_address
import netifaces
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["JSON_SORT_KEYS"] = False

class ValidateData:
    
    def __init__(self):
        self.items = request.get_json()


    def check(self):
        
        missing_flag = False
        format_flag = False
        items = self.items

        if len(items) == 0:
            missing_flag = True

            status_code = 101
            error = "Mandatory fields are missing"
        
        init_passCode = ["botconfigs ", "passCodes"]
        
        if missing_flag == False:
            cnt = 0
            try:
                sensors = items["sensor"]
                cnt += 1
                passcodes = items["passCode"]
            except:
                missing_flag = True
            if missing_flag == True:
                status_code = 101
                error = str(init_passCode[cnt])+"are missing!"
                
        # if missing_flag == False:
        #     sensors = items["sensor"]
        #     passcodes = items["passCode"]
        #     if len(sensors) == len(passcodes):
        #         missing_flag = False
        #     else:
        #         missing_flag = True
        #     if missing_flag == True:
        #         status_code = 101
        #         error = "Total number of Sensors and Passcodes should be same"

        required_vlaues = ["name","mode", "type","address",
                        "location","ip","siteId","nodeId",
                        "httpPort","rtspPort"]
        
        if missing_flag == False:
            try:
                cam = 0
                for sensor in sensors:
                    cam += 1
                    cnt = 0
                    name = sensor["name"]
                    cnt +=1 
                    mode = sensor["mode"]
                    cnt +=1
                    Type = sensor["type"]
                    cnt +=1
                    address = sensor["address"]
                    cnt +=1
                    location = sensor["location"]
                    cnt +=1
                    ip = sensor["ip"]
                    cnt +=1
                    siteId = sensor['siteId']
                    cnt +=1
                    nodeId = sensor['nodeId']
                    cnt +=1
                    httpPort = sensor["httpPort"]
                    cnt +=1
                    rtspPort = sensor["rtspPort"]
                  
            except:
                missing_flag = True

            if missing_flag == True:
                status_code = 101
                error = str(required_vlaues[cnt])+" is missing of "+str(cam)+" Sensor"
        
        required_vlaues = ["name","mode", "Type","address","siteId","nodeId","httpPort","rtspPort"]


        if missing_flag == False:
            cam = 0
            for sensor in sensors:
                cam += 1
                cnt = 0
                if type(sensor["name"]) == str:
                    cnt +=1
                    if type(sensor["mode"]) == int:
                        cnt += 1
                        if type(sensor["type"]) == int:
                            cnt += 1
                            if type(sensor["address"]) == str: 
                                cnt +=1
                                if type(sensor["siteId"]) == str:
                                    cnt += 1
                                    if type(sensor["nodeId"]) == str:
                                        cnt += 1
                                        if type(sensor["httpPort"]) == int:
                                            cnt += 1
                                            if type(sensor["rtspPort"]) == int:
                                                format_flag = False
                                            else:
                                                format_flag = True
                                        else:
                                            format_flag = True
                                    else:
                                        format_flag = True
                                else:
                                    format_flag = True
                            else:
                                format_flag = True
                        else:
                            format_flag = True
                    else:
                        format_flag = True
                else:
                    format_flag = True

                if missing_flag == False and format_flag == True:
                    status_code = 106
                    error = "Sensor:"+str(cam)+" " +str(required_vlaues[cnt])+" is Invalid"
                    break

        required_vlaues = ["name", "address","siteId","nodeId"]
        if missing_flag == False and format_flag == False:
            cam = 0
            for sensor in sensors:
                cam += 1
                cnt = 0
                if len(sensor["name"]) != 0:
                    cnt +=1
                    if len(sensor["address"]) != 0: 
                        cnt +=1
                        if len(sensor["siteId"]) != 0:
                            cnt += 1
                            if len(sensor["nodeId"]) != 0:
                                    format_flag = False
                            else:
                                format_flag = True
                        else:
                            format_flag = True
                    else:
                        format_flag = True
                else:
                    format_flag = True

                if missing_flag == False and format_flag == True:
                    status_code = 101
                    error = "Sensor:"+str(cam)+" " +str(required_vlaues[cnt])+" is Missing"
                    break
        




        if missing_flag == False and format_flag == False:
            try:
                cam = 0
                for passcode in passcodes:
                    cam += 1
                    cnt = 0
                    userName = passcode["userName"]
                    cnt +=1
                    password = passcode["password"]
            except:
                missing_flag = True

            if missing_flag == True:
                status_code = 101
                error = str(required_vlaues[cnt])+" is missing of passcodes "+str(cam)
        
        required_vlaues = ["userName","password"]


        if missing_flag == False and format_flag == False:
            cam = 0
            for passcode in passcodes:
                cam += 1
                cnt = 0
               
                if type(passcode["userName"]) == str:
                    cnt += 1
                    if type(passcode["password"]) == str:
                        format_flag = False
                    else:
                        format_flag = True
                else:
                    format_flag = True

                if missing_flag == False and format_flag == True:
                    status_code = 106
                    error = "passcodes:"+str(cam)+" " +str(required_vlaues[cnt])+" is Invalid"
                    break

        required_vlaues = ["userName","password"]
        if missing_flag == False and format_flag == False:
            cam = 0
            for passcode in passcodes:
                cam += 1
                cnt = 0 
                if len(passcode["userName"]) != 0:
                    cnt += 1
                    if len(passcode["password"]) !=0:
                        format_flag = False
                    else:
                        format_flag = True
                else:
                    format_flag = True

                if missing_flag == False and format_flag == True:
                    status_code = 101
                    error = "passcodes:"+str(cam)+" " +str(required_vlaues[cnt])+" is Missing"
                    break
                
        if missing_flag == False and format_flag == False:
            cam = 0
            for sensor in sensors:
                cam +=1
                loc = sensor["location"]
                if type(loc) == list and len(loc) == 2:
                    format_flag = False 
                else:
                    format_flag = True
                    break
                if format_flag == False:
                    lcs = sensor["location"]
                    for lc in lcs:
                        try:
                            check_lc = int(lc)
                        except:
                            format_flag = True
                            break
                    if format_flag == True:
                        break

            if format_flag == True:
                status_code = 106
                error = "Sensor:"+str(cam)+" location is Invalid"
                
            
        if missing_flag == False and format_flag == False:
            cam = 0
            for sensor in sensors:
                cam +=1
                ip_ad = sensor['ip']
                if type(ip) == str and len(ip) != 0:
                    format_flag = False
                else:
                    format_flag = True
                    break
                if format_flag == False:
                    ip_ad_cnt = ip_ad.count(".")
                    if ip_ad_cnt == 3:
                        format_flag = False
                    else:
                        format_flag = True
                        break
                if format_flag == False:
                    ip_ad_split = ip_ad.split(".")
                    for ad in ip_ad_split:
                        try:
                            check_ip = int(ad)
                        except:
                            format_flag = True
                            break
                    if format_flag == True:
                        break
            
            if format_flag == True:
                status_code = 106
                error = "Sensor:"+str(cam)+" ip address Invalid"
                
        if missing_flag == False and format_flag == False:
            resp = None
            return resp
        else:
            try:
                raise Exception(error)
            except Exception as error:
                
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                } 
            return resp

    class Camera:
        """This class is used to get the information from all cameras discovered on this specific
        network."""

        def __init__(self, ip, port, user, password):
            """Constructor.
            Args:
                ip (str): Ip of the camera.
                user (str): Onvif login.
                password (str): Onvif password.
            """
            # '/usr/local/onvif-0.2.0-py2.7.egg/wsdl/'
            #"/etc/onvif/wsdl/"

            try:
                self._mycam = ONVIFCamera(ip, port, user, password, '/etc/onvif/wsdl/')
            except:
                try:
                    self._mycam = ONVIFCamera(ip, port, user, password, 'wsdl/')

                except:
                    self._mycam = ONVIFCamera(ip, port, user, password, '/etc/onvif/wsdl/')

        @property
        def hostname(self) -> str:
            """Find hostname of camera.
            Returns:
                str: Hostname.
            """
            resp = self._mycam.devicemgmt.GetDeviceInformation()
           
            return resp.FirmwareVersion

        @property
        def model(self) -> str:
            """Find model of camera.
            Returns:
                str: Model.
            """
            resp = self._mycam.devicemgmt.GetDeviceInformation()
            return resp.Model

        @property
        def rtsp_uri(self):
            """ Find the rtsp uri for Sensor"""

            media_service = self._mycam.create_media_service()
            profiles = media_service.GetProfiles()
            token = profiles[0].token
            obj = media_service.create_type('GetStreamUri')
            obj.ProfileToken = token
            obj.StreamSetup = {'Stream': 'RTP-Unicast', 'Transport': {'Protocol': 'RTSP'}}
            resp = media_service.GetStreamUri(obj)

            return resp['Uri']
    
    def sensors_data(self, ip, port, username, password):
        try:
        
            camera = self.Camera(ip, port, username, password)
            
            uri = camera.rtsp_uri
            model = camera.model
            NVR = camera.hostname
            
            return [uri, model, NVR]
        except Exception as err:
            return [err, None]

    def validate_ip(self,valid_ip):
        iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
        ip = netifaces.ifaddresses(iface)[netifaces.AF_INET]
        addr = ip[0]["addr"]
        mask = ip[0]["netmask"]
        count_mask  = 0
        mask_list = mask.split(".")
        for i in mask_list:
            if i == "255":
                count_mask +=1
                
        addr_list = addr.split(".")
        valid_ip_list = valid_ip.split(".")
        
        check = 0
        for j in range(count_mask):
            if addr_list[j] == valid_ip_list[j]:
                check +=1
        
        if check == count_mask:
            return True
        else:
            return False

    
            
    # @app.route('/sensor', methods=['POST'])
    def post(self):
        items = self.items

        checking = self.check()
        
        
        if checking == None:
           
            sensors = items["sensor"]
            
            passcodes = items["passCode"]
            user = []
            passwrd = []

            for passcode in passcodes:
                user.append(passcode["userName"])
                passwrd.append(passcode["password"])

            uniq_usr = []
            uniq_pass = []
            for i in user:
                if i not in uniq_usr:
                    uniq_usr.append(i)

            for j in passwrd:
                if j not in uniq_pass:
                    uniq_pass.append(j)   
            
            data = []
            
            num = 0
            for sensor in sensors:
                

                ip = sensor["ip"]
                port = sensor["httpPort"]
                
                name = sensor["name"]
                mode = sensor["mode"]
                Type = sensor["type"]
                address = sensor["address"]
                location = sensor["location"]
                site_id = sensor["siteId"]
                node_id = sensor["nodeId"]
                http_port = sensor["httpPort"]
                rtsp_port = sensor["rtspPort"]

                if self.validate_ip(ip) == True:
                    for usr in uniq_usr:
                        for pass_word in uniq_pass:
                            
                            sensor_data = self.sensors_data(ip, port, usr, pass_word)
                            print(sensor_data)

                            if type(sensor_data) == list:
                                username = usr
                                password = pass_word
                                break
                        if type(sensor_data) == list:
                            username = usr
                            password = pass_word
                            break
                

                    if sensor_data[1] != None and sensor_data[2][:3] != "NVR":
                        
                        mac = get_mac_address(ip=ip)
                        model = sensor_data[1]

                        sensor_data = sensor_data[0]
                        rtsp = str(sensor_data)[:7] + str(usr) +":"+str(pass_word)+"@"+str(sensor_data)[7:7+len(ip)] + ":"+str(rtsp_port) + str(sensor_data)[7+len(ip):]


                        data.append(
                            {"success": True,
                            "ip": ip,
                            "portEntry": port,
                            "name":name,
                            "mode":mode, 
                            "Type":Type,
                            "address":address,
                            "location":location,
                            "siteId":site_id,
                            "mac":mac,
                            "modelNumber":model,
                            "nodeId":node_id,
                            "httpPort":http_port,
                            "rtspPort":rtsp_port,
                            "userName":username,
                            "password":password,
                            "rtspUrl": rtsp
                            })
                        
                    if sensor_data[1] == None:
                        data.append(
                            {
                            "status": False,
                            "reasonPhrase": "OK",
                            "statusCode": 422,
                            "data": [],
                            "error": str(sensor_data[0]),
                            "aividStatusCode": 159
                             } 
                        )
                    else:
                        data.append(
                            {
                            "status": False,
                            "reasonPhrase": "OK",
                            "statusCode": 422,
                            "data": [],
                            "error": "authentication error: ip, username or password is Invalid",
                            "aividStatusCode": 159
                        } 
                        )
                        # data.append(
                        #         {
                        #     "success": False,
                        #     "ip": ip,
                        #     "port": port,
                        #     "err": str(sensor_data)
                        #     }
                        # )

                        data.append(
                            {
                            "status": False,
                            "reasonPhrase": "OK",
                            "statusCode": 422,
                            "data": [],
                            "error": "authentication error: ip, username or password is Invalid",
                            "aividStatusCode": 159
                        } 
                        )
                # else:
                else:
                    data.append(
                            {
                            "status": False,
                            "reasonPhrase": "OK",
                            "statusCode": 422,
                            "data": [],
                            "error": "authentication error: ip, username or password is Invalid",
                            "aividStatusCode": 159
                        } 
                        )
                num = num+1

            resp = {
                "status": True,
                "reasonPhrase": "OK",
                "statusCode": 200,
                "data": data,
                "error": None,
                "aividStatusCode": 110
            }
            

      
        else:
            resp = checking
        
        return jsonify(resp)

# if __name__ == '__main__':
# 	app.run(debug=True)