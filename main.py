import cv2
from ultralytics import YOLO

# Load a pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")  # You can replace "yolov8n.pt" with any other YOLO model

# Access the webcam
cap = cv2.VideoCapture(0)  # 0 for the default camera

while cap.isOpened():
    success, frame = cap.read()

    if success:
        # Run inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("Webcam", annotated_frame)

        # Press 'q' to exit
        if cv2.waitKey(1) == ord('q'): 
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()