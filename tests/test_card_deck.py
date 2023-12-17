from shuffles import CardDeck
from shuffles import ch

import logging
logger = logging.getLogger("client")
logger.setLevel(logging.DEBUG)
logger.addHandler(ch)

def test_construction():
    print("\n")
    cd = CardDeck()
    logger.debug(cd)

def test_perfect_cut():
    print("\n")
    cd = CardDeck()
    logger.debug(cd.perfect_cut())

def test_perfect_bridge():
    print("\n")
    cd = CardDeck()
    cd.perfect_bridge(n=3)
    logger.debug(cd)