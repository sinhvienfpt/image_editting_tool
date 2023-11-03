import os
import random
from PIL import Image, ImageEnhance
import uuid


def enhance_image_color(input_path, output_folder="output"):
    # Open the image
    img = Image.open(input_path)

    # Apply color enhancement
    color_enhancer = ImageEnhance.Color(img)
    enhanced_img = color_enhancer.enhance(random.uniform(2,4))  # You can adjust the enhancement factor

    # Generate a random name for the enhanced image
    new_filename = str(uuid.uuid4())[:8] + ".jpg"

    # Save the enhanced image to the output folder
    output_path = os.path.join(output_folder, new_filename)
    enhanced_img.save(output_path)

    return enhanced_img
