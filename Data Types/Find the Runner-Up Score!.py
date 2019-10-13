if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
   
# sort the list
    new_ls = sorted(list(set(arr)))
# take 2nd greatest
    print(new_ls[-2])



