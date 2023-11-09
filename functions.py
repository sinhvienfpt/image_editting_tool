import os
import uuid
import random
import cv2
from functions import *
import numpy as np



#BLUR
def blur_image(img, output_directory="output"):  

    width = random.randint(1, 50)     #w, h are filter value
    height = random.randint(1, 50)

    #blur image 
    blurred_image = cv2.blur(img, ksize=(width, height))

    # Make a random name for it
    name = str(uuid.uuid4())[:8]

    #save image with random name into output folder
    output_path = os.path.join(output_directory, f"{name}.jpg")
    cv2.imwrite(output_path, blurred_image)

    return blurred_image



#CROP
def crop_image(image, output_directory="output"):
    # Get image dimensions
    width, height = image.shape[:2]

    # Determine random coordinates for the top-left corner of the cropped region
    x = random.randint(0, width // 2)
    y = random.randint(0, height // 2)

    # Crop the image
    cropped_image = image[y:y + height // 2, x:x + width // 2]

    # Generate a random name for the output image
    name = str(uuid.uuid4())[:8] + ".jpg"
    output_image_path = os.path.join(output_directory, name)

    # Save the cropped image
    cv2.imwrite(output_image_path, cropped_image)

    return cropped_image



#ROTATE
def rotate_image(img, output_directory='output'):
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

    return rotated_img



#FLIP
def flip_image(img,output_directory='output'):
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

    return flipped_img



#EDGE DETECTION
def find_edge(img, output_directory="output"):

    #blur image 
    blurred_image = cv2.Canny(img, 100, 200)

    #random name for it
    name = str(uuid.uuid4())[:8]

    #save image with random name into output folder
    output_path = os.path.join(output_directory, f"{name}.jpg")
    cv2.imwrite(output_path, blurred_image)

    return blurred_image



#GRAY SCALE
def gray_scale(image, output_folder="output"):
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Generate a random name for the grayscale image
    new_filename = str(uuid.uuid4())[:8] + ".jpg"

    # Save the grayscale image
    output_path = os.path.join(output_folder, new_filename)
    cv2.imwrite(output_path, grayscale_image)

    return grayscale_image

def change_color_image(img, output_folder="output"):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  # Tạo filter ngẫu nhiên
  filt = random.randint(1,20)

  if filt == 1:
    # Lọc tươi mới
    img = np.array(img * [1.1, 1.2, 0.9], dtype=np.uint8)

  elif filt == 2:
    # Lọc trong suốt
    img = np.array(img * [0.9, 1.1, 1.1], dtype=np.uint8)
    
  elif filt == 3:
    # Lọc ấm áp
    img = np.array(img * [1.2, 1.1, 0.9], dtype=np.uint8)

  elif filt == 4:

    img[0,:,:] = [255,255,255]
    img[:,0,:] = [255,255,255]
    img[-1,:,:] = [255,255,255]
    img[:,-1,:] = [255,255,255]
    img[1:-1,1:-1,:] = np.array(img[1:-1,1:-1,:] * [0.8,0.8,0.8], dtype=np.uint8)

  elif filt == 5:
    # Lọc màu vàng hiện đại
    img = np.array(img * [1.1, 1.1, 0.8], dtype=np.uint8)

  elif filt == 6:
    # Lọc nóng
    img = np.array(img * [1.1, 0.9, 0.9], dtype=np.uint8)

  elif filt == 7:
    # Lọc cổ điển
    img = np.array(img * [0.9, 0.9, 1.2], dtype=np.uint8)

  elif filt == 8:
    # Lọc mùa xuân 
    img = np.array(img * [1.1, 1.2, 1], dtype=np.uint8)

  elif filt == 9:
    # Lọc sương mù
    img = np.array(img * [0.6, 0.6, 0.6], dtype=np.uint8)

  elif filt == 10:
    # Lọc mùa thu
    img = np.array(img * [1.2, 1, 0.8], dtype=np.uint8)

  elif filt == 11:
    # Lọc sharpen
    img = np.array(img * [1.5, 1.5, 1.5], dtype=np.uint8)

  elif filt == 12:
    # Lọc nhiễu 
    noise = np.random.randint(-50,50,img.shape)
    img = img + noise
    img = np.clip(img, 0, 255)

  elif filt == 13:
    # Lọc tông xanh
    img = np.array(img * [1, 1.5, 1.5], dtype=np.uint8)

  elif filt == 14:
    # Lọc đồng quê
    img = np.array(img * [0.9, 0.9, 1.1], dtype=np.uint8)

  elif filt == 15:
    # Lọc hoàng hôn
    img = np.array(img * [1.1, 0.8, 0.9], dtype=np.uint8)

  elif filt == 16:
    # Lọc thành phố
    img = np.array(img * [0.8, 0.8, 1.2], dtype=np.uint8)

  elif filt == 17:
    # Lọc thực phẩm
    img = np.array(img * [1.2, 0.9, 0.8], dtype=np.uint8)

  elif filt == 18:
    # Lọc khu rừng
    img = np.array(img * [0.9, 1.1, 1], dtype=np.uint8)

  elif filt == 19:
    # Lọc mùa đông
    img = np.array(img * [1.1, 0.8, 1.2], dtype=np.uint8)

  elif filt == 20:
    # Lọc mùa hè
    img = np.array(img * [1.2, 0.9, 0.8], dtype=np.uint8)

  # Tạo tên ngẫu nhiên cho file ảnh
  new_name = str(uuid.uuid4())[:8] + ".jpg"

  # Lưu ảnh với tên mới    
  output_path = os.path.join(output_folder, new_name)
  cv2.imwrite(output_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

  return img