import string
fin = open('running-config.cfg')
mylist=[]
mynew=[]
d={}
for line in fin:
    new_line = line.strip()
    line2 = new_line.split()
    mylist.append(line2)
print(mylist)    
for i in mylist:
    if i[0] == 'access-list':
       d[i[0]]=i[1:]
for j in mylist:
     for k in j:
        k.replace('172','192')

print(d)
