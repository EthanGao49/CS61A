def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    n1_last_digit = n1%10
    n2_last_digit = n2%10
    return merge(n1//10, n2)*10 + n1_last_digit if n1_last_digit < n2_last_digit \
        else merge(n2//10, n1)*10 + n2_last_digit


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def any_factorial(x):
        if x == 1:
            return False
        return n%x == 0 or any_factorial(x - 1)
    return not any_factorial(n - 1)
    
def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    return m + multiply(m, n - 1) if n > 1 else m

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
        return 1
    elif n%2 == 0:
        return hailstone(n//2) + 1
    return hailstone(3*n + 1) + 1

def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    return count_stair_ways(n - 1) + count_stair_ways(n - 2) if n >= 2 else 1

def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs 
    when taking up to and including k steps at a time. 
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    # Caution: This version of implement don't work!
    # if n <= 1 or k == 1:
    #     return 1 
    # if k > n:
    #     return 2*count_k(n - 1, k)
    # return 2*count_k(n - 1, k) - count_k(n - k, k)
    if n == 0 or n == 1:
        return 1
    elif k == 1:
        return 1
    elif k >= n:
        return 2 * count_k(n - 1, n)
    else:
        return 2 * count_k(n - 1, k) - count_k(n - 1 - k, k)

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()