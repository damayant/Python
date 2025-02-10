from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #first check if the total gas is less than the total cost - if yes its not possible to complete the circuit
        if sum(gas) < sum(cost):
            return -1
        #initialize variables
        total_gas = 0
        start = 0
        #iterate over the gas and cost arrays
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            #if total gas is less than 0 then we need to start from the next station
            if total_gas < 0:
                total_gas = 0
                start = i+1
        return start



    print(canCompleteCircuit(None,gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
    print(canCompleteCircuit(None,gas = [2,3,4], cost = [3,4,3]))
    print(canCompleteCircuit(None,gas = [5,1,2,3,4], cost = [4,4,1,5,1]))