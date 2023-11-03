import os
import string
import random
import cv2

def blur_image(file_paths, output_directory="output"):

    
    img = cv2.imread(file_paths) #read image 
    

    width = random.randint(1, 50)     #w, h are filter value
    height = random.randint(1, 50)

    #blur image 
    blurred_image = cv2.blur(img, ksize=(width, height))

    #random name for it
    name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    #save image with random name into output folder
    output_path = os.path.join(output_directory, f"{name}.jpg")
    cv2.imwrite(output_path, blurred_image)

    return output_path






    


