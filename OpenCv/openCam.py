import cv2

def open_camera():
    cap = cv2.VideoCapture(0)  # 0 is usually the default webcam

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        cv2.imshow("Camera Feed", frame)

        # Press 'q' to exit the camera window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

