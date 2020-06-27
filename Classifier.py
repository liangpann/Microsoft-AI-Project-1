import sys
import os
import statistics
import math
import re


def NB(training_data, testing_data):
    # number of attributes
    attribute_length = len (training_data[0]) - 1

    yes = []
    no = []

    for i in training_data:
        if i[attribute_length] == 'yes':
            yes.append (i)

    for i in training_data:
        if i[attribute_length] == 'no':
            no.append (i)

    mean_yes = []
    mean_no = []
    stddev_yes = []
    stddev_no = []

    for i in range (attribute_length):
        temp_mean_yes = [float (item[i]) for item in yes]
        mean_yes.append (statistics.mean (temp_mean_yes))

        temp_mean_no = [float (item[i]) for item in no]
        mean_no.append (statistics.mean (temp_mean_no))

        temp_stddev_yes = [float (item[i]) for item in yes]
        stddev_yes.append (statistics.pstdev (temp_stddev_yes))

        temp_stddev_no = [float (item[i]) for item in no]
        stddev_no.append (statistics.pstdev (temp_stddev_no))

    p_yes = len (yes) / (len (yes) + len (no))
    p_no = len (no) / (len (yes) + len (no))

    for k in testing_data:
        yes_probabilities = []
        no_probabilities = []
        for i in range (attribute_length):
            yes_probabilities.append (1 / (stddev_yes[i] * math.sqrt (2 * math.pi)) * math.exp (
                (-(float (k[i]) - mean_yes[i]) ** 2) / (2 * stddev_yes[i] ** 2)))
            no_probabilities.append (1 / (stddev_no[i] * math.sqrt (2 * math.pi)) * math.exp (
                (-(float (k[i]) - mean_no[i]) ** 2) / (2 * stddev_no[i] ** 2)))

        final_yes = 1
        final_no = 1

        for x in yes_probabilities:
            final_yes = final_yes * x

        for x in no_probabilities:
            final_no = final_no * x

        final_yes = final_yes * p_yes
        final_no = final_no * p_no

        if final_yes >= final_no:
            print ("yes")
        else:
            print ("no")


def KNN(training_data, testing_data, num_neighbors):
    distences = []
    for each in training_data:
        distance = 0.0
        for i in range (len (testing_data)):
            distance += (float (testing_data[i]) - float (each[i])) ** 2
        distences.append ((each, math.sqrt (distance)))
    distances = sorted (distences, key=lambda x: x[1])
    neighbors = []
    for i in range (num_neighbors):
        neighbors.append (distances[i][0])
    res = []
    for row in neighbors:
        res.append (row[-1])
    return max (set (res), key=res.count)


def knn_pred(training_data, testing_data, num_neighbors):
    for each in testing_data:
        print (KNN (training_data, each, num_neighbors))


if __name__ == "__main__":

    if len (sys.argv) < 4:
        print ("Not enough arguments")
        exit ()

    if len (sys.argv) > 4:
        print ("Too many arguments")
        exit ()

    training_file = sys.argv[1]
    testing_file = sys.argv[2]
    classifier = sys.argv[3]

    training_data = []
    testing_data = []

    file_training = open (training_file, 'r')
    lines_training = file_training.readlines ()

    for i in lines_training:
        training_data.append (i.strip ('\n').split (","))
    file_testing = open (testing_file, 'r')
    lines_testing = file_testing.readlines ()

    for i in lines_testing:
        testing_data.append (i.strip ('\n').split (","))

    if classifier == "NB":
        NB (training_data, testing_data)
    else:
        num_neighbors = int (classifier.replace ('N', ""))
        knn_pred (training_data, testing_data, num_neighbors)
