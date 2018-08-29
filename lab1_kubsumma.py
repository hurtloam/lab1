def findXY(z):
    lower = 1
    upper = 50
    successList = []
    for y in range(lower,upper):
        for x in range(lower,upper):
            v = x**3 + y**3
            if (v > z):
                break
            if (v == z):
                successList.append([z,x,y])
                if (len(successList) == 4):
                    for s in successList[0:2]:
                        print "For z = %d: x = %d and y = %d" % (s[0], s[1], s[2])
                break

for z in range (1,30000):
    findXY(z)
