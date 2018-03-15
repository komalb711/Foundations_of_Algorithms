"""
CSCI-665: Foundations of Algorithms
Homework 1 - Problem 5

This program implements the bucket sort
Bucket Sort - Its best case time complexity is O(n), when the data
is uniformly distributed. Its worst case scenario is O(n^2), when all
the data ends up in one bucket. In bucket sort, we create n buckets
and put elements into different buckets and then each such bucket is
sorted and combined to form the sorted data

Note: The python List is used in the following program.
•	The append operation has the time complexity of amortized O(1).
•	The extend operation has the time complexity of O(n), where n is the
    number of elements in the list passed to extend operation.
•	The get item operation has the time complexity of O(1)

"""

import time
import numpy
import math
from InsertionSort import InsertionSort


class BucketSort:
    """
    This class implements the the bucket sort
    """
    __slots__ = 'original_data'

    def __init__(self, data):
        """
        This function is the constructor for the Sorting class
        :param data: it is the original data that we have to sort
        """
        self.original_data = data

    def bucket_sort(self):
        """
        this function performs bucket sort
        :return: the sorted data using bucket sort
        """

        # set bucket_size as the length of the original list
        bucket_size = len(self.original_data)

        # set the buckets as empty lists
        bucket = [[] for i in range(bucket_size)]

        # iterate over the unsorted list and put them into
        # buckets based on its value.
        for data in self.original_data:
            # find which bucket to add the current data using the
            # floor function of math, current data and bucket size
            index = int(math.floor(bucket_size * data))
            # put that data into bucket.
            bucket[index].append(data)

        # use insertion sort to sort each of the buckets and append
        # it to the resultant list
        result = []
        for sub_list in bucket:
            # if the length of bucket is more than 1 then use
            # insertion sort to sort it
            if len(sub_list) > 1:
                sorted_list = InsertionSort.insertion_sort()
                sub_list = sorted_list

            # append the sublist to the resultant list
            result.extend(sub_list)

        # return the result of the bucket sort
        return result


def main():
    """
    Main function that takes the input from the user for the value of n
    and the type of distribution of the numbers, i.e 1. for Uniform
    distribution and 2. for Gaussian distribution.

    Based on the value of n and the type of distribution, generate the
    numbers in between [0,1) and then use the bucket sort to sort the
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
    sorter = BucketSort(unsorted_data)

    # start timer for bucket sort
    start_time_bucket_sort = time.time()
    # get the sorted list using the bucket sort
    bucket_sort_data = sorter.bucket_sort()
    # calculate the time taken for the bucket sort to complete
    start_time_bucket_sort = time.time() - start_time_bucket_sort
    # display the bucket sort results
    print("\n--- Bucket Sort Results ---")
    for num in bucket_sort_data:
        print(num)

    # display the running time of the bucket sort
    print("--- Time taken for Bucket Sort : ", start_time_bucket_sort, " seconds ---")


if __name__ == '__main__':
    main()
