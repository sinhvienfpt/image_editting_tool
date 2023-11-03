import os
import string
import random
import cv2

def find_edge(file_paths, output_directory="output"):

    
    img = cv2.imread(file_paths) #read image 
    
    #blur image 
    blurred_image = cv2.Canny(img, 100, 200)

    #random name for it
    name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    #save image with random name into output folder
    output_path = os.path.join(output_directory, f"{name}.jpg")
    cv2.imwrite(output_path, blurred_image)

    return output_path






    


