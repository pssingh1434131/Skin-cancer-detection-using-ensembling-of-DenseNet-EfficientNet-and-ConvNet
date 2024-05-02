import pandas as pd
import os
import shutil

csv_path = '/home/anonymous/Mini project/2019/ISIC_2019_Training_GroundTruth.csv'
df = pd.read_csv(csv_path)

root_directory = '/home/anonymous/Mini project/2019'
training_directory = os.path.join(root_directory, 'train')
testing_directory = os.path.join(root_directory, 'test')
os.makedirs(training_directory, exist_ok=True)
os.makedirs(testing_directory, exist_ok=True)

image_folder_path = '/home/anonymous/Mini project/2019/ISIC_2019_Training_Input'
imagename = ["MEL", "NV", "BCC", "AK", "BKL", "DF", "VASC", "SCC", "UNK"]

for index, row in df.iterrows():
    image_name = f"{row[0]}.jpg"
    cancer_type = ""
    for i in range(9):
        if row[i + 1] == 1:  
            cancer_type = imagename[i]
            break

    
    train_subfolder = os.path.join(training_directory, cancer_type)
    test_subfolder = os.path.join(testing_directory, cancer_type)
    os.makedirs(train_subfolder, exist_ok=True)
    os.makedirs(test_subfolder, exist_ok=True)
    
    source_path = os.path.join(image_folder_path, image_name)
    destination_path_train = os.path.join(train_subfolder, image_name)
    destination_path_test = os.path.join(test_subfolder, image_name)

    # Copy images to the training or testing folder based on criteria (e.g., 80% training, 20% testing)
    if index % 5 == 0:  
        shutil.copy(source_path, destination_path_test)
    else:
        shutil.copy(source_path, destination_path_train)

print("Organizing images into training and testing folders completed.")