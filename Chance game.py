

import random
import sys
import time


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

def delay_print1(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)



game = input('\n \n \n \n \n \nPress [Enter] to start any else to quit: ')






a = random.randint(1,5)
b = random.randint(1,5)
c = random.randint(1,5)
while game == '':c
   delay_print('rolling...\n')
   delay_print('rolling...\n')
   delay_print('rolling...\n')
   delay_print('rolling...\n')
   delay_print('rolling...\n')
   delay_print('rolling...\n')
   print("[",a,"],[",b,"],[",c,"]\n")
   if a == b and b == c and c == a:
      delay_print('Yahoo three of a kind!!!\n')
      time.sleep(3)
   if a == b or a == c or b == c:
      delay_print('Not bad two of a kind.\n')
   else:
      delay_print('Heuuuum do you have bad luck......... \n')
   
   a = random.randint(1,5)
   b = random.randint(1,5)
   c = random.randint(1,5)
   game = input('Press [Enter] continue any else to quit: ')