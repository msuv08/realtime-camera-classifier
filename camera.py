import cv2 as cv

class Camera:

    def __init__(self):
        # Access camera module from connected computer (0 for integrated cam)
        self.camera = cv.VideoCapture(0)
        # Check if camera access was valid, raise error if not
        if self.camera.isOpened():
            self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
            self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)
        else:
            raise ValueError("Not able to access camera.")
    
    def __del__(self):
        # Close camera on object deletion
        if self.camera.isOpened():
            self.camera.release()
    
