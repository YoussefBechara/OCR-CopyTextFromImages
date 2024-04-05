import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def ocr_from_camera():
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Could not open camera")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if frame is not empty
        if ret:
            # Display the resulting frame
            cv2.imshow('Camera', frame)

            # Wait for the user to press any key
            if cv2.waitKey(1) != -1:
                # Release the camera
                cap.release()

                # Destroy the camera window
                cv2.destroyWindow('Camera')

                # Convert the image to grayscale
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Use Tesseract to do OCR on the image
                text = pytesseract.image_to_string(gray)

                # Display the gray image
                cv2.imshow('Processed Image', gray)
                
                # Wait for the user to press any key
                cv2.waitKey(0)

                # Destroy all windows
                cv2.destroyAllWindows()

                return text

# Test the function
print(ocr_from_camera())
