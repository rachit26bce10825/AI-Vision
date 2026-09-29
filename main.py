import cv2
from ultralytics import YOLO
from collections import Counter

# Load YOLO model
yolo = YOLO("yolov8s.pt")

# BGR colours for different objects
box_colour = {
    "person": (0, 255, 0),
    "car": (255, 0, 0),
    "truck": (0, 0, 255),
    "bus": (0, 165, 255),
    "bicycle": (0, 255, 255),
    "motorcycle": (255, 0, 255)
}

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Unable to access the camera.")
    exit()

while camera.isOpened():

    success, img = camera.read()

    if not success:
        print("No frame received.")
        break

    # Run object detection
    output = yolo.predict(
        img,
        conf=0.45,
        verbose=False
    )[0]

    detected = []

    # Read every detected object
    for item in output.boxes:

        confidence = float(item.conf[0])

        class_no = int(item.cls[0])
        object_name = yolo.names[class_no]

        if confidence < 0.45:
            continue

        detected.append(object_name)

        # Get bounding-box coordinates
        left, top, right, bottom = map(
            int,
            item.xyxy[0]
        )

        colour = box_colour.get(
            object_name,
            (255, 255, 255)
        )

        # Draw detection box
        cv2.rectangle(
            img,
            (left, top),
            (right, bottom),
            colour,
            2
        )

        # Show name and confidence
        caption = f"{object_name} : {confidence * 100:.1f}%"

        cv2.putText(
            img,
            caption,
            (left, max(top - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            colour,
            2
        )

    # Count detected objects
    object_count = Counter(detected)

    # Display counts on the screen
    position = 30

    for obj in sorted(object_count):

        text = f"{obj} = {object_count[obj]}"

        cv2.putText(
            img,
            text,
            (15, position),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2
        )

        position += 28

    # Number of objects currently visible
    cv2.putText(
        img,
        f"Total objects: {len(detected)}",
        (15, position + 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 255),
        2
    )

    cv2.imshow("AI Vision - Object Detection", img)

    # Press Q to close
    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
