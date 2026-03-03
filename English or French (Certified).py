#The input will contain the number followed by lines of text, where each line has at least one character and no more than characters.

N = 10000
thelines = input("Insert Line here")

def englishorfrenchsolver(thelines):
    tcount = 0
    scount = 0
    for i in thelines:
        if (i == "t") or (i == "T"):
            tcount = tcount + 1
    for i in thelines:
        if (i == "s") or (i == "S"):
            scount = scount + 1
    if (scount == tcount) or (scount > tcount):
        print("French")
    else:
        print("English")

englishorfrenchsolver(thelines)