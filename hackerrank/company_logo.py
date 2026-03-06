from collections import Counter, defaultdict

def solution(s:str,count:int=3):
    counter = Counter(s)
    sorted_items = sorted(counter.items(),key=lambda x:(-x[1],x[0]))
    for char,freq in sorted_items[:count]:
        print(char,freq)



# solution("qwertyuiopasdfghjklzxcvbnm")
solution("szrmtbttyyaymadobvwniwmozojggfbtswdiocewnqsjrkimhovimghixqryqgzhgbakpncwupcadwvglmupbexijimonxdowqsjinqzytkooacwkchatuwpsoxwvgrrejkukcvyzbkfnzfvrthmtfvmbppkdebswfpspxnelhqnjlgntqzsprmhcnuomrvuyolvzlni")