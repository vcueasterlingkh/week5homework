"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    incoming_list = [1, 2, 3, 4, 5, 6, 7, 8]
    print max(incoming_list)


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    incoming_list = [1, 2, 3, 4, 5, 6, 7, 8]
    print min(incoming_list)


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    incoming_list = [1, 2, 3, 4]
    Sum = sum(incoming_list)
    print (sum)


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    incoming_dict = {"dog": "cat", "a": "asdfasdfasdf"}
    longest_value_key = len(max(incoming_dict, key=len))
    return len(longest_value_key)
