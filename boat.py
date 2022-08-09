"""
people = [3,2,2,1]
boat = limit 3 to a boat 
results trip = 3
"""

def voyage(p=None, boat=None):
    """
    :params p: list() of integers
    :params boat: int() of limit of people on board a boat
    :return: int() of trips the boat has to make
    """
    assert p is not None, "must have an array"
    assert len(p) != 0, "array can't be empty"
    assert type(p[2]) is int, "must be integers"    
    trips = 0
    item = sum(p)
    foo = item / boat 
    mod_test = item % boat 
    if mod_test == 0:
        trips = int(foo) 
    if mod_test > 0:
        trips = int(foo) + 1
    return trips
 
if __name__ == "__main__":
    # test 1
    people = [3,2,2,1]
    print(voyage(people, 3))
    # test 2
    people1 = [3,2,2,1,2]
    print(voyage(people1, 3)) 
    # test 3
    people3 = [3,2,2,1,4]
    print(voyage(people3, 4))
    print("------")
    # unit test 1 
    try:
        print(voyage())
    except Exception as err1:
        print(err1)
   # unit test2
    try:
        print(voyage([], 3))
    except Exception as err2:
        print(err2)
    # unit test 3
    try:
        print(voyage([1,2,'three',2], 3))
    except Exception as err3:
        print(err3)

 


