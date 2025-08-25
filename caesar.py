text = input("Enter your text here : ")
alphabet ='abcdefghijklmnopqrstuvwxyz'
shift =3
encrypted =""
for i in text.lower():
   if i in alphabet:
        
     index = alphabet.find(i)
     shifted=(index+shift)% len(alphabet)
     encrypt = alphabet[shifted]
   
   else:
     encrypt = i
   encrypted += encrypt

print("Your encrypted text :",encrypted)
