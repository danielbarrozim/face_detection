import dlib
import numpy as np
from skimage import io

face_detector = dlib.get_frontal_face_detector()

win = dlib.image_window()

with open("images/all_file.txt") as file:
    for line in file:
        image_name = line
        
        # Next we load the image into an array.
        image = io.imread("images/" + image_name[:-1])
        
        # Run HOG face detector on the image. 
        # This will result in a set of bounding boxes on the faces.
        detected_faces = face_detector(image, 1)
        
        # Opens a window with a red rectangle overlaid on each face of every frame. 
        win.clear_overlay()
        win.set_image(image)
        #win.add_overlay(detected_faces)
    
