import cv2
import time

# 웹캠 연결
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

count = 0

while count < 1:
    # 웹캠에서 프레임 읽기
    ret, frame = cap.read()

    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # 사진 저장
    save_path = r"C:\프로젝트\회사프로젝트\객체인식\picture"
    filename = f"frame_{count}.jpg"
    cv2.imwrite(f"{save_path}/{filename}", frame)
    print(f"{filename} 저장됨.")

    count += 1
    time.sleep(2)

# 웹캠 해제
cap.release()