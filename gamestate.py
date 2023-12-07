# Class for GameStates

class GameState:
    def __init__(self, player):
        self.player = player  # The player object for the current turn
        self.total_damage = 0  # Total damage dealt this turn

    def calculateDamage(self, card_played):
        self.total_damage += card_played.attack

        return self.total_damage

    def resolveTurn(self, card_played):
        if card_played.goagian:
            return True
        else:
            return False

    def playCard(self, card_to_play):

        #Check if card is in player hands
        if card_to_play not in self.player.hand:
            print("Card is not in current hand!")
            return False
        
        #pitch cards to generate needed resources
        try:
            resources_needed = card_to_play.cost - self.player.resources
            if resources_needed > 0:
                for card in self.player.hand:
                    if card.pitch >= resources_needed:
                        self.player.pitchzone.append(card)
                        self.player.hand.remove(card)
                        self.player.resources += card.pitch
            
            #play the card 
            print("Playing Card " + card_to_play.cardName)

            self.player.playedcards.append(card_to_play)

            print("Trying to Remove " + card_to_play.cardName)
            self.calculateDamage(card_to_play)
            go_agian = self.resolveTurn(card_to_play)
            if go_agian:
                print("Play another Card!")
            else:
                print("Turn Ends")
        
            self.player.hand.remove(card_to_play)
            self.player.resources -= card_to_play.cost
            return True
        except:
            print("Can't play this hand!")
            return False
    

        
