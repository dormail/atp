# atp aufgabe 13 plot zur Wahrscheinlichkeit
import numpy as np
import matplotlib.pyplot as plt

def P(i,p):
    a = 5
    d = 0.25
    sum = 0
    if i == 1:
        return d/a
    if i == 2:
        return (d/a) - (d/a)**2
    sum_former = 0
    for k in range(1,int(i)):
        sum_former = sum_former + p[k-1]


    return (1 - sum_former) * d/a



r = 300
i = np.linspace(1,r,r)
print(i)
p = i.copy()
p_weighted = p.copy()
mean = 0

for k in range(0,len(i)):
    p[k] = P(i[k],p)
    p_weighted[k] = p[k] * (1+k)
    mean = mean + p_weighted[k]
    

for k in range(1,len(p)):
    print(p[k] / p[k-1])

print(mean)

f = plt.figure(1)
plt.bar(i,p)
plt.xlabel('i')
plt.ylabel('P(i)')
plt.title('Wahrscheinlichkeit an der i-ten Sichtebene am Baum zu landen')
#f.savefig('13.png', bbox_inches='tight', dpi=600)
f.show()

g = plt.figure(2)
plt.bar(i, p_weighted)
g.show()

#plt.bar(i,p_comul)
input()
