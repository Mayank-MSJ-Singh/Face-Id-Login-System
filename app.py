from flask import Flask, render_template, Response, redirect, url_for, session
import cv2
import face_recognition
import os
import FaceUnlock

app = Flask(__name__)



camera = cv2.VideoCapture(0)
a = 0
encoding = []
names = []

for image in os.listdir('Faces'):
    face_image = face_recognition.load_image_file(f'Faces/{image}')
    face_encoding = face_recognition.face_encodings(face_image)[0]

    encoding.append(face_encoding)
    names.append(image.split(".")[0])
def generate_frames():
    global encoding, result
    while True:
            success, frame = camera.read()
            frame_useful = cv2.flip(frame, 1)
            if not success:
                break
            else:
                    result = FaceUnlock.detection(encoding,frame_useful)
                    print(result)

                    ret, buffer = cv2.imencode('.jpg', frame_useful)
                    frame_useful = buffer.tobytes()
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + frame_useful + b'\r\n')

def results():
    global result
    return result

@app.route('/')
def loginpage():  # put application's code here
    return render_template("loginPage.html")


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/IdUnlock', methods = ['POST', 'GET'])
def IdUnlock():
    return render_template('IdUnlockPage.html')

@app.route('/check_face_recognition')
def check_face_recognition():
    if results() == "Hello":
        return redirect(url_for('LoggedIn'))
    return "Face not Known"
@app.route("/LoggedIn")
def LoggedIn():
    return "Redirected"


if __name__ == '__main__':
    app.run()
