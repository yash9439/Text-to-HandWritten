from PIL import Image
import string
import random


#random word either 1 or 0 
used_width , used_height = 0,0

back = Image.open("Dataset_online/zback.png")
width,height = 50,0
arr = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
arr = arr+" "

def condn(case):
    global width,height
    # global used_width , used_height
    print(case)
    k = random.randint(0,1)
    folder=""
    if(k==0):
        folder = "Dataset_online/"
    elif(k==1):
        folder = "letters_white_seperated (3rd copy)/"
    path = folder+case+".png"
    cases = Image.open(path)
    letter_width = cases.width
    
    back.paste(cases,(width,height))
    newwidth = cases.width
    width = width+newwidth
    if (width > 6000):
        width = 50
        height = height + 300

inp = "Virat Kohli is a world-famous Indian cricketer who has given multiple chances to the whole country to feel proud because of his personality and achievements. Writing an essay on Virat Kohli in English is fun and interesting because there are so many interesting facts about this cricketer, not just as a sportsman but as a person too. Virat Kohli is an inspiring figure and a role model for many youngsters and children. He has brought a class to Indian cricket. Under his captaincy, the Indian cricket team has reached heights. The legacy of Virat Kohli will never end, so this topic for essay writing will remain for long."

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
        
#save the image
back.save("Final_output.png")
back.show()
