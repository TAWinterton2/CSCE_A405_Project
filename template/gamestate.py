# Class for GameStates

class GameState:
    def __init__(self, player):
        self.player = player  # The player object for the current turn
        self.total_damage = 0  # Total damage dealt this turn

    def playCard(self, card_to_play):

        #Check if card is in player hands
        if card_to_play not in self.player.hand:
            print("Card is not in current hand!")
            return 
        
        #pitch cards to generate needed resources
        resources_needed = card_to_play.cost - self.player.resources
        if resources_needed > 0:
            for card in self.player.hand:
                if card.pitch >= resources_needed:
                    self.player.pitchzone.append(card)
                    self.player.hand.remove(card)
                    self.player.resources += card.pitch
        
        #play the card 
        self.player.played_cards.append(card_to_play)
        self.player.hand.remove(card_to_play)
        self.player.resources -= card_to_play.cost
        
        return True
        
