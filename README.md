# Lane Detection using OpenCV

A 5-step computer vision script in Python to extract lane markings from a front-facing road image (`road.jpg`/`road2.jpg`).

## Overview of the Pipeline

1. **Image Loading (`1_original.jpg`)**  
   Reads the input image using `cv2.imread()`. Uses dynamic pathing (`os.path`) so it runs regardless of where the terminal is opened from.

2. **HSV Color Masking (`2_hsv_mask.jpg`)**  
   Converts the image to HSV to separate color from lighting conditions. Masks are applied to isolate yellow and white paint while ignoring dark asphalt:
   - White range: Hue 0–180, Saturation 0–65, Value 175–255
   - Yellow range: Hue 15–40, Saturation 70–255, Value 80–255
   - Both masks are merged with `cv2.bitwise_or()`.

3. **Gaussian Blur (`3_gaussian_blur.jpg`)**  
   Converts the masked output to grayscale and applies a 5x5 Gaussian blur to reduce rough road texture and high-frequency noise before finding edges.

4. **Canny Edge Detection (`4_canny_edges.jpg`)**  
   Uses `cv2.Canny()` with thresholds set to 50 and 150 to locate pixel boundaries and paint line contours.

5. **Region of Interest Masking (`5_roi_edges.jpg`)**  
   Applies a trapezoidal mask over the driving corridor using `cv2.fillPoly()` and `cv2.bitwise_and()`. This drops all irrelevant edges outside the lane, including the horizon, sky, and guardrails.

---

## Stage Outputs

| Step 1: Input | Step 2: HSV Mask | Step 3: Gaussian Blur |
| :---: | :---: | :---: |
| ![Original](1_original.jpg) | ![HSV](2_hsv_mask.jpg) | ![Blur](3_gaussian_blur.jpg) |

| Step 4: Canny Edges | Step 5: ROI Masked Result |
| :---: | :---: |
| ![Canny](4_canny_edges.jpg) | ![ROI](5_roi_edges.jpg) |

---

## Directory Structure

```text
├── road.jpg              # Input road image
├── lane_detector.py      # Main pipeline script
├── 1_original.jpg        # Saved Step 1 output
├── 2_hsv_mask.jpg        # Saved Step 2 output
├── 3_gaussian_blur.jpg   # Saved Step 3 output
├── 4_canny_edges.jpg     # Saved Step 4 output
├── 5_roi_edges.jpg       # Saved Step 5 output
└── README.md