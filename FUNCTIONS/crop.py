import os
import random
import PIL.Image as image
import uuid




def crop_image(file_paths, output_directory="output"):
    # Get a random img path in list of img paths and open it
    img = image.open(file_paths)
    width, height = img.size

    # To be able to cut, the sub-image must be within the origin-image
    x = random.randint(0, width//2)
    y = random.randint(0, height//2)

    # Crop
    cropped_img = img.crop((x, y, x + width//2, y + height//2))

    # Make a random name for it
    name = str(uuid.uuid4())[:8] + ".jpg"
    output_img_path =os.path.join(output_directory, name)
    
    # Save cropped img
    cropped_img.save(output_img_path)

    return output_img_path

