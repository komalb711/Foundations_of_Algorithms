"""
CSCI-665: Foundations of Algorithms
Homework 1 - Problem 4

This program determines the number of elements from the first set that have
only one valid partner in stable matching. We have 2 groups of elements,
consider them as groupA and groupB. A match is said to be valid if an
element from groupA matches to an element of groupB in both cases of stable
matching i.e., when groupA does the asking part and when groupB does the
asking job.
Here we perform 2 stable matching i.e first groupA elements asks groupB
elements based on their preferences, and second when groupB elements asks
groupB based on their preferences. Then we compare the results of the two
stable matching. The number of elements that are matched to the same
elements is the number of valid pairs.
Input:- n - number of elements in each group
        a11,....a1n ]-- groupA preferences list for each element in groupB.
        a21,....a2n ]   Therefore input is n lines long and on each line
        an1,....ann ]   number separated by spaces.
        b11,....b1n ]-- groupB preferences list for each element in groupA
        b21,....b2n ]   Therefore input is n lines long and on each line
        bn1,....bnn ]   number separated by spaces.

Output:- number of valid matches for the give input.

Note: The python List is used in the following program.
•	The append operation has the time complexity of amortized O(1).
•	The extend operation has the time complexity of O(n), where n is the
    number of elements in the list passed to extend operation.
•	The get item operation has the time complexity of O(1)
"""


class GaleShapley:
    """
    This class implements the stable matching(gale-shapley) algorithm
    """

    __slots__ = 'cardinality', 'group_a_pref', 'group_b_pref', \
                'asked_group_a_count', 'inverse_group_A_preference', \
                'inverse_group_B_preference', 'partner_aTob', \
                'partner_bToa', 'unmatched_members'

    def __init__(self, number, group_a_pref, group_b_pref):
        """
        Constructor for the GaleShapley class
        :param number: number of people in each group
        :param group_a_pref: preference list of all people in group A
        :param group_b_pref: preference list of all people in group B
        """
        self.cardinality = number
        # set the count of number of people group A asked to 0
        self.asked_group_a_count = [0] * number
        # initialize the matching of groupA->groupB and groupB->groupA as -1
        self.partner_aTob, self.partner_bToa = [-1] * number, [-1] * number
        # set preferences
        self.group_a_pref = group_a_pref
        self.group_b_pref = group_b_pref
        # find set the inverse of preference list for both group A and group B
        self.inverse_group_A_preference = self.create_inverse_preference_list(group_a_pref)
        self.inverse_group_B_preference = self.create_inverse_preference_list(group_b_pref)

        # create a stack for all unmatched members form groupA
        self.unmatched_members = Stack()
        # add all members from groupA to the stack in descending order
        for i in range(number - 1, -1, -1):
            self.unmatched_members.push(i)

    def create_inverse_preference_list(self, group_preference_list):
        """
        This function creates an inverse preference list from a given
        preference list.
        :return: The inverse preference list
        """
        # initialize the inverse preference list as empty
        inverse_preference_list = []

        # iterate over the input preference list to and find the current
        # preference number and put that number as the value for that
        # member.
        for preference_list in group_preference_list:
            # initialize the temp prefernce list to all -1s
            temp_preference_list = [-1] * len(preference_list)

            # iterate over the preference list of each member of
            # group and assign the index at which the member is
            # as the preference number for that member in the
            # temp_preference_list
            for index, value in enumerate(preference_list):
                temp_preference_list[value] = index

            # append the temp_preference_list to the inverse list
            inverse_preference_list.append(temp_preference_list)

        # return the inverse preference list
        return inverse_preference_list

    def stable_matching_implementation(self):
        """
        This function implements the actual stable matching algorithm
        It takes an unmatched member of group A and asks a member of group B,
        based on his preference list. There can be three possibilities
        a) the member of group B is free/unmatched and therefore they are
            matched
        b) the member of group B is matched already, but prefers the asking
            member of group A rather than his currently matched person, and
            so he swaps between the two. In such a case, the previously matched
            member of group A is added back to stack of unmatched members.
        c) the member of group B prefers his existing match and declines
            the request.
        We keep on doing the above step until all members are matched
        :return: None
        """
        # continue the loop until all members are matched
        while self.unmatched_members.peek() != None:

            # get an unmatched member from the stack(peep+pop)
            group_a = self.unmatched_members.peek()
            self.unmatched_members.pop()
            # get the next preferred member of groupB
            # by the unmatched group a member
            group_b = self.group_a_pref[group_a][self.asked_group_a_count[group_a]]

            # check if that group B member is free or matched
            if self.partner_bToa[group_b] == -1:
                # if free match them up, and update partnerA->B and
                # partnerB->A lists
                self.partner_aTob[group_a] = group_b
                self.partner_bToa[group_b] = group_a

            # if group B member is already matched then check if he/she
            # prefers the current member over the previously matched member
            elif self.inverse_group_B_preference[group_b][group_a] < \
                    self.inverse_group_B_preference[group_b][self.partner_bToa[group_b]]:
                # if he prefers the current member then swap them and update
                # partnerA->B and partnerB->A lists and add the previously
                # matched member to the stack
                self.unmatched_members.push(self.partner_bToa[group_b])
                self.partner_aTob[self.partner_bToa[group_b]] = -1
                self.partner_aTob[group_a] = group_b
                self.partner_bToa[group_b] = group_a
            # if the group B member prefers the previously matched member then
            # add the group A member back to the stack
            else:
                self.unmatched_members.push(group_a)
            # increment the number of people the groupA member has asked
            self.asked_group_a_count[group_a] = self.asked_group_a_count[group_a] + 1


