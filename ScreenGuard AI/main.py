import cv2
from utils.detector import detect_objects
from notifications.alert import send_alert
from utils.detector import get_class_name

camera = cv2.VideoCapture(0)
previous_status = "SAFE"

while True:
    ret, frame = camera.read()
    if not ret:
        break

    detections, annotated_frame = detect_objects(frame)

    person_count = 0

    for box in detections:
        class_id = int(box.cls[0])
        cclass_name = get_class_name(class_id)

        if cclass_name == "person":
            person_count += 1

    print("عدد الأشخاص:", person_count)

    if person_count == 1:
        status = "SAFE"
    else:
        status = "SECURITY ALERT"

    if status == "SECURITY ALERT" and previous_status != "SECURITY ALERT":
        send_alert()

    previous_status = status

    if status == "SAFE":
        color = (0, 255, 0)
    else:
        color = (0, 0, 255)

    cv2.putText(
        annotated_frame,
        status,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        2
    )

    cv2.imshow('Camera Feed', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
