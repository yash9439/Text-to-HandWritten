from PIL import Image
import string
import random


#random word either 1 or 0 


back = Image.open("Dataset_online/zback.png")
width,height = 50,0
arr = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
arr = arr+" "

def condn(case):
    global width,height
    print(case)
    k = random.randint(0,1)
    folder=""
    if(k==0):
        folder = "Dataset_online/"
    elif(k==1):
        folder = "letters_white_seperated (3rd copy)/"
    path = folder+case+".png"
    cases = Image.open(path)
    back.paste(cases,(width,height))
    newwidth = cases.width
    width = width+newwidth

inp = "Chandu ke Chacha ne chandu ki chachi ko chandni raat me chatni chatai "

for letter in inp:
    if letter in arr:
        if letter == " ":
            letter = "zspace"
        if letter ==".":
            letter = "fs_"
        if letter == ",":
            letter = "coma_"
        if letter == "?":
            letter = "que_"
        condn(letter)
        
back.show()
