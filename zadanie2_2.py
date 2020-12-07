ch = int(input())

if (ch % 2 != 0 and ch % 3 == 0 and ch % 5 == 0 and ch % 10 != 0):
    print ('Y')
else:
    print ('N')