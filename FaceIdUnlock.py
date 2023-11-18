import cv2
import face_recognition
import os

cap = cv2.VideoCapture(0)
break_sys = 0

encoding = []
names = []

for image in os.listdir('Faces'):
    face_image = face_recognition.load_image_file(f'Faces/{image}')
    face_encoding = face_recognition.face_encodings(face_image)[0]

    encoding.append(face_encoding)
    names.append(image.split(".")[0])
while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

        try:
            frame_image = face_recognition.face_encodings(frame)[0]
            result = face_recognition.compare_faces(encoding, frame_image)

            for i in result:
                if i:
                    break_sys = 0
                    print("Hello")

            if break_sys == 1:
                   break
        except:
            pass
