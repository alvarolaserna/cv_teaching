
import cv2
import easyocr


# Open the video input
video_path = 0
cap = cv2.VideoCapture(video_path)
reader= easyocr.Reader(['en'])
# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    output_txts = reader.readtext(image=frame, batch_size=3, canvas_size=500, paragraph=True)
    # read all the text and mark them in the frame
    for output_txt in output_txts:
        coordinates = [output_txt[0][0][0], output_txt[0][0][1], output_txt[0][2][0], output_txt[0][2][1]]
        # draw a rectangle with OpenCV over the text recognised
        frame = cv2.rectangle(
            frame,
            pt1=(coordinates[0],coordinates[1]),
            pt2=(coordinates[2],coordinates[3]),
            color=(0, 255, 0),
            thickness=3,
        )
        x, y = coordinates[0],coordinates[1]
        # Write the text recognised on top of the rectangle where the text is placed
        cv2.putText(
            frame, output_txt[1], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 3
        )
    # Display the annotated frame
    cv2.imshow("OCR Tracking", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()