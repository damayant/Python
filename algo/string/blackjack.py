import sys
from typing import Tuple

def get_card_value(card_token:str)->Tuple[int,bool]:
    """
    Parse a card token like 'S-10', 'H-J', 'C-A' and return:
      (value_as_int, is_ace_flag)
    We treat Ace as 11 initially (is_ace_flag = True).
    Face cards J/Q/K are 10.
    Numeric cards 2-10 are their int values.
    """
    token=card_token.strip()
    #extract the rank part (after '-' ) , fallback if '-' missing
    if '-' in token:
        _,rank=token.split('-',1)
    else:
        rank=token[1:]

    if rank=='A':
        return 11,True 
    if rank in ('J','K','Q'):
        return 10,False 
    return int(rank),False 


def compute_hand_compute(card1:str,card2:str)->int:
    """
    Compute the best hand total for the two cards, 
    treating Ace as 11 or 1 to avoid busting if possible.
    """
    value1,is_ace1=get_card_value(card1)
    value2,is_ace2=get_card_value(card2)

    total_value=value1+value2
    aces_count=(1 if is_ace1 else 0) + (1 if is_ace2 else 0)

   # If total_value > 21 and we have Aces counted as 11,
    # convert an Ace from 11 to 1 by subtracting 10 (repeat if needed).
    while total_value>21 and aces_count>0:
        total_value-=10
        aces_count-=1
    return total_value

def select_action(total_value:int)->str:
    """
    Decide which action to print based on total_value:
      - 21 -> "BlackJack"
      - <= 16 -> "Hit"
      - 17..20 -> "Stay"
    """
    if total_value==21:
        return "BlackJack"
    if total_value<=16:
        return "Hit"
    return "Stay"


def main(tokens):
    card_token1,card_token2=tokens[0],tokens[1]
    total=compute_hand_compute(card_token1,card_token2)
    action=select_action(total)
    print(action)

tokens=['S-10','H-J']
if __name__=="__main__":
    main(tokens)