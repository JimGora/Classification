import os
import shutil
import random
from PIL import Image

def copy_and_resize_images(source_dir, dest_dir, resize_width, resize_height, percentage=10):
    # Crear el directorio de destino si no existe
    os.makedirs(dest_dir, exist_ok=True)

    # Obtener la lista de todas las imágenes en el directorio fuente y subdirectorios
    image_files = [os.path.join(root, file) for root, dirs, files in os.walk(source_dir) for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Calcular el número de imágenes a seleccionar aleatoriamente
    num_images_to_select = int(len(image_files) * percentage / 100)

    # Seleccionar aleatoriamente las imágenes
    selected_images = random.sample(image_files, num_images_to_select)

    # Copiar y redimensionar las imágenes seleccionadas manteniendo la estructura de subdirectorios
    for source_image_path in selected_images:
        # Obtener la ruta relativa desde el directorio fuente
        rel_path = os.path.relpath(source_image_path, source_dir)
        
        # Construir la ruta de destino
        dest_image_path = os.path.join(dest_dir, rel_path)

        # Crear los directorios necesarios en la ruta de destino
        os.makedirs(os.path.dirname(dest_image_path), exist_ok=True)

        # Copiar la imagen
        shutil.copy(source_image_path, dest_image_path)

        # Redimensionar la imagen
        with Image.open(dest_image_path) as img:
            resized_img = img.resize((resize_width, resize_height), Image.ANTIALIAS)
            resized_img.save(dest_image_path)

if __name__ == "__main__":
    # Especifica los directorios y el tamaño de redimensionamiento
    source_directory = 'E:\\Jim\\23\\ML Zoomcamp\\Capstone 2\\Data\\Histopathology'
    destination_directory = 'E:\\Jim\\23\\ML Zoomcamp\\Capstone 2\\Data\Histo'
    resize_width = 224  # Ajusta según sea necesario
    resize_height = 224  # Ajusta según sea necesario

    # Copiar y redimensionar el 10% de las imágenes de manera aleatoria manteniendo la estructura de subdirectorios
    copy_and_resize_images(source_directory, destination_directory, resize_width, resize_height, percentage=10)
    
print("Proceso completado")
