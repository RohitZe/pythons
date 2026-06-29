import random
print('Welcome to Pookie Zombie')
name=input('Enter your Name: ')

player={'name':name,'hp':100,'attack':12}

zhp = random.randint(10, 70)
zombie={'name':'pookie','hp':zhp,'attack':10}



choices=['retreat','battle']

userchoice=input('Enter your choice: ')

if userchoice==choices[0]:
    print('you are retreating')
    print('Exited')
elif userchoice==choices[1]:
    print('you are entering into battle zone')
    zombie['hp']=zombie['hp']-player['attack']
    player['hp']=player['hp']-zombie['attack']
    print('Player remaining HP:',player['hp'])
    print('Zombie remaining HP:',zombie['hp'])
    while True :
                zombie['hp']=zombie['hp']-player['attack']
                player['hp']=player['hp']-zombie['attack']
                print('Player remaining HP:',player['hp'])
                print('Zombie remaining HP:',zombie['hp'])
                if(zombie['hp']==0 or player['hp']==0):
                       break
    if(zombie['hp']<=0):
             print(f"{name} have won the match")
    elif(player['hp']<=0):
             print('you va losted')
else:
    print('Enter a valid choice')


