# Skin-Cancer-Classification

## Abstract
Diagnosis of skin cancer in early stage plays vital role in increasing its survival rate. Advancement in Artificial intelligence
and deep learning technologies provides the path for easing the detection of the disease using medical image analysis
particularly dermoscopic images. This repository studies several deep neural network (DNN) models and their comparative
performance. The study was performed on three dataset HAM10000, ISIC 2020 and ISIC 2019. Due to variations in the
structure of the datasets utilized, such as differing numbers of class labels and types of skin cancer, a modified dataset was
curated. This modified dataset ensured uniformity by providing common class labels across all datasets, thereby enabling
consistent training for the models across the entire dataset. The resultant dataset consists of 68,472 dermoscopic images.
Transfer learning approach was applied on three modified models: DenseNet201, EfficientNetV2M and ConvNeXtBase.
Fine-tuning methods were employed to increase the performance of models on modified dataset, while data augmentation
methods were applied to improve class balancing. The model's layered architecture classified the images into seven classes
which were aggregated into binary classes. The final classification was done using ensembling of the three models used.
The results favored ensembling of the models along with the superior individual model performance of DenseNet201.
Results show that ensembling the models achieved overall accuracy of 96.5% in multiclass and 98.7% in binary classification.

## Research paper
https://drive.google.com/file/d/1AOsPsFhR_vZiDTDkcbd-Zdd3lw7EUr3V/view?usp=drive_link

## Dataset:
- HAM10000: https://www.kaggle.com/datasets/pssingh1434131/ham10000/
- ISIC2020: https://www.kaggle.com/datasets/pssingh1434131/isic-2020/
- ISIC2019: https://www.kaggle.com/datasets/pssingh1434131/isic-2019/

## Model Architecture
![image](https://github.com/pssingh1434131/Skin-Cancer-Classification/assets/97393064/626af3e5-fe2d-4c7e-a9f4-518985a8c4f2)

## Flow Diagram
![image](https://github.com/pssingh1434131/Skin-Cancer-Classification/assets/97393064/d1dcb6f3-374b-4582-9b97-2bd40ea90fd3)

## Results

#### Accuracy of individual model on the dataset
![image](https://github.com/pssingh1434131/Skin-Cancer-Classification/assets/97393064/82ee0b51-59a8-496a-bf39-b53a5c17a0c7)

#### Performance of the Ensembled Model on the Dataset in Multiclass Classification
![image](https://github.com/pssingh1434131/Skin-Cancer-Classification/assets/97393064/f4ad7772-efe3-4207-853d-3649398e95b7)

#### Performance of the Ensembled Model on the Dataset in Binary Classification
![image](https://github.com/pssingh1434131/Skin-Cancer-Classification/assets/97393064/df4d17cb-0b72-466f-8274-2cecdb88df7d)
