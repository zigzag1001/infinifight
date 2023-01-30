from random import randint
from time import sleep
from sys import stdout
from names import nameg
from intro import introduct
introduct()

#starter money in account
acc = 500

while True:
  
  #starter money betted for both fighters
  money1 = 0
  money2 = 0

  #starter life of both fighters
  life1 = 100
  life2 = 100

  #either 1 or 2, changes to which fighter won
  win = 0
  
  #boolean to check if the fight is still going on
  done = False
  
  
  #boolean for all the times the user did something incorrectly
  invalid = True

  #boolean to check if the users balance is negative
  negative = True

  #fallback balance, when the user has 0$ left
  if acc <= 0:
    acc = 100
  
  print('money:','$'+str(acc))
  
  # asks the user to bet and checks if the user bets too much
  while negative:
    while invalid:
      try:
          bet = int(input('Bet: $'))
          invalid = False
      except:
          print('invalid input')
    if bet <= acc:
      negative = False
    else:
      print('Cant bet more than you have!')
    invalid = True

  # name generator for both fighters
  name1 = nameg()
  name2 = nameg()
  
  # checks if the fighter names are similar and regens if they are
  while name1[0:2] == name2[0:2] or name1[:-2] == name2[:-2]:
      name2 = nameg()
      print('.')
  
  print(name1, '1', 'or', name2, '2:')

  #prompts the user to chose their fighter
  while invalid:
    try:
        forwho = int(input())
        invalid = False
    except:
        print('invalid input')
  
  # generates random bets on both fighters
  for i in range(randint(1, 100)):
    money1 += randint(1, randint(50, 100))
  for i in range(randint(1, 100)):
    money2 += randint(1, randint(50, 100))

  #calculates payout multiplyer
  per = '('+str(round(max(money1, money2)/min(money1, money2), 1))+')'

  # prints payout multiplyer
  if money1 > money2:
    print(name1+':', '$'+str(money1), per, '\n'+name2+':', '$'+str(money2), '(1)')
  else:
    print(name1+':', '$'+str(money1), '(1)', '\n'+name2+':', '$'+str(money2), per)
    
  #prints total potential payout  
  if forwho == 1:
    print('potential payout:', '$'+str(round((bet/money1)*money2)))
  else:
    print('potential payout:', '$'+str(round((bet/money2)*money1)))

  input('\nPress enter to start fight\n')

  print('---------FIGHT---------')

  print(name1, 'VS', name2)

  #random max damage for both fighters
  d1 = randint(1, 30)
  d2 = randint(1, 30)

  #fighting by subtracting random health values from both fighters
  while not done:
    life1 -= randint(1, d1)
    life2 -= randint(1, d2)
    print('|'*int(abs(life1)/10), 'VS', '|'*int(abs(life2)/10), '   ', end="\r")
    sleep(0.7)
    if life1 <= 0 or life2 <= 0:
      done = True
      
  #checks to find out who won
  if life1 > life2:
    win = 1
    print(name1, 'WINS')
  else:
    win = 2
    print(name2, 'WINS')
    
  #prints the life of both fighters at the end
  if win == 1:
    print('HP:', abs(life1), 0)
  else:
    print('HP:', 0, abs(life2))
  print()
  
  #account before the fight
  oldacc = acc

  #puts/ takes money from account
  if forwho == win:
    if win == 1:
      acc += (bet/money1)*money2
    else:
      acc += (bet/money2)*money1
    print('YOU WIN')
    print('+$'+str(round(acc-oldacc)))
  else:
    acc -= bet
    print('YOU LOSE')
    print('$'+str(bet*(-1)))

  acc = round(acc)

  print('money:','$'+str(acc))
  print('\n\n')