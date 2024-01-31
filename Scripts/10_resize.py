import os
import shutil
import random
from PIL import Image

def copy_and_resize_images(source_dir, dest_dir, resize_width, resize_height, percentage=10):
    os.makedirs(dest_dir, exist_ok=True)

    image_files = [os.path.join(root, file) for root, dirs, files in os.walk(source_dir) for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    num_images_to_select = int(len(image_files) * percentage / 100)

    selected_images = random.sample(image_files, num_images_to_select)

    for source_image_path in selected_images:
        rel_path = os.path.relpath(source_image_path, source_dir)
        
        dest_image_path = os.path.join(dest_dir, rel_path)

        os.makedirs(os.path.dirname(dest_image_path), exist_ok=True)

        shutil.copy(source_image_path, dest_image_path)

        with Image.open(dest_image_path) as img:
            resized_img = img.resize((resize_width, resize_height), Image.ANTIALIAS)
            resized_img.save(dest_image_path)

if __name__ == "__main__":
    source_directory = 'E:\\Data\\Histopathology'
    destination_directory = 'E:\\Data\Histo'
    resize_width = 224 
    resize_height = 224
    copy_and_resize_images(source_directory, destination_directory, resize_width, resize_height, percentage=10)
    
print("Done")
