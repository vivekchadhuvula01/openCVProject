import cv2
import questionary

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

        cv2.imshow("Camera Feed (press x to close)", frame)

        # Press 'q' to exit the camera window
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

    cap.release()
    cv2.destroyAllWindows()



def Permissions(prompt_text:str, Choices:list):
    
    value = questionary.select(
        prompt_text,
        choices=Choices
    ).ask()
    return value

