'''
Seems that I need a separate function to pass queue arguments to mainprocess?
Make a consumer process that breaks when input is None?
idk

Currently, I need to implement the outputting of messages to the gui textbox whenever something pops in msgqueue
also pbar should look at outputqueue

Maybe this should be done in the GUI?
how to transfer the queue from functions to guifunctions though....
    - try doing this in functions.py first, it gets the objects...

UPDATE!
mainprocess NEEDS to accept multiple queues (input, output, msg), right now it doesn't!
'''

