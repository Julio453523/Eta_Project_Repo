#imports the functions needed for controlling the motors and accessing time features
#(cant actually import the rasberry pi software, cause we are not buying anything, but you get the idea)
import RPi.GPIO as GPIO
import time

#beginning state of movement. Sets up the positions 7,11,13,15. For context, the motors
#We are using are connected to those same 4 locations on the electrical grid
#Meaing that the changes of True/False will impact the 4 motors
def initial():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

#This function at first sets the cart to its initial state, then uses the 4 given
#inputs. (The 4 inputs arranged in this True/False way will cause the wheels to move the cart forward)
#it then resets and cleans up the grid
def forward(x):
    initial()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(x)
    gpio.cleanup()

#This function at first sets the cart to its initial state, then uses the 4 given
#inputs. (The 4 inputs arranged in this True/False way will cause the wheels to move the cart backwards)
#it then resets and cleans up the grid
def backwards(x):
    initial()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(x)
    gpio.cleanup()

#This function at first sets the cart to its initial state, then uses the 4 given
#inputs. (The 4 inputs arranged in this True/False way will cause the wheels to move the cart left)
#it then resets and cleans up the grid
def left(x):
    initial()
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(x)
    gpio.cleanup()

#This function at first sets the cart to its initial state, then uses the 4 given
#inputs. (The 4 inputs arranged in this True/False way will cause the wheels to move the cart right)
#it then resets and cleans up the grid
def right(x):
    initial()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(x)
    gpio.cleanup()

#Function takes a single key (w,a,s,d) and funnels that key into its corresponding
#movement function
def input(event):
    initial()
    key = event.char
    #sleep helps keep inputs from overlapping.
    sleep = 0.3

    if key.lower() == 'w':
        forward(sleep)
    elif key.lower() == 's':
        backwards(sleep)
    elif key.lower() == 'a':
        left(sleep)
    elif key.lower() == 'd':
        right(sleep)


#puts the console in a loop, and takes key presses and sends them to the input functions
command = tk.Tk()
command.bind('<KeyPress>', input)
command.mainloop
