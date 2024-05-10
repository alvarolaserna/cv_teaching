import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Open the video input
video_path = 0
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True, verbose=False)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # for result in results:
        #     for i in range(len(result.boxes.data.tolist())):
        #         data = result.boxes.data.tolist()[i]
        #         if len(data) == 7:
        #             xmin, ymin, xmax, ymax, id, confidence, class_id = data
        #             print(result.names[class_id], id)

        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()