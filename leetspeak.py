import random

def converttoleet(message):
    leetmessage=""
    charMapping = { 'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'], 'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'], 'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'], 'v': ['\\/']}
    for char in message:
        if(char.lower() in charMapping.keys() and (random.random() <=0.70)):
            possiblereplacements=charMapping.get(char.lower(),"")
            leetmessage+=random.choice(possiblereplacements)
        else:
            leetmessage+=char
    return leetmessage

def leettotext(message):
    text=""
    charMapping ={'4':['a'],'@':['a'],'/-\\':['a'],'(':['c'],'|)':['d'],'3':['e'],'ph':['f'],']-[':['h'],'|-|':['h'],'1':['i'],'!':['i'],'|':['i'],']<':['k'],'0':['o'],'$':['s'],'5':['s'],'7':['t'],'+':['7'],'|_|':['u'],'\\/':['v'],'a':['a'],'b':['b'],'c':['c'],'d':['d'],'e':['e'],'f':['f'],'g':['g'],'h':['h'],'i':['i'],'j':['j'],'k':['k'],'l':['l'],'m':['m'],'n':['n'],'o':['o'],'p':['p'],'q':['q'],'r':['r'],'s':['s'],'t':['t'],'u':['u'],'v':['v'],'w':['w'],'x':['x'],'y':['y'],'z':['z']}                                                                                                 
    for char in message:
        if(char in charMapping.keys()):
            decoded_replacements=charMapping.get(char,"")
            text+=random.choice(decoded_replacements)
        else:
            text+=char
    return text

y='Y'
while y=='Y'or y=='y':
    input_options=input("Do you want to cipher(1) or decode(2) your text?")
    if input_options=='1':
        input_message=input("Enter your message: ")
        output_message=converttoleet(input_message)
        print("Leetspeak for {} is {}".format(input_message,output_message))
    elif input_options=='2':
        input_message=input("Enter your message: ")
        output_message=leettotext(input_message)
        print("Decoded text for {} is {}".format(input_message,output_message))
    else:
        print("Please input a correct a option number")

    y=input("Do you still want to continue ? (Y/N): ")