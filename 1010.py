p1 = int(input())
cod1,q1,v1 = p1.split(" ")
q1 = int(q1)
v1 = float(v1)
p2 = int(input())
cod2,q2,v2 = p2.split(" ")
q2 = int(q2)
v2 = float(v2)
t = q1*v1+q2*v2
print(f"VALOR A PAGAR: R$ {t:.2f}")