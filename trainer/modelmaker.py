from trainer.src.trainer import train_model

def modelmaker(folders):
    print("Starting model training...")
    train_model(folders)
    print("Model training completed and saved.")
