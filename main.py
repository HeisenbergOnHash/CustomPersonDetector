

# # Example usage
# # folder_path = '/Users/heisenberg/Desktop/AI_Detector/trainer/data/chaithu'
# # rename_images_in_folder(folder_path)


from predictor.predictor import predict_image
from trainer.modelmaker import modelmaker
import os,cv2


# folders = {
#         "/Users/heisenberg/Desktop/AI_Detector/trainer/data/prudhvi": "prudhvi",
#         "/Users/heisenberg/Desktop/AI_Detector/trainer/data/chaithu": "chaithu",
#     }

# modelmaker(folders)



# Path to test images
test_image_path = [
    "/Users/heisenberg/Desktop/AI_Detector/chaithu_005.jpg",
    "/Users/heisenberg/Desktop/AI_Detector/prudhvi_013.jpg"
]

  
for i in test_image_path:
  if os.path.exists(i):
    print(f"\nRunning prediction on the test image: {i}")
    prediction, confidence = predict_image(i)