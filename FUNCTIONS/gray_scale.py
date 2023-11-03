import os
import PIL.Image as image
import uuid




def gray_scale(file_paths, output_directory="output"):
    # Get a random img path in list of img paths and open it
    img = image.open(file_paths)

    # Gray scale
    grayscale_img = img.convert('L')

    # Make a random name for it
    name = str(uuid.uuid4())[:8] + ".jpg"
    output_img_path = os.path.join(output_directory, name)
    # Save cropped img
    grayscale_img.save(output_img_path)

    return output_img_path

