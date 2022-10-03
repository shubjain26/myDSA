## Given a matrix of size n x m find the maximum number of squares present


def max_squares(a, b):

    min_dim = min(a, b)
    size = 1
    total = a*b

    while min_dim - size > 0:
        ## squares of size  i x i
        sq = (a - size) * (b - size)
        total += sq 
        size  += 1

    return total


print(max_squares(1,1))
print(max_squares(2,2))
print(max_squares(3,3))
print(max_squares(3,4))
print(max_squares(4,4))
print(max_squares(10,8))

