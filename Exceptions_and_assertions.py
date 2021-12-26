# calculating the sum of the decimal digits in a string.
def sumDigits(s):
    """Assumes s is a string
       Returns the sum of the decimal digits in s"""
    sum = 0
    for char in s:
        try:
            sum += int(char)
        except ValueError:
            pass
    return sum

# printing square of the number:
def square(s):
    """Assumes s is a string
       Returns the square of the s if it can be converted to an int"""
    try:
        print(f'The square of the number {s} is {int(s) ** 2}.')
    except ValueError:
        print(f'{s} is not an integer.')
        
# function to check beforehand if the user enters the correct input
def read_int():
    while True:
        value = input('Enter an integer: ')
        try:
            return int(value)
        except ValueError:
            print(f'{value} is not an integer.')
            
# Generalization of the function above
def read_val(val_type, request_msg, error_msg):
    """Assumes val_type is a type Class object (eg; int), 
       request_msg and error_msg are strings
       Returns the input value converted to the desired type 
       or sends a message to the user in case of conversion failure."""
    while True:
        value = input(request_msg + ': ')
        try:
            return val_type(value)
        except ValueError:
            print(value, error_msg)
            
# finds the first even integer in a list of integers
def find_an_even(L):
    """Assumes L is a list of integers
       Returns the first even number in L
       Raise ValueError if L does not contain an even number"""
    for i in L:
        if i%2 == 0:
            return i
    raise ValueError('No even number found.')
    
# element-wise division of two vectors/arrays, returns a list
def get_ratios(vect1, vect2):
    """Assumes: vect1 and vect2 are equal length lists of numbers
       Returns: a list containing the meaningful value of
       vect1[i]/vect2[i]"""
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) # nan = Not a Number
        except:
            raise ValueError('get_ratios called with bad arguments.')
    return ratios

# Potential use of the function above
try:
    print(get_ratios([1.0, 2.0, 7.0, 6.0],[1.0, 2.0, 0.0, 3.0]))
    print(get_ratios([], []))
    print(get_ratios([1.0, 2.0], [3.0]))
except ValueError as msg:
    print(msg)
    
# Comparison: Implementation of the function above without using the try-except
def get_ratios1(vect1, vect2):
    """Assumes: vect1 and vect2 are lists of equal length of numbers
       Returns: a list containing the meaningful values of vect1[i]/vect2[i]"""
    ratios = []
    if len(vect1) != len(vect2):
        raise ValueError('get_ratios called with bad arguments')
    for index in range(len(vect1)):
        vect1_elem = vect1[index]
        vect2_elem = vect2[index]
        if (type(vect1_elem) not in (int, float))\
            or (type(vect2_elem) not in (int, float)):
                raise ValueError('get_ratios called with bad arguments.')
        if vect2_elem == 0.0:
            ratios.append(float('NaN')) # NaN = Not a Number
        else:
            ratios.append(vect1_elem/vect2_elem)
    return ratios

def get_grades(fname):
    try:
        grades_file = open(fname, 'r') # open file for reading
    except IOError:
        raise ValueError('get_grades could not open', fname)
    grades = []
    for line in grades_file:
        try:
            grades.append(float(line))
        except:
            raise ValueError('Unable to convert line to float')
    return grades

try:
    grades = get_grades('quiz1grades.txt')
    grades.sort()
    median = grades[len(grades)//2]
    print('Median grade is', median)
except ValueError as error_msg:
    print('Whoops.', error_msg)