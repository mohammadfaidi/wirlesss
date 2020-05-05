
import math

numberA = []
numberB = []
numberb = []
f =19
f2 =15
H=3
for x in range(1,9):
    l=int(32.44 + 20 * math.log(f) + 20 * math.log(x))
    numberA.append(l)



print("this is numberA array :" + str(numberA))


for x in range(8,0,-1):
    y=int(32.44 + 20 * math.log(f2) + 20 * math.log(x))
    numberb.append(y+H)



#print("this is numberb array :" + str(numberb))




for x in range(8,0,-1):
    y=int(32.44 + 20 * math.log(f2) + 20 * math.log(x))
    numberB.append(y)




print("this is numberB array :" + str(numberB))



for x in range(0,8):
    if numberA[x] > numberB[x]:
        print(str(numberA[x]) +" "+ "is bigger " + str(numberB[x]) + " " +"then stop give me the index of this stop index :" +str(x+1))
        break



print("zeinah")