"""
finding the volume between two pointes in an array
array = [4, 2, 3, 5, 8, 7, 1]
"""

def water(data, x, y):
    height = []
    width = []
    for i, num in enumerate(data):
        if num == x:
            height.append(x)
            width.append(i)
        if num == y:
            height.append(y)
            width.append(i)
    volume = min(height) * (max(width)-min(width))
    return volume

                
my_array = [4, 2, 3, 5, 8, 7, 1]
print(water(my_array, 2, 7))
        





