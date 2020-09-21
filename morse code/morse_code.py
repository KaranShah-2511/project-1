
M =(('a','.- '),('b', '-... '),('c','-.-. '),('d','-.. '),('e','. '),('f','..-. '),('g','--. '),('h','.... '),('i','.. '),('j','.--- '),('k','-.- '),('l','.-.. '),('m','-- '),('n','-. '),('o','--- '),('p','.--. '),('q','--.- '),('r','.-. '),('s','... '),('t','- '),('u','..- '),('v','...- '),('w','.-- '),('x','-..- '),('y','-.-- '),('z','--.. '),(' ',' '))

def convertedMorce(morce):
    for a,b in M:
        morce = morce.replace(a,b)
    return morce

if __name__ == '__main__':
    morce = input("Enter your message to convert into morce code::")
    morce = convertedMorce(morce)
    print(f"morce code is :{morce}")