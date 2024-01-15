def strStr(haystack:str, needle:str)->int:
    if needle not in haystack :
        return -1
    else:
        return find(haystack,needle)

def find(haystack,needle):
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            for j in range(0,len(needle)):
                if needle[j] != haystack[i+j]:
                    break
                else:
                    if j == len(needle)-1:
                        return i

            

            

print(strStr(haystack = "mississippi", needle = "issip"))
