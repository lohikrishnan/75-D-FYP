
#import the necessary packages
#import dlib
#import numpy as np
from flask import Flask, Response, render_template
import cv2
import face_recognition

app = Flask(__name__)

# Using opencv modules we are switching on the default Web Camera
webcam = cv2.VideoCapture(0)

# Inorder to verfify the image we have to load a sample image to get all the 128 face dimensions
demo_image = face_recognition.load_image_file(r"C:\Users\DELL\OneDrive\Desktop\Capstone_Phase_01_Demo\Image_Dataset\demo.jpg")
demo_face_encodings = face_recognition.face_encodings(demo_image)[0]

demo_image1 = demo_image = face_recognition.load_image_file(r"C:\Users\DELL\OneDrive\Desktop\Capstone_Phase_01_Demo\Image_Dataset\swaroop.jpg")
demo_face_encodings1 = face_recognition.face_encodings(demo_image1)[0]

# Save all the encodings in a list inorder to verify it further
verified_encodings = [demo_face_encodings, demo_face_encodings1]
verified_face_names = ["You have been verified: Sudharmendra", "You have been verified: Swaroop"] 
#verified_face_names1 = ["You have been verified: Swaroop"] 
# When the face is verified it prints the above statement

# Initializing all the list variables to hold the entire face locations, embeddings, encodings 
total_face_locations = []
total_face_encodings = []
total_face_names = []
@app.route('/')
def index():
    return render_template('index.html')
def gen(video):
    while True:
        # We must get the currrent frame from the scanned video as an image
        keys,curr = webcam.read()
        # Resizing the current obtained frame to 1/4 size inorder to proces it faster
        small_curr = cv2.resize(curr, (0,0), fx=0.25, fy=0.25)
        # Detecting faces in the image
        # Important arguments: image, upsample number, and the model used
        total_face_locations = face_recognition.face_locations(small_curr, number_of_times_to_upsample=2, model='hog')
        
        # Retreiving all face encodings for the face detected
        total_face_encodings = face_recognition.face_encodings(small_curr, total_face_locations)
    
        # We must loop through all the face embeddings and the face locations
        for curr_face_loc, curr_face_encoding in zip(total_face_locations, total_face_encodings):
            # Split the tuple inorder to get all the four position values of current face
            top_position, right_position, bottom_position, left_position = curr_face_loc
            
            # Changing the position maginitude inorder to fit in the obtained video frame
            top_position = top_position*4
            right_position = right_position*4
            bottom_position = bottom_position*4
            left_position = left_position*4
            
            # Get te list of all the matches
            total_matches = face_recognition.compare_faces(verified_encodings, curr_face_encoding)
           
            # If the validation is Unsuccessful then the below line will be printed
            name_user = 'Validation Unsuccessful: Unknown face'
            
            # Checking if the all the matches have at least one index
            # If yes, retreive the index number
            # After getting the name that corresponds to the index number store the same into a variable
            if True in total_matches:
                matching_index = total_matches.index(True)
                #print(matching_index)
                name_user = verified_face_names[matching_index]
                
                
            
            # Drawing rectangle around the face    
            cv2.rectangle(curr,(left_position, top_position),(right_position, bottom_position),(255,0,0),2)
            
            # Display the name as text inside the image with random FONT
            font_displayed = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(curr, name_user, (left_position, bottom_position), font_displayed, 0.5, (255,255,255),1)
        
        # Display the final video
        #cv2.imshow("Final Recognized Webcam Video",curr)
        
        image = curr
        # Release the camera and the stream
        '''
        webcam.release()
        cv2.destroyAllWindows() 
        '''
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True)
    
'''
from flask import Flask, render_template, Response
from camera import Camera
app = Flask(__name__)
@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')
def gen(camera1):
    while True:
        #get camera frame
        frame = camera1.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='2204', debug=True)
    
'''
    
    