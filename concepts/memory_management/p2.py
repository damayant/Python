import sys

int_one=1
int_list=[1]
string_one="1"

print(f"size of int : {sys.getsizeof(int_one)} bytes")
print(f"size of list : {sys.getsizeof(int_list)} bytes")
print(f"size of string : {sys.getsizeof(string_one)} bytes")