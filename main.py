import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


print(art.logo)
print("lets play blackjack")
def play_game():
    first_card=random.choice(cards)
    second_card=random.choice(cards)
    your_card=[first_card,second_card]
    dealer_card=random.choice(cards)
    sum_of_cards=sum(your_card)
    print("your cards are:",your_card)
    print("sum of your card is",sum_of_cards)
    print("dealers first card is:",dealer_card)



    if sum(your_card)==21 and len(your_card)==2:
        print("blackjack !you win")
    else:
        def another_card(current_sum):
            while True:
                if current_sum>21 and 11 in your_card:
                    your_card.remove(11)
                    your_card.append(1)
                    current_sum=sum(your_card)
        another_card_needed=input("if you need another card type 'y' , if not type 'n'").lower()
        if another_card_needed=="y":
            new_card=random.choice(cards)
            your_card.append(new_card)
            print("your cards are:",your_card)
            print("sum of your card is")
            current_sum=sum(your_card)
            print(current_sum)
            print("dealers first card is:")
            print(dealer_card)
            if current_sum> 21:
                print("you went over 21 dealer wins :((((((((((")
            else:
                return current_sum

        your_sum=another_card(sum_of_cards)
        dealer_sum=dealer_card
        while dealer_sum<17:
            other_card=random.choice(cards)
            dealer_sum+=other_card
        print("the sum of dealers card is:",dealer_sum)
        if dealer_sum>21:
            print("you have won since dealers score went over 21.")
        if int(your_sum)<=21 and int(dealer_sum)<=21:
                if 21-your_sum>21-dealer_sum :
                    print("dealer wins the game")
                elif 21-your_sum<21-dealer_sum:
                    print("you win the game")
                elif your_sum==dealer_sum:
                    print("its a draw-")
                elif your_sum==21:
                    print("you win the game;)))))))))))")
                else:
                    print("dealer wins the game")
print(play_game())

play_blackjack = input("Do you wan to play blackjack or not? if yes type 'y' if not type 'n'.").lower()
while play_blackjack=="y":
    print("\n"*22)
    print(art.logo)
    print(play_game())
if play_blackjack=="n":
    print("The game was not started since you chose no!!!!")
