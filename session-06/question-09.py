products={"P01":("Laptop",1200,5),"P02":("Phone",800,0),\
          "P03":("Tablet",500,12),"P04":("Mouse",50,25),\
              "P05":("Keyboard",100,0)}    #(product name,price,stock)

d={}
AP={}       #available products
UAP={}      #unavailable products
sum=0
for i in products.values():
    
    if i[2]!=0:
       if AP.setdefault(i[0],i[2]):
           if i[0]=="Laptop":
              TVL=i[1]*i[2]              #Total Value of Laptop
           if i[0]=="Tablet":
              TVT=i[1]*i[2]              #Total Value of Tablet
           if i[0]=="Mouse":
              TVM=i[1]*i[2]              #Total Value of Mouse
              
    if i[2]==0:
        if UAP.setdefault(i[0],i[2]):
           if i[0]=="Phone" or "Keyboard":
              TVP=i[1]*i[2]              #Total value of Phone and Keyboard  
                    
    if d.setdefault(i[0],i[1]*i[2]):        
        if d[i[0]]==max(d.values()):            
            print("PHV:",i[0],end=" ")   #Product with the highest value
l=list(d.values())
for i in l:
    sum=sum+i
        
print()
print("AP:",AP) 
print("UAP:",UAP)                        
print("TVL:",TVL)
print("TVT:",TVT)
print("TVM:",TVM)
print("TVP or TVK:",0)
print(d)
print("TIV:",sum)               #Total inventory value  
   