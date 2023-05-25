def cubesum(num):
    '''this function adds the cube sum of individual digits.
    '''
    cubesum = 0
    while num:
        rem = num%10
        cubesum += rem**3
        num = num//10
    return cubesum
