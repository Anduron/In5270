import numpy as np

n1000B = [0.000256, 0.000244,0.00022,0.000219,0.000238,0.000333,0.000254,0.000191,0.000267,0.000263]
avg1 = sum(n1000B)/float(10)
print(avg1)
n1000C = [0.000153,0.000237,0.000197,0.000092,0.000118,0.00023,0.000214,0.000074,0.000199,0.000155]
avg2 = sum(n1000C)/float(10)
print(avg2)

n1000E = [0.01552,0.014225,0.018428,0.015997,0.016671,0.01624,0.021747,0.013251,0.012255,0.015446]
avg3 = sum(n1000E)/float(10)
print(avg3)

print(avg1/avg2)
print(avg3/avg1)

n1000000B = [0.085026,0.082073,0.083745,0.077583,0.076608,0.079726,0.075888,0.082063,0.075499,0.074668]
avg4 = sum(n1000000B)/float(10)
print(avg4)
n1000000C = [0.067286,0.073819,0.068381,0.069205,0.068625,0.064745,0.064465,0.064431,0.071291,0.065802]
avg5 = sum(n1000000C)/float(10)
print(avg5)


print(avg4/avg5)
