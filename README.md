# AI Vision - Real-Time Object Detection

## Project Overview
AI Vision is a Python-based real-time object detection system. It uses a webcam, OpenCV, and the YOLOv8 object-detection model to identify objects in live video.

The program draws a bounding box around detected objects, displays the object name and confidence score, and shows a live count of each detected object.

## Features
- Real-time webcam detection
- YOLOv8 object detection
- Bounding boxes around detected objects
- Confidence percentage for each detection
- Object-wise counting
- Total visible object count
- Different colours for common object classes
- Simple keyboard control: press `Q` to exit

## Technologies / Tools
- Python 3
- OpenCV
- Ultralytics YOLO
- YOLOv8s pretrained model
- Collections Counter

## Project Structure
```text
AI_Vision_Object_Detection/
├── main.py
├── requirements.txt
├── README.md
├── statement.md
├── .gitignore
├── docs/
│   └── pseudocode.md
└── assets/
    └── screenshots/
```

## Installation

1. Install Python 3.
2. Open a terminal in the project folder.
3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. The `yolov8s.pt` model can be downloaded automatically by Ultralytics when the program is first run, depending on your installed version and internet connection.

## Run the Project

```bash
python main.py
```

Allow camera access if your operating system asks for permission.

Press **Q** while the camera window is active to stop the program.

## Testing Instructions
Test the system with:
- One person in front of the camera.
- Multiple people.
- A phone, laptop, bottle, chair, or other common object.
- Vehicles or bicycles where visible.
- Different distances and lighting conditions.

Check that:
1. A bounding box appears around detected objects.
2. The correct object name is shown.
3. A confidence percentage is displayed.
4. Object counts update as objects enter or leave the frame.
5. The total object count is updated.
6. Pressing `Q` closes the camera window safely.

## Important Note
The current program counts objects visible in the current video frame. It does not track the same object across multiple frames, so the count can change as detections change.

## Future Scope
- Add object tracking.
- Add detection history and logging.
- Save annotated video.
- Add a graphical dashboard.
- Add alerts for selected objects.
- Add image/video file input in addition to the webcam.
