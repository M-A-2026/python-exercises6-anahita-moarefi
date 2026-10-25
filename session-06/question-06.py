#Tuple
sales=(("Ali","Laptop",1200),("Sara","Phone",800),("Ali","Phone",800),\
       ("Reza","Laptop",1200),("Sara","Laptop",1200),("Ali","Mouse",50))
sum_A=0    
sum_S=0    
sum_R=0
sum_L=0
sum_P=0
sum_M=0
for i in sales:
    if i[0]=="Ali":
        sum_A=sum_A+i[2]
    if i[0]=="Sara":
        sum_S=sum_S+i[2]
    if i[0]=="Reza":
        sum_R=sum_R+i[2]
    if i[1]=="Laptop":
        sum_L=sum_L+1
    if i[1]=="Phone":
        sum_P=sum_P+1  
    if i[1]=="Mouse":
        sum_M=sum_M+1
for i in (sum_A,sum_S,sum_R):
    if i==max(sum_A,sum_S,sum_R):
        if i==sum_A:
            print("Wealthy buyer:","Ali")    
        if i==sum_S:
            print("Wealthy buyer:","Sara")
        if i==sum_R:
            print("Wealthy buyer:","Reza")

print("Sara paid:",sum_S)        
print("Ali paid:",sum_A)        
print("Reza paid:",sum_R)
print("Total sales:",sum_A+sum_S+sum_R)    
print("NSL:",sum_L)             #The number of sold laptops    
print("NSP:",sum_P)             #The number of sold phones
print("NSM:",sum_M)             #The number of sold mouses
                  