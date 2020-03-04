def setup_bricks():
  '''
  Run this function once at the beginning of the game.
  Creates a main pile of 60 bricks, represented as a list containing the integers 1 –60.
  Creates a discard pile of 0 bricks, represented as an empty list.
  '''
  main_pile=list(range(1,61))
  discard_pile=[]
  return(main_pile,discard_pile)

import random
def shuffle_bricks(bricks):
  '''
  Shuffle the given bricks (represented as a list).(Do this to start the game)
  '''
  shuffle_bricks=random.shuffle(bricks)
  #This function does not return anything

def check_bricks(main_pile,discard_pile):
  '''
  Check if there are any bricks left in the given main pile.
  If not, shuffle the discard pile (using the shuffle function) and move those bricks to the main pile.
  Then turn over the top card to be the start of the new discard pile.
  '''
  if len(main_pile)==0:
    print("There is no card left in the given main pile of bricks. Let's reset the main pile and discard pile!")
    shuffle_bricks(discard_pile)#reuse the shuffle_bricks function
    main_pile=discard_pile
    discard_pile=main_pile[0]
  return(main_pile,discard_pile)

def check_tower_blaster(tower):
  '''
  Given a tower (the user’s or the computer’s list), determine if stability has been achieved.
  '''
  return(bool(sorted(tower)==tower))

def get_top_brick(brick_pile):
  '''
  Remove and return the top brick from any given pile of bricks
  '''
  top_brick=brick_pile[0]#get the value of the top brick of given pile
  brick_pile.pop(0)
  return(top_brick)

def deal_initial_bricks(main_pile):
  '''
  Start the game by dealing two sets of 10 bricks each, from the given main_pile.
  The computer is always the first person that gets dealt to.
  The rule is placing bricks one on top of the other.
  '''
  i=0
  computer_pile=[]
  user_pile=[]
  while i <= 19:#use loop to ensure that only taking 20 bricks from the main pile
    number=main_pile[i]
    if i % 2 == 0:#The odd position like 1,3,5...19 in the main pile goes into computer pile.  
      computer_pile.append(number)#To ensure computer is the first person that gets deal to
      main_pile.pop(i)
    else:#The even position 2,4,6...20 in the main pile goes into computer pile
      user_pile.append(number)
      main_pile.pop(i)
    i+=1
  return(computer_pile,user_pile)

def add_brick_to_discard(brick, discard_pile):
  '''
  Add the given brick (represented as an integer) to the top of the given discard pile (which is a list)
  '''
  discard_pile.insert(0,brick)

def find_and_replace(new_brick, brick_to_be_replaced, tower, discard_pile):
  '''
  Check and make sure that the given brick to be replaced is truly a brick in the given tower.
  Find the given brick to be replaced (represented by an integer) in the given tower and replace it with the given new brick.
  The given brick to be replaced then gets put on top of the given discard pile.
  '''
  if brick_to_be_replaced in tower:
    index=tower.index(brick_to_be_replaced)
    tower[index]=new_brick
    add_brick_to_discard(brick_to_be_replaced,discard_pile)#reuse the add_brick_to_discard function
    return True
  else:
    return False

