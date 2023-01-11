list_St = list()
listlen = int(input('Enter the number of words you would like to enter!\n'))
for i in range(0,listlen,1):
    ap = input()
    list_St.append(ap)
print(list_St)
wordlen = len(list_St[0])
for i in range (1,listlen,1):
    if(len(list_St[i])>wordlen):
        wordlen = len(list_St[i])
style = '*'
print(type(wordlen))
print(style*(wordlen+4))
for i in range(0,listlen,1):
    print_line = list_St[i].center(wordlen+2," ")
    print('*{}*'.format(print_line))
print(style*(wordlen+4))
