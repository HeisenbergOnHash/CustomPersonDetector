import os

def rename_images_in_folder(folder_path, prefix="chaithu"):
  files = os.listdir(folder_path);files.sort()
  for i, file in enumerate(files):
    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
      new_filename = f"{prefix}_{i+1:03d}.jpg"
      current_file_path = os.path.join(folder_path, file)
      new_file_path = os.path.join(folder_path, new_filename)
      os.rename(current_file_path, new_file_path)
      print(f"Renamed {file} to {new_filename}")
  print("Renaming complete.")
