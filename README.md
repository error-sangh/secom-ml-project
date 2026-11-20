
# Semiconductor Manufacturing Fault Prediction Using Machine Learning

**Dataset Submission**


## 1. Dataset Description

**Dataset Name:** SECOM (Semiconductor Manufacturing)

**Original Source:** UCI Machine Learning Repository

**Original Contributors:** Michael McCann and Adrian Johnston

**Year Released:** 2008

**Official Dataset URL:**  
https://archive.ics.uci.edu/dataset/179/secom

**Dataset DOI:**  
https://doi.org/10.24432/C54305

### Download Instructions

1. Visit the official UCI dataset page.
2. Download the SECOM dataset archive.
3. Extract the files.
4. Place the extracted files inside `data/raw/`.

The SECOM dataset contains real world semiconductor manufacturing process measurements.

In the following dataset, each row represents a manufacturing sample and each column represents a numerical process measurement.

### Dataset Characteristics

| Property | Description |
|----------|-------------|
| Total Samples | 1,567 |
| Input Features | 590 |
| Feature Type | Numerical |
| Classification Type | Binary Classification |
| Passing Samples | 1,463 (93.36%) |
| Failing Samples | 104 (6.64%) |
| Missing Values | 41,951 |

### Dataset Files

The original dataset consists of three files:

- `secom.data`: Contains the numerical manufacturing process measurements.
- `secom_labels.data`: Contains the pass/fail labels and timestamps.
- `secom.names`: Contains documentation about the dataset.

### Input Features

The dataset contains 590 numerical features representing measurements collected during semiconductor manufacturing.

The original dataset does not provide the specific physical meaning or units of individual measurements.

The features are represented as:

`sensor_000, sensor_001, ... sensor_589`

The dataset contains missing values which needs preprocessing before model training.

### Target Labels

The dataset contains two classes:

| Label | Meaning |
|-------|---------|
| -1 | Pass |
| +1 | Fail |

## 2. Engineering Problem

The main engineering problem addressed in this project is automated fault detection in semiconductor manufacturing. Modern semiconductor manufacturing systems generate large amounts of process data. Analyzing these measurements manually can be difficult due to huge number of variables, missing measurements and complex relationships between process conditions. Machine learning can help identify patterns associated with manufacturing failures.

The project aims to address the following problems in semiconductor manufacturing:

1. **Manufacturing Fault Detection:** Develop machine learning models to identify defective semiconductor manufacturing samples using process measurements.

2. **High-Dimensional Data:** Handle the large number of sensor features which is about 590 in number and identify the most relevant measurements for fault prediction.

3. **Class Imbalance:** Address the imbalance between passing and failing samples to improve the detection of manufacturing failures.

4. **Missing Data:** Handle missing sensor measurements to improve data quality and model reliability.

5. **Model Performance and Efficiency:** Compare different machine learning algorithms to identify a model that provides accurate fault detection with reasonable computational cost.



## 3. Reference Research Paper

The initial methodological reference for this project is:

**Study on Data Preprocessing for Machine Learning Based on Semiconductor Manufacturing Processes.**

*Sensors*, 2024, 24(17), 5461.

Paper URL:  
https://www.mdpi.com/1424-8220/24/17/5461

This paper investigates preprocessing techniques and machine learning algorithms for semiconductor manufacturing classification.

The project will use it as a reference for developing baseline models and comparing different preprocessing strategies.

## 4. Dataset Citation

McCann, M., & Johnston, A. (2008). *SECOM* [Dataset]. UCI Machine Learning Repository.

https://doi.org/10.24432/C54305

**Dataset License:** Creative Commons Attribution 4.0 (CC BY 4.0)
