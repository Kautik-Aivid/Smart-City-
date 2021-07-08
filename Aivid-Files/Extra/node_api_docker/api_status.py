from flask import Flask, jsonify
from flask_cors import CORS
import time
app = Flask(__name__)
CORS(app)

class Status:

    def status(self):
        timestamp = time.time()
        return jsonify({"message":"request received",
                        "timestamp":int(timestamp)})     