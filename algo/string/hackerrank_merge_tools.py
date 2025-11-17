def merge_the_tools(string, k):
    # your code goes here
    length = len(string)
    # substr_length = int(length/k)<--- incorrect understanding
    result = []
    
    count = 0 
    
    while count < length:
        visit = set()
        substr = ""
        # start , end = count ,  count + substr_length
        start , end = count ,  count + k
        while start < end:
            if string[start] not in visit:
                visit.add(string[start])
                substr+=string[start]
            start+=1
        count =start
        result.append(substr)
        
    for substr in result:
        print(substr)
                
        
    
    
merge_the_tools(string="AABCAAADA", k=3)