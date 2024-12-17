import cv2
from ultralytics import YOLO
import os
import csv
import sys
from pathlib import Path
import subprocess

# Meassure the time between first_label and second_label. Use a reference_label to reset the values and get a new meassure
def coldAppStartup(model, video_path, first_label, second_label, reference_label):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("File to analyse: ", video_path, ". FrameRate: ", fps)

    notified = False
    first_label_detected = False
    first_label_detected_frame = 0
    second_label_detected = False
    second_label_detected_frame = 0
    latency_frames = []
    
    frame_number = 0
    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 tracking on the frame, persisting tracks between frames
            results = model.track(frame, persist=True, verbose=False)
            
            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            for result in results:
                for i in range(len(result.boxes.data.tolist())):
                    data = result.boxes.data.tolist()[i]
                    if len(data) == 7:
                        xmin, ymin, xmax, ymax, id, confidence, class_id = data
                    if len(data) == 6:
                        xmin, ymin, xmax, ymax, confidence, class_id = data
                    #print(result.names[class_id])
                    if (result.names[class_id] == first_label and not first_label_detected):
                        first_label_detected = True
                        first_label_detected_frame = frame_number
                        #print(result.names[class_id], " detected in frame: ", first_label_detected_frame)
                    if (result.names[class_id] == second_label and not second_label_detected):
                        second_label_detected = True
                        second_label_detected_frame = frame_number
                        #print(result.names[class_id], " detected in frame: ", second_label_detected_frame)
                    if (result.names[class_id] == reference_label):
                        #print(result.names[class_id], " detected in frame: ", frame_number)
                        first_label_detected = False
                        first_label_detected_frame = 0
                        second_label_detected = False
                        second_label_detected_frame = 0
                        notified = False

            # Display the annotated frame
            cv2.imshow("YOLOv8 Tracking", annotated_frame)
            frame_number += 1

            if first_label_detected and second_label_detected and not notified:
                # If both labels were detected, then latency is calculated 
                latency = (second_label_detected_frame - first_label_detected_frame)/fps
                latency_frames.append(latency)
                print("Latency detected between ", first_label, " and ", second_label, " is ", latency, " seconds")
                notified = True    

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    cap.release()
    return latency_frames # array of seconds

model = YOLO('resources/best-youtube.pt')
# Specify the folder path where the videos are
video_path = sys.argv[1]
# Specify the application we want to analyse 
application = sys.argv[2]
# Specify the scenario we want to meassure
scenario = sys.argv[3]


print("Looking for files in: ", video_path)
file_with_results = video_path + "-latencies.csv"
path_file_encoded = video_path.replace("recording", "recording-encoded")
number_frame = 0

path_file_encoded = video_path
if os.path.isfile(path_file_encoded):
    latency = []

    match application:
        case 'YouTube':
            match scenario:
                case 'ColdAppStartup':
                    print(scenario)
                    latency = coldAppStartup(model, path_file_encoded, "youtube_opening", "youtube_feed_full", "youtube_icon")
                case 'WarmAppStartup':
                    print(scenario)
        case _:
            print("Default case executed")    

    print("Latencies: ", latency)
    # Release the video capture object and close the display window
    cv2.destroyAllWindows()

    # Write a file with the results
    with open(file_with_results, 'w') as f:
            csv.writer(f, delimiter=',').writerow(latency)
      
print("All files processed")
