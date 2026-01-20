import time
import threading

def say(s):
    for i in range(5):
        time.sleep(0.1)      
        print(s)

def main():
    
    t = threading.Thread(target=say, args=("world",))
    t.start()


    say("hello")

    t.join()   

main()
