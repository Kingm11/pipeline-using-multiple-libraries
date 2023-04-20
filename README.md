# Creating pipline using Pycaret3
## Overview
 
 1. ### The code uses Pycaret3, a Python library for machine learning, to create a pipeline on the Iris dataset.
2. ### The pipeline includes steps for data preprocessing, model training, model tuning, and model evaluation.
3. ### The code also includes functions for comparing and visualizing multiple models.

1. ### The pipeline uses Pycaret3 to create a machine learning model to predict the species of an iris flower based on its characteristics.

2. ### The pipeline loads the iris dataset from Pycaret3's built-in datasets and sets the target variable as 'species'.

3. ### The pipeline uses Pycaret3's setup() function to preprocess the data and set up the machine learning pipeline.

4. ### The pipeline creates a Random Forest model using Pycaret3's create_model() function.

5. ### The pipeline evaluates the model using Pycaret3's plot_model() function to visualize the confusion matrix.

6. ### The pipeline deploys the model using Pycaret3's deploy_model() function, making it available for predictions through an API endpoint.

## Scope 



1. ### The scope of this pipeline is to demonstrate how Pycaret3 can be used to build an end-to-end machine learning pipeline with minimal coding effort.
2. ### Pycaret3 automates the machine learning pipeline, making it easier and faster to build and deploy machine learning models.
3. ### This pipeline demonstrates how easy and fast it is to create a machine learning model using Pycaret3. By automating the end-to-end machine learning process, Pycaret3 enables data scientists and machine learning practitioners to focus on high-level tasks such as feature engineering, hyperparameter tuning, and model selection.
4. ### The code is intended for users who are new to machine learning and want to quickly create a pipeline on a dataset.The code is focused on classification tasks and is specifically tailored to the Iris dataset.The code assumes that the user has some basic knowledge of Python and data preprocessing techniques.

## Data

### For this Project, we will use the classic Iris dataset, which contains information about the physical characteristics of different types of iris flowers.


## Steps

1. ### Import the necessary libraries, including Pycaret3 and the Iris dataset.
2. ### Use the setup() function to preprocess the data and split it into training and testing sets.
3. ### Use the compare_models() function to compare multiple models and select the best performing one.
4. ### Use the tune_model() function to tune the hyperparameters of the best performing model.
5. ### Use the plot_model() function to visualize the performance of the best performing model.
6. ### Use the predict_model() function to make predictions on new data using the best performing model.

## Technol0gies used

[.pycaret](https://pycaret.org/)

## Visualization


![image](https://github.com/Kingm11/AppliedDS/blob/main/Visuals/Screenshot%202023-04-19%20235416.png)


![image](https://github.com/Kingm11/AppliedDS/blob/main/Visuals/2.png)

![image](https://github.com/Kingm11/AppliedDS/blob/main/Visuals/3.png)

![image](https://github.com/Kingm11/AppliedDS/blob/main/Visuals/4.png)

![image](https://github.com/Kingm11/AppliedDS/blob/main/Visuals/5.png)



