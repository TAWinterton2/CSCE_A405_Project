
def maximizeDamage(game_state, go_again=True):

    max_damage = 0
    best_sequence = []

    print("Beginning MinMax")

    #Termination state
    if not game_state.hasPlayableCard() or not go_again:
        return game_state.total_damage
    

    for card in game_state.hand:
        if game_state.canPlayCard(card):
            #simulate playing the card
            new_state = game_state.playCard(card)
            damage, sequence = maximizeDamage(new_state, card.go_again)

            if damage > max_damage:
                max_damage = damage
                best_sequence = sequence

    return max_damage, best_sequence