import random


secret_number = random.randint(1, 10)
while True:
     user_number= int(input('Enter the guessed number: '))
     if (secret_number==user_number):
          print('Congrats you ve won')
          break
     elif(user_number<secret_number):
          print('Too low try with some bigger value')
     elif(user_number>secret_number):
          print('Too high try with some lower value')
     else:
          print('Try with numerical values')


















