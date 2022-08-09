"""
Move the zeros to the end but have other elements sorted

array=[0,0,1,3,12]
array=[0,3,0,12,1]
array=[0,0,0,0,0] 
results: [1,3,12,0,0]
"""

def move_zero(array=None):
    """
    :params array: list() of integers
    :return list() sorted but numbers but with zero's at the end
    """
    assert array is not None, "We must have an array to work with"
    assert len(array) != 0, "the array can't be empty"
    assert type(array[2]) is int, "must have integers"
    new_ar = []
    temp_ar = []
    for i in array:
        if i == 0:
            temp_ar.append(i)
        if i != 0:
            new_ar.append(i)
    return list(sorted(new_ar)+temp_ar)


if __name__ == "__main__":
    # test case 1
    my_array1 = [0,0,1,3,12]
    print(move_zero(my_array1))
    # test case 2
    my_array2 = [0,3,0,12,1]
    print(move_zero(my_array2))
    # test case 3
    my_array3 = [0,0,0,0,0]
    print(move_zero(my_array3))
    # unit test 1    
    try:
        print(move_zero())
    except Exception as err1:
        print(err1)
    # unit test 2
    try:
        print(move_zero([]))
    except Exception as err2:
        print(err2)
    # unit test 3
    try:
        print(move_zero([1, 2, 'three', 4, 0]))
    except Exception as err3:
        print(err3)
