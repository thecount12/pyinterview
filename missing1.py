"""
finding missing number in array
"""

m_array = [1,2,3,5,6,7,8,9,10]

def get_missing(data, n):
    """
    equation n(n+1)/2
    (10*11)/2
    ;params data: str()
    ;params n: str()
    return None;
    """

    sum1 = 10*11/2
    sum2 = sum(data)
    print(sum1-sum2)


if __name__ == "__main__":
    get_missing(m_array, 10)
    
