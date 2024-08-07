from ultralytics import YOLO
import cvzone
import cv2
import math
from twilio.rest import Client

# Function to send SMS
def send_sms():
    account_sid = 'your_twilio_sid'
    auth_token = 'your_twilio_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Fire has been detected by the UAV.',
        from_='your_twilio_number',
        to='reciever_number'
    )

    print(f"SMS sent successfully. SID: {message.sid}")

# Running real-time from webcam or video file
cap = cv2.VideoCapture('UAVfire.mp4')
model = YOLO('best.pt')

# Reading the classes
classnames = ['fire']
sms_sent = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame or end of video.")
        break

    frame = cv2.resize(frame, (640, 480))
    result = model(frame, stream=True)

    # Getting bbox, confidence, and class names information to work with
    for info in result:
        boxes = info.boxes
        for box in boxes:
            confidence = box.conf[0]
            confidence = math.ceil(confidence * 100)
            Class = int(box.cls[0])
            if confidence > 50:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
                cvzone.putTextRect(frame, f'{classnames[Class]} {confidence}%', [x1 + 8, y1 + 100],
                                   scale=1.5, thickness=2)

                # Send SMS if not already sent
                if not sms_sent:
                    print("Fire detected. Sending SMS...")
                    send_sms()
                    sms_sent = True

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
