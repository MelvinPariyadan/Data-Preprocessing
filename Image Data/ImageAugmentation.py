import cv2
import numpy as np

# Load image
img = cv2.imread('dog.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Flip image horizontally
flipped = cv2.flip(img, 1)

# Randomly rotate image
angle = np.random.randint(-10, 10)
rows, cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
rotated = cv2.warpAffine(img, M, (cols, rows))

# Randomly adjust brightness and contrast
brightness = np.random.randint(-50, 50)
contrast = np.random.uniform(0.5, 1.5)
b_c = cv2.addWeighted(img, contrast, img, 0, brightness)

# Add salt and pepper noise
noise = np.zeros(img.shape, np.uint8)
# Set a noise threshold of 0.4
# => 40% of the pixels will be changed to black or white
threshold = 0.4
# Loop through each pixel in the image
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r = np.random.rand()
        if r < threshold/2:
            # Set pixel to black
            noise[i, j] = 0
        elif r < threshold:
            # Set pixel to white
            noise[i, j] = 255
        else:
            # Pixel unchanged
            noise[i, j] = img[i, j]

noised = cv2.add(img, noise)

# Show output
cv2.imshow('Input Image', img)
cv2.imshow('Grayscale Image', gray)
cv2.imshow('Flipped Image', flipped)
cv2.imshow('Rotated Image', rotated)
cv2.imshow('Brightness and Contrast Image', b_c)
cv2.imshow('Noise Image', noised)
cv2.waitKey(0)
cv2.destroyAllWindows()
