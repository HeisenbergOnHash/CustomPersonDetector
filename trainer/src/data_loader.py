
import os,cv2
import face_recognition

def load_images_from_folders(folders):
  images = [];labels = []
  for folder, label in folders.items():
    for filename in os.listdir(folder):
      if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        img_path = os.path.join(folder, filename)
        img = cv2.imread(img_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_encoding = face_recognition.face_encodings(img_rgb)
        if face_encoding:images.append(face_encoding[0]);labels.append(label)             
  return images, labels
