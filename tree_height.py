# python3
import sys
import threading
import numpy as np


def compute_height(n, parents):
    max_height=0
    current=np.zeros(n, int)
    for x in range(n):
        height=0
        count=x
        while count!=-1:
            if current[count]==0:
                height+=1
            else:
                height+=current[count]
                break
            count=parents[count]
        current[x]=height

    for y in range(n):
        if current[y]>max_height:
            max_height=current[y]

    return max_height


def main():
    global n
    entry=input()
    if "I" in entry:
        n=int(input())
        parents=np.array(list(map(int, input().split())))
        print(compute_height(n, parents))

    if "F" in entry:
        filepath="test/"+input()
        if not "a" in filepath:
            with open(filepath, "r") as f:
                parents=np.array(list(map(int, f.readline().split())))
                print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))
