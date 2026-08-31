import cv2
import numpy as np

# 1. WEBCAM ON KARO
cap = cv2.VideoCapture(0)
cap.set(3, 1280) # width
cap.set(4, 720) # height

# 2. DRAWING KE LIYE KHALI CANVAS
canvas = np.zeros((720, 1280, 3), np.uint8)

# 3. GREEN COLOR KA RANGE - HSV me
# Agar dusra color chahiye to ye values change karo
lower_green = np.array([40, 70, 70])
upper_green = np.array([80, 255, 255])

points = [] # jahan jahan pen gaya uske points save karenge

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # mirror effect

    # 4. COLOR DETECT KARO
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask = cv2.erode(mask, np.ones((5,5), np.uint8), iterations=1)
    mask = cv2.dilate(mask, np.ones((5,5), np.uint8), iterations=1)

    # 5. SABSE BARA CONTOUR = PEN KI TIP
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    center = None
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        if M["m00"] > 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            # Pen ko circle se highlight karo
            cv2.circle(frame, center, int(radius), (0,255,0), 2)

            # Agar pen ka size theek hai to point add karo
            if radius > 10:
                points.append(center)
            else:
                points.append(None) # pen utha liya

    # 6. POINTS KO LINE SE JORO = DRAWING
    for i in range(1, len(points)):
        if points[i-1] is not None and points[i] is not None:
            cv2.line(canvas, points[i-1], points[i], (0,0,255), 5) # Red color se draw

    # 7. CANVAS + CAMERA KO MILAO
    output = cv2.add(frame, canvas)

    cv2.imshow("Virtual Paint", output)
    cv2.imshow("Canvas", canvas)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"): # q dabao to band
        break
    if key == ord("c"): # c dabao to canvas clear
        canvas = np.zeros((720, 1280, 3), np.uint8)
        points = []

cap.release()
cv2.destroyAllWindows()