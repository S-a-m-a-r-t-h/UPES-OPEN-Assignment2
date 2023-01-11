#
numeric_position = list([1,2,3,4,5,6,7,8]) 
alphabet_position = list(["a","b", "c","d","e","f","g","h"])
numeric_rep        = list([101,102,103,104,105,106,107,108])      
#                      
# a:101 b:102 c:103 d:104 e:105 f:106 g:107 h:108

#
position = list() 
user_i = int(input('Enter the numeric position\n'))
position.append(user_i)
user_i = input('Enter the alphabetical position\n')
for i in range(0,8,1):
    if (user_i == alphabet_position[i]):
        user_i = numeric_rep[i]
position.append(user_i)
#

#
piece = input('Enter the piece: king/queen/knight/bishop/rook/pawn\n')
#

def convertToAlphabet(position):
    position%=100
    return alphabet_position[position-1]
            

def king(position):
	init_number = position[0]
	init_alphabet = position[1]
	if(init_number+1<=8 and init_alphabet+1<=108):
		print('{}{}'.format(init_number+1,convertToAlphabet(init_alphabet+1)))
	if(init_number+1<=8 and init_alphabet-1>=101):
	    print('{}{}'.format(init_number+1,convertToAlphabet(init_alphabet-1)))
	if(init_number-1>=1 and init_alphabet+1<=108):
	    print('{}{}'.format(init_number-1,convertToAlphabet(init_alphabet+1)))
	if(init_number-1>=1 and init_alphabet-1>=101):
	    print('{}{}'.format(init_number-1,convertToAlphabet(init_alphabet-1)))
	if(init_number+1<=8):
	    print('{}{}'.format(init_number+1,convertToAlphabet(init_alphabet)))
	if(init_number-1>=1):
	    print('{}{}'.format(init_number-1,convertToAlphabet(init_alphabet)))
	if(init_alphabet+1<=108):
	    print('{}{}'.format(init_number,convertToAlphabet(init_alphabet+1)))
	if(init_alphabet-1>=101):
	    print('{}{}'.format(init_number,convertToAlphabet(init_alphabet-1)))
                 
def queen(position):
    init_num = position[0]
    init_alphabet = position[1]
    for i in range(0,8,1):                                                                      #rook1
        if(numeric_rep[i]!= position[1]):
            print('{}{}'.format(position[0],convertToAlphabet(numeric_rep[i])))
    for i in range(0,8,1):                                                                      #rook2
        if(numeric_position[i] != position[0]):
            print('{}{}'.format(numeric_position[i],convertToAlphabet(position[1])))
            
    while(init_alphabet!=108 and init_num!=8):
        init_num+=1 
        init_alphabet+=1
        print('{}{}'.format(init_num,convertToAlphabet(init_alphabet)))
    
    init_num = position[0]
    init_alphabet = position[1]
    while(init_alphabet!=108 and init_num!=1):
        init_num-=1 
        init_alphabet+=1 
        print('{}{}'.format(init_num,convertToAlphabet(init_alphabet)))
    
    init_num = position[0]
    init_alphabet = position[1]
    while(init_alphabet!=101 and init_num!=8):
        init_num+=1 
        init_alphabet-=1
        print('{}{}'.format(init_num,convertToAlphabet(init_alphabet)))
    
    init_num = position[0]
    init_alphabet = position[1]
    while(init_alphabet!=101 and init_num!=1):
        init_num-=1 
        init_alphabet-=1
        print('{}{}'.format(init_num,convertToAlphabet(init_alphabet)))
    
    
def knight(position):
    init_num = position[0]
    init_alphabet=position[1]
    if(init_num+2<=8 and init_alphabet+1<=108):
        print('{}{}'.format(init_num+2,convertToAlphabet(init_alphabet+1)))
        
    if(init_num+1<=8 and init_alphabet+2<=108):
        print('{}{}'.format(init_num+1,convertToAlphabet(init_alphabet+2)))
        
    if(init_num+2<=8 and init_alphabet-1>=101):
        print('{}{}'.format(init_num+2,convertToAlphabet(init_alphabet-1)))
        
    if(init_num+1<=8 and init_alphabet-2>=101):
        print('{}{}'.format(init_num+1,convertToAlphabet(init_alphabet-2)))
        
    if(init_num-2>=1 and init_alphabet+1<=108):
        print('{}{}'.format(init_num-2,convertToAlphabet(init_alphabet+1)))
        
    if(init_num-1>=1 and init_alphabet+2<=108):
        print('{}{}'.format(init_num-1,convertToAlphabet(init_alphabet+2)))
        
    if(init_num-2>=1 and init_alphabet-1>=101):
        print('{}{}'.format(init_num-2,convertToAlphabet(init_alphabet-1)))
        
    if(init_num-1>=1 and init_alphabet-2>=101):
        print('{}{}'.format(init_num-1,convertToAlphabet(init_alphabet-2)))

def bishop(position):
    init_num = position[0]
    init_alphabet = position[1]
    while(init_alphabet!=108 and init_num!=8):
        init_num+=1 
        init_alphabet+=1
        print('{}{}'.format(init_num,convertToAlphabet(init_alphabet)))
    
    init_num = position[0]
    init_alphabet = position[1]
    while(init_alphabet!=108 and init_num!=1):
        init_num-=1 
        init_alphabet+=1 
        print('{}{}'.format(init_num,convertToAlphabet(init_alphabet)))
    
    init_num = position[0]
    init_alphabet = position[1]
    while(init_alphabet!=101 and init_num!=8):
        init_num+=1 
        init_alphabet-=1
        print('{}{}'.format(init_num,convertToAlphabet(init_alphabet)))
    
    init_num = position[0]
    init_alphabet = position[1]
    while(init_alphabet!=101 and init_num!=1):
        init_num-=1 
        init_alphabet-=1
        print('{}{}'.format(init_num,convertToAlphabet(init_alphabet)))
    
    
def rook(position):
    for i in range(0,8,1):                                                                      #rook1
        if(numeric_rep[i]!= position[1]):
            print('{}{}'.format(position[0],convertToAlphabet(numeric_rep[i])))
    for i in range(0,8,1):                                                                      #rook2
        if(numeric_position[i] != position[0]):
            print('{}{}'.format(numeric_position[i],convertToAlphabet(position[1])))
            
def pawn(position):
    init_num = position[0]
    init_alphabet = position[1]
    if(init_num+1<=8):
        print('{}{}'.format(init_num+1,convertToAlphabet(init_alphabet)))

if(piece == 'king'):
    king(position)
if(piece == 'queen'):
    queen(position)
if(piece == 'knight'):
    knight(position)
if(piece == 'bishop'):
    bishop(position)
if(piece == 'rook'):
    rook(position)
if(piece== 'pawn'):
    pawn(position)
    
    
