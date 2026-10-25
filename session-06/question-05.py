d={"Ali":[18,17,20],"Sara":[15,19,18],"Reza":[12,14,10],"Mina":[20,20,19]}

sum_A=0
sum_S=0
sum_R=0
sum_M=0
"""Due to different values in the list,I have used d.fromkeys() function. how 
ever if the same values are in list like Mina grades, we have to use d["key"]"""

for i in d.fromkeys(d["Ali"]):  
   sum_A=sum_A+i   
   ave_A=sum_A/len(d["Ali"])      #ave:average
print("Ali average:",ave_A)
if ave_A>15:
     print("Passed")
else:
     print("Failed")
print("Max Grade:",max(d["Ali"]))

for i in d.fromkeys(d["Sara"]):
    sum_S=sum_S+i
    ave_S=sum_S/len(d["Sara"])
print("Sara average:",ave_S)
if ave_S>15:
    print("Passed")
else:
    print("Failed")
print("Max Grade:",max(d["Sara"]))

for i in d.fromkeys(d["Reza"]):    
    sum_R=sum_R+i
    ave_R=sum_R/len(d["Reza"])
print("Reza average:",ave_R)
if ave_R>15:
    print("Passed")
else:
    print("Failed")
print("Max Grade:",max(d["Reza"]))

for i in d["Mina"]:
    sum_M=sum_M+i
    ave_M=sum_M/len(d["Mina"])
print("Mina average:",ave_M)
if ave_M>15:
    print("Passed")
else:
    print("Failed")
print("Max Grade:",max(d["Mina"]))

for i in {"Ali":ave_A,"Sara":ave_S,"Reza":ave_R,"Mina":ave_M}:
    if d[i]==max(d.values()):
        print("Best Student:",i)
        
for i in d.setdefault("average",[ave_A,ave_S,ave_R,ave_M]):
    if i in d["average"]:
        MA=max(d["average"])  #MA:Max Average
print("Max Average:",MA)

