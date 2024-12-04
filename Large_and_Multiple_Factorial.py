import multiprocessing.pool
import sys
import multiprocessing
import time
import math

sys.set_int_max_str_digits(100000000)

def computer_factorial(number):
    print(f"Calculating factorial of {number}")
    answer=math.factorial(number)
    print(f"Factorial of {number} is {answer}")
    return answer

if __name__=="__main__":
    numbers=[10000,20000,30000,40000]

    start=time.time()

    with multiprocessing.Pool() as pool:
        answers=pool.map(computer_factorial,numbers)

    end=time.time()

    print(f"Results: {answers}")
    print(f"Time taken: {end - start} seconds")