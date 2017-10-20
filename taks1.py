import string
fin1 = open('Book1.txt')
list1=[]
for line in fin1:
    new_line = line.strip(string.whitespace)
    my_line = line .strip(string.punctuation)
    my_last = my_line.split()
    list1.extend(my_last)
fin2 = open('Book2.txt')
list2=[]
for line in fin2:
    new_line = line.strip(string.whitespace)
    my_line = line .strip(string.punctuation)
    my_last = my_line.split()
    list2.extend(my_last)
fin3 = open('Book3.txt')
list3=[]
for line in fin3:
    new_line = line.strip(string.whitespace)
    my_line = line .strip(string.punctuation)
    my_last = my_line.split()
    list3.extend(my_last)

def my_word(alist):
    mydic={}
    for i in alist:
        mydic[i]=len(i)
    
    mylist=[(value,key) for (key,value) in sorted(mydic.items(),reverse = True)]
    print (mylist)
my_word(list1)
my_word(list2)
my_word(list3)
