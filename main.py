import dlib
import numpy as np
from skimage import io

with open("images/all_file.txt") as file:

    # Create a window object to display the images
    win = dlib.image_window()

    # Create the HOG face detector
    face_detector = dlib.get_frontal_face_detector()

    for line in file:
        image_name = line
        # Load the image into an array.
        image = io.imread("images/" + image_name[:-1])
        # Run HOG face detector on the image.
        # This will result in a set of bounding boxes on the faces.
        detected_faces = face_detector(image, 1)

        # Clear previous overlays & add the image to the window
        win.clear_overlay()
        win.set_image(image)
        
        # For each face detected, add the overlay
        for i, face_rect in enumerate(detected_faces):
            win.add_overlay(detected_faces)