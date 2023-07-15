# Image Processing

This Python program reads an input image and applies some morphological operators to enhance, binarize, filter, and overlay the image. The processed images are displayed using matplotlib and will be saved to separate image files.

## Prerequisites

Make sure you have the following dependencies installed:

- Python (version 3 or above)
- OpenCV (cv2) library
- NumPy library
- Matplotlib library

## Getting Started

1. Clone or download the repository to your local machine.
2. Place the input satellite image file named "input_sat_image.jpg" in the same directory as the program file.

## Running the Program

Execute the following command to run the program:

python image_processing.py

On Ubuntu and macOS, you may need to use `python3` instead of `python`

The program will process the input image and display a series of images showing the different stages of the analysis. The processed images will also be saved as separate files in the same directory.

## Results

The program generates the following images:

1. **Input**: The original satellite image.
2. **Enhanced**: The enhanced version of the input image using a min-max normalization technique.
3. **Binarization**: The binarized image where pixels above a certain threshold are set to 255 (white) and pixels below are set to 0 (black).
4. **Filtered**: The filtered image obtained by applying morphological opening and closing operations to the binarized image.
5. **Overlay**: The overlay image, which combines the enhanced image with the filtered image using alpha blending.


