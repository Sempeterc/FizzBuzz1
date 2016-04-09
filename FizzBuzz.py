stevilo_x = int(raw_input ("vnesi stevilo med 1 in 100:"))  #vnese stevilo

if stevilo_x >= 1 and stevilo_x <= 100:
    for x in range(1, (stevilo_x+1)):
        if x % 3 == 0 and x % 5 == 0:
            print "fizzbuzz"
        elif x % 3 == 0:
            print "fizz"
        elif x % 5 == 0:
            print "buzz"
        else:
            print str(x)
else:
    print "vneseno stevilo mora biti med 1 in 100"

