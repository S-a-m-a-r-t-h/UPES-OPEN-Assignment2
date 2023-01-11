def takeString():
    global Input
    Input = input('Enter an input of lowercase characters\n')
    print('The input recieved is :{}'.format(Input))
    print('which character would you like to remove from this string')
    print('string length is:{}\nchose from 0 to {} - 1 '.format(len(Input),len(Input)))
    edit = int(input())
    print('edit value is {}'.format(edit))
    if edit==0:
        Input = Input[1:len(Input)]
    elif edit == len(Input)-1:
            Input = Input[0:len(Input)-1]
    else:
        Input = Input[0:edit] + Input[edit+1:len(Input)]
    print(Input)
    print(Input[::-1])
takeString()
if(Input == Input[::-1]):
    print('It is a palindrome')
else:
    print('It is not a palindrome')