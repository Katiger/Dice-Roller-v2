import random
import math
yesroll = 'yes'
rolls = []
while yesroll == 'yes':
  diceAmount = input('How many dice would you like to roll? ')
  count = 0
  while count < int(diceAmount):
    diceroll = random.randint(1,6)
    rolls.append(diceroll)
    count += 1
    #print (diceroll)
  else:  
    #finds the average of the rolls
    diceSum = math.fsum(rolls)
    print ('The sum of your rolls is ',diceSum)
    #finds the index of the rolls list
    diceAverage = len(rolls)
    #prints the average of the rolls which is the sum of the rolls divided by the number of rolls.
    print('The average of your rolls is ', int(diceSum)/int(diceAverage))
    #lists what the rolls are
    print ('You rolled ', rolls)
    #writes the rolls into a text doc
    f =  open("diceroll.txt","a")
    f.write(str(rolls))
    f.close()
    yesroll = input('Would you like to roll again? ')


