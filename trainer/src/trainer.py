
import joblib,os
from sklearn.svm import SVC
from trainer.src.data_loader import load_images_from_folders


def train_model(folders):
  print("Loading and encoding images...")
  images, labels = load_images_from_folders(folders)
  if not images:print("No images found or encodings failed.");return
  print("Training SVM classifier...")  # Train the classifier
  classifier = SVC(kernel='linear', probability=True)
  classifier.fit(images, labels)
  # Create model directory if not exists
  os.makedirs('trainer/model', exist_ok=True) 
  # Save the trained model and embeddings
  joblib.dump(classifier, 'trainer/model/person_classification_model.pkl')
  joblib.dump(images, 'trainer/model/person_embeddings.pkl')
  print("Model and embeddings saved successfully.")

