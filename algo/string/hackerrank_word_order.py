from typing import List


def wordOrder(no_words:int,words:List[str])->None :
    distinct_word_map = {}
    for word in words:
        if word not in distinct_word_map:
            distinct_word_map[word] = 1
        else:
            distinct_word_map[word]+=1
    
    print(len(distinct_word_map.keys()))
    for word in words:
        if distinct_word_map[word]!= "X":
            print(distinct_word_map[word])
            distinct_word_map[word] ="X"

wordOrder(4,["bcdef","abcdefg","bcde","bcdef"])