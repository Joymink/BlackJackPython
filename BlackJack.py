import random
import time
import os
deck =[]

#Spade = S
#Diamond = D
#Heart = H
#Club = C

x = 2
y = 1
check = 1
suit =""
#Filling the deck of cards

for i in range(52):
    if i < 13:
        suit="♠"
    elif i <26:
        suit = "♦"
    elif i < 39:
        suit = "♥"
    else:
        suit = "♣"
    if x<=10:   
        deck.append([x, suit])
        x+=1
    elif x>10:
        if y==1:
            deck.append(["A",suit])
            y+=1
        elif y==2:
            deck.append(["J",suit])
            y+=1
        elif y==3:
            deck.append(["Q",suit])
            y+=1
        elif y==4:
            deck.append(["K",suit])
            y=1
            x=2



def printCard(cards):
    for i in range(len(cards)):
        print(" _________", end =" ")
    print()
    for i in range(len(cards)):
        print("|        |", end =" ")
    print()
    for i in range(len(cards)):
        print(f"|    {cards[i][0]}   |", end =" ")
    print()
    for i in range(len(cards)):
        print("|        |", end =" ")
    print()
    for i in range(len(cards)):
        print(f"|    {cards[i][1]}   |", end =" ") 
    print()
    for i in range(len(cards)):
        print("|________|", end =" ")
    print()
         
    
def addCards(cards):
    total =0
    for i in range(len(cards)):
        if str(cards[i][0])=='J' or str(cards[i][0])=='K' or str(cards[i][0])=='Q':
            total+=10
        elif str(cards[i][0])=='A':
            test = total+ 11
            if test >21:
                total+=1
            else:
                total+=11
        else:
            total+=cards[i][0]
    if total <=21:
        return total
    elif total>21:
        total=0
        for i in range(len(cards)):
            if str(cards[i][0])=='J' or str(cards[i][0])=='K' or str(cards[i][0])=='Q':
                total+=10
            elif str(cards[i][0])=='A':
                total+=1
            else:
                total+=cards[i][0]
        if total <= 21:
            return total
        else:
            return -1
    else:
        return -1
def extraCard(cards):
    return 0



    
deck_shuffled = random.sample(deck, len(deck))
while True:
    answer = input("Would you like to play Black Jack?\n")
    if answer.lower()=="yes":
        deck_removed = []
        player= []
        dealer= []
        #initial deal
        for i in range(4):
            if i%2 ==0:
                player.append(deck_shuffled[i])
                deck_removed = deck_shuffled.pop(i)
            else:
                dealer.append(deck_shuffled[i]) 
                deck_removed = deck_shuffled.pop(i)
        hidden_card= dealer[1]
        dealer[1]=["X","X"]

        print("Dealer's Hand:")
        printCard(dealer)
        print("Players Hand:")
        printCard(player)
        it =0
        while True:
            dealer[1]=hidden_card
            print(f"Total: {addCards(player)}")
            if addCards(player) == 21 and addCards(dealer)!=21 and it ==0:
                print("Black Jack!\nYOU WIN!")
                break
            elif addCards(player) == 21 and addCards(dealer)==21:
                print("Push")
                break
            else:
                it+=1
                dealer[1]=["X","X"]
                response = input("Would you like to:\n(1)Hit\n(2)Stand\n")
                if response == "1":
                    player.append(deck_shuffled[0])
                    deck_removed = deck_shuffled.pop(0)
                    print("Dealer's Hand:")
                    printCard(dealer)
                    print("Dealing...")
                    time.sleep(1)
                    print("Players Hand:")
                    printCard(player)
                    c = addCards(player)
                    if c <0:
                        print("You busted")
                        print("You lost")
                        break
                elif response == "2":
                    dealer[1]=hidden_card
                    print("Dealer's Hand:")
                    printCard(dealer)
                    print("Players Hand:")
                    printCard(player)
                    
                    deal = addCards(dealer)
                    play = addCards(player)
                    if deal > play:
                        print(f'Dealer had {deal}, you had {play}')
                        print("You lost")
                        break
                    elif play == deal and deal>=17:
                        print(f'Dealer had {deal}, you had {play}')
                        print("Push")
                        break
                    elif int(deal) < 17 and play >= int(deal):
                        while deal<17 and deal > 0:
                            dealer.append(deck_shuffled[0]) 
                            deck_removed = deck_shuffled.pop(0)
                            deal = addCards(dealer)
                            time.sleep(.5)
                            print("Dealing...")
                            time.sleep(1)
                            print("Dealer's Hand:")
                            printCard(dealer)
                            
                            
                        print("Dealer's Hand:")
                        printCard(dealer)
                        print("Players Hand:")
                        printCard(player)
                        
                        if deal>0:
                            if deal > play:
                                print(f'Dealer had {deal}, you had {play}')
                                print("You lost")
                                break
                            elif deal== play:
                                print(f'Dealer had {deal}, you had {play}')
                                print("Push")
                                break
                            else:
                                print(f'Dealer had {deal}, you had {play}')
                                print("You win")
                                break
                        else:
                            print("The Dealer Bust\nYOU WIN!")
                            break
                    else:
                        print(f'Dealer had {deal}, you had {play}')
                        print("YOU WIN!")
                        break
        #putting the cards back in the deck
        for i in deck_removed:
            deck_shuffled.append(i)
    elif answer.lower()=="no":
        break
    else:
        print("Please try again! (Yes/No)")





            