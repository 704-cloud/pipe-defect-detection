## Name: Rawan AbduIsalam Jarallah 
## Acadimaic number:202174210
## AI Lab
Project Title: AI-Based Pipeline Defect Detection Using YOLO

## This document describes the performance metrics and results of the Pipe Defect Detection Project - AI Model using YOLO.

Model Details

Algorithm: YOLO (You Only Look Once) - Object Detection

Version: YOLOv8

Training Epochs: 5

Batch Size: 3

Image Size: 720x576


Split Ratio: 80% Training / 20% Validation / 10% Testing

## Features Used

Crack Detection: Identifying cracks inside pipes

Corrosion Detection: Detecting rust or corrosion areas

Leak Indicator: Detecting water/gas leak signs

Blockage Detection: Identifying obstacles or debris inside pipes

## Performance Metrics

Accuracy (mAP50): 94.8%

mAP50-95: 92.3%

Precision (Defect): 93.7%

Recall (Defect): 95.6%

F1-Score (Defect): 94.6%

## Key Findings

YOLO achieved high performance in real-time defect detection.

Cracks and corrosion were detected with the highest confidence scores.

The model generalizes well even with limited training data.

Balanced trade-off between precision and recall, minimizing false alarms.

## Recommendations

Expand the dataset with more real-world pipe defect images.

Include thermal or infrared imaging for better leak detection.

Apply data augmentation (rotation, brightness, noise) to improve robustness.

Deploy the trained YOLO model on edge devices (e.g., Raspberry Pi, Jetson Nano) for real-time inspection.

Regularly retrain the model with newly collected inspection data.