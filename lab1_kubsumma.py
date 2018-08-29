
z = 1729
lower = 1
upper = 15

for 

for y in range(lower,upper):
    for x in range(lower,upper):
        v = x**3 + y**3
        if (v > z):
            break
        if (v == z):
            print "Values of x and y: x = %d and y = %d" % (x, y)
            break
    


