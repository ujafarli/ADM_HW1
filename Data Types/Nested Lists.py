my_list = []

if __name__ == '__main__':

# takes names and scores 
        for _ in range(int(input())):
                name = input()
                score = float(input())
                my_list += [[name,score]]

# sort for marks and then take max 2
        sorted_list = sorted(list(set([marks for name, marks in my_list])))

        for a,b in sorted(my_list):
            if b == sorted_list[1] :
                print(a)
