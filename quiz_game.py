from cgi import print_environ


print('Welcome to my 1st game!')

playing=input('Do you wanna play? ')
# using playing.lower to convert user input to lower to avoid bugs
if playing.lower()!='yes':
    quit()

print('Okay lets play!')

score=0

answer=input('What does CPU stand for? ')
if answer.lower()=='central processing unit':
    print('Correct!')
    score+=1
else:
    print('Incorrect')

answer=input('What does GPU stand for? ')
if answer.lower()=='graphics processing unit':
    print('Correct!')
    score+=1
else:
    print('Incorrect')

answer=input('What does RAM stand for? ')
if answer.lower()=='random access memory':
    print('Correct!')
    score+=1
else:
    print('Incorrect')

answer=input('What does PSU stand for? ')
if answer.lower()=='power supply unit':
    print('Correct!')
    score+=1
else:
    print('Incorrect')

# str(score) so that we can add score which is int to str.
print('You got '+ str(score) +' questions correct.')
print('You got '+ str((score/4) * 100) +'% questions correct.')