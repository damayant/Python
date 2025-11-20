class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open paranthesis if open < n
        #only add a closing paranthesis if closd<open
        #valid if open==closed == n 
        result , stack = [] , []
        def backtrack(open, close):
            if open == close == n :
                result.append("".join(stack))
                return 
            if open<n:
                stack.append("(")
                backtrack(open+1, close)
                stack.pop()
            if close<open:
                stack.append(")")
                backtrack(open, close+1)
                stack.pop()
        backtrack(0, 0)
        return result
        