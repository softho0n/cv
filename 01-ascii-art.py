import cv2
import numpy as np
import time

# Characters that you want to print
chars = "@!*#$=;:~-., "

# Define width => resizing Resource(image or video)
nw = 40

# Set the resource Path: String Type
_path = "resources/01-resource.mp4"

# If the resource is video,
# Use below codes

_cap = cv2.VideoCapture(_path)
# Clear Terminal window
print("\x1b[2J", end='')

while True :
    # Get image from video every single frame
    ret, img = _cap.read()

    if not ret :
        break
    
    # Convert 3-Dim to 2-Dim
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Resizing image
    h, w = img.shape
    nh   = int(h / w * nw)
    img  = cv2.resize(img, (nw * 2, nh))

    # Get each pixel and process it
    for row in img :
        for pixel in row :
            # pixel value range: 0 ~ 255 (GRAYSCALE)
            index = int(pixel / 256 * len(chars))
            print(chars[index], end='')
        
        print()

    # Clear Terminal window
    print("\x1b[H", end='')

# Video processing finish

# If the resource is image,
# Just use L29 ~ L46 codes without while statement.