
import time

def fun(x):
    print("Function fun going to sleep.....")
    time.sleep(x)
    print("Function fun just woke up.......")

print("Calling function......")
st = time.perf_counter()
fun(2)
fun(2)
fun(2)
et = time.perf_counter()
print("Execution completed......")
print(f"The total time taken by the function to execute :{round(et - st, 2)}")