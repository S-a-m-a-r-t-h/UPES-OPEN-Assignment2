list_fibonacci = [1]
def fibonacci():
    initial = 1
    previous = 0
    for i in range(1,100,1):
        list_fibonacci.append(initial) 
        print('{}'.format(initial), end = ' ') 
        incremented = initial  + previous
        previous = initial
        initial = incremented
fibonacci()     