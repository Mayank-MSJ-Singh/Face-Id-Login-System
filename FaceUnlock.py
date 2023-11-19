
import face_recognition

def detection(encoding, frame):
    try:
      frame_image = face_recognition.face_encodings(frame)[0]
      result = face_recognition.compare_faces(encoding, frame_image)

      for i in result:
        if i:
            return "Hello"
    except:
        pass
