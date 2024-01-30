import os
import json
import shutil

def separate_images_by_category(data_folder, output_folder, json_file):
    # Cargar el archivo JSON
    with open(json_file, 'r') as json_data:
        data = json.load(json_data)

    # Iterar sobre los datos y copiar las imágenes a las subcarpetas
    for item in data:
        label = str(item['label'])
        image_name = item['name']

        source_path = os.path.join(data_folder, image_name)
        destination_folder = os.path.join(output_folder, label)

        # Crear la subcarpeta si no existe
        os.makedirs(destination_folder, exist_ok=True)

        # Copiar la imagen a la subcarpeta
        shutil.copy(source_path, destination_folder)

if __name__ == "__main__":
    # Rutas de los directorios y archivos JSON
    train_data_folder = 'E:\\Jim\\23\\ML Zoomcamp\\Capstone 2\\Data\\chaoyang-data'
    test_data_folder = 'E:\\Jim\\23\\ML Zoomcamp\\Capstone 2\\Data\\chaoyang-data'
    output_folder = 'E:\\Jim\\23\\ML Zoomcamp\\Capstone 2\\Data\\Chaoyang'
    train_json_path = 'E:\\Jim\\23\\ML Zoomcamp\\Capstone 2\\Data\\chaoyang-data\\train.json'
    test_json_path = 'E:\\Jim\\23\\ML Zoomcamp\\Capstone 2\\Data\\chaoyang-data\\test.json'

    # Separar imágenes de entrenamiento
    separate_images_by_category(train_data_folder, output_folder, train_json_path)

    # Separar imágenes de prueba
    separate_images_by_category(test_data_folder, output_folder, test_json_path)

print('Done!')