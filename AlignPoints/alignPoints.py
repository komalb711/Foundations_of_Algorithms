"""
CSCI-665: Foundations of Algorithms
Homework 2 - Problem 4

This program takes n different points as input and find the
maximum number of pair of points that can aligned if we
fold the plane of paper.

Input:- n(number of points)
        x1 y1 ( x and y
        x2 y2   coordinates
        .  .    of n points)
        .  .
        Xn yn

Output:- m (maximum number of pair of points that align
            if we fold the plane of paper)

Note: The python List is used in the following program.
•	The append operation has the time complexity of amortized O(1).
•	The get item operation has the time complexity of O(1)
"""

import math


def main():
    """
    The main function of the program which takes the number of points and
    the x and y coordinate values of those points and save them in the in
    a list. Then we find all the possible line of reflections. Further we
    sort these lines of reflections based on the slope of them and their
    intercepts and finally use this sorted list to find the number of pair
    of points that align with a line of reflections
    """

    number = int(input())  # number of points
    group_of_points = []  # initialize list to save points

    # iterate over the input and fill the x and y values of points
    for i in range(0, number):
        coordinates = list(map(int, input().split()))
        group_of_points.append(coordinates)

    # find all the lines of reflections
    reflection_lines = find_line_of_reflection(group_of_points)

    # sort the lines of reflection based on the slope and
    # the intercept using the merge sort
    sorted_reflection_lines = merge_sort(reflection_lines)

    # find the reflection line that occurs the maximum number
    # of time and its count would be our answer
    find_max_repeating_value(sorted_reflection_lines)


def find_line_of_reflection(points):
    reflection_lines = []

    for cntr_1 in range(0, len(points)):
        point1_x = (points[cntr_1])[0]
        point1_y = (points[cntr_1])[1]
        for cntr_2 in range(cntr_1 + 1, len(points)):
            point2_x = (points[cntr_2])[0]
            point2_y = (points[cntr_2])[1]
            slope, midpoint_x, midpoint_y = get_slope_midpoint_of_2_points(point1_x, point1_y, point2_x, point2_y)
            bisector_slope, intercept = get_bisector_slope_and_intercept(slope, midpoint_x, midpoint_y)
            line = [bisector_slope, intercept]
            reflection_lines.append(line)

    return reflection_lines


def get_slope_midpoint_of_2_points(x1, y1, x2, y2):
    """

    :param x1: x coordinate of point 1
    :param y1: y coordinate of point 1
    :param x2: x coordinate of point 2
    :param y2: y coordinate of point 2
    :return: the slope of line joining the 2 points, the midpoint
                of the line joining the 2 points
    """
    # find the change in x and y i.e dx and dy
    x_diff = x2 - x1
    y_diff = y2 - y1

    # if x change is zero, then the slope is infinite
    if x_diff == 0:
        slope = math.inf
    # otherwise calculate the slope using the formula
    # slope = dy/dy
    else:
        slope = y_diff / x_diff

    # find x and y coordinate of midpoint of the line joining 2 points
    midpoint_X = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2

    # return the slop and coordinates of the midpoint
    return slope, midpoint_X, midpoint_y


def get_bisector_slope_and_intercept(slope, x, y):
    """
    This function finds the slope of the perpendicular bisector
    of the line formed by 2 points using the slope of line formed
    by joining them slope. Additionally we also find the y intercept
    of the perpendicular bisector. Only in case of line with slope
    as infinity we use the x intercept as there is no y intercept.
    :return: the slope of bisector line and the its y intercept
                in case the slope of line is infinity, we return
                the x intercept as its the onl differencing factor
                between 2 lines with slope as infinity.

    """
    # if slope of line is infinity, then the slope of its perpendicular
    # line is 0, and in this case the y intercept is the y coordinate value
    # of the line passing through it as slope is 0
    if math.isinf(slope):
        bisector_slope = 0
        intercept = y

    # if slope of line is 0, then the slope of its perpendicular line
    # is infinity and in this case the y intercept is infinity, so we use
    # the x intercept
    elif slope == 0:
        bisector_slope = math.inf
        intercept = x

    # in all cases the slope of its perpendicular line(m1) is calculate by
    # using the formula (m1 = -1/m2) where the m2 is the slope of the line
    # passing through the two points. next we calculate the y intercept
    # using the equation of the line y = mx + c, where c is intercept
    # and m is slope, and x and y are coordinates of a point on the line

    else:
        bisector_slope = -1 / slope
        intercept = y - bisector_slope * x

    # return the slope of bisector and the intercept value
    return bisector_slope, intercept


def merge_sort(reflection_lines):
    """
    this function sorts the data using  __merge_sort__()
    :return: the sorted list of data
    """
    return __merge_sort__(reflection_lines, len(reflection_lines))


def __merge_sort__(data, size):
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
    left = __merge_sort__(data[:middle], middle)
    right = __merge_sort__(data[middle:], size - middle)

    # merge the sorted left and right sublist and return it
    return __merge__(left, right)


def __merge__(left, right):
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

        # check if element at left index from left list is smaller than element
        # at right index of the right list
        if left[left_index][0] < right[right_index][0] or (
                        left[left_index][0] == right[right_index][0] and left[left_index][1] <= right[right_index][1]):
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


def find_max_repeating_value(reflection_lines):
    """
    This function finds the maximum occurring reflection line in the
    reflection_lines list as it determines the line over which if the
    plane is folded maximum number of pair of points align.
    :param reflection_lines:
    :return: None
    """

    # initialize max value and current count to 1
    max_value = 1
    count = 1

    # initialize the current value to the 1st value in the list
    current_value = reflection_lines[0]

    # iterate over the list and check if the current value matches with
    # the next value in the list if yes then increment the current count
    # by 1, else update the current value to the next value.
    # Since the list is sorted based on slope and the intercept value
    # all the entries with same value will be saved consecutively and can
    # be counted in linear time
    for counter in range(1, len(reflection_lines)):
        # check if the current value matches with  the next value
        # if yes then increment the current count
        if reflection_lines[counter][0] == current_value[0] and reflection_lines[counter][1] == current_value[1]:
            count += 1
        else:
            # else update the current value to the next value and reset count
            count = 1
            current_value = reflection_lines[counter]

        # if the current count is greater than the max value then update
        # the maximum value to the current count
        if count > max_value:
            max_value = count

    # print the answer which is the maximum number of pair of points that align
    print(max_value)


if __name__ == '__main__':
    main()
