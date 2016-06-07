# Mike Goldman
# mikerah@gmail.com
# put link to github here

# Create a function (in whatever language you're most comfortable) to round 
# a number to the nearest X, where X can be any positive integer. Numbers 
# should be rounded up or down based on their proximity to the nearest X. 
# Numbers at the midpoint should be rounded up. And the only exception is 
# that a number must not round to 0 (i.e., roundNearest(1, 5) == 5, not 0).
#  Here are some examples:
# round to nearest 50
# 54 -> 50
# 75 ->100
# 98 -> 100
# 119 -> 100
# round to nearest 22
# 22 -> 22
# 29 -> 22
# 33 -> 44
# 7 -> 22     # corrected



def nearest(origin, base):
    try:
        int(origin)
        int(base)
    except ValueError as e:
        print "All arguments must be numeric"
        raise
    response = int(base * round(float(origin)/base))
    return response if (response != 0) else base
