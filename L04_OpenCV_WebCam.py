import cv2 as cv
import sys

# 카메라와 연결 시도 
cap=cv.VideoCapture(0, cv.CAP_DSHOW)   
# cv.VideoCapture: 웹 캠과 연결을 시도
# cv.CAP_DSHOW: 비디오가 화면에 바로 나타나게 함

if not cap.isOpened():
    sys.exit('Camera connection failed')

while True:
    ret, frame = cap.read()     # 비디오를 구성하는 프레임 획득
    # ret: 카메라로부터 프레임을 성공적으로 읽었는지를 나타내는 변수 

    if not ret:
        print('Failed to acquire frame')
        break
    
    cv.imshow('Video display', frame)

    key=cv.waitKey(1)   # 1밀리초 동안 키보드 입력 기다림
    if key==ord('q'):   # 'q' 키가 들어오면 루프를 빠져나감
        break

# 카메라와 연결을 끊음
cap.release()   # 카메라 연결 해제
cv.destroyAllWindows()  # 윈도우창 종료