def computer_play(tower, main_pile, discard_pile):
  '''
  Because there are 60 bricks in total, the number of top brick of computer should be 1-6. Next one should be 7-12.then 13-18...
  Calculate the position the number of top brick of discard_pile should be in computer first.
  Then check whether the actual number of the brick in that position is in the correct range or not.
  If it is, then switch the brick from discard pile with that brick.
  If not take the top brick of main pile. Then do the same thing.
  This time, If it is, then replace that brick with the top brick of main pile. Then throw that brick into discard pile.
  If not, do nothing with the computer pile. Throw the top brick of main pile into dicard pile.
  '''
  discard=discard_pile[0]
  index_discard=discard // 6
  if discard % 6 == 0:#if the top brick of the discard pile is a common multiple of 6
    index_discard-=1#its position in the tower is supposed to minus 1
  if tower[index_discard] not in range(index_discard*6+1,(index_discard+1)*6+1):
    discard_pile[0]=tower[index_discard]
    tower[index_discard]=discard
    print('The computer picked',discard,'from the discard pile')
    print('The computer replaced a brick')
  else:
    main=main_pile[0]
    index_main=main // 6
    if main % 6 == 0:#if the top brick of the discard pile is a common multiple of 6
      index_main-=1#its position in the tower is supposed to minus 1
    if tower[index_main] not in range(index_main*6+1,(index_main+1)*6+1):
      discard_pile[0]=tower[index_main]#throw the number on the top of the tower to the discard pile
      tower[index_main]=main
      print('The computer picked',main,'from the main pile')
      print('The computer replaced the brick')
    else:
      discard_pile.insert(0, main)
      main_pile.pop(0)
      print('The computer picked',main,'from the main pile')
      print('The computer rejected a brick')
  return(main_pile, discard_pile, tower)
        
def main():
  print("Let's play Tower Blaster!")
  main_pile,discard_pile=setup_bricks()#set up the main pile and discard pile
  shuffle_bricks(main_pile)#shuffle the main pile
  computer_pile, user_pile=deal_initial_bricks(main_pile)#get the computer pile and user pile using deal_initial_bricks function
  computer_pile_old=computer_pile.copy()
  print("Computer's initial tower is " ,computer_pile)
  print("Your initial tower is ", user_pile)
  top_brick=get_top_brick(main_pile)#get the top brick of the main pile
  add_brick_to_discard(top_brick, discard_pile)#add the top brick of main pile into discard pile
  discard=discard_pile[0]#get the value of the top brick of discard pile
  main=main_pile[0]#get the value of the top brick of main pile
  print("The top brick on the discard pile is", discard_pile[0])
  while check_tower_blaster(user_pile)==False:#use loop to let this game keep going
    print("It's computer's turn!")
    main_pile, discard_pile, computer_pile=computer_play(computer_pile, main_pile, discard_pile)
    check_bricks(main_pile,discard_pile)#after computer making a choice, we should check whether the main pile is empty or not
    discard=discard_pile[0]
    main=main_pile[0]
    if check_tower_blaster(computer_pile):#check whether computer wins or not
      print('The computer won!')
      break
    else:
      print("Now it's your turn!")
      print("Your tower:",user_pile)
      print('The top brick on the discard pile is',discard)
      user_choice=input("Type 'D' to take the discard brick, 'M' for a mystery brick")
      if user_choice=='D':
        print('You picked',discard,'from the discard pile')
        brick_to_be_replaced=int(input('Where do you want to place this brick? Type a brick number to replace in your tower'))
        while find_and_replace(discard, brick_to_be_replaced, user_pile, discard_pile)==False:#use loop to ask user enter a right position
          print('Sorry, the brick that you picked is not a brick in your tower. Please try again!')
          brick_to_be_replaced=int(input('Where do you want to place this brick? Type a brick number to replace in your tower'))
      if user_choice=='M':
        print('You picked',main,'from the main pile')
        user_second_choice=input("Do you want to use this brick? Type'Y' or 'N' to skip this turn")
        if user_second_choice=='Y':
           brick_to_be_replaced=int(input('Where do you want to place this brick? Type a brick number to replace in your tower'))
           while find_and_replace(main, brick_to_be_replaced, user_pile, discard_pile)==False:#use loop to ask user enter a right position
             print('Sorry, the brick that you picked is not a brick in your tower. Please try again!')
             brick_to_be_replaced=int(input('Where do you want to place this brick? Type a brick number to replace in your tower'))
        else:
          discard_pile.insert(0, main)
        main_pile.pop(0)
      check_bricks(main_pile,discard_pile)#after user making a choice, we should check whether the main pile is empty or not
      discard=discard_pile[0]
      main=main_pile[0]
    if check_tower_blaster(user_pile):#check whether user wins or not
      print('Cogradulations! You won the game!')
  
if __name__=='__main__':
  main()
