def readfiles(filenames):
    for f in filenames:
        #print f,
        for line in open(f):
            #print line,
            yield line

def grep(pattern, lines):
    return (line for line in lines if pattern.upper()\
            in line.upper())

def printlines(lines):
    for line in lines:
        print line,

def main(pattern, filenames):
    lines = readfiles(filenames)
    lines = grep(pattern, lines)
    #for line in lines:
    #    print line
    printlines(lines)

if __name__ == '__main__':
    main('is',[r'C:\Python27\classwork\t1.txt','t2.txt'])
