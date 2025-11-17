def compress(string:str):
    start,end =0,0
    length = len(string)
    result = []

    while end<length:
        start_char = string[start]
        while end <length and start_char == string[end]:
            end+=1
        frequency = end - start
        result.append((frequency,start_char))
        start = end
    return result

compress('1222311')