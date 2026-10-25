orders=[("Ali","Laptop"),("Sara","Phone"),\
        ("Ali","Phone"),("Reza","Laptop"),\
        ("Sara","Laptop"),("Ali","Tablet"),("Reza","Phone")]
     
l1=[]
l2=[]
l3=[]
d={}    
for i in orders:
    if i[0]=="Ali":
        l1.append(i[1])
        d["Ali"]=d.setdefault("Ali",l1)
#print(l1)           #These prints must be used at the end
#print(d)   #print(l1) & print(d) show list & dict of Ali orders
    if i[0]=="Sara":
        l2.append(i[1])
        d["Sara"]=d.setdefault("Sara",l2)
#print(l2)           #print(l2) shows list of Sara orders
#print(d)            #print(d) shows dict of Ali & Sara orders
    if i[0]=="Reza":
        l3.append(i[1])
        d["Reza"]=d.setdefault("Reza",l3)
#print(l3)           #print(l3) shows list of Reza orders
print(d)
       
        