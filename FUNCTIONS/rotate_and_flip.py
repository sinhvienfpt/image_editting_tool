import os
import random
import cv2
import uuid

def rotage_image(image_path, output_directory='output'):
    # Open the image
    img = cv2.imread(image_path)
    # Generate a random rotation angle between 0 and 360 degrees
    rotate_angle = random.randint(0, 360)
    # Rotate the image
    rows, cols = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), rotate_angle, 1)
    rotated_img = cv2.warpAffine(img, M, (cols, rows))

    # Generate a random name for the output image
    name = str(uuid.uuid4())[:8] + ".jpg"

    # Save the rotation variation image to the output directory
    output_path = os.path.join(output_directory, name)
    cv2.imwrite(output_path, rotated_img)

    return output_path

def flip_image(image_path, output_directory='output'):

    # Open the image
    img = cv2.imread(image_path)

    # Generate a random flip direction
    flip_direction = random.choice(['horizontal', 'vertical'])

    # Flip the rotated image
    if flip_direction == 'horizontal':
        flipped_img = cv2.flip(img, 1)
    else:
        flipped_img = cv2.flip(img, 0)

    # Generate a random name for the output image
    name = str(uuid.uuid4())[:8] + ".jpg"

    # Save the flip variation image to the output directory
    output_path = os.path.join(output_directory, name)
    cv2.imwrite(output_path, flipped_img)

    return output_path

