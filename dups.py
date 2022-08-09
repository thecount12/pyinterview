"""
Sript to find duplicates
"""

# my_list = [1,20,30,44,5,56,57,8,19,10,31,12,13,14,35,16,27,58,19,21]


def dups(array=None):
    """
    :params array: list() of integers
    :return: int() 
    """
    m_dict = dict()
    for i in array:
        if i not in m_dict.keys():
            m_dict[i] = 1 
        else:
            m_dict[i] += 1
    dat = {k:v for k,v in m_dict.items() if v > 1}
    return list(dat.keys())[0]

if __name__ == "__main__":
    my_list = [1,20,30,44,5,56,57,8,19,10,31,12,13,14,35,16,27,58,19,21]
    print(dups(my_list))

