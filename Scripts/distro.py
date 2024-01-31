import os
import json
import shutil

def separate_images_by_category(data_folder, output_folder, json_file):
    with open(json_file, 'r') as json_data:
        data = json.load(json_data)

    for item in data:
        label = str(item['label'])
        image_name = item['name']

        source_path = os.path.join(data_folder, image_name)
        destination_folder = os.path.join(output_folder, label)

        os.makedirs(destination_folder, exist_ok=True)

        shutil.copy(source_path, destination_folder)

if __name__ == "__main__":
    train_data_folder = 'E:\\Data\\chaoyang-data'
    test_data_folder = 'E:\\Data\\chaoyang-data'
    output_folder = 'E:\\Data\\Chaoyang'
    train_json_path = 'E:\\Data\\chaoyang-data\\train.json'
    test_json_path = 'E:\\Data\\chaoyang-data\\test.json'

    separate_images_by_category(train_data_folder, output_folder, train_json_path)
    separate_images_by_category(test_data_folder, output_folder, test_json_path)

print('Done!')