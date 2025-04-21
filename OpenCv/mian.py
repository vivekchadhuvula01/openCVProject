import Functions as generalFunctions
import Variables 


Access:bool = False


if (Access == False):
    permission = generalFunctions.Permissions(prompt_text=Variables.Prompt , Choices=Variables.Choices)
    
while not Access:
    if (permission == "Yes"):
         Access = True
         generalFunctions.open_camera()
         
    elif Access== False:
        print("Permission required to run the Application \n Please Allow")
        permission = generalFunctions.Permissions(prompt_text=Variables.Prompt , Choices=Variables.Choices)
    
     
     
    


import cv2

# Load pre-trained model
net = cv2.dnn.readNetFromCaffe("deploy.prototxt", "mobilenet_iter_73000.caffemodel")

# List of class labels MobileNet SSD was trained on
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant",
           "sheep", "sofa", "train", "tvmonitor"]

def open_camera_and_detect():
    cap = cv2.VideoCapture(0)  # 0 for default camera

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize frame to 300x300 and create a blob
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 
                                     0.007843, (300, 300), 127.5)

        net.setInput(blob)
        detections = net.forward()

        # Loop over detections
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence > 0.5:
                idx = int(detections[0, 0, i, 1])
                label = CLASSES[idx]
                box = detections[0, 0, i, 3:7] * \
                      [frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]]
                (startX, startY, endX, endY) = box.astype("int")

                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                cv2.putText(frame, label, (startX, startY - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Show frame
        cv2.imshow("Object Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run it
open_camera_and_detect()
