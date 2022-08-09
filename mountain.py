"""
valid maountain array
ar = [0,3,2,1]
it must increase, then decrease at the end
Nothing left over
not valid 0,1
because its smaller than three, 
1 is not valid and empty is not valid
0,1,2 not valid array it does not decrease afte
"""
up = []
down = []

def mountain(data):
    num = -1 
    for i in data:
        print(i)
        if i > num: 
            up.append(i)
        if i < num:
            down.append(i)
        num = i

if __name__ == "__main__":
    # test case 1
    my_arr = [0, 3, 2, 1]
    mountain(my_arr)
    print(up)
    print(down)
