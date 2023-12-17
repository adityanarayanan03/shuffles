import numpy as np

class CardDeck:
    '''
    Represents a deck of cards.

    Has methods to simulate different types of shuffles.
    '''
    def __init__(self):
        self.cards = [i for i in range(52)]
    
    def perfect_cut(self):
        '''
        Partitions the deck perfectly into 26/26
        '''
        a = [self.cards[i] for i in range(26)]
        b = [self.cards[i] for i in range(26, 52)]
        return a, b
    
    def perfect_bridge(self, n=1):
        '''
        Using a perfect cut, executes a perfect bridge n times.
        '''
        for _ in range(n):
            a, b = self.perfect_cut()
            
            #Random choice on whether we start with a or b
            x = np.random.choice(2)
            if x == 1:
                a,b = b,a

            #Do the interleaving part
            out = []
            for i in range(len(a)):
                out.append(a[i])
                out.append(b[i])
            
            self.cards = out

    def __str__(self):
        return str(self.cards)