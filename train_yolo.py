from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml").load("yolov8n.pt")

# Use the model
model.train(data="/Users/alvarolaserna/Github/AI_automation/cv_teaching/data/example.yaml", epochs=100, imgsz=640)  # train the model
# metrics = model.val()  # evaluate model performance on the validation set
# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
# path = model.export(format="onnx")  # export the model to ONNX format