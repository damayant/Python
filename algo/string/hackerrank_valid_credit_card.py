import re
def valid_credit_card(card:str)->bool:
    valid = False
    card_exp=r'^[0-9-]+$'
    substr_exp=r'^[0-9]+$'
    substr_list = []
    length = 0

    if "-" in card:
        if re.match(card_exp,card):
            substr_list = card.split("-")
        else:
            if len(card) == 16:
                for i in range(0,len(card),4):
                    substr_list.append(card[i])
            return False
    for i in  range(len(substr_list)):
        if i==1:
            if substr_list[i][0] not in "456":
                return False
        length +=len(substr_list[i])
        if re.match(substr_exp,substr_list[i]):
            if len(substr_list[i]) != 4:
                return False
    return length== 16




print(valid_credit_card("5123-4567-8912-3456"))
