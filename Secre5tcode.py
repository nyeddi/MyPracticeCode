low = 0
high = 100
#91
while True:
    SC = (high + low)/2
    print "Is your secret number {0}?".format(SC)
    inp = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if inp == 'l':
        low = SC
    elif inp =='h':
        high =  SC
    elif inp == 'c':
        print "Game over. Your secret number was:{0}".format(SC)
        break
    else:
        print "Sorry, I did not understand your input."
