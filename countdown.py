import time

# define the countdown func.
FILE_NAME = 'countdown.txt'
def countdown(t):

    while t:
        with open(FILE_NAME,'w') as f:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            f.write(timer + "\n")
            f.close()
            #print(timer)
            time.sleep(1)
            t -= 1

    print('Lets gooo!!')


# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))
