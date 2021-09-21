""" Make a two-player Rock-Paper-Scissors game. 
(Hint : aks for players(usinng input),compare them, print out a message of congratulations to  the winner, 
and ask if the players want to start a new game)

Remember the Rules:
Rock beats Siccsors => R(r)beats S(s)
Siccsors beats Paper =>S(s)beats P(p)
Paper beats rock => P(p) beats R(r)"""


series = int(input("Enter the rounds"))
 
player1a=0
player2a=0
for i in range(series):
  player1 =input ("Enter your choice (R,S,P):").upper()
  player2 =input ("Enter your choice (R,S,P):").upper()

  if player1 == player2:
   print("Draw")
  elif (player1 =="R" and  player2 =="S") or (player1 =="S" and  player2 =="P") or (player1 =="P" and  player2 =="R"):
    print("Player1 beats Player2")
    player1a += 1
  else:
    player2a +=1
    print("Player2 beats Player1")

if player1a > player2a:
  print("Player1 won the series")
elif player1a < player2a:
  print("Player2 won the series")
else:
  print("Series is a tie")

