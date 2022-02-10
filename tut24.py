# time module
# check time duration
import time
# initial=time.time()
# print(initial)
# k=0
# i=0
# while(k<45):
#     print("This is harry bhai")
#     #stop any value for any seconds,minutes etc
#     # time.sleep(2)
#     k+=1
#     print("while loop ran in", "in seconds",time.time()-initial)
#     initial2=time.time()
#     for i in range(i<45):
#         print("This is harry bhai")
#         i+=1
#         print("for loop an in",time.time()-initial2)
localtime=time.asctime(time.localtime(time.time()))
print(localtime)

