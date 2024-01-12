import math

f = open('Testcase4.txt', 'r')
f1 = open('op4.txt', 'a')
ip = {}
for line in f:
    listedline = line.strip().split(':')
    if len(listedline) > 1:
        ip[listedline[0]] = int(listedline[1])
        
radius=(ip['WaferDiameter'])/2
angle=math.radians(ip['Angle'])
dis=ip['WaferDiameter']/(ip['NumberOfPoints']-1)
#print(dis)
x,y=radius*math.cos(angle),radius*math.sin(angle)
a=str("("+str(round(x,4))+","+str(round(y,4))+")"+"\n")
f1.write(a)
#print(a)
    
for i in range(ip['NumberOfPoints']-1):
    x,y=x-dis*math.cos(angle),y-dis*math.sin(angle)
    b=str("("+str(round(x,4))+","+str(round(y,4))+")"+"\n")
    f1.write(b)
    #print(b)

f.close()
f1.close()