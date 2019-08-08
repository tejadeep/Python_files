import time
class Test:
    def __init__(self):
        print ("*********")
    def __del__(self):
        print("&&&&&&&&&&&&")
t1=Test()
time.sleep(3)
del t1
time.sleep(5)
quit()
print ("end")

