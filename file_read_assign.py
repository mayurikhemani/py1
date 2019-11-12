#read from a file like 2 lines

"""def file_read(filename):
    txt= open(filename)
    print(txt.read())

file_read("file1.txt")"""

#read first lien of file

def file_read_line(filename,nlines):
    from itertools import islice
    with open(filename) as f:
        for line in islice(f,nlines):
            print(line)
file_read_line("file1.txt",2)
