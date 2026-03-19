from ultralytics import YOLO
import cv2

# Load pretrained YOLO model
model = YOLO("yolov8n.pt")

# Load image
img_path = "test.jpg"
img = cv2.imread(img_path)

# Run detection
results = model(img)

car_count = 0

for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])
        
        # COCO class 2 = car
        if cls == 2:
            car_count += 1
            
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(img, "Car", (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

# Show result
cv2.putText(img, f"Cars: {car_count}", (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

cv2.imshow("YOLO Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

total_slots = 20
empty = total_slots - car_count

print("Occupied:", car_count)
print("Empty:", empty)