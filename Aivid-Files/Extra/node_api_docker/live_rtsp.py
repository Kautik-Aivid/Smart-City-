from flask import Flask, Response, request
import cv2
import threading
import cv2 as cv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class FreshestFrame(threading.Thread):
	def __init__(self, capture, name='FreshestFrame'):
		self.capture = capture
		assert self.capture.isOpened()

		# this lets the read() method block until there's a new frame
		self.cond = threading.Condition()

		# this allows us to stop the thread gracefully
		self.running = False

		# keeping the newest frame around
		self.frame = None

		# passing a sequence number allows read() to NOT block
		# if the currently available one is exactly the one you ask for
		self.latestnum = 0
		
		super().__init__(name=name)
		self.start()

	def start(self):
		self.running = True
		super().start()

	def release(self, timeout=None):
		self.running = False
		self.join(timeout=timeout)
		self.capture.release()

	def run(self):
		counter = 0
		while self.running:
			# block for fresh frame
			(rv, img) = self.capture.read()
			assert rv
			counter += 1

			# publish the frame
			with self.cond: # lock the condition for this operation
				self.frame = img if rv else None
				self.latestnum = counter
				self.cond.notify_all()

	def read(self, wait=True, seqnumber=None, timeout=None):

		with self.cond:
			if wait:
				if seqnumber is None:
					seqnumber = self.latestnum+1
				if seqnumber < 1:
					seqnumber = 1
				
				rv = self.cond.wait_for(lambda: self.latestnum >= seqnumber, timeout=timeout)
				if not rv:
					return (self.latestnum, self.frame)

			return (self.latestnum, self.frame)

class LiveRtsp(FreshestFrame):

    def __init__(self):
        self.rtsp_url = request.args.get("rtsp")
        

    def gen_frames(self):

        if self.rtsp_url == "None" or self.rtsp_url == "none":
            while True:
            # Capture frame-by-frame
                frame = cv2.imread("No_Image_Available.jpg")  # read the camera frame
               
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
        else:

            cap = cv.VideoCapture(str(self.rtsp_url))
            cap.set(cv.CAP_PROP_BUFFERSIZE, 1)
            
            fresh = FreshestFrame(cap)
            cnt = 0
            while True:
                # Capture frame-by-frame
                success,frame = fresh.read(seqnumber=cnt+1)  # read the camera frame
                if not success:
                    break
                else:
                    ret, buffer = cv2.imencode('.jpg', frame)
                    frame = buffer.tobytes()
                    yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


    @app.route('/video_feed')
    def video_feed(self):
        return Response(self.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


