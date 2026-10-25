"""nested dictionary:"""


d={"E01":{"name":"Ali","age":28,"salary":3000},\
           "E02":{"name":"Sara","age":32,"salary":4500},\
           "E03":{"name":"Reza","age":25,"salary":2800}}
money=[3000,4500,2800]    #A list is cosidered for money.
sum=0
for i in d.keys():            #keys are determined for 1st dictionary.
    for j in d[i].keys():     #keys are determined for 2nd dictionary.
        if d[i]["salary"]==d[i][j]:   #d[i]["salary"] is used for nested dict.
            #print("name:",d[i]["name"],"salary:",d[i][j])
            if d[i]["salary"]==max(money):
                print("name:",d[i]["name"],";","max salary:",d[i]["salary"])
            if d[i]["salary"]==min(money):
                print("name:",d[i]["name"],";","min salary:",d[i]["salary"])
            if d[i]["salary"]>=3000:
                print("name:",d[i]["name"],";","salary>=3000")
for k in money:
    sum=k+sum
    ave=sum/len(i)
print("average:",ave)
                