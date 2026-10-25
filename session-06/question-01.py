d={"laptop":1200,"phone":800,"tablet":500,"headphone":150,"mouse":50}
sum=0
for i in d.keys():
    if d[i]==max(d.values()):        
        print("MEP:",i)                  #Most Expensive Product
    if d[i]==min(d.values()):
        print("CP:",i)                   #Cheapest Product
    if d[i]>500:
        print("HPP:",i)                  #High-Priced Products
    if d.get(i):
        sum=sum+d.get(i)
        ave=sum/len(d)
print("total price:",sum,"   ","average:",ave)
