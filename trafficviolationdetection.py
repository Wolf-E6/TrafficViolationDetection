# -*- coding: utf-8 -*-
"""TrafficViolationDetection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zRd8qroT3LJza_pDbvYF0sHoDAymzMG0
"""

import cv2
import mediapipe as mp
import numpy as np
from google.colab.patches import cv2_imshow
import torch

# Load YOLOv5 model
yolo_model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, model_complexity=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Load video
cap = cv2.VideoCapture('/content/Roadsafetyviolation_14.mp4')
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Initialize variables to track vehicle movement for illegal U-turn detection
vehicle_positions = {}
illegal_uturn_flagged = False

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Error: Failed to read frame.")
        break

    # Convert the image to RGB for pose detection
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    # YOLOv5 Object Detection
    yolo_results = yolo_model(frame)
    detections = yolo_results.pred[0]  # Get detections for the frame

    # Draw bounding boxes from YOLO and track positions
    for *box, conf, cls in detections:
        x1, y1, x2, y2 = map(int, box)
        label = f"{yolo_results.names[int(cls)]} {conf:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Track vehicles for illegal U-turn detection
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        vehicle_id = f"{int(cls)}-{center_x}-{center_y}"  # Unique identifier based on class and position

        # Update vehicle positions
        if vehicle_id in vehicle_positions:
            prev_x, prev_y = vehicle_positions[vehicle_id]
            # Check if direction has reversed within a short span, indicating a potential illegal U-turn
            if abs(center_x - prev_x) > 50 and not illegal_uturn_flagged:  # Threshold for direction change
                cv2.putText(frame, "Illegal U-turn Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                illegal_uturn_flagged = True
        vehicle_positions[vehicle_id] = (center_x, center_y)

    # Draw pose landmarks if detected for phone usage detection
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
        )

        # Get key landmarks for phone usage detection
        landmarks = results.pose_landmarks.landmark
        left_hand = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]
        right_hand = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]
        left_ear = landmarks[mp_pose.PoseLandmark.LEFT_EAR]
        right_ear = landmarks[mp_pose.PoseLandmark.RIGHT_EAR]

        # Check if hands are near the head (phone usage detection)
        def is_near_head(hand, ear, threshold=0.1):
            distance = np.sqrt((hand.x - ear.x)**2 + (hand.y - ear.y)**2)
            return distance < threshold

        if is_near_head(left_hand, left_ear) or is_near_head(right_hand, right_ear):
            cv2.putText(frame, "Phone Usage Detected", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame with object detection and pose landmarks
    cv2_imshow(frame)

    # Use a small delay between frames
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
pose.close()