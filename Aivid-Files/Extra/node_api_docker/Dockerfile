FROM python:3.7

RUN  pip install Flask==1.1.2 && pip install elasticsearch==7.13.0 && pip install WSdiscovery==2.0.0 && pip install sockets==1.0.0 && pip install onvif-zeep==0.2.12 && pip install flask_cors==3.0.10 && pip install getmac==0.8.2 && pip install opencv-python 

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python
RUN apt-get install ffmpeg libsm6 libxext6  -y


RUN mkdir /video_uploads

ENV "HOSTNAME"="localhost"
ENV "DB_PORT"=30892
ENV "API_PORT"=4003
ENV "UPLOAD_LOCATION"=/video_uploads
COPY . .

RUN python setup_onvif.py install

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]