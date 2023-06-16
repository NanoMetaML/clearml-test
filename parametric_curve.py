import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply edge detection to extract the edges
edges = cv2.Canny(image, 50, 150)

# Find contours in the edge image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Select the largest contour
largest_contour = max(contours, key=cv2.contourArea)

# Convert the contour points to a parametric curve
curve_x = []
curve_y = []
for point in largest_contour:
    x, y = point[0]
    curve_x.append(x)
    curve_y.append(y)

# Plot the parametric curve
plt.plot(curve_x, curve_y)
plt.axis('equal')
plt.show()
