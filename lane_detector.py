import os
import cv2
import numpy as np

base_dir = os.path.dirname(os.path.abspath(__file__)) #to find path of img file
image_path = os.path.join(base_dir, "road.jpg")

image = cv2.imread(image_path) #loading the image

if image is None:
    print(f"Error: Could not find 'road.jpg' in {base_dir}")
    exit()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #converting to HSV
'what it is -> HSV - hue, saturation, value(brightness); used like RGB'

# Color bounds for white lanes
lower_white = np.array([0, 0, 175])
upper_white = np.array([180, 65, 255])
white_mask = cv2.inRange(hsv, lower_white, upper_white)

# Color bounds for yellow lanes
lower_yellow = np.array([15, 70, 80])
upper_yellow = np.array([40, 255, 255])
yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

lane_mask = cv2.bitwise_or(white_mask, yellow_mask) #combined
filtered_image = cv2.bitwise_and(image, image, mask=lane_mask)

gray = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2GRAY) #gaussian blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blurred, 50, 150) #canny edge

#region of interest (roi) masking
height, width = edges.shape 

polygon = np.array([[
    (int(width * 0.10), height),
    (int(width * 0.45), int(height * 0.55)),
    (int(width * 0.55), int(height * 0.55)),
    (int(width * 0.90), height)
]], dtype=np.int32)

roi_mask = np.zeros_like(edges)
cv2.fillPoly(roi_mask, polygon, 255)
roi_edges = cv2.bitwise_and(edges, roi_mask)

#saving
cv2.imwrite(os.path.join(base_dir, "1_original.jpg"), image)
cv2.imwrite(os.path.join(base_dir, "2_hsv_mask.jpg"), filtered_image)
cv2.imwrite(os.path.join(base_dir, "3_gaussian_blur.jpg"), blurred)
cv2.imwrite(os.path.join(base_dir, "4_canny_edges.jpg"), edges)
cv2.imwrite(os.path.join(base_dir, "5_roi_edges.jpg"), roi_edges)

print("Pipeline execution complete! Saved all images.")