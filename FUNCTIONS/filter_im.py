from PIL import Image
import random
import uuid
import os

def change_color_image(input_path, output_folder="output"):
    # Open the image
    img = Image.open(input_path)
    pixels = img.load()
    filter = random.randint(1,20)

    if filter == 1:
    # Lọc tươi mới
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r * 1.1), int(g * 1.2), int(b * 0.9))

    elif filter == 2:
    # Lọc trong suốt 
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r * 0.9), int(g * 1.1), int(b * 1.1))
        
    elif filter == 3:
    # Lọc ấm áp
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r * 1.2), int(g * 1.1), int(b * 0.9))

    # Bộ lọc viền
    elif filter == 4:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                if i == 0 or j == 0 or i == img.width-1 or j == img.height-1:
                    pixels[i, j] = (255, 255, 255)
                else: 
                    pixels[i, j] = (int(r*0.8), int(g*0.8), int(b*0.8))

    elif filter == 5:
    # Lọc màu vàng hiện đại
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r*1.1), int(g*1.1), int(b*0.8))  


    # Bộ lọc nóng
    elif filter == 6:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r*1.1), int(g*0.9), int(b*0.9))

    # Bộ lọc cổ điển  
    elif filter == 7:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r*0.9), int(g*0.9), int(b*1.2))
        
    # Bộ lọc mùa xuân
    elif filter == 8:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r * 1.1), int(g * 1.2), b)

    # Bộ lọc sương mù
    elif filter == 9:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r*0.6), int(g*0.6), int(b*0.6))

    # Bộ lọc mùa thu
    elif filter == 10:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r*1.2), int(g), int(b*0.8))

    # Lọc sharpen
    elif filter == 11:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r*1.5), int(g*1.5), int(b*1.5))

    # Bộ lọc nhiễu  
    elif filter == 12:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                nr = r + random.randint(-50,50)
                ng = g + random.randint(-50,50)
                nb = b + random.randint(-50,50)
                
                pixels[i, j] = (nr, ng, nb)

    # Bộ lọc tông màu xanh
    elif filter == 13:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r), int(g*1.5), int(b*1.5))

    #Bộ lọc đồng quê
    elif filter == 14:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j] 
                pixels[i, j] = (int(r * 0.9), int(g * 0.9), int(b * 1.1))

    # Bộ lọc hoàng hôn 
    elif filter == 15:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r * 1.1), int(g * 0.8), int(b * 0.9))

    # Bộ lọc thành phố
    elif filter == 16:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r * 0.8), int(g * 0.8), int(b * 1.2))

    # Bộ lọc thực phẩm
    elif filter == 17:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r * 1.2), int(g * 0.9), int(b * 0.8))

    # Bộ lọc khu rừng
    elif filter == 18:
        for i in range(img.width): 
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r * 0.9), int(g * 1.1), int(b))

    # Bộ lọc mùa đông
    elif filter == 19:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r * 1.1), int(g * 0.8), int(b * 1.2))
  
    # Bộ lọc mùa hè
    elif filter == 20:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (int(r * 1.2), int(g * 0.9), int(b * 0.8))


    # Generate a random name for the enhanced image
    new_filename = str(uuid.uuid4())[:8] + ".jpg"

    output_path = os.path.join(output_folder, new_filename)
    img.save(output_path)

    return output_path




