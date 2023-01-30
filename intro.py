from time import sleep
from random import random
import sys

def introduct():
  # logo
  text = '''
 _        __ _       _  __ _       _     _   
(_)_ __  / _(_)_ __ (_)/ _(_) __ _| |__ | |_ 
| | '_ \| |_| | '_ \| | |_| |/ _` | '_ \| __|
| | | | |  _| | | | | |  _| | (_| | | | | |_ 
|_|_| |_|_| |_|_| |_|_|_| |_|\__, |_| |_|\__|
                             |___/           
           ʳᵃⁿᵈᵒᵐ ᶠˡᵍʰᵗ ᵇᵉᵗᵗᶦⁿᵍ              
'''
  # stupid thing 1
  text1 = 'exec infinifight.exe'
  #stupid thing 2
  text2 = 'starting infinifight...'
  #prints text1 letter by letter
  for i in text1:
    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(random()/3)
  print()
  #input " " to skip intro
  if input("press enter\n") == " ":
    print("(skipped intro)")
  else:
    #prints text2 letter by letter
    for i in text2:
      sys.stdout.write(i)
      sys.stdout.flush()
      sleep(0.05)
    print()
    #squiggly line that is supposed to stay on one line but mostly prints the animation line by line, sometimes it works correctly
    for i in range(1):
      for j in range(25):
        print('-'*j, '  '*j, end = '\r')
        sleep(0.1)
        print('~'*j, '  '*j, end = '\r')
        sleep(0.1)
    print()
    #prints logo letter by letter
    for i in text:
      sys.stdout.write(i)
      sys.stdout.flush()
      sleep(0.01)