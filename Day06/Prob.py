
import time
def TimeCalc(fnc):
    def helper(s):
        print("Strated to execute.....")
        start_time = time.perf_counter()
        fnc(s)
        end_time = time.perf_counter()
        print('Completed the execution.....')
        print(f"total time taken :{round(end_time - start_time, 2)}")
        print("-" * 60)
    return helper

@TimeCalc
def fun(secs):
    lst = []
    for i in range(1, secs):
        for j in range(1, i+1):
            lst.append(j ** 2)

fun(8000)



# write a decorator to calculate the  time taken by the function to execute

