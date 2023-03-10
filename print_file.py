import time

i = 0
while(i < 2):
    i = i + 1
    if i > 2:
        print("Game over")
        break
    else: 
        my_timer = input("Insert time to count down (h:m:s) ").split()

        if len(my_timer) == 3:

            s = int(my_timer[2])
            m = int(my_timer[1]) *60
            h = int(my_timer[0]) *3600
            sum_timer = s + m + h

            for x in range(sum_timer, 0, -1):
                second = x % 60
                minute = int(x / 60) % 60
                hour = int(x / 3600)
                time.sleep(1)
                print(f"{hour:02}:{minute:02}:{second:02}")
        elif i < 2:
            print("pleas insert (h:m:s) time to count down like this 0 5 6 where it`s mean 0 hour 5 minuts and 6 seconds")
        else :
            print("You write the time in wrong form")
            break
    



