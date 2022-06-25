def rev_letter():
    s = input(" ")
    lst = s.split(".")
    lst = [elem[::-1] for elem in lst]
    return ".".join(lst)

print(rev_letter())