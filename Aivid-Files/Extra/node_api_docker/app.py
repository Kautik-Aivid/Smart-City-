
from flask import Flask
from os import environ
from onvif_app import onvif
from common import CommonData
from live_rtsp import LiveRtsp
from validate import ValidateData
from upload_file import UploadVideo
from api_status import Status
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_PORT = environ.get('API_PORT')

app.config["JSON_SORT_KEYS"] = False

@app.route('/onvif', methods=['POST'])
def OnvifDiscovery_post():
    return onvif.post()

@app.route('/common', methods=['POST'])
def getcommon_post():
    return CommonData().post()

@app.route('/validate', methods=['POST'])
def validate_post():
    return ValidateData().post()

@app.route('/live_rtsp',methods=['GET','POST'])
def live_rtsp():
    return LiveRtsp().video_feed()

@app.route('/uploader', methods = ['GET','POST'])
def uploadvideo_rtsp():
    return UploadVideo().upload_file()

@app.route('/nodeapi')
def status():
    return Status().status()


if __name__ == '__main__':
	# app.run(debug=True)
    app.run(host = "0.0.0.0",port=API_PORT)
