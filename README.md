# Histopathology Image Classification Project

## Overview

This project focuses on classifying cell images into four categories using the MobileNetV2 model. The Chaoyang dataset utilized is based on the "Hard Sample Aware Noise Robust Learning for Histopathology Image Classification" paper, and the goal is to develop an accurate-simple model for cell classification as Capstone 2 project for ML Zoomcamp 2023.

## Table of Contents

- [Introduction](#introduction)
- [Repository Structure](#repository-structure)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Usage](#usage)
- [Results](#results)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)
- [Future Improvement](#future-improvement)
- [License](#license)

## Introduction

Cell classification is a crucial task in the field of cancer diagnosis. This project employs the state-of-the-art MobileNetV2 model to accurately categorize cell images, aiming to contribute to advancements in machine learning and patology.

## Repository Structure

- `data/`: Contains the training, validation and testing data sets.
- `scripts/`: Python scripts for data and model manipulation.
- `src/`: Project source code, including the training and evaluation script.
- `saved_models/`: Directory to store the trained models.

## Dataset

The dataset used in this project is derived from the ["Hard Sample Aware Noise Robust Learning for Histopathology Image Classification"](https://ieeexplore.ieee.org/document/9600806) paper. It consists of a diverse set of cell images labeled into four distinct categories. 

- (0) Normal cells.
- (1) Serrated cells.
- (2) Adenocarcinoma cells.
- (3) Adenoma cells. 

The dataset is preprocessed and divided into training, validation, and testing sets.

```bash
@article{zhuhard,
  title={Hard Sample Aware Noise Robust Learning for Histopathology Image Classification},
  author={Zhu, Chuang and Chen, Wenkai and Peng, Ting and Wang, Ying and Jin, Mulan},
  journal={IEEE transactions on medical imaging}
}
```

## Model Architecture

The model architecture chosen for this project is MobileNetV2. This is a powerful convolutional neural network known for its efficiency and high performance in image classification tasks. The model has been fine-tuned on the cell dataset to optimize its performance for this specific task.

## Usage

### Requirements

- Python (version 3.10.12)
- TensorFlow (version 2.15.10)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/JimGora/Classification.git
   cd Classification

## Results

The model was trained and evaluated on the cell classification dataset. The following metrics provide insights into the performance of the model:

- **Accuracy:** 99.58%
- **Precision:** 74.84%

## Acknowledgments

This project is the culmination of the ML Zoomcamp 2023 program led by Alexey Grigorev, his expertise and dedication played a crucial role in shaping this project and expanding my understanding of Machine Learning.

Special thanks to Chuang Zhu [email: czhu@bupt.edu.cn] for providing the foundational dataset from the [HSA-NRL](https://github.com/bupt-ai-cz/HSA-NRL?tab=readme-ov-file) repo used in this project.

## Contact
For any inquiries or issues, please contact:
Jimmy Gora: jimmy.r.gora@gmail.com

## Future Improvements
Train a different model and compare with other dataset to improve the model.

## License
This project is under the MIT license.
