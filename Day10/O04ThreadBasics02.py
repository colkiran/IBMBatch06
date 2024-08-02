# asynchronous execution code

import threading
import time


def doJob():
    print(f"Going to sleep for 2 secs......{threading.current_thread().name}")
    time.sleep(2)
    print(f"Just got up from sleep........{threading.current_thread().name}")

ST = time.perf_counter()

thrd1 = threading.Thread(target=doJob, name = "th1")
thrd2 = threading.Thread(target=doJob, name = "th2")
thrd3 = threading.Thread(target=doJob, name = "th3")
thrd4 = threading.Thread(target=doJob, name = "th1")
thrd5 = threading.Thread(target=doJob, name = "th2")
thrd6 = threading.Thread(target=doJob, name = "th3")

thrd1.start()
thrd2.start()
thrd3.start()
thrd4.start()
thrd5.start()
thrd6.start()

# asks the main thread to wait until all child threads complete
thrd1.join()
thrd2.join()
thrd3.join()
thrd4.join()
thrd5.join()
thrd6.join()

ET = time.perf_counter()
print(f"The total time taken by the task is {ET - ST}")
