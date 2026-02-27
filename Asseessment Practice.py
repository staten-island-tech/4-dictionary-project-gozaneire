#The first line of input contains the integer . The second and third lines of input contain characters each. The second line of input records the information about yesterday's parking spaces, and the third line of input records the information about today's parking spaces. Each of these characters will either be C to indicate an occupied space or . to indicate it was an empty parking space.

def occupation(c,y,t):
    spot = 0
    for i in range(c):
       if (y[i] == "C" and t[i] == "C"):
           spot += 1
    print(spot)

occupation(6,"C.C.CC","..CC.C")