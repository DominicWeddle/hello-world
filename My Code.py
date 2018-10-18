print("Dominic: Hello everyone, my name is Dominic!")
x = raw_input("What is your name?:")
print("Dominic: Hello " + x + " :)")
a = raw_input("Are you a boy or a girl?")
print("Dominic: Ah you are a ") + a +"."
b = raw_input("Is that correct?")
if b == ("yes"):
    print ("Dominic: Okay, I see you are a ")+a+(".")
elif b == ("Yes"):
    print("Dominic: Okay, I see you are a ")+a+(".")
else:
    a = raw_input("Dominic: Are you a boy or a girl?")
    print ("Dominic: Okay, I see you are a ")+a+(".")