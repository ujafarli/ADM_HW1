if __name__ == '__main__':

# Take inputs
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
# List of floats
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    result = student_marks[query_name]    
    print('%.2f' %(sum(result)/3))


