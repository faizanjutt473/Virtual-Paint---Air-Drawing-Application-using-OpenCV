Ye project ek "Virtual Whiteboard" hai jo bina touch ke kaam karta hai. 

**Kaise kaam karta hai:**
1.  Webcam on hoti hai aur har frame ko HSV color space me convert kiya jata hai
2.  Specific color range jaise Green ko `cv2.inRange()` se track kiya jata hai
3.  Sabse bare contour ka center point nikal kar uski location save ki jati hai
4.  Har 2 points ko `cv2.line()` se jor kar canvas par drawing banai jati hai
5.  User 'C' press karke canvas clear aur 'Q' press karke exit kar sakta hai

**Key Features:**
- Real-time Air Drawing with any colored marker/pen
- No touch screen required
- Canvas Clear and Save option
- Multiple color support
- Mirror view for easy use

**Applications:** 
Online Teaching, Virtual Meetings, Presentation, Kids Drawing App

**Tools Used:** Python, OpenCV, Numpy
