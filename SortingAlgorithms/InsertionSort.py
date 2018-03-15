"""
CSCI-665: Foundations of Algorithms
Homework 1 - Problem 5

This program implements Insertion Sort
Insertion Sort - Its best, worst, and average case time complexity
is O(n^2).In this sort we take each new element and try to insert it
into its correct position by comparing it with all the previously
sorted elements.

Note: The python List is used in the following program.
•	The append operation has the time complexity of amortized O(1).
•	The extend operation has the time complexity of O(n), where n is the
    number of elements in the list passed to extend operation.
•	The get item operation has the time complexity of O(1)

"""

import time
import numpy


class InsertionSort:
    """
    This class implements the insertion sort.
    """
    __slots__ = 'original_data'

    def __init__(self, data):
        """
        This function is the constructor for the Sorting class
        :param data: it is the original data that we have to sort
        """
        self.original_data = data

    def insertion_sort(self):
        """
        this function does the actual insertion sort on the
        original data
        :return: the sorted data using insertion sort
        """

        data = self.original_data

        # iterate over the list of unsorted data and insert
        # each element in its correct position based on its
        # value and all the values before it
        for index in range(1, len(data)):
            position = index

            # compare current data element with its previous sorted elements
            # keep on swapping value until the current data reaches its
            # correct psoition
            while position > 0 and data[position - 1] > data[position]:
                data[position], data[position - 1] = data[position - 1], data[position]
                position -= 1

        # return the sorted list
        return data


def main():
    """
    Main function that takes the input from the user for the value of n
    and the type of distribution of the numbers, i.e 1. for Uniform
    distribution and 2. for Gaussian distribution.

    Based on the value of n and the type of distribution, generate the
    numbers in between [0,1) and then use the insertion sort to sort
    numbers
    :return: None
    """

    # take user input for the value of n
    count = int(input("Enter value of n:"))

    # take user input for the type of distribution
    distribution_type = int(input("Kind of distribution:"
                                  "\n1) Uniform "
                                  "\n2) Gaussian distribution"
                                  "\nEnter selection number:)"))
    unsorted_data = []

    # distribution_type 1 equals uniform distribution, and distribution_type 2
    # equals the gaussian distribution with ( mu =0.5, and sigma = 1/1000)
    # so use numpy function to generate the of unsorted list of numbers
    if distribution_type == 1:
        unsorted_data = numpy.random.uniform(0, 1, count)
    elif distribution_type == 2:
        unsorted_data = numpy.random.normal(0.5, 1 / 1000, count)

    # create object of type sorting
    sorter = InsertionSort(unsorted_data)

    # start timer for insertion sort
    start_time_insertion_sort = time.time()
    # get the sorted list using the insertion sort
    insertion_sort_data = sorter.insertion_sort()
    # calculate the time taken for the insertion sort to complete
    start_time_insertion_sort = time.time() - start_time_insertion_sort
    # display the insertion sort results
    print("\n--- Insertion Sort Results ---")
    for num in insertion_sort_data:
        print(num)

    # display the running time of the sorts
    print("--- Time taken for Insertion Sort : ", start_time_insertion_sort, " seconds ---")


if __name__ == '__main__':
    main()
