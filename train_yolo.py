from pathlib import Path
from ultralytics import YOLO

# Build the absolute path programmatically, relative to this script.
# This will work on both MacOS and Windows.
BASE_DIR = Path(__file__).resolve().parent
data_path = BASE_DIR / "data" / "example.yaml"  # adjust the relative path as needed

# Load a model
model = YOLO("yolov8n.yaml").load("yolov8n.pt")

# Use the model with the absolute path
model.train(data=str(data_path), epochs=100, imgsz=640)  # train the model
# metrics = model.val()  # evaluate model performance on the validation set
# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
# path = model.export(format="onnx")  # export the model to ONNX format