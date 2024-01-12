import math

f = open('Testcase2.txt', 'r')
f1 = open('op1.txt', 'a')
ip = {}
for line in f:
    listedline = line.strip().split(':')
    if len(listedline) > 1:
        ip[listedline[0]] = int(listedline[1])
        
radius=5

dis=10/4
print(dis)
dis1=2*math.pi/5
print(dis1)
x,y=(radius*math.cos(ip['Angle'])),radius*math.sin(ip['Angle'])
a=str("("+str(round(x,4))+","+str(round(y,4))+")"+"\n")
#f1.write(a)
print(a)
    
for i in range(5-1):
    x,y=(x-dis*math.cos(ip['Angle'])),y-dis*math.sin(ip['Angle'])
    b=str("("+str(round(x,4))+","+str(round(y,4))+")"+"\n")
    #f1.write(b)
    print(b)

f.close()
f1.close()
