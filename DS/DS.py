#Assiging elements to different lists
ls1=[1,2,3,4,5]
ls2=[0,5,10]
ls1.append(7)
print(ls1+ls2)

#Accesing  elements from tuple
t1=("Hello","World",7,'a',10,20,"Earth")
#Print from first to second last element by jumping to 2nd next element
print(t1[0:-2:2])

#Deleting different dictionary elements

dict={"Monday":1,"Tuesday":2,"Wednesday":3}
dict.pop("Tuesday")
print(dict)
