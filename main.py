import cv2
import numpy as np

# Read the image
image = cv2.imread("test.jpg")
print(f"Original image dimensions: {image.shape}")

# Resize 
width = 800
height = int(image.shape[0] * (width / image.shape[1]))
resized_image = cv2.resize(image, (width, height))

cv2.imshow('Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows() 

# Convert image to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to get a binary image
_, thresh_image = cv2.threshold(gray_image, 220, 255, cv2.THRESH_BINARY)

# Find contours in the binary imagej
contours, _ = cv2.findContours(thresh_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

max_contour_area = 100000  # Set a threshold large enough to exclude the frame


# Iterate over contours orginal 2
for contour in contours:
    area = cv2.contourArea(contour)
    if area > max_contour_area:
        continue  # Skip large contours
    if area > 1000:  # Filter out small contours
        epsilon = 0.01 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Draw the contour on the image
        #cv2.drawContours(resized_image, [approx], 0, (0, 0, 0), 4)

        # Check if the shape has 4 vertices (quadrilateral)
        if len(approx) == 4:
            # Get bounding box of the contour
            x, y, w, h = cv2.boundingRect(approx)

            # Calculate aspect ratio
            aspect_ratio = float(w) / h

            # Define text properties
            x_mid = int(x + w / 2)
            y_mid = int(y + h / 2)
            coords = (x_mid, y_mid)
            colour = (0, 0, 0)
            font = cv2.FONT_HERSHEY_DUPLEX

            # Determine if it's a square or rectangle based on aspect ratio
            if 0.9 <= aspect_ratio <= 1.1:
                shape_name = "Square"
                # Put text on the image
                cv2.putText(resized_image, shape_name, coords, font, 0.5, colour, 1)
            else:
                shape_name = "Rectangle"
                # Put text on the image
                cv2.putText(resized_image, shape_name, coords, font, 0.5, colour, 1)
        else:
            # Other shapes
            x, y, w, h = cv2.boundingRect(approx)
            x_mid = int(x + w / 2)
            y_mid = int(y + h / 2)
            coords = (x_mid, y_mid)
            colour = (0, 0, 0)
            font = cv2.FONT_HERSHEY_DUPLEX

            # Detect other shapes based on number of vertices
            if len(approx) == 3:
                shape_name = "Triangle"
                # Put text on the image
                cv2.putText(resized_image, shape_name, coords, font, 0.5, colour, 1)
            else:
                shape_name = "Circle"
                # Put text on the image
                cv2.putText(resized_image, shape_name, coords, font, 0.5, colour, 1)

# Display the result
cv2.namedWindow("Shapes Detected", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Shapes Detected", resized_image.shape[1], resized_image.shape[0])
cv2.imshow("Shapes Detected", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the image
cv2.imwrite("processed_image.jpg", resized_image)
