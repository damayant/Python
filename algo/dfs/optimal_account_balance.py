from collections import defaultdict
from typing import List


class Solution:
    def minTransfers(self, transactions:List[list[int]])->int:
        #map person:to their net balnace
        net_balance=defaultdict(int)
        for giver,reciever,amt in transactions:
            net_balance[giver] -= amt
            net_balance[reciever] += amt 
        #we only care abt ppl who still have a balance to settle
        #positive value -> they owe money
        #negative value -> they are owed money
        settle_list = [bal for bal in net_balance.values() if bal!=0]
        num_people = len(settle_list)

        def backtrack(current_index):
            #skip anyone whose balance is zeroed
            while current_index < num_people and settle_list[current_index] == 0:
                current_index += 1
            
            #base case: evryone is settled
            if current_index == num_people:
                return 0 
            
            min_transactions = float('inf')

            #try to balnce current index person with any other person with opp balance(-/+)
            for next_person in range(current_index+1,num_people):
                if settle_list[current_index] * settle_list[current_index+1] < 0:
                    #process-> current index person debt to next person
                    settle_list[next_person] += settle_list[current_index]
                    #move to the next person and add 1 for this transaction
                    min_transactions = min(min_transactions,1+backtrack(current_index+1))
                    #backtrack:restore next person balance for next loop iteration
                    settle_list[next_person] -= settle_list[current_index]
                    #pruning: if current index and next person perfectly cancel out
                    #there is no better outcome for this person
                    if settle_list[current_index] + settle_list[next_person] == 0:
                        break 
                return min_transactions
        
        return backtrack(0)
            