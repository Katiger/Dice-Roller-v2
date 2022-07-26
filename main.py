import random
from prettytable import PrettyTable

#Creating overall rolls array
overallRolls = []
#creating roll again variable
again = 'yes'

#Function to add rolls to array
def arrayadd(array):
  array.append(diceroll)

#Function to add dice rolls
def rollsum(array):
  total = 0
  for num in array:
    total += num
  return total

#Function to average out dice rolls  
def rollaverage(array):
  average = rollsum(array)//len(array)
  return average

def rolloccur(dice,array):
  occur = 0
  dicenum = dice
  for i in array:  
    if i == dicenum:
      occur +=1
  return occur
  
#Rolling the dice
while again == 'yes':
  #Creating rolls array
  rolls = []
  #Asking how many dice to roll
  diceAmount = input('How many dice would you like to roll? ')
  #Setting count to zero
  count = 0
  while count < int(diceAmount):
    diceroll = random.randint(1,6)
    #adding to the dice roll count
    count += 1
    #adding the rolls to an array
    arrayadd(rolls)
    arrayadd(overallRolls)


  print('\nYou rolled these dice ',(rolls))
  print('\nThe sum of your last roll is ',(rollsum(rolls)))
  print ('The Average of your last roll is ',(rollaverage(rolls)))
  print('\nThe sum of ALL your rolls is',(rollsum(overallRolls)))
  print ('The average of ALL your rolls is ',(rollaverage(overallRolls)))
  print('\nYou have rolled a total of ',str(len(overallRolls)),' times.')
  f =  open("diceroll.txt","a")
  f.write('\n\n')
  f.write(str(rolls))
  f.close() 
  
  #asking if they would like to roll again
  again = input('Would you like to roll again? ')

f =  open("total dicerolls.txt","w")
f.write('\n You have rolled these dice ')
f.write(str(overallRolls))
f.write('\n The sum of your all your rolls is ')
f.write(str(rollsum(overallRolls)))
f.write('\n Your average roll was ')
f.write(str(rollaverage(overallRolls)))
f.close()   


#how many times did I roll each dice
dice = [1,2,3,4,5,6]
print('\n')
dicerolled=['Overall Times rolled']
for i in dice:
  dicerolled.append(rolloccur((i),overallRolls))
  #print('You rolled a',(i) ,str(rolloccur((i),overallRolls)), 'times.')

print('\n')
dicetable = PrettyTable(['Dice Numbers','One','Two', 'Three','Four','Five','Six'])
dicetable.add_row((dicerolled))
print(dicetable)

#Which dice did I roll the most
highamount = 0
for i in dicerolled:
  if i == 'Overall Times rolled':
      continue
  if highamount < int(i):
    highamount = i
print ('\n You rolled ',(dicerolled.index(highamount)),'the most amount of times at',(highamount),'times.')
       