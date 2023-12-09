# Class for GameStates

class GameState:
    def __init__(self, player):
        self.player = player  # The player object for the current turn
        self.total_damage = 0  # Total damage dealt this turn
        self.resources = player.pitch
        self.hand = player.hand.copy()
        self.last_card_had_go_again = False
        
        
    def getPlayedCards(self):
        return self.player.playedcards
        

    def isHandEmpty(self):
        return len(self.player.hand) == 0
    
    def hasResources(self):
        return self.player.resources > 0

    def calculateDamage(self, card_played):
        self.total_damage += card_played.attack

        return self.total_damage

    def resolveTurn(self, card_played):
        if card_played.go_again:
            return True
        else:
            return False


    def canPlayCard(self, card_to_play):
        resources_needed = card_to_play.cost - self.player.resources

        return resources_needed <= 0

    def hasPlayableCard(self):
        for card in self.player.hand:
            if self.canPlayCard(card):
                return True
        return False

    def playCard(self, card_to_play):
        # Check if the card is in the player's hand
        if card_to_play not in self.player.hand:
            print("Card is not in current hand!")
            return False

        # Pitch cards to generate needed resources
        try:
            resources_needed = card_to_play.cost - self.player.resources
            if resources_needed > 0:
                best_pitch_card = None
                for card in self.player.hand:
                    if card != card_to_play and card.pitch >= resources_needed:
                        if best_pitch_card is None or card.pitch > best_pitch_card.pitch:
                            best_pitch_card = card

                # Pitch the best card found, if any
                if best_pitch_card:
                    self.player.pitchzone.append(best_pitch_card)
                    self.player.hand.remove(best_pitch_card)
                    self.player.resources += best_pitch_card.pitch
                else:
                    print("Not enough resources to play the card!")
                    return False

            # Play the card
            self.player.playedcards.append(card_to_play)
            self.player.hand.remove(card_to_play)
            self.player.resources -= card_to_play.cost

            # Update the last_card_had_go_again flag
            self.last_card_had_go_again = card_to_play.go_again 
            # Calculate damage and resolve turn
            self.calculateDamage(card_to_play)
            if self.resolveTurn(card_to_play):
                print("Play another Card!")
            else:
                print("Turn Ends")

            return True

        except Exception as e:
            print("Error playing card:", e)
            return False
    

        
