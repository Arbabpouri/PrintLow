from time import sleep
text = "test"
for char in text:
    sleep(0.1)
    print(char, end= '', flush= True)
