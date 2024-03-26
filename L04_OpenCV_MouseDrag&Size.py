import cv2 as cv
import sys

img = cv.imread('apples.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

def draw(event, x, y, flags, param):
    # gloabl ix, iy: 10행이 없으면 xi와 iy는 함수가 시작할 때 생겼다가 끝날 때 소멸하는 지역 변수로
    #                작용해 드래그 동안 발생하는 여러 번의 함수 호출에서 생성과 소멸을 반복하므로 좌푯값 유지 못함
    global ix, iy

    if event == cv.EVENT_LBUTTONDOWN:   # 마우스 왼쪽 버튼 클릭했을 때 초기 위치 저장
        ix, iy = x, y
    elif event == cv.EVENT_LBUTTONUP:   # 마우스 왼쪽 버튼 클릭했을 때 직사각형 그리기
        cv.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 2)
    
    cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break