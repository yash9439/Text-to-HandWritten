from PIL import Image
import string

back = Image.open("zback.png")
width,height = 50,0
arr = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
arr = arr+" "

def condn(case):
    global width,height
    print(case)
    cases = Image.open("%s.png"%case)
    back.paste(cases,(width,height))
    newwidth = cases.width
    width = width+newwidth

inp = "Ekdum krishna lage che WOW , but how ? "

for letter in inp:
    if letter in arr:
        if letter == " ":
            letter = "zspace"
        if letter ==".":
            letter = "fs"
        if letter == ",":
            letter = "coma"
        if letter == "?":
            letter = "que"
        condn(letter)
        
back.show()
