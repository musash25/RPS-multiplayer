again = "y"

while (again == 'y'):

    p1 = input("Player 1 --> Rock, Paper or Scissors? " )
    p1 = p1.lower()

    print() 

    p2 = input("Player 2 --> Rock, Paper, or Scissors? ")
    p2 = p2.lower()

    print()

    if(p1 == "rock"):
        if(p2 == "rock"):
            print("Tie")
        elif(p2 == "paper"):
            print("P2 wins!")
        elif(p2 == "scissors"):
            print("P1 Wins!")
    elif(p1 == "scissors"):
        if(p2 == "scissors"):
          print("Tie")
        elif(p2 == "rock"):
            print("P2 wins!")
        elif(p2 == "paper"):
            print("P1 wins!")
    elif(p1 == "paper"):
        if(p2 == "paper"):
            print("Tie")
        elif(p2 == "scissors"):
            print("P2 wins!")
        elif(p2 == "rock"):
            print("P1 wins!")
    else:
      print("Error-input not recognized. Maybe you mistyped?")
      


    again = input("Thanks for playing! ")

print()
