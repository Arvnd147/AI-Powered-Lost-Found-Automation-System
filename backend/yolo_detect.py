import cv2
import numpy as np
import requests
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_objects(image_url):
    response = requests.get(image_url, stream=True)
    
    if response.status_code != 200:
        return {"error": "Failed to fetch the image."}

    image = np.asarray(bytearray(response.content), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    results = model(image)
    detected_objects = [results.names[int(cls)] for cls in results[0].boxes.cls]

    return detected_objects