def square(n):
    return n**2

i=square(3)
print(i)
print

wordlist = ['cat','dog','rabbit']
letterlist = []
for aword in wordlist:
    for aletter in aword:
        if aletter not in letterlist:
            letterlist.append(aletter)
print(letterlist)
