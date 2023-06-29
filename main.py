import picture as p
import time as t
import logo as l
def repeat():
        Repeat=input('Do you want to make bit-map using another sentence or word ????(y/n)')
        if Repeat.lower()=='yes' or Repeat.lower()=='y':
            pass
        elif Repeat.lower()=='no' or Repeat.lower()=='n':
            exit()
        else: 
            print('Hey Dear, You have entered a wrong wrong input .')
            t.sleep(1)
            repeat()
while True:
    input_1=input('Please enter the text you want to enter in bit map.')## takes the input of user.
    input_2=['-']
    output_1='a'
    c=0
    for i in input_1: ## saves the input_1 in the input_2 without the blank spaces.
        if i!=' ':
            input_2.append(i)
        else : pass
    for i in p.b:
        if i!=' ' and i!='\n':
            output_1=output_1+input_2[c]
            c=c+1
        elif i==' ':
            output_1=output_1+' '
        elif i=='\n':
            output_1=output_1+'\n'
        if c>=len(input_2):
            c=0
    print(output_1)
    repeat()
    
                              