"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data
from math import sqrt

# Part 1: vowel_count
def vowel_count(text: str) -> int:
    # Purpose: Counts the number of vowels in a string
    # Input(s): text: str, the string that has its vowels counted
    # Output: Returns the number of vowels in a string
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    num_vowels = 0

    for char in text:
        if char.lower() in vowels:
            num_vowels += 1

    return num_vowels


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # Purpose: Given a nested list, creates and returns a new list whose length is exactly 2
    # Input(s): items: A 2D list
    # Output: A new 2D list containing every list that has exactly 2 elements
    short_lists_list = [sublist for sublist in items if len(sublist) == 2]

    return short_lists_list

# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # Purpose: Create a new list where every pair of the original list is sorted in a non-descending order
    # Input(s): items: A 2D list 
    # Output: Returns a new list where every sublist of length 2 is sorted in non-descending order, 
    #         keeping nested lists of any other length in their original order
    ascending_pairs_list = []
    for sublist in items:
        if len(sublist) == 2 and sublist[0] > sublist[1]:
            # swap
            ascending_pairs_list.append([sublist[1], sublist[0]])
        else:
            ascending_pairs_list.append(sublist)

    return ascending_pairs_list


# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # TODO: Purpose: Computes the sum of two prices given dollars (int) and cents (int) of each
    # TODO: Input(s): first: Price object, second: Price object
    # TODO: Output: Returns a Price object containing the sum of first and second
    total_cents = first.cents + second.cents

    dollar_sum = first.dollars + second.dollars + (total_cents >= 100)
    cents_sum = total_cents % 100

    sum_price = data.Price(dollar_sum, cents_sum)

    return sum_price


# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # Purpose: The area of a rectangle bounded by a top-left corner point and bottom-right corner point
    # Input(s): A Rectangle object which contains a top-left corner Point object and bottom-right corner Point object
    # Output: The area of the rectangle (float)
    
    abs_dx = abs(rectangle.top_left.x - rectangle.bottom_right.x)
    abs_dy = abs(rectangle.top_left.y - rectangle.bottom_right.y)

    area = abs_dx * abs_dy

    return area


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # Purpose: Finds every book in a list that has a specified author
    # Input(s): author: str, the string to search for in each book's author list. books: list, a list of Book objects to search through
    # Output: A new list of Book objects that contains only the books that contain the specified author in their author list
    matching_books = []
    for book in books:
        if author in book.authors:
            matching_books.append(book)

    return matching_books


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # Purpose: Computes the smallest circle enclosing a rectangle
    # Input(s): rectangle: a Rectangle object
    # Output: A Circle object that represents the smallest circle enclosing the given Rectangle object
    rect_dx = rectangle.bottom_right.x - rectangle.top_left.x
    rect_dy = rectangle.top_left.y - rectangle.bottom_right.y

                    # distance to center + leftmost edge
    circle_center_x = rect_dx / 2 + rectangle.top_left.x
    circle_center_y = rect_dy / 2 + rectangle.bottom_right.y

    circle_center_point = data.Point(circle_center_x, circle_center_y)

    circle_to_corner_distance_x = rectangle.top_left.x - circle_center_x 
    circle_to_corner_distance_y = rectangle.top_left.y - circle_center_y

    circle_to_corner_distance = sqrt(circle_to_corner_distance_x*circle_to_corner_distance_x + circle_to_corner_distance_y*circle_to_corner_distance_y)

    smallest_enclosed_circle = data.Circle(circle_center_point, radius=circle_to_corner_distance)

    return smallest_enclosed_circle
    
    



# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # Purpose: Computes a list of names of employees whose pay is below the average of the given list of employees
    # Input(s): employees: a list of Employee objects 
    # Output: a list of strings of the name of employees whose pay is below the average of the given list of Employees
    
    if len(employees) == 0:
        return []


    total_pay = 0
    for employee in employees:
        total_pay += employee.pay_rate
    
    avg_pay = total_pay / len(employees)

    employees_below_avg = []

    for employee in employees:
        if employee.pay_rate < avg_pay:
            employees_below_avg.append(employee.name)

    return employees_below_avg



