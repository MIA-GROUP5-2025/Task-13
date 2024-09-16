import cv2
from ultralytics import YOLO

class detection:
    # Load a pretrained YOLOv8n model
    def __init__(self):
        self.model = YOLO("best.pt")
        self.cap = None

    def detect_camera(self):
        # Open a camera feed (0 is typically the default camera)
        self.cap = cv2.VideoCapture(0)
        # Set frame size (optional)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

    # Loop to read and process each frame
    def detect(self,ret,frame):
        if not ret:
            print("Failed to grab frame")
            return None
        center_x = None
        center_y = None
        class_id = None
        # Run inference on the frame
        results = self.model.predict(frame, imgsz=640, conf=0.5,verbose=False)
        # Extract the bounding boxes and calculate their centers
        for box in results[0].boxes:
            x1, y1, x2, y2 = box.xyxy[0]  # Coordinates of the bounding box
            confidence = box.conf[0]  # Confidence score
            # 0:x, 1:0
            class_id = box.cls[0]  # Class ID of the detected object
            print("confidence:", confidence)
            print("class_id:", class_id)
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            print(f"Center of the bounding box: ({center_x:.2f}, {center_y:.2f})")
        # Visualize the results on the frame
        annotated_frame = results[0].plot()  # YOLOv8 plotting method for visualizing results

        # Display the frame with YOLO predictions
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        return [center_x,center_y,class_id]

    def close_window(self):
        # Release the video capture object and close windows
        self.cap.release()
        cv2.destroyAllWindows()