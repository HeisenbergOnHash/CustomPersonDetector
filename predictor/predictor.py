

import cv2,os,joblib,face_recognition

save_folder = "/Users/heisenberg/Desktop/AI_Detector/saved_predictions"
classifier_location = '/Users/heisenberg/Desktop/AI_Detector/trainer/model/person_classification_model.pkl'

def load_image(img_path):
  if img_path.lower().endswith(('.jpg', '.jpeg', '.png')):
    return cv2.imread(img_path)
  print(f"Unsupported format: {img_path}")
  return None

def predict_image(img_path):
  classifier = joblib.load(classifier_location)
  img = cv2.imread(img_path)
  img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  face_encoding = face_recognition.face_encodings(img_rgb)
  
  if not face_encoding:
    print("No face features detected in the image.");return
  
  # Make prediction on the first detected face (if multiple faces are detected, you can choose the one with the highest confidence)
  prediction = classifier.predict([face_encoding[0]])
  confidence = classifier.predict_proba([face_encoding[0]])  # Get prediction probabilities
  
  # Print prediction and confidence
  print(f"Prediction: {prediction[0]}")
  print(f"Confidence: {confidence.max() * 100:.2f}%")

  if prediction[0]:
    img = load_image(img_path)
    if img is not None:
      save_path = os.path.join(save_folder, f"{prediction[0]}_{os.path.basename(img_path)}")
      cv2.imwrite(save_path, img);print(f"Image saved at: {save_path}")
  
  return prediction[0], confidence.max()

