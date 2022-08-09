"""
Multi functional tool for data structure validation 
"""


def transform(array=None):
    """
    ;params array: list() of integers
    ;return: None
    """
    # Testing
    assert array is not None, "Must have an array"
    assert len(array) != 0, "Aarray must not be empty" 
    assert type(array[2]) is int, "Must be integers"
    m_dict = dict()
    for i in array:
        if i not in m_dict.keys():
            m_dict[i] = 1
        else:
            m_dict[i] += 1
    data = {k: v for k, v in m_dict.items() if v > 1 } 
    foo = list(data.keys())
    print(f"Duplicates: {str(foo)}")
    clean = [x for x in array if x not in foo]
    print(f"Non duplicates: {str(clean)}") 


if __name__ == "__main__":
    m_list = [1,4,7,8,9,4,10,11, 10]
    new_list = [1,2,"three", 4]
    print(f"Original: {m_list}")
    transform(m_list)
    # ### unit test 1
    try: 
        transform()
    except Exception as err1:
        print(err1)
    # ### unit test 2
    try:
        transform([])
    except Exception as err2:
        print(err2)
    # ### unit test 3
    try:
        transform(new_list)
    except Exception as err3:
        print(err3)

