
def maximizeDamage(game_state):

    print("Beginning MinMax")

    #Termination state
    if game_state.isHandEmpty() or not game_state.hasResources():
       
        return game_state.total_damage

    max_damage = 0
    best_sequence = []

    for card in game_state.hand:
        if game_state.canplayCard(card):
            #simulate playing the card
            new_state = game_state.playCard(card)
            damage = maximizeDamage(new_state)

            if damage > max_damage:
                max_damage = damage
                best_sequence = new_state.getPlayedCards()
    return max_damage, best_sequence