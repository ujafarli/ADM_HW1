if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    #used python tuple function
    t=tuple(integer_list)
    #then print hash of tuple t
    print (hash(t))
