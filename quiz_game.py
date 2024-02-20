print('welcome to my computer quiz')

playing = input('do you want to play? ')

if playing.lower() != "yes":
    quit()

print('okay! lets play')
score = 0
answer = input('what does CPU stand for? ')
if answer == 'central processing unit':
    print("correct")
    score = score + 1
else:
    print("incorrect")
    
answer = input('waht does GPU stand for? ')
if answer == 'graphics processing unit':
    print("correct")
    score = score + 1
else:
    print("incorrect")

answer = input('what does RAM stand for? ')
if answer == 'random access memory':
    print("correct")
    score = score + 1
else:
    print("incorrect")

print(f'you got {score} question correct')