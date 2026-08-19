# OpenCV Color Detection

A real-time computer vision project built with Python and OpenCV.

The program uses the Mac camera to detect blue objects using HSV color segmentation.

## Features

- Real-time webcam capture
- BGR to HSV color conversion
- Blue color segmentation
- Binary mask generation
- Contour detection
- Noise filtering by contour area
- Bounding box around detected blue objects

## Technologies

- Python
- OpenCV
- NumPy

## How it works

Camera → HSV conversion → Color mask → Contours → Bounding box

## Run

Install the dependencies:

pip install -r requirements.txt

Then run:

python color_detector.py