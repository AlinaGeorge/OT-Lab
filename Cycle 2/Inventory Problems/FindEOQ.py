import math
def EOQ(A,B,C):
    eoq=math.ceil(math.sqrt((2*A*B)/C))
    print("EOQ=",eoq)

A=float(input("Enter the annual demand:"))
B=float(input("Enter the Ordering Cost:"))
C=float(input("Enter the Holding Cost:"))
EOQ(A,B,C)
