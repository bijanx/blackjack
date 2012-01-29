min_bet = 5
suits = [ "SPADES", "CLUBS", "DIAMONDS", "HEARTS" ]
ranks = { 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'A':11 }
outcomes = { "Surrender": 0.5, "Win" : 2, "Lose" : 0, "Push" : 1, "Blackjack" : 2.5 } # outcomes-> payoff bet multipliers


def shuffle(cards):
    "shuffle a series of cards"
    pass
         
def play_hand(x,bet):
    "distribute cards to dealer and player(s)"

    dealers_hand,players_hand = [] # start with empty hands
    
    for i in range(2):
        dealers_hand.append(pull_card(x))
        players_hand.append(pull_card(x))
        
    player_score,dealer_score = score_hand(players_hand), score_hand(dealers_hand)
    
    if (res = eval(dealers_hand,players_hand)) is not None: return outcomes[res]
   
    # Get response from player
    if player_score < 21:
        while player_score < 21:
            pdecision = get_player_decision() # Hit or Stay?
            if pdecision == "HIT":
                players_hand.append(deck.pull_card)
                if (res = eval(dealers_hand,players_hand)) is not None: return outcomes[res]
            elif pdecision == "STAY": # Based on dealer now whether player wins or loses
                while dealer_score < 17:
                    dealers_hand.append(deck.pull_card) # Dealer obligatory hit
                    if (res = eval(dealers_hand,players_hand)) is not None: return outcomes[res]


def new_deck():
    "returns set of tuples representing cards"
    cards = []
    for suit in suits:
        for rank in ranks:
            card = {"suit" : suit, "rank" : rank}
            cards.append(card)
    return cards

def get_bet():
    "retrieves bet from player prior to hand"
    pass

def pull_card(x):
    "return a new shoe with a card removed from the shoe"
    return 0

def eval_hand(dealers_hand,players_hand):
    
    dealer_score,player_score = score_hand(dealers_hand), score_hand(players_hand)
    
    def push():
        if dealer_score == 21 and player_score == 21: # Check for Dealer-Player blackjack
            return outcomes["Even Money"]
    
    def beats():
        if dealer_score == 21 and player_score != 21:     # Check for Dealer-only blackjack
            return outcomes["Lose"]
    
    def broke():
        if dealer_score == 21:
            return outcomes["Lose"]
    
    def blackjack():
        pass
    
    if player_score==21:# Check for Player-only blackjack
        return outcomes["Blackjack"]
    
    if dealer_score >=17:
        pass
    
    if dealer_score > 21:
        return outcomes["Win"]
    
    if dealer_score > player_score:
        return outcomes["Lose"]
    
    elif dealer_score < player_score:
        return outcomes["Win"]
    
    elif dealer_score == player_score:
        return outcomes["Even Money"]
    
    if player_score > 21:
        return outcomes["Lose"]
    
def score_hand(hand):
    pass # TODO
                
def apply_player_decision(shoe,decision,player_hand,dealer_hand):
    pass
                
    
    # if dealer blackjack, game ov    

def get_player_decision():
    "player responds to hand"
    # SURRENDER
    # HIT
    # STAND
    # DOUBLE DOWN
    # SPLIT
    # INSURANCE
    
    # Explain STEP

def game(chips,bet_limit = 100,decks=6):
    "A game encompasses a series of hands or a 'session'"
    while True:
        chips += outcomes[play_hand()]
        print chips
        if chips < min_bet: return "Out of money. Game over."