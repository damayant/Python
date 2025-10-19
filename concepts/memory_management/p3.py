# from memory_profiler import profile

# @profile
# def my_memory_intensive_function():
#     a = [i*100 for i in range(1000000)]
#     b = [j/2 for j in a]
#     return b


# if __name__ == "__main__":
#     my_memory_intensive_function()


def check_age(age:int):
    try:
        if age>18:
            print('success')
    except TypeError as e:
        print(f'error:{e}')
        # raise e

check_age('age')