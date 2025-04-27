import math
def EOQ(A,B,C):
    eoq=math.ceil(math.sqrt((2*A*B)/C))
    print("EOQ of the company is",eoq)

A=10000
B=200
C=5
EOQ(A,B,C)