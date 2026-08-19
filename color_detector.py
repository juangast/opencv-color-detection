import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        break
    
    height, width, _ = frame.shape

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 100, 50])
    upper_blue = np.array([140, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)
            center_x = x + w // 2
            center_y = y + h // 2
            camera_center = width // 2
   
            tolerance = 80
            if center_x < camera_center - tolerance:
                position = "LEFT"
                command = "TURN LEFT"

            elif center_x > camera_center + tolerance:
                position = "RIGHT"
                command = "TURN RIGHT"
   
            else:
                position = "CENTER"
                command = "MOVE FORWARD"
    

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )
            
            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                (0,0, 255),
                -1
            )

            cv2.putText(
                frame,
                position,
                (x,y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2
            )
            
            cv2.putText(
                frame,
                command,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255,255,255),
                2
 
                )              

    cv2.imshow("Camera", frame)
    cv2.imshow("HSV", hsv)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
