
from flask import Flask,request, jsonify
from elasticsearch import Elasticsearch
from os import environ
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


HOSTNAME = environ.get('HOSTNAME')
DB_PORT = environ.get('DB_PORT')
app.config["JSON_SORT_KEYS"] = False
class CommonData:

    def __init__(self):
        self.items = request.get_json()
    
    def check_common(self):

        missing_flag = False
        format_flag = False
        items = self.items

        if len(items) == 0:
            missing_flag = True

            status_code = 101
            error = "Mandatory fields are missing"
        
        init_keys = ["botconfigs ", "sites","nodes","sensors","rules","responsetypes","activities","kpis","notifications","zones"]
        
        if missing_flag == False:
            
            for item in items:
                cam = 0
                try:
                    cam += 1
                    cnt = 0
                    botconfigs = item["botconfigs"]
                    cnt += 1
                    sites = item["sites"]
                    cnt += 1
                    nodes = item["nodes"]
                    cnt += 1
                    sensors = item["sensors"]
                    cnt += 1
                    rules = item["rules"]
                    cnt += 1
                    responsetypes = item["responsetypes"]
                    cnt  += 1
                    activities = item["activities"]
                    cnt += 1
                    kpis = item["kpis"]
                    cnt += 1
                    notification = item["notifications"]
                    cnt += 1
                    zone = item["zones"]
                except:
                    missing_flag = True

                if missing_flag == True:
                    status_code = 101
                    error = str(init_keys[cnt])+" "+str(cam)+" is missing!"

                if missing_flag == False:
                    init_keys = ["botconfigs ", "sites","nodes","sensors","rules","responsetypes","activities","kpis","notifications","zones"]
                    
                    cnt = 0
                    if type(botconfigs) == dict:
                        cnt +=1
                        if type(sites) == dict:
                            cnt += 1
                            if type(nodes) == dict:
                                cnt += 1
                                if type(sensors) == dict: 
                                    cnt +=1
                                    if type(rules) == dict:
                                        cnt += 1
                                        if type(responsetypes) == dict:
                                            cnt += 1
                                            if type(activities) == dict:
                                                cnt += 1
                                                if type(kpis) == dict:
                                                    cnt += 1
                                                    if type(notification) == list:
                                                        cnt += 1
                                                        if type(zone) == list:
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
                        else:
                            format_flag = True
                    else:
                        format_flag = True

                    if missing_flag == False and format_flag == True:
                        status_code = 106
                        error = str(init_keys[cnt])+" "+str(cam)+" is Invalid!"
                        break

                if missing_flag == False and format_flag == False:
                    init_keys = ["botconfigs ", "sites","nodes","sensors","rules","responsetypes","activities","kpis"]
                    
                    cnt = 0
                    if len(botconfigs) != 0:
                        cnt +=1
                        if len(sites) != 0:
                            cnt += 1
                            if len(nodes) != 0:
                                cnt += 1
                                if len(sensors) != 0: 
                                    cnt +=1
                                    if len(rules) != 0:
                                        cnt += 1
                                        if len(responsetypes) != 0:
                                            cnt += 1
                                            if len(activities) != 0:
                                                cnt += 1
                                                if len(kpis) != 0:
                                                    cnt += 1
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
                        status_code = 101
                        error = str(init_keys[cnt])+" "+str(cam)+" is missing!"
                        break

            if missing_flag == False and format_flag == False:
              
                return None
            else:
                print("____________1")
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                }
                return jsonify(resp)

    def check_botconfigs(self):
        items = self.items
        
        botconfigs_flag = False
        if botconfigs_flag == False:
            missing_flag =False
            format_flag = False
            cam = 0
            for item in items:
                botconfigs_keys = ["_id","description","botId","sopId","activityId","kpisId","siteId","nodeId","sensorId","inspectScheduleId",
                            "botStatus","responseTypeId","ruleId","progressIndex","createdBy","modifiedBy","isActive","__v","createdAt","updatedAt"]
                cam += 1
                botconfigs = item["botconfigs"]
                try:
                    cnt = 0
                    _id = botconfigs["_id"]
                    cnt += 1
                    description = botconfigs["description"]
                    cnt += 1
                    botId = botconfigs["botId"]
                    cnt += 1
                    sopId = botconfigs["sopId"]
                    cnt += 1
                    activityId = botconfigs["activityId"]
                    cnt += 1
                    kpisId = botconfigs["kpisId"]
                    cnt += 1
                    siteId = botconfigs["siteId"]
                    cnt += 1
                    nodeId = botconfigs["nodeId"]
                    cnt += 1
                    sensorId = botconfigs["sensorId"]
                    cnt += 1
                    inspectScheduleId = botconfigs["inspectScheduleId"]
                    cnt += 1
                    botStatus = botconfigs["botStatus"]
                    cnt += 1
                    responseTypeId = botconfigs["responseTypeId"]
                    cnt += 1
                    ruleId = botconfigs["ruleId"]
                    cnt += 1
                    progressIndex = botconfigs["progressIndex"]
                    cnt += 1
                    createdBy = botconfigs["createdBy"]
                    cnt += 1
                    modifiedBy = botconfigs["modifiedBy"]
                    cnt += 1
                    isActive = botconfigs["isActive"]
                    cnt += 1
                    __v = botconfigs["__v"]
                    cnt += 1
                    createdAt = botconfigs["createdAt"]
                    cnt += 1
                    updatedAt = botconfigs["updatedAt"]
               
                except:
                    missing_flag = True
                   
                if missing_flag == True:
                    status_code = 101
                    error = str("botconfigs "+str(cam)+" "+ botconfigs_keys[cnt])+" is missing!"
                    break
                if missing_flag == False:
                    botconfigs_keys = ["_id","description","botId","sopId","activityId","kpisId","siteId","nodeId","sensorId","inspectScheduleId",
                            "botStatus","responseTypeId","ruleId","progressIndex","createdBy","modifiedBy","isActive","__v","createdAt","updatedAt"]
                    
                    cnt = 0
                    if type(_id) == str:
                        cnt +=1
                        if type(description) == str:
                            cnt += 1
                            if type(botId) == str:
                                cnt += 1
                                if type(sopId) == str: 
                                    cnt +=1
                                    if type(activityId) == str:
                                        cnt += 1
                                        if type(kpisId) == str:
                                            cnt += 1
                                            if type(siteId) == str:
                                                cnt += 1
                                                if type(nodeId) == str:
                                                    cnt += 1
                                                    if type(sensorId) == str:
                                                        cnt += 1
                                                        if type(inspectScheduleId) == str:
                                                            cnt += 1
                                                            if botStatus == 0 or botStatus ==1:
                                                                cnt +=1
                                                                if type(responseTypeId) == str:
                                                                    cnt += 1
                                                                    if type(ruleId) == str:
                                                                        cnt += 1
                                                                        if type(progressIndex) == int:
                                                                            cnt += 1
                                                                            if type(createdBy) == str:
                                                                                cnt += 1
                                                                                if type(modifiedBy) == str or modifiedBy == None:
                                                                                    cnt += 1
                                                                                    if isActive == True or isActive == False:
                                                                                        cnt +=1
                                                                                        if __v == 0 or __v ==1:
                                                                                            cnt += 1
                                                                                            if type(createdAt) == str:
                                                                                                cnt += 1
                                                                                                if type(updatedAt) == str:
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
                        error = str("botconfigs "+str(cam)+" "+ botconfigs_keys[cnt])+" is Invalid!"
                        break
                if missing_flag == False and format_flag == False:
                    botconfigs_keys = ["_id","description","botId","sopId","activityId","kpisId","siteId","nodeId","sensorId","inspectScheduleId",
                            "responseTypeId","ruleId","createdBy","modifiedBy","createdAt","updatedAt"]
                    
                    cnt = 0
                    if len(_id) != 0:
                        cnt +=1
                        if len(description) != 0:
                            cnt += 1
                            if len(botId) != 0:
                                cnt += 1
                                if len(sopId) != 0: 
                                    cnt +=1
                                    if len(activityId) != 0:
                                        cnt += 1
                                        if len(kpisId) != 0:
                                            cnt += 1
                                            if len(siteId) != 0:
                                                cnt += 1
                                                if len(nodeId) != 0:
                                                    cnt += 1
                                                    if len(sensorId) != 0:
                                                        cnt += 1
                                                        if len(inspectScheduleId) != 0:
                                                            cnt += 1
                                                            if len(responseTypeId) != 0:
                                                                cnt += 1
                                                                if len(ruleId) != 0:
                                                                    cnt += 1
                                                                    if len(createdBy) != 0:
                                                                        cnt += 1
                                                                        if len(createdAt) != 0:
                                                                            cnt += 1
                                                                            if len(updatedAt) != 0:
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
                        status_code = 101
                        error = str("botconfigs "+str(cam)+" "+ botconfigs_keys[cnt])+" is missing!"
                        break

            if missing_flag == False and format_flag == False:
                botconfigs_flag = False
                return None
            else:
                print("____________2")
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                }
                return jsonify(resp)

    def check_sites(self):

        items = self.items
        sites_flag = False
        
        if  sites_flag == False:
            missing_flag =False
            format_flag = False
            cam = 0
            for item in items:
                sitess_keys = ["_id","location","regionId","areaId","isActive","name","email","contactPerson","mobile","countryCode",
                            "address","createdAt","updatedAt","__v"]
                cam += 1
                sites = item["sites"]
                try:
                    cnt = 0
                    _id = sites["_id"]
                    cnt += 1
                    location = sites["location"]
                    cnt += 1
                    regionId = sites["regionId"]
                    cnt += 1
                    areaId = sites["areaId"]
                    cnt += 1
                    isActive = sites["isActive"]
                    cnt += 1
                    name = sites["name"]
                    cnt += 1
                    email = sites["email"]
                    cnt += 1
                    contactPerson = sites["contactPerson"]
                    cnt += 1
                    mobile = sites["mobile"]
                    cnt += 1
                    countryCode = sites["countryCode"]
                    cnt += 1
                    address = sites["address"]
                    cnt += 1
                    createdAt = sites["createdAt"]
                    cnt += 1
                    updatedAt = sites["updatedAt"]
                    cnt += 1
                    __v = sites["__v"]
                    

                except:
                    missing_flag = True
                    
                if missing_flag == True:
                    status_code = 101
                    error = str("sites "+str(cam)+" "+ sitess_keys[cnt])+" is missing!"
                    break
                if missing_flag == False:
                    sitess_keys = ["_id","location","regionId","areaId","isActive","name","email","contactPerson","mobile","countryCode",
                            "address","createdAt","updatedAt","__v"]
                    
                    cnt = 0
                    if type(_id) == str:
                        cnt +=1
                        if type(location) == dict:
                            cnt += 1
                            if type(regionId) == str:
                                cnt += 1
                                if type(areaId) == str: 
                                    cnt +=1
                                    if isActive == True or isActive == False:
                                        cnt += 1
                                        if type(name) == str:
                                            cnt += 1
                                            if type(email) == str:
                                                cnt += 1
                                                if type(contactPerson) == str:
                                                    cnt += 1
                                                    if type(mobile) == int or type(mobile) == str or mobile == None:
                                                        cnt += 1
                                                        if type(countryCode) == int:
                                                            cnt += 1
                                                            if type(address) == str:
                                                                cnt +=1
                                                                if type(createdAt) == str:
                                                                    cnt += 1
                                                                    if type(updatedAt) == str:
                                                                        cnt += 1
                                                                        if __v == 0 or __v ==1:
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
                        error = str("sites "+str(cam)+" "+ sitess_keys[cnt])+" is Invalid!"
                        break
                if missing_flag == False and format_flag == False:
                    sitess_keys = ["_id","regionId","areaId","name",
                            "address","createdAt","updatedAt"]
                    
                    cnt = 0
                    if len(_id) != 0:
                        cnt +=1
                        if len(regionId) != 0:
                            cnt += 1
                            if len(areaId) != 0:
                                cnt += 1
                                if len(name) != 0: 
                                    cnt +=1
                                    if len(address) != 0:
                                        cnt += 1
                                        if len(createdAt) != 0:
                                            cnt += 1
                                            if len(updatedAt) != 0:
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

                    if missing_flag == False and format_flag == True:
                        status_code = 101
                        error = str("sites "+str(cam)+" "+ sitess_keys[cnt])+" is missing!"
                        break
                if missing_flag == False and format_flag == False:
                    location = sites["location"]
                    cnt = 0
                    sitess_keys = ["type","coordinates"]
                    try:
                        _type = location["type"]
                        cnt += 1
                        coordinates = location["coordinates"]
                    except:
                        missing_flag = True
                    
                    if missing_flag == True:
                        status_code = 101
                        error = str("sites "+str(cam)+" "+ sitess_keys[cnt])+" is missing!"
                        break
                    if missing_flag == False:
                        cnt = 0
                        if type(_type) == str:
                            cnt += 1
                            if type(coordinates) == list:
                                format_flag = False
                            else:
                                format_flag = True
                        else:
                            format_flag = True

                        if format_flag == True:

                            status_code = 106
                            error = str("sites "+str(cam)+" "+ sitess_keys[cnt])+" is Invalid!"
                            break
                    
                    if missing_flag == False and format_flag == False:
                        cnt = 0
                        if len(_type) != 0:
                            cnt += 1
                            if len(coordinates) != 0:
                                format_flag = False
                            else:
                                format_flag = True
                        else:
                            format_flag = True
                        if format_flag == True:

                            status_code = 101
                            error = "sites "+str(cam)+" "+ str(sitess_keys[cnt])+" is missing!"
                            break
                    
                    if missing_flag == False and format_flag == False:
                        for coordinate in coordinates:
                            if type(coordinate) == int or type(coordinate) == float:
                                format_flag = False
                            else:
                                format_flag = True
                        
                        if format_flag == True:
                            status_code = 106
                            error = "sites "+str(cam)+" "+ "coordinate is Invalid!"
                            break


            if missing_flag == False and format_flag == False:
                sites_flag = False
                
            else:
                print("____________3")
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                }
                return jsonify(resp)

    def check_nodes(self):
        items = self.items
        nodes_flag = False
        
        if  nodes_flag == False:
            missing_flag =False
            format_flag = False
            cam = 0
            for item in items:
                nodes_keys = ["_id","location","isActive","name","ip","port","siteId","address",
                            "createdAt","updatedAt","__v"]
                cam += 1
                nodes = item["nodes"]
                try:
                    cnt = 0
                    _id = nodes["_id"]
                    cnt += 1
                    location = nodes["location"]
                    cnt += 1
                    isActive = nodes["isActive"]
                    cnt += 1
                    name = nodes["name"]
                    cnt += 1
                    ip = nodes["ip"]
                    cnt += 1
                    port = nodes["port"]
                    cnt += 1
                    address = nodes["address"]
                    cnt += 1
                    siteId = nodes["siteId"]
                    cnt += 1
                    createdAt = nodes["createdAt"]
                    cnt += 1
                    updatedAt = nodes["updatedAt"]
                    cnt += 1
                    __v = nodes["__v"]

                except:
                    missing_flag = True
                    
                if missing_flag == True:
                    status_code = 101
                    error = str("nodes "+str(cam)+" "+ nodes_keys[cnt])+" is missing!"
                    break
                if missing_flag == False:
                    nodes_keys = ["_id","location","isActive","name","ip","port","siteId","address",
                            "createdAt","updatedAt","__v"]
                    
                    cnt = 0
                    if type(_id) == str:
                        cnt +=1
                        if type(location) == dict:
                            cnt += 1
                            if isActive == True or isActive == False:
                                cnt += 1
                                if type(name) == str:
                                    cnt += 1
                                    if type(ip) == str:
                                        cnt += 1
                                        if type(port) == int:
                                            cnt += 1
                                            if type(siteId) == str:
                                                cnt +=1
                                                if type(address) == str:
                                                    cnt +=1
                                                    if type(createdAt) == str:
                                                        cnt += 1
                                                        if type(updatedAt) == str:
                                                            cnt += 1
                                                            if __v == 0 or __v ==1:
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
                            else:
                                format_flag = True
                        else:
                            format_flag = True
                    else:
                        format_flag = True

                    if missing_flag == False and format_flag == True:
                        status_code = 106
                        error = str("nodes "+str(cam)+" "+ nodes_keys[cnt])+" is Invalid!"
                        break
                if missing_flag == False and format_flag == False:
                    nodes_keys = ["_id","name","ip","siteId","address",
                            "createdAt","updatedAt"]
                    cnt = 0
                    if len(_id) != 0:
                        cnt +=1
                        if len(name) != 0:
                            cnt += 1
                            if len(ip) != 0:
                                cnt += 1
                                if len(siteId) != 0: 
                                    cnt +=1
                                    if len(address) != 0:
                                        cnt += 1
                                        if len(createdAt) != 0:
                                            cnt += 1
                                            if len(updatedAt) != 0:
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

                    if missing_flag == False and format_flag == True:
                        status_code = 101
                        error = str("nodes "+str(cam)+" "+ nodes_keys[cnt])+" is missing!"
                        break
                if missing_flag == False and format_flag == False:
                    location = nodes["location"]
                    cnt = 0
                    nodes_keys = ["type","coordinates"]
                    try:
                        _type = location["type"]
                        cnt += 1
                        coordinates = location["coordinates"]
                    except:
                        missing_flag = True
                        
                    if missing_flag == True:
                        status_code = 101
                        error = str("nodes "+str(cam)+" "+ nodes_keys[cnt])+" is missing!"
                        break
                    if missing_flag == False:
                        cnt = 0
                        if type(_type) == str:
                            cnt += 1
                            if type(coordinates) == list:
                                format_flag = False
                            else:
                                format_flag = True
                        else:
                            format_flag = True

                        if format_flag == True:

                            status_code = 106
                            error = str("nodes "+str(cam)+" "+ nodes_keys[cnt])+" is Invalid!"
                            break
                    
                    if missing_flag == False and format_flag == False:
                        cnt = 0
                        if len(_type) != 0:
                            cnt += 1
                            if len(coordinates) != 0:
                                format_flag = False
                            else:
                                format_flag = True
                        else:
                            format_flag = True
                        if format_flag == True:

                            status_code = 101
                            error = "nodes "+str(cam)+" "+ str(nodes_keys[cnt])+" is missing!"
                            break
                    
                    if missing_flag == False and format_flag == False:
                        for coordinate in coordinates:
                            if type(coordinate) == int or type(coordinate) == float:
                                format_flag = False
                            else:
                                format_flag = True
                        
                        if format_flag == True:
                            status_code = 106
                            error = "nodes "+str(cam)+" "+ "coordinate is Invalid!"
                            break

                if missing_flag == False and format_flag == False:
                    check_ip = ip.count(".")
                    if check_ip == 3:
                        format_flag = False 
                    else:
                        format_flag = True 
                        status_code = 106
                        error = "nodes "+str(cam)+" "+ "ip is Invalid!"
                        break   
                    if format_flag == False:
                        split_ip = ip.split(".") 
                        
                        for _split in split_ip:
                            try:
                                temp_spl = int(_split)
                            except:
                                format_flag = True
                                break

                        if format_flag == True:
                            status_code = 106
                            error = "nodes "+str(cam)+" "+ "ip is Invalid!"
                            break 


            if missing_flag == False and format_flag == False:
                
                return None
            else:
                print("____________4")
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                }
                return jsonify(resp) 
    
    def check_sensors(self):
        items = self.items
        sensors_flag = False
        
        if  sensors_flag == False:
            missing_flag =False
            format_flag = False
            cam = 0
            for item in items:
                sensors_keys = ["_id","channelId","name","deviceId","rtspUrl","__v", "createdAt","updatedAt"]
                cam += 1
                sensors = item["sensors"]
                try:
                    cnt = 0
                    _id = sensors["_id"]
                    cnt += 1
                    channelId = sensors["channelId"]
                    cnt += 1
                    name = sensors["name"]
                    cnt += 1
                    deviceId = sensors["deviceId"]
                    cnt += 1
                    rtspUrl = sensors["rtspUrl"]
                    cnt += 1
                    __v = sensors["__v"]
                    cnt += 1
                    createdAt = sensors["createdAt"]
                    cnt += 1
                    updatedAt = sensors["updatedAt"]

                except:
                    missing_flag = True
                    
                if missing_flag == True:
                    status_code = 101
                    error = str("sensors "+str(cam)+" "+ sensors_keys[cnt])+" is missing!"
                    break
                if missing_flag == False:
                    sensors_keys = ["_id","channelId","name","deviceId","rtspUrl","__v", "createdAt","updatedAt"]
                    
                    cnt = 0
                    if type(_id) == str:
                        cnt += 1
                        if channelId == None or type(channelId) == str:
                            cnt += 1
                            if type(name) == str:
                                cnt += 1
                                if type(deviceId) == str:
                                    cnt += 1
                                    if type(rtspUrl) == str:
                                        cnt += 1
                                        if __v == 0 or __v == 1:
                                            cnt +=1
                                            if type(createdAt) == str:
                                                cnt += 1
                                                if type(updatedAt) == str:
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
                        error = str("sensors "+str(cam)+" "+ sensors_keys[cnt])+" is Invalid!"
                        break
                if missing_flag == False and format_flag == False:
                    sensors_keys = ["_id","name","deviceId","rtspUrl", "createdAt","updatedAt"]
                    cnt = 0
                    if len(_id) != 0:
                        cnt +=1
                        if len(name) != 0:
                            cnt += 1
                            if len(deviceId) != 0:
                                cnt += 1
                                if len(rtspUrl) != 0: 
                                    cnt +=1
                                    if len(createdAt) != 0:
                                        cnt += 1
                                        if len(updatedAt) != 0:
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

                    if missing_flag == False and format_flag == True:
                        status_code = 101
                        error = str("sensors "+str(cam)+" "+ sensors_keys[cnt])+" is missing!"
                        break
                

            if missing_flag == False and format_flag == False:
                return None
            else:
                print("____________5")
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                }
                return jsonify(resp) 
        
    def check_rules(self):
        items = self.items
        rules_flag = False
        
        if  rules_flag == False:
            missing_flag =False
            format_flag = False
            cam = 0
            for item in items:
                rules_keys = ["_id","activityId","operator","key","value","type", "createdAt","updatedAt","__v"]
                cam += 1
                rules = item["rules"]
                try:
                    cnt = 0
                    _id = rules["_id"]
                    cnt += 1
                    activityId = rules["activityId"]
                    cnt += 1
                    operator = rules["operator"]
                    cnt += 1
                    key = rules["key"]
                    cnt += 1
                    value = rules["value"]
                    cnt += 1
                    _type = rules["type"]
                    cnt += 1
                    createdAt = rules["createdAt"]
                    cnt += 1
                    updatedAt = rules["updatedAt"]
                    cnt += 1
                    __v = rules["__v"]

                except:
                    missing_flag = True
                    
                if missing_flag == True:
                    status_code = 101
                    error = str("rules "+str(cam)+" "+ rules_keys[cnt])+" is missing!"
                    break
                if missing_flag == False:
                    rules_keys = ["_id","activityId","operator","key","value","type", "createdAt","updatedAt","__v"]
                    
                    cnt = 0
                    if type(_id) == str:
                        cnt +=1
                        if type(activityId) == str:
                            cnt += 1
                            if operator == None or type(operator) == str:
                                cnt += 1
                                if type(key) == str:
                                    cnt += 1
                                    if type(value) == str:
                                        cnt += 1
                                        if type(_type) == str:
                                            cnt += 1
                                            if type(createdAt) == str:
                                                cnt += 1
                                                if type(updatedAt) == str:
                                                    if __v == 0 or __v == 1:
                                                        
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
                    else:
                        format_flag = True

                    if missing_flag == False and format_flag == True:
                        status_code = 106
                        error = str("rules "+str(cam)+" "+ rules_keys[cnt])+" is Invalid!"
                        break
                if missing_flag == False and format_flag == False:
                    rules_keys = ["_id","activityId","key","value","type", "createdAt","updatedAt"]
                    cnt = 0
                    if len(_id) != 0:
                        cnt +=1
                        if len(activityId) != 0:
                            cnt += 1
                            if len(key) != 0:
                                cnt += 1
                                if len(value) != 0: 
                                    cnt +=1
                                    if len(_type) != 0:
                                        cnt += 1
                                        if len(createdAt) != 0:
                                            cnt += 1
                                            if len(updatedAt) != 0:
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

                    if missing_flag == False and format_flag == True:
                        status_code = 101
                        error = str("rules "+str(cam)+" "+ rules_keys[cnt])+" is missing!"
                        break
                

            if missing_flag == False and format_flag == False:
                return None
            else:
                print("____________6")
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                }
                return jsonify(resp)

    def check_responsetypes(self):
        
        items = self.items
        responsetypes_flag = False
        
        if  responsetypes_flag == False:
            missing_flag =False
            format_flag = False
            cam = 0
            for item in items:
                responsetypes_keys = ["_id","falseResponse","trueResponse",
                            "createdAt","updatedAt","__v"]
                cam += 1
                responsetypes = item["responsetypes"]
                try:
                    cnt = 0
                    _id = responsetypes["_id"]
                    cnt += 1
                    falseResponse = responsetypes["falseResponse"]
                    cnt += 1
                    trueResponse = responsetypes["trueResponse"]
                    cnt += 1
                    createdAt = responsetypes["createdAt"]
                    cnt += 1
                    updatedAt = responsetypes["updatedAt"]
                    cnt += 1
                    __v = responsetypes["__v"]

                except:
                    missing_flag = True
                    
                if missing_flag == True:
                    status_code = 101
                    error = str("responsetypes "+str(cam)+" "+ responsetypes_keys[cnt])+" is missing!"
                    break
                if missing_flag == False:
                    responsetypes_keys = ["_id","falseResponse","trueResponse",
                            "createdAt","updatedAt","__v"]
                    
                    cnt = 0
                    if type(_id) == str:
                        cnt +=1
                        if type(falseResponse) == dict:
                            cnt += 1
                            if type(trueResponse) == dict:
                                cnt += 1
                                if type(createdAt) == str:
                                    cnt += 1
                                    if type(updatedAt) == str:
                                        cnt += 1
                                        if __v == 0 or __v ==1:
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

                    if missing_flag == False and format_flag == True:
                        status_code = 106
                        error = str("responsetypes "+str(cam)+" "+ responsetypes_keys[cnt])+" is Invalid!"
                        break

                if missing_flag == False and format_flag == False:
                    responsetypes_keys = ["_id","createdAt","updatedAt","__v"]
                    cnt = 0
                    if len(_id) != 0:
                        cnt +=1
                        if len(createdAt) != 0:
                            cnt += 1
                            if len(updatedAt) != 0:
                                format_flag = False
                            else:
                                format_flag = True
                        else:
                            format_flag = True
                    else:
                        format_flag = True

                    if missing_flag == False and format_flag == True:
                        status_code = 101
                        error = str("responsetypes "+str(cam)+" "+ responsetypes_keys[cnt])+" is missing!"
                        break

                if missing_flag == False and format_flag == False:
                    falseResponse = responsetypes["falseResponse"]
                    cnt = 0
                    responsetypes_keys = ["name","score","colorCode"]
                    try:
                        name = falseResponse["name"]
                        cnt += 1
                        score = falseResponse["score"]
                        cnt += 1
                        colorCode = falseResponse["colorCode"]
                    except:
                        missing_flag = True
                       
                    if missing_flag == True:
                        status_code = 101
                        error = str("responsetypes "+str(cam)+" "+ responsetypes_keys[cnt])+" is missing!"
                        break

                    if missing_flag == False:
                        cnt = 0
                        if type(name) == str:
                            cnt += 1
                            if type(score) == int:
                                cnt += 1
                                if type(colorCode) == str:
                                    format_flag = False
                                else:
                                    format_flag = True
                            else:
                                format_flag = True
                        else:
                            format_flag = True

                        if format_flag == True:

                            status_code = 106
                            error = str("responsetypes "+str(cam)+" "+ responsetypes_keys[cnt])+" is Invalid!"
                            break

                    
                    if missing_flag == False and format_flag == False:
                        responsetypes_keys = ["name","colorCode"]
                        cnt = 0
                        if len(name) != 0:
                            cnt += 1
                            if len(colorCode) != 0:
                                format_flag = False
                            else:
                                format_flag = True
                        else:
                            format_flag = True

                        if format_flag == True:

                            status_code = 101
                            error = "responsetypes "+str(cam)+" "+ str(responsetypes_keys[cnt])+" is missing!"
                            break

                if missing_flag == False and format_flag == False:
                    trueResponse = responsetypes["trueResponse"]
                    cnt = 0
                    responsetypes_keys = ["name","score","colorCode"]
                    try:
                        name = trueResponse["name"]
                        cnt += 1
                        score = trueResponse["score"]
                        cnt += 1
                        colorCode = trueResponse["colorCode"]
                    except:
                        missing_flag = True
                       
                    if missing_flag == True:
                        status_code = 101
                        error = str("responsetypes "+str(cam)+" "+ responsetypes_keys[cnt])+" is missing!"
                        break

                    if missing_flag == False:
                        cnt = 0
                        if type(name) == str:
                            cnt += 1
                            if type(score) == int:
                                cnt += 1
                                if type(colorCode) == str:
                                    format_flag = False
                                else:
                                    format_flag = True
                            else:
                                format_flag = True
                        else:
                            format_flag = True

                        if format_flag == True:

                            status_code = 106
                            error = str("responsetypes "+str(cam)+" "+ responsetypes_keys[cnt])+" is Invalid!"
                            break
                    
                    if missing_flag == False and format_flag == False:
                        responsetypes_keys = ["name","colorCode"]
                        cnt = 0
                        if len(name) != 0:
                            cnt += 1
                            if len(colorCode) != 0:
                                format_flag = False
                            else:
                                format_flag = True
                        else:
                            format_flag = True
                        if format_flag == True:

                            status_code = 101
                            error = "responsetypes "+str(cam)+" "+ str(responsetypes_keys[cnt])+" is missing!"
                            break


            if missing_flag == False and format_flag == False:
                
                return None
            else:
                print("____________7")
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                }
                return jsonify(resp) 

    def check_activities(self):
        items = self.items
        activities_flag = False
        
        if  activities_flag == False:
            missing_flag =False
            format_flag = False
            cam = 0
            for item in items:
                activities_keys = ["_id","sopId","version","nonNegotiable","modifiedBy","name", "uniqueName","createdAt","updatedAt","__v"]
                cam += 1
                activities = item["activities"]
                try:
                    cnt = 0
                    _id = activities["_id"]
                    cnt += 1
                    sopId = activities["sopId"]
                    cnt += 1
                    version = activities["version"]
                    cnt += 1
                    nonNegotiable = activities["nonNegotiable"]
                    cnt += 1
                    modifiedBy = activities["modifiedBy"]
                    cnt += 1
                    name = activities["name"]
                    cnt += 1
                    uniqueName = activities["uniqueName"]
                    cnt += 1
                    createdAt = activities["createdAt"]
                    cnt += 1
                    updatedAt = activities["updatedAt"]
                    cnt += 1
                    __v = activities["__v"]

                except:
                    missing_flag = True
                    
                if missing_flag == True:
                    status_code = 101
                    error = str("activities "+str(cam)+" "+ activities_keys[cnt])+" is missing!"
                    break
                if missing_flag == False:
                    activities_keys = ["_id","sopId","version","nonNegotiable","modifiedBy","name", "uniqueName","createdAt","updatedAt","__v"]
                    
                    cnt = 0
                    if type(_id) == str:
                        cnt +=1
                        if type(sopId) == str:
                            cnt += 1
                            if version == 1 or version == 0:
                                cnt += 1
                                if nonNegotiable == True or nonNegotiable == False:
                                    cnt += 1
                                    if modifiedBy == None or type(modifiedBy) == str:
                                        cnt += 1
                                        if type(name) == str:
                                            cnt += 1
                                            if type(uniqueName) == str:
                                                cnt += 1
                                                if type(createdAt) == str:
                                                    cnt += 1
                                                    if type(updatedAt) == str:
                                                        if __v == 0 or __v == 1:
                                                            
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
                        else:
                            format_flag = True
                    else:
                        format_flag = True

                    if missing_flag == False and format_flag == True:
                        status_code = 106
                        error = str("activities "+str(cam)+" "+ activities_keys[cnt])+" is Invalid!"
                        break

                if missing_flag == False and format_flag == False:
                    activities_keys = ["_id","sopId","name", "uniqueName","createdAt","updatedAt"]
                    cnt = 0
                    if len(_id) != 0:
                        cnt +=1
                        if len(sopId) != 0:
                            cnt += 1
                            if len(name) != 0:
                                cnt += 1
                                if len(uniqueName) != 0: 
                                    cnt +=1
                                    if len(createdAt) != 0:
                                        cnt += 1
                                        if len(updatedAt) != 0:
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

                    if missing_flag == False and format_flag == True:
                        status_code = 101
                        error = str("activities "+str(cam)+" "+ activities_keys[cnt])+" is missing!"
                        break
                

            if missing_flag == False and format_flag == False:
                return None
            else:
                print("____________8")
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                }
                return jsonify(resp)

    def check_kpis(self):
        items = self.items
        kpis_flag = False
        
       
        if  kpis_flag == False:
            missing_flag =False
            format_flag = False
            cam = 0
            for item in items:
                kpis_keys = ["_id","aividBotId","activityId","notificationTags","rules","name", "stage","botName","description","createdAt","updatedAt","__v"]
                cam += 1
                kpis = item["kpis"]
                cnt = 0
                try:
                    
                    _id = kpis["_id"]
                    cnt += 1
                    aividBotId = kpis["aividBotId"]
                    cnt += 1
                    activityId = kpis["activityId"]
                    cnt += 1
                    notificationTags = kpis["notificationTags"]
                    cnt += 1
                    rules = kpis["rules"]
                    cnt += 1
                    name = kpis["name"]
                    cnt += 1
                    stage = kpis["stage"]
                    cnt += 1
                    botName = kpis["botName"]
                    cnt += 1
                    description = kpis["description"]
                    cnt += 1
                    createdAt = kpis["createdAt"]
                    cnt += 1
                    updatedAt = kpis["updatedAt"]
                    cnt += 1
                    __v = kpis["__v"]

                except:
                  
                    missing_flag = True
                    
                if missing_flag == True:
                    status_code = 101
                  
                    error = "kpis "+str(cam)+" "+ kpis_keys[cnt]+" is missing!"
                    break
                if missing_flag == False:
                    kpis_keys = ["_id","aividBotId","activityId","notificationTags","rules","name", "stage","botName","description","createdAt","updatedAt","__v"]
                    
                    cnt = 0
                    if type(_id) == str:
                        cnt +=1
                        if type(aividBotId) == str:
                            cnt += 1
                            if type(activityId) == str:
                                cnt += 1
                                if type(notificationTags) == list:
                                    cnt += 1
                                    if type(rules) == list:
                                        cnt += 1
                                        if type(name) == str:
                                            cnt += 1
                                            if type(stage) == list:
                                                cnt += 1
                                                if type(botName) == str:
                                                    cnt += 1
                                                    if type(description) == str:
                                                        cnt += 1
                                                        if type(createdAt) == str:
                                                            cnt += 1
                                                            if type(updatedAt) == str:
                                                                if __v == 0 or __v == 1:
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
                        error = str("kpis "+str(cam)+" "+ kpis_keys[cnt])+" is Invalid!"
                        break

                if missing_flag == False and format_flag == False:
                    kpis_keys = ["_id","aividBotId","activityId","notificationTags","rules","name","botName","description","createdAt","updatedAt"]
                    
                    cnt = 0
                    if len(_id) != 0:
                        cnt +=1
                        if len(aividBotId) != 0:
                            cnt += 1
                            if len(activityId) != 0:
                                cnt += 1
                                if len(notificationTags) != 0: 
                                    cnt +=1
                                    if len(rules) != 0:
                                        cnt += 1
                                        if len(name) != 0:
                                            cnt += 1
                                            if len(botName) != 0: 
                                                cnt +=1
                                                if len(description) != 0: 
                                                    cnt +=1
                                                    if len(createdAt) != 0:
                                                        cnt += 1
                                                        if len(updatedAt) != 0:
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
                        else:
                            format_flag = True
                    else:
                        format_flag = True

                    if missing_flag == False and format_flag == True:
                        status_code = 101
                        error = str("kpis "+str(cam)+" "+ kpis_keys[cnt])+" is missing!"
                        break

            
                if missing_flag == False and format_flag == False:
                    rules = kpis["rules"]
                    
                    cnt = 0
                    kpis_keys = ["key","value","type"]
                    try:
                        for rule in rules:
                        
                            key = rule["key"]
                            cnt += 1
                            value = rule["value"]
                            cnt += 1
                            _type = rule["type"]
                    except:
                        missing_flag = True
                        
                        
                    if missing_flag == True:
                        status_code = 101
                        error = str("kpis "+str(cam)+" "+ kpis_keys[cnt])+" is missing!"
                        break

                    elif missing_flag == False:
                        for rule in rules:
                            cnt = 0
                            if type(rule["key"]) == str:
                                cnt += 1
                                if type(rule["value"]) == str:
                            
                                    cnt += 1
                                    if type(rule["type"]) == str:
                                        format_flag = False
                                    else:
                                        format_flag = True
                                        break
                                else:
                                    format_flag = True
                                    break
                            else:
                                format_flag = True
                                break

                        if format_flag == True:

                            status_code = 106
                            error = str("kpis "+str(cam)+" "+ kpis_keys[cnt])+" is Invalid!"
                            break

                    if missing_flag == False:

                        for rule in rules:
                                cnt = 0
                                if len(rule["key"]) != 0:
                                    cnt += 1
                                    if len(rule["value"]) != 0:
                                        cnt += 1
                                        if len(rule["type"]) != 0:
                                            format_flag = False
                                        else:
                                            format_flag = True
                                            break
                                    else:
                                        format_flag = True
                                        break
                                else:
                                    format_flag = True
                                    break

                        if format_flag == True:

                            status_code = 101
                            error = "kpis "+str(cam)+" "+ str(kpis_keys[cnt])+" is missing!"
                            break
                

            if missing_flag == False and format_flag == False:
                return None
            else:
                print("____________9")
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                }
                return jsonify(resp)

    def check_notification(self):
        items = self.items
        
        main_flag = False
        if main_flag == False:
            missing_flag =False
            format_flag = False
            cam = 0
            error = None
            for item in items:
                if error != None:
                    break
                
                cam += 1
                notifications = item["notifications"]
                if len(notifications) != 0:
                    for notification in notifications:
                        notification_keys = ["notificationconfigs","rules","responsetypes","templates"]
                        
                        try:
                            cnt = 0
                            notificationconfigs = notification["notificationconfigs"]
                            cnt += 1
                            rules = notification["rules"]
                            cnt += 1
                            responsetypes = notification["responsetypes"]
                            cnt += 1
                            templates = notification["templates"]
                            
                        except:
                            missing_flag = True
                            
                        
                        if missing_flag == True:
                            status_code = 101
                            error = str("notifications "+ notification_keys[cnt])+" is missing!"
                            break
                        if missing_flag == False:
                            notification_keys = ["notificationconfigs","rules","responsetypes","templates"]
                            
                            
                            cnt = 0
                            if type(notificationconfigs) == dict:
                                cnt +=1
                                if type(rules) == dict:
                                    cnt += 1
                                    if type(responsetypes) == dict:
                                        cnt += 1
                                        if type(templates) == dict: 
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
                                status_code = 106
                                error = str("notifications "+ notification_keys[cnt])+" is Invalid!"
                                break
                        
                        if missing_flag == False and format_flag == False:
                            notification_keys = ["notificationconfigs","rules","responsetypes","templates"]
                            
                            cnt = 0
                            if len(notificationconfigs) != 0:
                                cnt +=1
                                if len(rules) != 0:
                                    cnt += 1
                                    if len(responsetypes) != 0:
                                        cnt += 1
                                        if len(templates) != 0: 
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
                                error = str("notifications "+ notification_keys[cnt])+" is missing!"
                                break
                    

            if missing_flag == False and format_flag == False:
                main_flag = False
            
            else:
                print("____________10")
                main_flag = True
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                }
                return jsonify(resp)
                
        if main_flag == False:
            notification_flag = False
            missing_flag =False
            format_flag = False
            cam = 0
            error = None
            for item in items:
                if error != None:
                    break
                cam += 1
                
                notifications = item["notifications"]
                temp_cnt = 0
                if len(notifications) != 0:
                    for notification in notifications:
                        notificationconfig = notification["notificationconfigs"]
                        temp_cnt += 1
                        notificationconfig_keys = ["_id","type","ruleId","notificationMedium","responseTypeId","attachedClip","attachedSnap",
                                            "isSourceCamera","lockClip","isResend","createdBy","modifiedBy","isActive","botConfigId","templateId",
                                            "isResponseType","resendInterval","__v","createdAt","updatedAt"]
                        
                        
                        try:
                            cnt = 0
                            _id = notificationconfig["_id"]
                            cnt += 1
                            _type = notificationconfig["type"]
                            cnt += 1
                            ruleId = notificationconfig["ruleId"]
                            cnt += 1
                            notificationMedium = notificationconfig["notificationMedium"]
                            cnt += 1
                            responseTypeId = notificationconfig["responseTypeId"]
                            cnt += 1
                            attachedClip = notificationconfig["attachedClip"]
                            cnt += 1
                            attachedSnap = notificationconfig["attachedSnap"]
                            cnt += 1
                            isSourceCamera = notificationconfig["isSourceCamera"]
                            cnt += 1
                            lockClip = notificationconfig["lockClip"]
                            cnt += 1
                            isResend = notificationconfig["isResend"]
                            cnt += 1
                            createdBy = notificationconfig["createdBy"]
                            cnt += 1
                            modifiedBy = notificationconfig["modifiedBy"]
                            cnt += 1
                            isActive = notificationconfig["isActive"]
                            cnt += 1
                            botConfigId = notificationconfig["botConfigId"]
                            cnt += 1
                            templateId = notificationconfig["templateId"]
                            cnt += 1
                            isResponseType = notificationconfig["isResponseType"]
                            cnt += 1
                            resendInterval = notificationconfig["resendInterval"]
                            cnt += 1
                            __v = notificationconfig["__v"]
                            cnt += 1
                            createdAt = notificationconfig["createdAt"]
                            cnt += 1
                            updatedAt = notificationconfig["updatedAt"] 
                        
                        except:
                            missing_flag = True
                        
                        if missing_flag == True:
                            status_code = 101
                            error = "Notifications "+ notificationconfig_keys[cnt]+" is missing!"
                            break
                        if missing_flag == False:
                            notificationconfig_keys = ["_id","type","ruleId","notificationMedium","responseTypeId","attachedClip","attachedSnap",
                                            "isSourceCamera","lockClip","isResend","createdBy","modifiedBy","isActive","botConfigId","templateId",
                                            "isResponseType","resendInterval","__v","createdAt","updatedAt"]
                            
                            cnt = 0
                            if type(_id) == str:
                                cnt +=1
                                if _type == 1 or _type == 0:
                                    cnt += 1
                                    if type(ruleId) == str:
                                        cnt += 1
                                        if type(notificationMedium) == int: 
                                            cnt +=1
                                            if type(responseTypeId) == str:
                                                cnt += 1
                                                if attachedClip == True or attachedClip == False:
                                                    cnt += 1
                                                    if attachedSnap == True or attachedSnap == False:
                                                        cnt += 1
                                                        if isSourceCamera == True or isSourceCamera == False:
                                                            cnt += 1
                                                            if lockClip == True or lockClip == False:
                                                                cnt += 1
                                                                if isResend == True or isResend == False:
                                                                    cnt += 1
                                                                    if type(createdBy) == str:
                                                                        cnt +=1
                                                                        if modifiedBy == None or type(modifiedBy) == str:
                                                                            cnt += 1
                                                                            if isActive == True or isActive == False:
                                                                                cnt += 1
                                                                                if type(botConfigId) == str:
                                                                                    cnt += 1
                                                                                    if type(templateId) == str:
                                                                                        cnt +=1
                                                                                        if isResponseType == False or isResponseType == True:
                                                                                            cnt += 1
                                                                                            if type(resendInterval) == int:
                                                                                                cnt += 1
                                                                                                if __v == 0 or __v ==1:
                                                                                                    cnt += 1
                                                                                                    if type(createdAt) == str:
                                                                                                        cnt += 1
                                                                                                        if type(updatedAt) == str:
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
                            
                                error = "Notifications "+ notificationconfig_keys[cnt]+" is Invalid!"
                                break
                        if missing_flag == False and format_flag == False:
                            notificationconfig_keys = ["_id","ruleId","responseTypeId","createdBy","botConfigId","templateId",
                                                        "createdAt","updatedAt"]
                            
                            cnt = 0
                            if len(_id) != 0:
                                cnt +=1
                                if len(ruleId) != 0:
                                    cnt += 1
                                    if len(responseTypeId) != 0:
                                        cnt += 1
                                        if len(createdBy) != 0: 
                                            cnt +=1
                                            if len(botConfigId) != 0:
                                                cnt += 1
                                                if len(templateId) != 0:
                                                    cnt += 1
                                                    if len(createdAt) != 0:
                                                        cnt += 1
                                                        if len(updatedAt) != 0:
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
                                status_code = 101
                                error = "Notifications "+ notificationconfig_keys[cnt]+" is Missing!"
                                break

            if missing_flag == False and format_flag == False:
                notification_flag = False
            
            else:
                notification_flag = True
                print("____________11")
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                }
                return jsonify(resp)
        
        if notification_flag == False:
            rules_flag = False
            missing_flag =False
            format_flag = False
            cam = 0
            for item in items:
                if error != None:
                    break
                cam += 1
                notifications = item["notifications"]
                temp_cnt = 0
                if len(notifications) != 0:
                    for notification in notifications:
                        rule = notification["rules"]
                        temp_cnt += 1
                        rules_keys = ["_id","activityId","operator","key","value","type","__v","createdAt","updatedAt"]
                        
                        
                        try:
                            cnt = 0
                            _id = rule["_id"]
                            cnt += 1
                            activityId = rule["activityId"]
                            cnt += 1
                            operator = rule["operator"]
                            cnt += 1
                            key = rule["key"]
                            cnt += 1
                            value = rule["value"]
                            cnt += 1
                            _type = rule["type"]
                            cnt += 1
                            __v = rule["__v"]
                            cnt += 1
                            createdAt = rule["createdAt"]
                            cnt += 1
                            updatedAt = rule["updatedAt"] 
                        
                        except:
                            missing_flag = True
                        
                        if missing_flag == True:
                            status_code = 101
                            error = "Notifications "+str(cam)+" -> "+"rule "+str(temp_cnt)+ rules_keys[cnt]+" is missing!"
                            break
                        if missing_flag == False:
                            rules_keys = ["_id","activityId","operator","key","value","type","__v","createdAt","updatedAt"]
                            
                            cnt = 0
                            if type(_id) == str:
                                cnt +=1
                                if type(activityId) == str:
                                    cnt += 1
                                    if operator == None or str(operator) == str:
                                        cnt += 1
                                        if type(key) == str: 
                                            cnt +=1
                                            if type(value) == str:
                                                cnt += 1
                                                if type(_type) == str:
                                                    cnt += 1
                                                    if __v == 0 or __v ==1:
                                                        cnt += 1
                                                        if type(createdAt) == str:
                                                            cnt += 1
                                                            if type(updatedAt) == str:
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
                            else:
                                format_flag = True

                            if missing_flag == False and format_flag == True:
                                status_code = 106
                                error = "Notifications "+ rules_keys[cnt]+" is Invalid!"
                                break
                        if missing_flag == False and format_flag == False:
                            rules_keys = ["_id","activityId","key","value","type","createdAt","updatedAt"]
                            
                            cnt = 0
                            if len(_id) != 0:
                                cnt +=1
                                if len(activityId) != 0:
                                    cnt += 1
                                    if len(key) != 0:
                                        cnt += 1
                                        if len(value) != 0: 
                                            cnt +=1
                                            if len(_type) != 0:
                                                cnt += 1
                                                if len(createdAt) != 0:
                                                    cnt += 1
                                                    if len(updatedAt) != 0:
                                                    
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

                            if missing_flag == False and format_flag == True:
                                status_code = 101
                                error = "Notifications "+ rules_keys[cnt]+" is Missing!"
                                break

            if missing_flag == False and format_flag == False:
                rules_flag = False
            
            else:
                rules_flag = True
                print("____________12")

                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                }
                return jsonify(resp)


        if rules_flag == False:
            responsetypes_flag = False
            missing_flag =False
            format_flag = False
            cam = 0
            for item in items:
                if error != None:
                    break
                cam += 1
                
                
                notifications = item["notifications"]
                temp_cnt = 0
                if len(notifications) != 0:
                    for notification in notifications:
                        responsetype = notification["responsetypes"]
                        temp_cnt += 1
                        responsetypes_keys = ["_id","falseResponse","trueResponse","__v","createdAt","updatedAt"]
                        
                        
                        try:
                            cnt = 0
                            _id = responsetype["_id"]
                            cnt += 1
                            falseResponse = responsetype["falseResponse"]
                            cnt += 1
                            trueResponse = responsetype["trueResponse"]
                            cnt += 1
                            __v = responsetype["__v"]
                            cnt += 1
                            createdAt = responsetype["createdAt"]
                            cnt += 1
                            updatedAt = responsetype["updatedAt"] 
                        
                        except:
                            missing_flag = True

                        if missing_flag == True:
                            status_code = 101
                            error = "Notifications "+ responsetypes_keys[cnt]+" is missing!"
                            break

                        if missing_flag == False:
                            responsetypes_keys = ["_id","falseResponse","trueResponse","__v","createdAt","updatedAt"]
                            
                            cnt = 0
                            if type(_id) == str:
                                cnt +=1
                                if type(falseResponse) == dict:
                                    cnt += 1
                                    if type(trueResponse) == dict:
                                        cnt += 1
                                        if __v == 0 or __v ==1:
                                            cnt += 1
                                            if type(createdAt) == str:
                                                cnt += 1
                                                if type(updatedAt) == str:
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

                            if missing_flag == False and format_flag == True:
                                status_code = 106
                                error = "Notifications "+ responsetypes_keys[cnt]+" is Invalid!"
                                break

                        if missing_flag == False and format_flag == False:
                            responsetypes_keys = ["_id","falseResponse","trueResponse","createdAt","updatedAt"]
                            
                            cnt = 0
                            if len(_id) != 0:
                                cnt +=1
                                if len(falseResponse) != 0:
                                    cnt += 1
                                    if len(trueResponse) != 0:
                                        cnt += 1
                                        if len(createdAt) != 0:
                                            cnt += 1
                                            if len(updatedAt) != 0:
                                                
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
                                status_code = 101
                                error = "Notifications "+ responsetypes_keys[cnt]+" is Missing!"
                                break
                        
                        if missing_flag == False and format_flag == False:
                            falseResponse = responsetype["falseResponse"]
                            cnt = 0
                            responsetypes_keys = ["name","score","colorCode"]
                            try:
                                name = falseResponse["name"]
                                cnt += 1
                                score = falseResponse["score"]
                                cnt += 1
                                colorCode = falseResponse["colorCode"]
                            except:
                                missing_flag = True
                            
                            if missing_flag == True:
                                status_code = 101
                                error = "Notifications "+ responsetypes_keys[cnt]+" is missing!"
                                break

                            if missing_flag == False:
                                cnt = 0
                                if type(name) == str:
                                    cnt += 1
                                    if type(score) == int:
                                        cnt += 1
                                        if type(colorCode) == str:
                                            format_flag = False
                                        else:
                                            format_flag = True
                                    else:
                                        format_flag = True
                                else:
                                    format_flag = True

                                if format_flag == True:

                                    status_code = 106
                                    error = "Notifications "+ responsetypes_keys[cnt]+" is Invalid!"
                                    break
                            responsetypes_keys = ["name","colorCode"]
                            if missing_flag == False and format_flag == False:
                                cnt = 0
                                if len(name) != 0:
                                    cnt += 1
                                    if len(colorCode) != 0:
                                        format_flag = False
                                    else:
                                        format_flag = True
                                else:
                                    format_flag = True
                                if format_flag == True:

                                    status_code = 101
                                    error = "Notifications "+ responsetypes_keys[cnt]+" is Missing!"
                                    break

                        if missing_flag == False and format_flag == False:
                            trueResponse = responsetype["trueResponse"]
                            cnt = 0
                            responsetypes_keys = ["name","score","colorCode"]
                            try:
                                name = trueResponse["name"]
                                cnt += 1
                                score = trueResponse["score"]
                                cnt += 1
                                colorCode = trueResponse["colorCode"]
                            except:
                                missing_flag = True
                            
                            if missing_flag == True:
                                status_code = 101
                                error = "Notifications "+ responsetypes_keys[cnt]+" is Missing!"
                                break

                            if missing_flag == False:
                                cnt = 0
                                if type(name) == str:
                                    cnt += 1
                                    if type(score) == int:
                                        cnt += 1
                                        if type(colorCode) == str:
                                            format_flag = False
                                        else:
                                            format_flag = True
                                    else:
                                        format_flag = True
                                else:
                                    format_flag = True

                                if format_flag == True:

                                    status_code = 106
                                    error = "Notifications "+ responsetypes_keys[cnt]+" is Invalid!"
                                    break
                            
                            if missing_flag == False and format_flag == False:
                                responsetypes_keys = ["name","colorCode"]
                                cnt = 0
                                if len(name) != 0:
                                    cnt += 1
                                    if len(colorCode) != 0:
                                        format_flag = False
                                    else:
                                        format_flag = True
                                else:
                                    format_flag = True
                                if format_flag == True:

                                    status_code = 101
                                    error = "Notifications "+responsetypes_keys[cnt]+" is Missing!"
                                    break

                

            if missing_flag == False and format_flag == False:
                responsetypes_flag = False
            
            else:
                responsetypes_flag = True
                print("____________13")
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                }
                return jsonify(resp)

        if responsetypes_flag == False:
            templates_flag = False
            missing_flag =False
            format_flag = False
            cam = 0
            for item in items:
                if error != None:
                    break
                cam += 1
                notifications = item["notifications"]
                temp_cnt = 0
                if len(notifications) != 0:
                    for notification in notifications:
                        template = notification["templates"]
                        temp_cnt += 1
                        templates_keys = ["_id","email","whatsApp","voice","type","isActive","name","createdBy","__v","createdAt","updatedAt"]
                        
                        
                        try:
                            cnt = 0
                            _id = template["_id"]
                            cnt += 1
                            email = template["email"]
                            cnt += 1
                            whatsApp = template["whatsApp"]
                            cnt += 1
                            voice = template["voice"]
                            cnt += 1
                            _type = template["type"]
                            cnt += 1
                            isActive = template["isActive"]
                            cnt += 1
                            name = template["name"]
                            cnt += 1
                            createdBy = template["createdBy"]
                            cnt += 1
                            __v = template["__v"]
                            cnt += 1
                            createdAt = template["createdAt"]
                            cnt += 1
                            updatedAt = template["updatedAt"] 
                        
                        except:
                            missing_flag = True

                        if missing_flag == True:
                            status_code = 101
                            error = "Notifications "+ templates_keys[cnt]+" is missing!"
                            break

                        if missing_flag == False:
                            templates_keys = ["_id","email","whatsApp","voice","type","isActive","name","createdBy","__v","createdAt","updatedAt"]

                            
                            cnt = 0
                            if type(_id) == str:
                                cnt +=1
                                if type(email) == dict:
                                    cnt += 1
                                    if type(whatsApp) == dict:
                                        cnt += 1
                                        if type(voice) == dict:
                                            cnt += 1
                                            if type(_type) == str:
                                                cnt += 1
                                                if isActive == True or isActive ==False:
                                                    cnt += 1
                                                    if type(name) == str:
                                                        cnt += 1
                                                        if type(createdBy) == str:
                                                            cnt +=1
                                                            if __v == 0 or __v ==1:
                                                                cnt += 1
                                                                if type(createdAt) == str:
                                                                    cnt += 1
                                                                    if type(updatedAt) == str:
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
                                    else:
                                        format_flag = True
                                else:
                                    format_flag = True
                            else:
                                format_flag = True

                            if missing_flag == False and format_flag == True:
                                status_code = 106
                                error = "Notifications "+ templates_keys[cnt]+" is Invalid!"
                                break

                        if missing_flag == False and format_flag == False:
                            templates_keys = ["_id","email","whatsApp","voice","type","name","createdBy","createdAt","updatedAt"]
                            
                            cnt = 0
                            if len(_id) != 0:
                                cnt +=1
                                if len(email) != 0:
                                    cnt += 1
                                    if len(whatsApp) != 0:
                                        cnt += 1
                                        if len(voice) != 0:
                                            cnt += 1
                                            if len(_type) != 0:
                                                cnt += 1
                                                if len(name) != 0:
                                                    cnt += 1
                                                    if len(createdBy) != 0:
                                                        cnt += 1
                                                        if len(createdAt) != 0:
                                                            cnt += 1
                                                            if len(updatedAt) != 0:    
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
                            else:
                                format_flag = True

                            if missing_flag == False and format_flag == True:
                                status_code = 101
                                error = "Notifications "+templates_keys[cnt]+" is Missing!"
                                break
                        
                        if missing_flag == False and format_flag == False:
                            email = template["email"]
                            cnt = 0
                            templates_keys = ["to","bcc","cc","subject","message"]
                            try:
                                to = email["to"]
                                cnt += 1
                                bcc = email["bcc"]
                                cnt += 1
                                cc = email["cc"]
                                cnt += 1
                                subject = email["subject"]
                                cnt += 1
                                message = email["message"]
                            except:
                                missing_flag = True
                            
                            if missing_flag == True:
                                status_code = 101
                                error = "Notifications "+ templates_keys[cnt]+" is missing!"
                                break

                            if missing_flag == False:
                                cnt = 0
                                if type(to) == list:
                                    cnt += 1
                                    if type(bcc) == list:
                                        cnt += 1
                                        if type(cc) == list:
                                            cnt =+ 1 
                                            if type(subject) == str:
                                                cnt += 1
                                                if type(message) == str:
                                        
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

                                if format_flag == True:

                                    status_code = 106
                                    error = "Notifications "+ templates_keys[cnt]+" is Invalid!"
                                    break
                        
                        

                        if missing_flag == False and format_flag == False:
                            whatsApp = template["whatsApp"]
                            cnt = 0
                            templates_keys = ["to"]
                            try:
                                to = whatsApp["to"]
                                
                            except:
                                missing_flag = True
                            
                            if missing_flag == True:
                                status_code = 101
                                error = "Notifications "+ templates_keys[cnt]+" is Missing!"
                                break

                            if missing_flag == False:
                                cnt = 0
                                if type(to) == list:
                                    format_flag = False
                                else:
                                    format_flag = True

                                if format_flag == True:

                                    status_code = 106
                                    error = "Notifications "+ templates_keys[cnt]+" is Invalid!"
                                    break
                        
                        if missing_flag == False and format_flag == False:
                            voice = template["voice"]
                            cnt = 0
                            templates_keys = ["to"]
                            try:
                                to = voice["to"]
                                
                            except:
                                missing_flag = True
                            
                            if missing_flag == True:
                                status_code = 101
                                error = "Notifications "+ templates_keys[cnt]+" is Missing!"
                                break

                            if missing_flag == False:
                                cnt = 0
                                if type(to) == list:
                                    format_flag = False
                                else:
                                    format_flag = True

                                if format_flag == True:

                                    status_code = 106
                                    error = "Notifications "+ templates_keys[cnt]+" is Invalid!"
                                    break

            if missing_flag == False and format_flag == False:
                templates_flag = False
                return None
            
            else:
                templates_flag = True
                print("____________14")
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                }
                return jsonify(resp)

    def check_zone(self):
        items = self.items
        
        main_flag = False
        if main_flag == False:
            missing_flag =False
            format_flag = False
            cam = 0
            error = None
            for item in items:
                if error != None:
                    break
                
                cam += 1
                zones = item["zones"]
                if len(zones) != 0:
                    for zone in zones:
                        zones_keys = ["_id","sensorId","nodeId","coordinate","type","botConfigId","name","__v","createdAt","updatedAt"]
                    
                        try:
                            cnt = 0
                            _id = zone["_id"]
                            cnt += 1
                            sensorId = zone["sensorId"]
                            cnt += 1
                            nodeId = zone["nodeId"]
                            cnt += 1
                            coordinate = zone["coordinate"]
                            cnt += 1
                            _type = zone["type"]
                            cnt += 1
                            botConfigId = zone["botConfigId"]
                            cnt += 1
                            name = zone["name"]
                            cnt += 1
                            __v = zone["__v"]
                            cnt += 1
                            createdAt = zone["createdAt"]
                            cnt += 1
                            updatedAt = zone["updatedAt"]
                            
                            
                        except:
                            missing_flag = True
                        
                        if missing_flag == True:
                            status_code = 101
                            error = str("zones "+ zones_keys[cnt])+" is missing!"
                            break

                        if missing_flag == False:
                            zones_keys = ["_id","sensorId","nodeId","coordinate","type","botConfigId","name","__v","createdAt","updatedAt"]
                            
                            cnt = 0
                            if type(_id) == str:
                                cnt +=1
                                if type(sensorId) == str:
                                    cnt += 1
                                    if type(nodeId) == str:
                                        cnt += 1
                                        if type(coordinate) == list:
                                            cnt += 1
                                            if _type == 1 or _type == 0:
                                                cnt += 1
                                                if type(botConfigId) == str:
                                                    cnt += 1
                                                    if type(name) == str: 
                                                        cnt += 1
                                                        if __v == 1 or __v == 0:
                                                            cnt += 1
                                                            if type(createdAt) == str:
                                                                cnt += 1
                                                                if type(updatedAt) == str: 
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
                                else:
                                    format_flag = True
                            else:
                                format_flag = True


                            if missing_flag == False and format_flag == True:
                                status_code = 106
                                error = str("zones "+ zones_keys[cnt])+" is Invalid!"
                                break
                    
                        if missing_flag == False and format_flag == False:
                            zones_keys = ["_id","sensorId","nodeId","coordinate","botConfigId","name","createdAt","updatedAt"]
                            
                            cnt = 0
                            if len(_id) != 0:
                                cnt +=1
                                if len(sensorId) != 0:
                                    cnt += 1
                                    if len(nodeId) != 0:
                                        cnt += 1
                                        if len(coordinate) != 0: 
                                            cnt += 1
                                            if len(botConfigId) != 0:
                                                cnt +=1
                                                if len(name) != 0:
                                                    cnt += 1
                                                    if len(createdAt) != 0:
                                                        cnt += 1
                                                        if len(updatedAt) != 0: 
                                                            
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
                                status_code = 101
                                error = str("zones "+ zones_keys[cnt])+" is missing!"
                                break
                    

            if missing_flag == False and format_flag == False:
                main_flag = False
                return None
            
            else:
                main_flag = True
                print("____________15")
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                }
                return jsonify(resp)

    def connect_elasticsearch(self):
        db_connect = True
        try:
            _es = Elasticsearch([{'host': HOSTNAME, 'port':DB_PORT}])
            return _es
        except Exception as db_err:
            db_connect = False
            return [db_err, db_connect]

    def verify_ids(self):
        items = self.items
        
        main_flag = False
        flag = False
        if main_flag == False:
            error = None
            for item in items:
                if error != None:
                    break

                if item["botconfigs"]["activityId"] != item["activities"]["_id"]:
                    error = "botconfigs -> activityId and activities -> _id should be same"
                    status_code = 106
                    flag = True
                    break
                if item["botconfigs"]["kpisId"] != item["kpis"]["_id"]:
                    error = "botconfigs -> kpisId and kpis -> _id should be same"
                    status_code = 106
                    flag = True
                    break
                if item["botconfigs"]["siteId"] != item["sites"]["_id"]:
                    error = "botconfigs -> siteId and sites -> _id should be same"
                    status_code = 106
                    flag = True
                    break
                if item["botconfigs"]["nodeId"] != item["nodes"]["_id"]:
                    error = "botconfigs -> nodeId and nodes -> _id should be same"
                    status_code = 106
                    flag = True 
                    break
                if item["botconfigs"]["sensorId"] != item["sensors"]["_id"]:
                    error = "botconfigs -> sensorId and sensors -> _id should be same"
                    status_code = 106 
                    flag = True
                    break
                if item["botconfigs"]["responseTypeId"] != item["responsetypes"]["_id"]:
                    error = "botconfigs -> responseTypeId and responsetypes -> _id should be same"
                    status_code = 106 
                    flag = True
                    break
                if item["botconfigs"]["ruleId"] != item["rules"]["_id"]:
                    error = "botconfigs -> ruleId and rules -> _id should be same"
                    status_code = 106 
                    flag = True
                    break
                notifications = item["notifications"]
                if len(notifications) != 0:
                    for notification in notifications:
                        if notification["notificationconfigs"]["ruleId"] != notification["rules"]["_id"]:
                            error = "notificationconfigs -> ruleId and rules -> _id should be same"
                            status_code = 106 
                            flag = True
                            break

                        if notification["notificationconfigs"]["responseTypeId"] != notification["responsetypes"]["_id"]:
                            error = "notificationconfigs -> responseTypeId and responsetypes -> _id should be same"
                            status_code = 106 
                            flag = True
                            break

                        if notification["notificationconfigs"]["templateId"] != notification["templates"]["_id"]:
                            error = "notificationconfigs -> templateId and templates -> _id should be same"
                            status_code = 106 
                            flag = True
                            break
            if flag == False:
                return None
            
            else:
                print("____________16")
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": str(error),
                    "aividStatusCode": status_code
                }
                return jsonify(resp)

    def update_delete_db(self, old_botconfigs, new_botconfigs, temp_id_1, temp_id_2, temp_id_3, db, item, index_name):
        flag = True
        check_flag = False
        
        if temp_id_1 != None and old_botconfigs[temp_id_1] != new_botconfigs[temp_id_1]:
            try:
                _id = new_botconfigs[temp_id_2]
                db.delete(index=index_name, doc_type="_doc", id = _id)
                new_kpi = item[index_name]
                del new_kpi['_id']
                db.index(index=index_name, doc_type="_doc", id=_id, body=new_kpi)
                flag = False
                check_flag = True
            except Exception as er:
                raise Exception (er)

        elif temp_id_3 != None and old_botconfigs[temp_id_3] != new_botconfigs[temp_id_3]:
            try:
                _id = new_botconfigs[temp_id_2]
                db.delete(index=index_name, doc_type="_doc", id = _id)
                new_kpi = item[index_name]
                del new_kpi['_id']
                db.index(index=index_name, doc_type="_doc", id=_id, body=new_kpi)
                flag = False
                check_flag = True
            except Exception as er:
                raise Exception (er)
                

        elif old_botconfigs[temp_id_2] == new_botconfigs[temp_id_2] and flag == True:
            try:
                _id = new_botconfigs[temp_id_2]
                db.delete(index=index_name, doc_type="_doc", id = _id)
                new_kpi = item[index_name]
                del new_kpi['_id']
                db.index(index=index_name, doc_type="_doc", id=_id, body=new_kpi)
                check_flag = True
            except Exception as er:
                raise Exception (er)
                
                
        elif old_botconfigs[temp_id_2] != new_botconfigs[temp_id_2] and flag == True:
            try:
                _id = new_botconfigs[temp_id_2]
                new_kpi = item[index_name]
                del new_kpi['_id']
                db.index(index=index_name, doc_type="_doc", id=_id, body=new_kpi)
                check_flag = True
            except Exception as er:
                raise Exception (er)
        if check_flag == True:
            return True 

    def update_delete_db_type2(self, old_botconfigs, new_botconfigs, temp_id_1, temp_id_2, temp_id_3, db, item, index_name, ori_index):
        flag = True
        check_flag = False
        
        if temp_id_1 != None and old_botconfigs[temp_id_1] != new_botconfigs[temp_id_1]:
            try:
                _id = new_botconfigs[temp_id_2]
                db.delete(index=ori_index, doc_type="_doc", id = _id)
                new_kpi = item[index_name]
                del new_kpi['_id']
                db.index(index=ori_index, doc_type="_doc", id=_id, body=new_kpi)
                flag = False
                check_flag = True
            except Exception as er:
                raise Exception (er)

        elif temp_id_3 != None and old_botconfigs[temp_id_3] != new_botconfigs[temp_id_3]:
            try:
                _id = new_botconfigs[temp_id_2]
                db.delete(index=ori_index, doc_type="_doc", id = _id)
                new_kpi = item[index_name]
                del new_kpi['_id']
                db.index(index=ori_index, doc_type="_doc", id=_id, body=new_kpi)
                flag = False
                check_flag = True
            except Exception as er:
                raise Exception (er)
                

        elif old_botconfigs[temp_id_2] == new_botconfigs[temp_id_2] and flag == True:
            try:
                _id = new_botconfigs[temp_id_2]
                db.delete(index=ori_index, doc_type="_doc", id = _id)
                new_kpi = item[index_name]
                del new_kpi['_id']
                db.index(index=ori_index, doc_type="_doc", id=_id, body=new_kpi)
                check_flag = True
            except Exception as er:
                raise Exception (er)
                
                
        elif old_botconfigs[temp_id_2] != new_botconfigs[temp_id_2] and flag == True:
            try:
                _id = new_botconfigs[temp_id_2]
                new_kpi = item[index_name]
                del new_kpi['_id']
                db.index(index=ori_index, doc_type="_doc", id=_id, body=new_kpi)
                check_flag = True
            except Exception as er:
                raise Exception (er)
        if check_flag == True:
            return True 

    def post(self):
        items = self.items

        checking_common = self.check_common()
        checking_botconfigs = self.check_botconfigs()
        checking_sites = self.check_sites()
        checking_nodes = self.check_nodes()
        checking_sensors = self.check_sensors()
        checking_rules = self.check_rules()
        checking_responsetypes = self.check_responsetypes()
        checking_activities = self.check_activities()
        checking_kpis = self.check_kpis()
        checking_notification = self.check_notification()
        checking_zone = self.check_zone()
        verifying_ids = self.verify_ids()

        if checking_common == None and checking_botconfigs == None and checking_sites == None and checking_nodes == None and checking_sensors == None and checking_rules == None and checking_responsetypes == None and checking_activities == None and checking_kpis == None and checking_notification == None and checking_zone == None and verifying_ids == None:
            db = self.connect_elasticsearch()
            if type(db) != list and  db.ping() == True:
                try:
                    db.indices.create(index="botconfigs")
                    db.indices.create(index="rules")
                    db.indices.create(index="responsetypes")
                    db.indices.create(index="activities")
                    db.indices.create(index="kpis")
                    db.indices.create(index="templates")
                    db.indices.create(index="notificationconfigs")
                    db.indices.create(index="zones")
                    
                except Exception as db_err:
                    print(db_err)
                
                for item in items:

                    
                    site_lat = item["sites"]["location"]["coordinates"][0]
                    site_lon = item["sites"]["location"]["coordinates"][1]
                    if site_lat < 0:
                        site_lat = "n"+str(site_lat)[1:].replace(".","d")
                    else:
                        site_lat = str(site_lat).replace(".","d")
                    if site_lon < 0:
                        site_lon = "n"+str(site_lon)[1:].replace(".","d")
                    else:
                        site_lon = str(site_lon).replace(".","d")
                    site_index = "sites_"+site_lat+"_"+site_lon

                    node_lat = item["nodes"]["location"]["coordinates"][0]
                    node_lon = item["nodes"]["location"]["coordinates"][1]
                    if node_lat < 0:
                        node_lat = "n"+str(node_lat)[1:].replace(".","d")
                    else:
                        node_lat = str(node_lat).replace(".","d")
                    if node_lon < 0:
                        node_lon = "n"+str(node_lon)[1:].replace(".","d")
                    else:
                        node_lon = str(node_lon).replace(".","d")
                    node_index = "nodes_"+node_lat+"_"+node_lon

                    provision_index = "provisions_"+node_lat+"_"+node_lon
                    return_flag = True

                    # Notification Index
                    notification_flag = True

                    try:
                        db.indices.create(index=site_index)
                    except Exception as err:
                        print(err)
                    try:
                        db.indices.create(index=node_index)
                    except Exception as err:
                        print(err)
                    try:
                        db.indices.create(index=provision_index)
                    except Exception as err:
                        print(err)

                    notifications = item["notifications"]
                    if len(notifications) != 0:
                        for notification in notifications:
                            notificationconfigs = notification["notificationconfigs"]
                            _id = notificationconfigs["_id"]

                            try:
                                note_res = db.get(index = "notificationconfigs", id = _id)
                                note_old_data = note_res["_source"]
                                notification_flag = False
                            except Exception as er:
                                print(er)

                            if notification_flag == True:
                                
                                _rules = notification["rules"]
                                _id = _rules["_id"]
                                del _rules["_id"]
                                db.index(index="rules", doc_type="_doc", id=_id, body=_rules)

                                _responsetypes = notification["responsetypes"]
                                _id = _responsetypes["_id"]
                                del _responsetypes["_id"]
                                db.index(index="responsetypes", doc_type="_doc", id=_id, body=_responsetypes)

                                _templates = notification["templates"]
                                _id = _templates["_id"]
                                del _templates["_id"]
                                db.index(index="templates", doc_type="_doc", id=_id, body=_templates)

                                _notificationconfig = notification["notificationconfigs"]
                                _id = _notificationconfig["_id"]
                                del _notificationconfig["_id"]
                                db.index(index="notificationconfigs", doc_type="_doc", id=_id, body=_notificationconfig)

                            if notification_flag == False:
                                old_note_config = note_old_data
                                new_note_configs = notification["notificationconfigs"]

                                if old_note_config["ruleId"] == new_note_configs["ruleId"]:

                                    try:
                                        _id = new_note_configs["ruleId"]
                                        db.delete(index="rules", doc_type="_doc", id = _id)
                                        new_kpi = notification["rules"]
                                        del new_kpi['_id']
                                        db.index(index="rules", doc_type="_doc", id=_id, body=new_kpi)
                                    except Exception as er:
                                        return_flag = False
                                        print("____________17")
                                        resp = {
                                            "status": False,
                                            "reasonPhrase": "OK",
                                            "statusCode": 422,
                                            "data": [],
                                            "error": str(er),
                                            "aividStatusCode": 117
                                        }
                                        return jsonify(resp)

                                elif old_note_config["ruleId"] != new_note_configs["ruleId"]:
                                    try:
                                        _id = new_note_configs["ruleId"]
                                        new_kpi = notification["rules"]
                                        del new_kpi['_id']
                                        db.index(index="rules", doc_type="_doc", id=_id, body=new_kpi)
                                    except Exception as er:
                                        return_flag = False
                                        print("____________18")
                                        resp = {
                                            "status": False,
                                            "reasonPhrase": "OK",
                                            "statusCode": 422,
                                            "data": [],
                                            "error": str(er),
                                            "aividStatusCode": 117
                                        }
                                        return jsonify(resp)

                                if old_note_config["responseTypeId"] == new_note_configs["responseTypeId"]:

                                    try:
                                        _id = new_note_configs["responseTypeId"]
                                        db.delete(index="responsetypes", doc_type="_doc", id = _id)
                                        new_kpi = notification["responsetypes"]
                                        del new_kpi['_id']
                                        db.index(index="responsetypes", doc_type="_doc", id=_id, body=new_kpi)
                                    except Exception as er:
                                        return_flag = False
                                        print("____________19")
                                        resp = {
                                            "status": False,
                                            "reasonPhrase": "OK",
                                            "statusCode": 422,
                                            "data": [],
                                            "error": str(er),
                                            "aividStatusCode": 117
                                        }
                                        return jsonify(resp)

                                elif old_note_config["responseTypeId"] != new_note_configs["responseTypeId"]:
                                    try:
                                        _id = new_note_configs["responseTypeId"]
                                        new_kpi = notification["responsetypes"]
                                        del new_kpi['_id']
                                        db.index(index="responsetypes", doc_type="_doc", id=_id, body=new_kpi)
                                    except Exception as er:
                                        return_flag = False
                                        print("____________20")
                                        resp = {
                                            "status": False,
                                            "reasonPhrase": "OK",
                                            "statusCode": 422,
                                            "data": [],
                                            "error": str(er),
                                            "aividStatusCode": 117
                                        }
                                        return jsonify(resp)


                                temp_flag = True
                                if old_note_config["createdBy"] != new_note_configs["createdBy"]:
                                    try:
                                        _id = new_note_configs["templateId"]
                                        db.delete(index="templates", doc_type="_doc", id = _id)
                                        new_kpi = notification["templates"]
                                        del new_kpi['_id']
                                        db.index(index="templates", doc_type="_doc", id=_id, body=new_kpi)
                                        temp_flag = False
                                    except Exception as er:
                                        return_flag = False
                                        print("____________21")
                                        resp = {
                                            "status": False,
                                            "reasonPhrase": "OK",
                                            "statusCode": 422,
                                            "data": [],
                                            "error": str(er),
                                            "aividStatusCode": 117
                                        }
                                        return jsonify(resp)

                                elif old_note_config["templateId"] == new_note_configs["templateId"] and temp_flag == True:

                                    try:
                                        _id = new_note_configs["templateId"]
                                        db.delete(index="templates", doc_type="_doc", id = _id)
                                        new_kpi = notification["templates"]
                                        del new_kpi['_id']
                                        db.index(index="templates", doc_type="_doc", id=_id, body=new_kpi)
                                    except Exception as er:
                                        return_flag = False
                                        print("____________22")
                                        resp = {
                                            "status": False,
                                            "reasonPhrase": "OK",
                                            "statusCode": 422,
                                            "data": [],
                                            "error": str(er),
                                            "aividStatusCode": 117
                                        }
                                        return jsonify(resp)

                                elif old_note_config["templateId"] != new_note_configs["templateId"] and temp_flag == True:
                                    try:
                                        _id = new_note_configs["templateId"]
                                        new_kpi = notification["templates"]
                                        del new_kpi['_id']
                                        db.index(index="templates", doc_type="_doc", id=_id, body=new_kpi)
                                    except Exception as er:
                                        print("____________23")
                                        return_flag = False
                                        resp = {
                                            "status": False,
                                            "reasonPhrase": "OK",
                                            "statusCode": 422,
                                            "data": [],
                                            "error": str(er),
                                            "aividStatusCode": 117
                                        }
                                        return jsonify(resp)

                    # Zone index
                    zones = item["zones"]
                    zone_cnt  = 0
                    zone_flag = True
                    if len(zones) != 0:
                        for zone in zones:
                            
                            try:
                                _id = zone["_id"]
                                zone_res = db.get(index="zones", id=_id)
                                zone_old_data = zone_res['_source']
                                zone_flag = False
                            except Exception as er:
                                print(er)

                            if zone_flag == True:
                                _id = zone["_id"]
                                del zone["_id"]
                                db.index(index="zones", doc_type="_doc", id= _id, body = zone)
                        
                            if zone_flag == False:
                                zone_new_data = zone

                                if zone_old_data["sensorId"] != item["botconfigs"]["sensorId"] or zone_old_data["nodeId"] != item["botconfigs"]["nodeId"] or zone_old_data["botConfigId"] != notifications[zone_cnt]["notificationconfigs"]["botConfigId"]:
                                    
                                    try:
                                        _id = zone_new_data["_id"]
                                        db.delete(index="zones", doc_type="_doc", id = _id)
                                        new_kpi = zone
                                        del new_kpi['_id']
                                        db.index(index="zones", doc_type="_doc", id=_id, body=new_kpi)
                                    except Exception as er:
                                        print("____________24")
                                        return_flag = False
                                        resp = {
                                            "status": False,
                                            "reasonPhrase": "OK",
                                            "statusCode": 422,
                                            "data": [],
                                            "error": str(er),
                                            "aividStatusCode": 117
                                        }
                                        return jsonify(resp)
                                    
                                else:
                                    
                                    try:
                                        _id = zone_new_data["_id"]
                                        db.delete(index="zones", doc_type="_doc", id = _id)
                                        new_kpi = zone
                                        del new_kpi['_id']
                                        db.index(index="zones", doc_type="_doc", id=_id, body=new_kpi)
                                    except Exception as er:
                                        return_flag = False
                                        print("____________25")
                                        resp = {
                                            "status": False,
                                            "reasonPhrase": "OK",
                                            "statusCode": 422,
                                            "data": [],
                                            "error": str(er),
                                            "aividStatusCode": 117
                                        }
                                        return jsonify(resp)
                            zone_cnt += 1

                    # Other indexes

                    botconfig = item["botconfigs"]
                    _id = botconfig["_id"]
                    creat_flag = True
                    try:
                        res = db.get(index="botconfigs", id=_id)
                        old_data = res['_source']
                        creat_flag = False
                    except Exception as er:
                        print(er)


                    if creat_flag == True:
                        botconfig = item["botconfigs"]
                        _id = botconfig["_id"]
                        del botconfig['_id']
                        db.index(index="botconfigs", doc_type="_doc", id=_id, body=botconfig)

                        site = item["sites"]
                        _id = site["_id"]
                        del site['_id']
                        db.index(index=site_index, doc_type="_doc", id=_id, body=site)

                        node = item["nodes"]
                        _id = node["_id"]
                        del node['_id']
                        db.index(index=node_index, doc_type="_doc", id=_id, body=node)

                        sensor = item["sensors"]
                        _id = sensor["_id"]
                        del sensor['_id']
                        db.index(index=provision_index, doc_type="_doc", id=_id, body=sensor)

                        rule = item["rules"]
                        _id = rule["_id"]
                        del rule['_id']
                        db.index(index="rules", doc_type="_doc", id=_id, body=rule)

                        responsetype = item["responsetypes"]
                        _id = responsetype["_id"]
                        del responsetype['_id']
                        db.index(index="responsetypes", doc_type="_doc", id=_id, body=responsetype)

                        activitie = item["activities"]
                        _id = activitie["_id"]
                        del activitie['_id']
                        db.index(index="activities", doc_type="_doc", id=_id, body=activitie)

                        kpi = item["kpis"]
                        _id = kpi["_id"]
                        del kpi['_id']
                        db.index(index="kpis", doc_type="_doc", id=_id, body=kpi)

                    if creat_flag == False:
                        old_botconfigs = old_data
                        new_botconfigs = item["botconfigs"]
                        botname = item["kpis"]["botName"]
                        location = item["nodes"]["location"]
                        ip_text = item["sensors"]["rtspUrl"]
                        ip_text = ip_text.split("@")[-1]
                        ip_text = ip_text.split(":")[0]
                        item["sensors"]["algorithm"] = botname
                        item["sensors"]["ip_text"] = ip_text
                        item["sensors"]["office"] = location

                        try:

                            # Kpi___________________________________________________________________________________________________
                            _kpi = self.update_delete_db(old_botconfigs, new_botconfigs, "botId", "kpisId", "activityId",db, item, "kpis")

                            # Activity______________________________________________________________________________________________
                            activity = self.update_delete_db(old_botconfigs, new_botconfigs, "sopId", "activityId", None, db, item, "activities")

                            # Site_____________________________________________________________________________________________________
                            sites = self.update_delete_db_type2(old_botconfigs, new_botconfigs, None, "siteId", None, db, item, "sites", site_index)

                            # Rule______________________________________________________________________________________________________
                            rules = self.update_delete_db(old_botconfigs, new_botconfigs, None , "ruleId", None, db, item, "rules")

                            # Sensor______________________________________________________________________________________________________
                            _sensor = self.update_delete_db_type2(old_botconfigs, new_botconfigs, None , "sensorId", None, db, item, "sensors", provision_index)

                            # Nodes__________________________________________________________________________________________________
                            _nodes = self.update_delete_db_type2(old_botconfigs, new_botconfigs, None , "nodeId", None, db, item, "nodes", node_index)

                            # Nodes__________________________________________________________________________________________________
                            _responsetypes = self.update_delete_db(old_botconfigs, new_botconfigs, None , "responseTypeId", None, db, item, "responsetypes")

                        except Exception as err:
                            return_flag = False
                            print("____________26")
                            resp = {
                                "status": False,
                                "reasonPhrase": "OK",
                                "statusCode": 422,
                                "data": [],
                                "error": str(err),
                                "aividStatusCode": 117
                            }
                            return jsonify(resp)

            elif type(db) == list or db.ping() != True:
                return_flag = False
                if type(db) == list:
                    error = db[0]
                    print("____________27")
                    resp = {
                            "status": False,
                            "reasonPhrase": "OK",
                            "statusCode": 422,
                            "data": [],
                            "error": str(error),
                            "aividStatusCode": 117
                        }
                else:
                    try:
                        db.indices.create(index="botconfigs")
                    except Exception as error:
                        print("____________28")
                        resp = {
                            "status": False,
                            "reasonPhrase": "OK",
                            "statusCode": 422,
                            "data": [],
                            "error": str(error),
                            "aividStatusCode": 117
                        }
                return jsonify(resp)

            if return_flag == True:
                print("____________29")
                resp = {
                    "status": True,
                    "reasonPhrase": "OK",
                    "statusCode": 200,
                    "data": [],
                    "error": None,
                    "aividStatusCode": 110
                }
                return jsonify(resp)
            
                          
            
        elif checking_common != None:
            return checking_common
        elif checking_botconfigs != None:
            return checking_botconfigs
        elif checking_sites != None:
            return checking_sites
        elif checking_nodes != None:
            return checking_nodes
        elif checking_sensors != None:
            return checking_sensors 
        elif checking_rules != None:
            return checking_rules 
        elif checking_responsetypes != None:
            return checking_responsetypes 
        elif checking_activities != None:
            return checking_activities 
        elif checking_kpis != None:
            return checking_kpis 
        elif checking_notification != None:
            return checking_notification
        elif checking_zone != None:
            return checking_zone
        elif verifying_ids != None:
            return verifying_ids

# if __name__ == '__main__':
# 	app.run(host="192.168.1.36", port=4000, debug=True)