import sys
'''
try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    errno, strerror = e.args
    #print("I/O error({0}): {1}".format(errno,strerror))
    # e can be printed directly without using .args:
    print(e)
except ValueError:
    print("No valid integer in line.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
'''
def f():
    x = int("four")

try:
    f()
except ValueError as e:
    print("got it :-) ", e)


print("Let's get on")
