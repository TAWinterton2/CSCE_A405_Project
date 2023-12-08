from card import card_database as card
from template import deck_template as deck
from template import player_template as player
from gamestate import GameState
from minmax import maximizeDamage






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



#Create player objects
player_1 = player.player()

#Create Deck Object
player1_deck = deck.deck()
player1_deck.constructDeck(decklist)


#Shuffle Deck
player1_deck.shuffle()

#Draw Cards
player_1.draw(player1_deck)
player_1.showHand()
print('\n')

#create gamestate
game_state = GameState(player_1)


try:
    max_damage, best_sequence = maximizeDamage(game_state)
    print("Max Damage:", max_damage)
    print("Best Sequence:", best_sequence)
except Exception as e:
    print("Error trying to set up test:", e)