class Stack:
    """
    This class implements the stack using node class.
    """
    __slots__ = "top"

    def __init__(self):
        """
        constructor for the stack.
        """
        # initially the stack is empty and so top is None
        self.top = None

    def is_empty(self):
        """
        function to check if the stack is empty
        :return: True - if stack is empty
                 False - if stack is not empty
        """
        return self.top == None

    def push(self, value):
        """
        function to push a value on the stack
        :param value: the value to be pushed to the stack
        :return: None
        """
        # push the value on the stack and update the
        # top to be the the new value
        self.top = Node(value, self.top)

    def pop(self):
        """
        function to pop the top from the stack
        :return: None
        """
        # check if the stack is not empty
        # if not empty then remove the top item and
        # make the top as the next item on the stack
        if not self.is_empty():
            self.top = self.top.next

    def peek(self):
        """
        function to get the value at the top of the stack
        :return: None - if stack is empty
                 value at the top - otherwise
        """
        # check if stack is empty, if yes return None,
        # else return the value at the top of stack
        if not self.is_empty():
            return self.top.data
        else:
            return None


class Node:
    """
    This class implements a node with data and next link to
    implement a node based stack
    """
    __slots__ = 'data', 'next'

    def __init__(self, data, next=None):
        """
        constructor for the class Node
        :param data: the actual data to be stored
        :param next: the link to the next item,
                     default value is None
        """
        self.data = data
        self.next = next

    def __str__(self):
        """
        function to return the string equivalent of the node, ie the data
        :return:
        """
        return str(self.data)


def main():
    """
    Mina function to take input from user, and find the stable matching in 2 cases
    1) when group A asks group B
    2) when group B asks group A
    Then we compare the matching of the above 2 cases and calculate
    the number of valid matches, i.e., the number of people from either group
    that we matched to the same people in both of the above cases
    :return:None
    """
    number = int(input())  # number of people in each group

    # initialize the pref list as empty list
    group_1 = []
    group_2 = []

    # iterate over the input and fill the preference of group1
    for i in range(0, number):
        preferences = list(map(int, input().split()))
        group_1.append(preferences)

    # iterate over the input and fill the preference of group2
    for i in range(0, number):
        preferences = list(map(int, input().split()))
        group_2.append(preferences)

    # perform the stable matching when group 1 asks group 2
    ab_matching = GaleShapley(number, group_1, group_2)
    ab_matching.stable_matching_implementation()
    # get the result of this stable matching
    result1 = ab_matching.partner_aTob

    # perform the stable matching when group 2 asks group 1
    ba_matching = GaleShapley(number, group_2, group_1)
    ba_matching.stable_matching_implementation()
    # get the result of this stable matching
    result2 = ba_matching.partner_bToa

    ppl_with_same_matches = 0

    # iterate over the results and find the number of people
    # who were matched to same people in the 2 stable matching s
    for i in range(0, len(result1)):
        # check if member of group 1 they were matched to same
        # person of group 2 in the 2 stable matching
        if result1[i] == result2[i]:
            # yes then increment the counter
            ppl_with_same_matches += 1

    # print the number of valid matches
    print(ppl_with_same_matches)


if __name__ == '__main__':
    main()
