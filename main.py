import random
import math

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


  print('You rolled these dice ',(rolls))
  print('The sum of your last roll is ',(rollsum(rolls)))
  print ('The Average of your last roll is ',(rollaverage(rolls)))
  print('The sum of ALL your rolls is',(rollsum(overallRolls)))
  print ('The average of ALL your rolls is ',(rollaverage(overallRolls)))
  print('You have rolled a total of ',str(len(overallRolls)),' times.')
  f =  open("diceroll.txt","a")
  f.write('\n You rolled these dice ')
  f.write(str(rolls))
  f.write('\n The sum of your rolls was ')
  f.write(str(rollsum(rolls)))
  f.write('\n Your average roll was ')
  f.write(str(rollaverage(rolls)))
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
