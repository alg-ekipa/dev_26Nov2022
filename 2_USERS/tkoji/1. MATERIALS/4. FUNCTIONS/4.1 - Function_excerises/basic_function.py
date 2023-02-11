from statistics import median

def tripled_number(number: float) -> float:
    print(f'\nNumber {number} is tripled.')
    return round(number * 3,2)

def find_abs(number1: float, number2: float) -> float:
    return abs(number1 - number2)


def average_grade(g1: float, g2: float, g3:float) -> float:
    return (g1 + g2 + g3) / 3    
    
def top_three_avg(grade1, grade2, grade3, grade4):
    total = grade1 + grade2 + grade3 + grade4
    top_three = total - min(grade1,grade2,grade3,grade4)
    return max()


def weeks_elapsed(day1, day2):
    """ (int, int) -> int
    day1 and day2 are days in the same year. Return the number of full weeks
    that have elapsed between the two days.
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    0
    >>> weeks_elapsed(40, 61)
    3
    """
    return int(abs(day1 - day2) / 7)
    
print(weeks_elapsed.__doc__)
print(weeks_elapsed(1,365))


print(print.__annotations__)