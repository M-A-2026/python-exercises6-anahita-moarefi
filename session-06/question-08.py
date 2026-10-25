users=[("Ali",25,"Python"),("Sara",30,"Java"),("Reza",22,"Python"),\
       ("Mina",28,"C++"),("John",35,"Python"),("David",30,"Java")]

d={}
d1={} 
d2={} 
d3={}
d4={}  
l1=[]
l2=[]
l3=[]
sum_P=0
sum_J=0
sum_C=0
sum1=0
sum2=0
sum3=0
for i in users:
    if i[2]=="Python":
        l1.append(i[0])
        d["Python"]=d.setdefault("Python",l1)
        sum_P=sum_P+i[1]
        ave_P=sum_P/len(l1)       #average of the users age wrt Python 
        d1[i[0]]=d1.setdefault(i[0],i[1])       
        if d1[i[0]]==max(d1.values()):
            i1=i[0]               #Oldest User of Python
   
    if i[2]=="Java":
        l2.append(i[0])
        d["Java"]=d.setdefault("Java",l2)
        sum_J=sum_J+i[1]
        ave_J=sum_J/len(l2)            #average of the users age wrt Java
        d2[i[0]]=d2.setdefault(i[0],i[1])    #i[0] is key & i[1] is value
        if d2[i[0]]==max(d2.values()):
            i2=i[0]                    #Oldest User of Java
            
    if i[2]=="C++":
        l3.append(i[0])
        d["C++"]=d.setdefault("C++",l3)
        sum_C=sum_C+i[1]
        ave_C=sum_C/len(l3)            #average of the users age wrt C++
        d3[i[0]]=d3.setdefault(i[0],i[1])
        if d3[i[0]]==max(d3.values()):
            i3=i[0]                    #Oldest User of C++
print("Grouping Output:",d) 
print("ave_P:",ave_P) 
print("ave_j:",ave_J) 
print("ave_C:",ave_C)
print("OUP:",i1)     #Oldest User of Python
print("OUJ:",i2)     #Oldest User of Java
print("OUC:",i3)     #Oldest User of C++     
#print("d1:",d1)
#print("d2:",d2)           
#print("d3:",d3)
#print("l1:",l1)       
#print("l2:",l2)
#print("l3:",l3)

l=l1+l2+l3
sum=(sum1,sum2,sum3)
for i in l:
    sum1=sum1+l1.count(i)
    sum2=sum2+l2.count(i)
    sum3=sum3+l3.count(i)
#print(sum1)
#print(sum2)
#print(sum3)
if d4.setdefault("Python",sum1):
    
    if d4.setdefault("Java",sum2):
    
        if d4.setdefault("C++",sum3):
            print(d4)
for i in d4.keys():    
    if d4[i]==max(d4.values()):
        print("LMU:",i)           #a language with more users
    print(i,end=" ")              #All programming languages
