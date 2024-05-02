import pandas as pd
import os
import shutil

csv_path = '/home/anonymous/Mini project/HAM10000/HAM10000_metadata.csv'
df = pd.read_csv(csv_path)

root_directory = '/home/anonymous/Mini project/HAM10000'
training_directory = os.path.join(root_directory, 'train')
testing_directory = os.path.join(root_directory, 'test')

image_folder_path = '/home/anonymous/Mini project/HAM10000/ham10000_images_part_1'

for index, row in df.iterrows():
    image_name = f"{row[1]}.jpg"
    cancer_type = row[2]
    
    train_subfolder = os.path.join(training_directory, cancer_type)
    test_subfolder = os.path.join(testing_directory, cancer_type)

    source_path = os.path.join(image_folder_path, image_name)
    destination_path_train = os.path.join(train_subfolder, image_name)
    destination_path_test = os.path.join(test_subfolder, image_name)

    # Copy images to the training or testing folder based on criteria (e.g., 80% training, 20% testing)
    if index % 5 == 0:  
        shutil.copy(source_path, destination_path_test)
    else:
        shutil.copy(source_path, destination_path_train)

print("Organizing images into training and testing folders completed.")