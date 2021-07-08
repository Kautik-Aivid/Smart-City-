from flask import Flask,request, jsonify
from wsdiscovery.discovery import ThreadedWSDiscovery as WSDiscovery
from wsdiscovery import Scope
import socket
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class onvif:

    @app.route('/onvif', methods=['POST'])
    def post():
        items = request.get_json()
        
        required_vlaues = ["ipRangeStart", "ipRangeEnd", "portList"]
        
        missing_flag = False
        format_flag = False

        if len(items) == 0:
            missing_flag = True

            status_code = 101
            error = "Mandatory fields are missing"       
            
        if missing_flag == False:
        
            cnt = 0
            try:
                start_ip_address = items['ipRangeStart']
                cnt = cnt + 1
                end_ip_address = items['ipRangeEnd']
                cnt = cnt + 1
                ports = items['portList']
                
            except:
                missing_flag = True
        
            
            if missing_flag == True:
                status_code = 101
                error = str(required_vlaues[cnt])+" is missing!" 

            requ = ["ipRangeStart", "ipRangeEnd","port"]
            if missing_flag == False:
                cnt = 0
                if type(start_ip_address) == str:
                    cnt += 1
                    if type(end_ip_address) == str:
                        cnt +=1
                        if type(ports) == list:
                            missing_flag = False
                        else:
                            missing_flag = True
                    else:
                        missing_flag = True
                else:
                    missing_flag = True

                if missing_flag == True:
                    status_code = 101
                    error = str(requ[cnt])+" is Invalid!" 

            requ = ["ipRangeStart", "ipRangeEnd"]
            if missing_flag == False:
                cnt = 0
                if len(start_ip_address) != 0:
                    cnt += 1
                    if len(end_ip_address) != 0:
                        missing_flag = False
                    else:
                        missing_flag = True
                else:
                    missing_flag = True

                if missing_flag == True:
                    status_code = 101
                    error = str(requ[cnt])+" is missing!" 

            if missing_flag == False:
                if start_ip_address == end_ip_address:
                    format_flag = True
                    status_code = 135
                    error = "Start IP Address and End IP Address should be different"
                    missing_flag = True
             

        if missing_flag == False and format_flag == False:

            cnt = 0
            if type(start_ip_address) == str:
                start_ip = start_ip_address.count('.')
                
                if start_ip == 3:
                    cnt = cnt+1
                    if type(end_ip_address) == str:
                        end_ip = end_ip_address.count('.')
                        if end_ip == 3:
                            cnt = cnt+1
                            for port in ports:
                                if type(port) == int:
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
                    
            
        if missing_flag == False and format_flag == True:
            status_code = 106
            error = "Invalid " +str(required_vlaues[cnt]) 
        
        
        if missing_flag == False and format_flag == False:
            if len(ports) == 0:
                missing_flag=True
                status_code = 101
                error = "Ports are missing"
           

        if missing_flag == False and format_flag == False:
            startip_ls = start_ip_address.split(".")
            endip_ls = end_ip_address.split(".")
            
            for i in range(len(startip_ls)):
                cnt = 0
                try:
                    check_startip = int(startip_ls[i])
                    cnt = cnt+1
                    check_endip = int(endip_ls[i])
                     
                except:
                    format_flag = True

                if format_flag == True:
                    status_code = 106
                    error = "Invalid " +str(required_vlaues[cnt]) 
                   
                    break
        
            if format_flag == False:
                startip_ls = start_ip_address.split(".")
                endip_ls = end_ip_address.split(".")
                startip_ls = startip_ls[:-1]
                endip_ls = endip_ls[:-1]
                
                temp_cnt = 0
                for k in range(len(startip_ls)):
                    if startip_ls[k] == endip_ls[k]:
                        temp_cnt+=1
                if temp_cnt !=3:
                    format_flag = True
                    status_code = 136
                    error = "Start IP address and End Ip address should be in same subnet" 
                
                if format_flag == False:
                    if int(start_ip_address.split(".")[-1]) < int(end_ip_address.split(".")[-1]):
                        format_flag = False
                    else:
                        format_flag = True
                        error = "Start Ip should be less than End Ip"
                        status_code = 106
                    
        print(format_flag, missing_flag)
        if format_flag == False and missing_flag==False:
            def fetch_devices():
                wsd = WSDiscovery()
                scope1 = Scope("onvif://www.onvif.org/Profile")
                wsd.start()
                services = wsd.searchServices(scopes=[scope1])
                ipaddresses = []
                for service in services:
                    ipaddress = re.search('(\d+|\.)+', str(service.getXAddrs()[0])).group(0)
                    ipaddresses.append(ipaddress)
                wsd.stop()
                return ipaddresses

            range_start = int(items['ipRangeStart'].split(".")[-1])
            range_end = int(items['ipRangeEnd'].split(".")[-1]) + 1
            
            ls = start_ip_address.split(".")
            init_ip = ls[0] +"."+ls[1]+"."+ls[2]+"."

            final_ips = []
            print("fetch_devices",fetch_devices())
            for ip in fetch_devices():
                rang = int(ip.split(".")[-1])
                if rang < range_end and rang > range_start:
                    final_ips.append(ip)
          
            data = []
            for i in range(range_start, range_end):
                
                temp_ip = init_ip+str(i)

                if temp_ip in final_ips:
                
                    
                    for port in ports:
                        try:

                            a_socket = socket.socket()
                            location = (temp_ip, port)
                            socket.setdefaulttimeout(1)
                            result_of_check = a_socket.connect(location)

                            # if result_of_check == 0:
                                
                            data.append({
                            "success": True,
                            "ip": temp_ip,
                            "port": port
                            })
                            
                            
                        except socket.error as err:
                            # try:
                            #     raise Exception(socket.error)
                            # except Exception as err:

                                data.append({
                                "success": False,
                                "ip": temp_ip,
                                "port": port,
                                "err": str(err)
                                })

                else:
                    for port in ports:
                        print("port",port)
                        try:
                            raise Exception("connect ECONNREFUSED "+ temp_ip+":"+str(port))
                        except Exception as err:
                            
                            data.append({
                            "success": False,
                            "ip": temp_ip,
                            "port": port,
                            "err": str(err)
                            })

            resp = {
                    "status": True,
                    "reasonPhrase": "OK",
                    "statusCode": 200,
                    "data": data,
                    "error": None,
                    "aividStatusCode": 110
            }
            return jsonify(resp)
        else:
            try:
                raise Exception(error)
            except Exception as error:
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error":str(error),
                    "aividStatusCode": status_code
                }
            return jsonify(resp)

# if __name__ == '__main__':
# 	app.run(debug=True)
     

