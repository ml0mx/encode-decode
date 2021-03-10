import string

#CONSTANTS
ALPHA = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
CIPH = ["c","i","d","u","t","z","w","n","g","m","x","f","j","h","o","b","y","l","e","r","q","k","v","p","a","s"]

def main():
    choice = input("Press 1 to encode and 2 to decode: ")
    numchoice = int(choice)
    if numchoice == 1:
        userword = input("Type your word to encode: ")
        encode(userword)
    else:
        userword = input("Type your word to decode:" )
        decode(userword)

def split(word):
    return [char for char in word] #returns each character as item in lsit

def encode(word):
    characterlist = split(word)
    newlist = []
    for x in characterlist:
        ind = ALPHA.index(x) #get index location of current letter
        indd = CIPH[ind] #match to cipher location
        newlist.append(indd)
    codeoutput = ''.join(newlist) #join it up as a string
    print("Your encoded word is: ",codeoutput)
    main()

def decode(word):
    #decode just works in reverse to encode
    characterlist = split(word)
    newlist = []
    for x in characterlist:
        ind = CIPH.index(x)
        indd = ALPHA[ind]
        newlist.append(indd)
    codeoutput = ''.join(newlist)
    print("Your decoded word is: ",codeoutput)
    main()
main()

'''
TODO
add option for multiple cipher options
perhaps some common encoding options
windows gui
'''