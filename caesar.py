text = "Hello world"
your_key = "python"
def vigenere(message,key):
 alphabet ='abcdefghijklmnopqrstuvwxyz'
 encrypted =" "
 key_index =0

 for i in message.lower():
   if i == " ":
     encrypted += i
   else:
     key_char = key[key_index %len(key)]
     offset = alphabet.find(key_char)
     index = alphabet.find(i)
     shifted=(index+offset) % len(alphabet)
     encrypt = alphabet[shifted]
     encrypted +=encrypt
     key_index +=1
    
 return encrypted

x =vigenere(text,your_key)
print(x)
