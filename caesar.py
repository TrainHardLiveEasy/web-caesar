from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    cipher = ''
    for value in text:
        if value.isalpha():             
            cipher += rotate_character(value,rot)
        else:
            cipher += value
    return cipher
def main():
    text = raw_input("Type a message: ")  
    rot = raw_input("Rotate by: ")
    rot = int(rot)                
    print (encrypt(text,rot))

if __name__ == '__main__':
    main()
