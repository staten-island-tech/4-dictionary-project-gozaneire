#The input will contain the number followed by lines of text, where each line has at least one character and no more than characters.

N = 1
thelines = input("Insert Line here")

def englishorfrenchsolver(thelines):
    tcount = 0
    scount = 0
    for i in range(N):
        if (thelines[i] == "t") or (thelines[i] == "T"):
            tcount =+ 1
        if (thelines[i] == "s") or (thelines[i] == "S"):
            scount =+ 1
    if (scount == tcount) or (scount > tcount):
        print("French")
    else:
        print("English")

englishorfrenchsolver(thelines)