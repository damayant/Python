class Solution :
    def convert(s:str,numRows:int)->str :
        string = s
        noRows = numRows
        if noRows == 1:
            return string
        result = []
        result_str = ''
        d = ({})
        for i in range(0, noRows):
            d[i] = []
        start = 0
        i = 0
        j = 0
        end = len(string)
    

        while start < end:
            while i < noRows and start<end:
                d[i].append(string[start])
            # print(d)
                i += 1
                start += 1
            j = i -1
            while j != 1 and start<end:
                j -= 1
                d[j].append(string[start])
                start += 1
            i = 0

        for value in d.values():
            result.append(value)
        for inner_arr in result:
            for element in inner_arr:
                result_str += element
        return result_str

    print(convert(s = "PAYPALISHIRING", numRows = 3))
