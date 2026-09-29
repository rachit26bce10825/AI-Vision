# Project Statement

## Problem Statement
Manual identification and counting of objects in a live scene can be slow and difficult, especially when several objects are present at the same time. A computer-vision system is needed to automatically identify visible objects and provide useful information in real time.

## Scope of the Project
The project focuses on real-time object detection through a webcam. It uses YOLOv8 to detect objects and OpenCV to process and display the camera frames. The system provides object labels, confidence values, bounding boxes, and current-frame counts.

## Target Users
- Students learning computer vision and AI
- Beginners working with Python and OpenCV
- Demonstration and academic project users
- Developers experimenting with real-time object detection

## High-Level Features
1. Capture frames from the webcam.
2. Send each frame to the YOLOv8 model.
3. Read detected object classes and confidence values.
4. Draw bounding boxes and labels.
5. Count detected objects by class.
6. Display the total number of visible objects.
7. Allow the user to stop the application with the Q key.
