class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit_str = ''
        for digit in digits:
            digit_str+=str(digit)
        
        digit= int(digit_str)
        d_sum=str(digit+1)

        for i in range(len(d_sum)):
            if i < len(digits):
                digits[i]=int(d_sum[i])
            else:
                digits.append(int(d_sum[i]))

        return digits


            
            
        