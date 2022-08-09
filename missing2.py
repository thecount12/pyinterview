"""
finding missing number in array
"""

m_array = [1,2,3,5,6,7,8,9,10]


def missing(data=None):
    """
    ;params data: list() of integers in array
    ;return: int() of found array
    """
    assert data is not None, "Need an array"
    assert len(data) !=0, "Empty array"
    assert type(data[2]) is int, "Must have integers"
    for i in range(len(data)):
        if m_array[i] != i+1:
            found =  i+1
            return found
            break 


if __name__ == "__main__":
    print(missing(m_array))
    foo = []
    bar = [1, 2, "three", 4, 5]
    try:
        # print(missing())
        # print(missing(foo))
        print(missing(bar))
    except Exception as error:
        print(error)

