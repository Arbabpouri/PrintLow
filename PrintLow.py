from time import sleep
text = "test"
for i in text:
    sleep(0.1)
    print(i,end= '', flush= True)