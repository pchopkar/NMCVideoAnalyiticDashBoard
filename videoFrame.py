import cv2
import numpy as np
from flask import Flask, request,render_template
from pymongo import MongoClient
from datetime import datetime
import os
import connect as c

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_video():
    client = c.connectdb()
    db = client.get_database("NMCVideoAnalytic")
    collection = db.nmcimages2
    if request.method == 'POST':
        video_file = request.files['video_file']

        # Convert the video file to a numpy array
        video_np = np.frombuffer(video_file.read(), dtype=np.uint8)

        # Open the video using OpenCV
        video = cv2.VideoCapture(video_np)

        # Get the video frame rate
        fps = video.get(cv2.CAP_PROP_FPS)

        # Calculate the number of frames to skip between each output frame
        skip_frames = int(fps / 15)

        # Get the video's name
        video_name = os.path.basename(video.get(cv2.CAP_PROP_POS_AVI_RATIO))

        # Initialize frame counter
        frame_count = 0

        while True:
            # Read a frame from the video
            ret, frame = video.read()

            # Break the loop if we've reached the end of the video
            if not ret:
                break

            # Only save every nth frame
            if frame_count % skip_frames == 0:
                # Encode the frame in JPEG format
                _, frame_buf = cv2.imencode('.jpg', frame)

                # Convert the image to binary
                frame_binary = frame_buf.tobytes()

                now = datetime.utcnow()
                date = now.strftime("%B %d, %Y")
                timed = now.strftime("%I:%M %p")
                # Create a document to insert into MongoDB
                document = {
                    "frame_number": frame_count,
                    "image_name": video_name,
                    "frame_data": frame_binary,
                    "count" : None,
                    "date": date,
                    "time": timed,
                    "medicle_college" : "Nagpur Medical College",
                    "camera_location_area" : "OPD",
                    "camera_location_sub_area" : "Gynaecological"
                }
                # Insert the document into MongoDB
                collection.insert_one(document)
            # Increment the frame counter
            frame_count += 1

        # Release the video file
        video.release()
    return render_template("success.html") 