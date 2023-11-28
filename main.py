from card import card_database as card
from template import deck_template as deck
from template import player_template as player






#Declare cards in decklist
Bittering_Thorns = card.Bittering_Thorns

Salt_The_Wound = card.Salt_The_Wound

Torrent_Of_Tempo = card.Torrent_of_Tempo

Flying_Kick = card.Flying_Kick

Head_Jab = card.Head_Jab

Brutal_Assult = card.Brutal_Assult

Scar_for_a_Scar = card.Scar_for_a_Scar


#Create Deck for Player
#This will serve as our database

decklist = [Bittering_Thorns, Bittering_Thorns, Bittering_Thorns, 
            Salt_The_Wound, Salt_The_Wound, Salt_The_Wound,
            Torrent_Of_Tempo, Torrent_Of_Tempo, Torrent_Of_Tempo,
            Flying_Kick,Flying_Kick, Flying_Kick,
            Scar_for_a_Scar, Scar_for_a_Scar, Scar_for_a_Scar,
            Brutal_Assult, Brutal_Assult, Brutal_Assult,
            Head_Jab, Head_Jab, Head_Jab]



#Create deck object and pass it deck list to construct deck
my_deck = deck.deck()

print("My Deck Created \n")

my_deck.constructDeck(decklist)
#Shuffle
my_deck.shuffle()

#Create player object
player_1 = player.player()




player_1.draw(my_deck)
player_1.showHand()












