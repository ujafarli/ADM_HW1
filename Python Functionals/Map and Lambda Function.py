cube = lambda x: x**3

# Write function for fibonacci algorithm
def fibonacci(n):
    nums = [0,1]
    for i in range(2,n):
        nums.append(nums[i-2] + nums[i-1])
    return(nums[0:n])

if __name__ == '__main__':
    n = int(input())

#print as cube
    print(list(map(cube, fibonacci(n))))
