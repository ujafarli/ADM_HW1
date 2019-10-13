import operator

def person_lister(f):
    def inner(people):
        # complete the function
	# only adding one line code, by returning sorted version by x[2] which means 3rd element
        return map(f, sorted(people, key=lambda x: x[2]))  
    return inner

@person_lister
	# Mr and Mr part here
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
