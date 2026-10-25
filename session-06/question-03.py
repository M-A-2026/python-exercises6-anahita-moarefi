"""Inasmuch as a dictionary can not be determined through a string,we have to
 convert a string to a list. Then, by a list, we can assign a dictionary
 keys and values.In addition, we have to delete the specific characters
 and spaces. Therefore, we use isalpha and replace functions of string."""

s=input("string:")
l=list(s)     
d={}
for i in l:
    if i.isalpha() and i.replace(" ","") in d:
        d[i]=d[i]+1
    elif i.isalpha() and i.replace(" ","") not in d:
        d[i]=1
print(d)