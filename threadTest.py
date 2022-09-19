import threading


def function(i):
    print("function called by thread %i\n" % i)
    return


threads = []

for i in range(5):
    t = threading.Thread(target=function, args=(i, ))
    threads.append(t)
    t.start()

    # if use join() method, will output in fixed order, or output in random order.
    #t.join()
