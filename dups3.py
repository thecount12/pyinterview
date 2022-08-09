"""
find duplicate integers
"""


def dups(array=None):
    """
    :params data: list() of integers
    :return: int() of duplicate integer
    """ 
    assert array is not None, "array can't be None"
    assert len(array) != 0, "array can't be empty" 
    assert type(array[2]) is int, "array must be integers"
    my_dict = {}
    for i in array:
        if i not in my_dict.keys():
            my_dict[i] = 1
        else:
            my_dict[i] += 1 
    found2 = {k:v for k,v in my_dict.items() if v == 2}
    return list(found2.keys())[-1]


if __name__ == "__main__":
    my_list = [1,20,30,44,5,56,57,8,19,10,31,12,13,14,35,16,27,58,19,21]
    print(dups(my_list))

    # testing
    try:
        print(dups())
    except Exception as err1:
        print(err1)
    # testing2
    try:
        print(dups([]))
    except Exception as err2:
        print(err2)
    # testing3
    try:
        print(dups([1, 2, 'three', 4]))
    except Exception as err3:
        print(err3)


