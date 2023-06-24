A simple python code for reading an input image and applying morphological 
operators on them including enhancement, binarization, filtering, and overlay. The processed images are displayed using matplotlib and can also be saved to separate image files.

Before running the program, make sure you have the following installed:

Python (version 3 or above)
OpenCV (cv2) library
NumPy library
Matplotlib library

Clone or download the repository to your local machine.

Place the input satellite image file named "input_sat_image.jpg" in the same directory as the program file.

Run the program by executing the following command:

python image_processing.py or python3 image_processing.py on Ubunto and Mac. 

The program will process the input image and display a series of images showing the different stages of the analysis.
The processed images will also be saved as separate files in the same directory.

Results
The program generates the following images:

Input: The original satellite image.
Enhanced: The enhanced version of the input image using a min-max normalization technique.
Binarization: The binarized image where pixels above a certain threshold are set to 255 (white) and pixels below are set to 0 (black).
Filtered: The filtered image obtained by applying morphological opening and closing operations to the binarized image.
Overlay: The overlay image, which combines the enhanced image with the filtered image using alpha blending.
