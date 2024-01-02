class Solution :
    def convert(s:str,numRows:int)->str :
        string = s
        no_rows = numRows 

        if no_rows == 1 : return string

        result = []
        result_str = ''
        d = ({})

        for i in range(0,no_rows):
            d[i] = []

        i , j, start = 0, 0 , 0
        end = len(string)

        while start < end :
            while i < no_rows and start < end :
                d[i].append(string[start])
                i += 1
                start += 1

            j =  i - 1
            while j != 1 and start <end :
                j -= 1
                d[j].append[string[start]]
                start += 1

            i = 0

        for value in d.values():
            result.append(value)
        
        for inner_arr_val in result :
            for element_val in inner_arr_val :
                result_str += element_val
        
        return result_str
