from ultralytics import YOLO
model = YOLO("yolov8n.pt")
def get_class_name(class_id):
    return model.names[class_id]
def detect_objects(frame):
    #results = model(frame)
    results = model(
    frame,
    conf=0.6,
    classes=[0],
    verbose=False
)
    annotated_frame = results[0].plot()
    return results[0].boxes, annotated_frame
