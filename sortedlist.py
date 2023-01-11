#merge two sorted lists
list1= list()
list2= list()
len1 = int(input('Enter the length of list 1\n'))
for i in range(0 ,len1,1):
    ap = int(input())
    list1.append(ap)
len2 = int(input('Enter the length of list 2\n'))
for i in range(0,len2,1):
    ap = int(input())
    list2.append(ap)
print('list 1:{} list 2:{}'.format(list1,list2))
i = j = 0
list_main = list()
while(i!= len1 and j!= len2):
    if(list1[i]>=list2[j]):
        list_main.append(list2[j])
        #print(list_main)
        j+=1 
    elif(list1[i]<list2[j]):
        list_main.append(list1[i])
      # print(list_main)
        i+=1
if(i>j):
    list_main = list_main + list2[j:]
elif(i<j):
    list_main = list_main + list1[i:]
print(list_main)

