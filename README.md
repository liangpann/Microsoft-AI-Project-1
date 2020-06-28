# Microsoft-AI-Project-1

1. Detailed Description of the Idea and Project

- My project implements the K-Nearest Neighbour and Naive Bayes algorithms (Machine Learning) on the Pima Indian Diabetes dataset to classify new patients as either having diabetes or not based on new medical data ('test data').

- More information about the project data and results on the classifiers accuracies are included in the MSA 2020 Project 1 PDF File.


2. Environment Setup & Dependencies

- The Classifier is named Classifier.py and the training dataset is called pima.csv. The classifier has been written using Python3. An example test file has been provided called testing.txt.

- The dataset used is the Pima Indian Diabetes dataset. It contains 768 instances described by 8 numeric attributes. There are two classes - yes and no. Each entry in the dataset corresponds to a patient's record; the attribtues are personal characteristics and test measurements; the class shows if the person shows signs of diabetes or not. The patients are from Pima Indiain heritage, hence the name of the dataset.

- The original dataset is sourced from UCI Machine Learning Repository. However, it has been modified for consistency and has been pre-processed to normalise the values for each attribute to make sure they are in the range [0,1]. This was done using a program called Weka.


3. Step-by-Step instruction on how to train and/or test your model

- My program takes 3 command line arguments. The first argument is the path to the training data file, the second is the path to the testing data file, and the third is the name of the algorithm to be executed (NB for Naive Bayes and kNN for the Nearest Neighbour, where k is replaced with a number; e.g. 5NN). An example command line argument is: python3 Classifier.py pima.csv testing.txt NB

- The input training file will consist of several rows of data, each with n attributes plus a single class value (yes or no). The file will not have a header row, will have one example per line, and each line will consist of a normalised value for each of the non-class attributes separated by commas, followed by a class value.

- The input testing data file will consist of several new examples to test your data on. The file will not have a header row, will have one example per line, and each line will consists of a normalised value for each of the non-class attributes separated by commas.

- My progam will output to standard output (a.k.a. "the console"). The output will be one class value (yes or no) per line - each line representing my program's classification of the corresponding line in the input file.
