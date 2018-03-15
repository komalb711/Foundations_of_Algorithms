"""
CSCI-665: Foundations of Algorithms
Homework 1 - Problem 5

This program implements the Merge Sort
Merge Sort - Its best. average and worst case time complexity is
O(n.logn). It uses the concept of divide and conquer, and divides the
data in half in each recursive call, and then merges the two parts to
form the sorted data.


Note: The python List is used in the following program.
•	The append operation has the time complexity of amortized O(1).
•	The extend operation has the time complexity of O(n), where n is the
    number of elements in the list passed to extend operation.
•	The get item operation has the time complexity of O(1)

"""

import time
import numpy


class MergeSort:
    """
    This class implements the  the merge sort
    """
    __slots__ = 'original_data'

    def __init__(self, data):
        """
        This function is the constructor for the Sorting class
        :param data: it is the original data that we have to sort
        """
        self.original_data = data

    def merge_sort(self):
        """
        this function sorts the data using internal __merge_sort__()
        :return: the sorted list of data
        """
        return self.__merge_sort__(self.original_data, len(self.original_data))

    def __merge_sort__(self, data, size):
        """
        This is a recursive function.It divides the data in 2 halfs (left
        and right) recursively until the only 1 element remains in the list and
        returns that list. Then it merges the sorted left and right lists into
        one list and returns it.

        :param data: the list of unsorted data
        :param size: the size of the unsorted data
        :return: the merged list of sorted left and right list
        """

        # if list size is one then return it
        if size == 1:
            return data

        # else find the middle index
        middle = size // 2

        # recursively call the merge sort on the left and right sub-lists
        left = self.__merge_sort__(data[:middle], middle)
        right = self.__merge_sort__(data[middle:], size - middle)

        # merge the sorted left and right sublist and return it
        return self.__merge__(left, right)

    def __merge__(self, left, right):
        """
        This function merges the 2 sorted list into one list
        and return that list
        :param left: a left sorted list
        :param right: a right sorted list
        :return: the sorted and merge list containing all elements
                    of left and right list
        """

        # initialize indices for left and right lists
        left_index, right_index = 0, 0

        # initialize the merged list as empty
        merged_list = []

        # iterate over the left and right lists until of the them is run over
        # i.e the left index is less than length of left list and right index
        # is less than length of right list
        while left_index < len(left) and right_index < len(right):

            # check if element at left index from left list is greater than element
            # at right index of the right list
            if left[left_index] > right[right_index]:
                # yes so we add the left element to the merged list
                # and increment the left index
                merged_list.append(left[left_index])
                left_index += 1
            else:
                # no so we add the right element to the merged list
                # and increment the right index
                merged_list.append(right[right_index])
                right_index += 1

        # now copy the remaining elements from either the
        # left or right list to the merged list
        if left_index < len(left):
            merged_list.extend(left[left_index:])
        elif right_index < len(right):
            merged_list.extend(right[right_index:])

        # return the merged list
        return merged_list


def main():
    """
    Main function that takes the input from the user for the value of n
    and the type of distribution of the numbers, i.e 1. for Uniform
    distribution and 2. for Gaussian distribution.

    Based on the value of n and the type of distribution, generate the
    numbers in between [0,1) and then use the merge sort to sort numbers
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
    sorter = MergeSort(unsorted_data)

    # start timer for merge sort
    start_time_merge_sort = time.time()
    # get the sorted list using the merge sort
    merge_sort_data = sorter.merge_sort()
    # calculate the time taken for the merge sort to complete
    start_time_merge_sort = time.time() - start_time_merge_sort
    # display the merge sort results
    print("\n--- Merge Sort Results ---")
    for num in merge_sort_data:
        print(num)

    # display the running time of the merge sort
    print("--- Time taken for Merge Sort : ", start_time_merge_sort, " seconds ---")


if __name__ == '__main__':
    main()
