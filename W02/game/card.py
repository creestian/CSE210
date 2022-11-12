import random

class Card:
    """Individual cards represented as numbers from 1 to 13.
    
    The responsibility of the Card is to keep track of the value of the current and the next card.
    
    Attributes:
        value (int): The card number.
    """
    def __init__(self):
        """Constructs a new instance of the card.
        
        Args:
            self (Card): An instance of the card.
        """
        self.value = 0
        

    def draw(self):
        self.value = random.randint(1,13)