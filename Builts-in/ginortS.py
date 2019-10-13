# List of alphabet and 1-9 numbers
all_of = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"
print(*sorted(input(), key = all_of.index), sep ="")
