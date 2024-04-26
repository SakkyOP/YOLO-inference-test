import cv2
from model import model

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if not ret:
       print('no video')
       cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
       continue
    
    frame = model(frame, verbose=False)[0].plot()
    cv2.imshow("Detection!", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()