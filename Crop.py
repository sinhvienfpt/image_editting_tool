import os
import random
import PIL.Image as image
import uuid

# Get the path of the folder and output
output_path = os.path.join(os.getcwd(), "./Output")

# make a folder output if it doesn't exist
if not os.path.exists(output_path):
    os.makedirs(output_path)


def crop_image(file_paths, output_directory=output_path):
    
    # #Delete the old things
    # for file in os.listdir(output_path):
    #     os.remove(os.path.join(output_path, file))

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

    # Save cropped img
    cropped_img.save(os.path.join(output_directory, name))

    