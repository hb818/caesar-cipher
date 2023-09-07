from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser_cipher(direction,text,shift):
  shift=shift%26
  new_text=[]
  for i in range(0,len(text)):
    if text[i] in alphabet:
      position=alphabet.index(text[i])
      if(direction=='encode'):
        new_position =(position+shift)%26
      elif(direction=='decode'):
        new_position =position-shift
        if(new_position<0):
          new_position+=26
      new_text.append(alphabet[new_position])
    else:
      new_text.append(text[i])
  print(''.join(new_text))

print(logo)

answer='Yes'

while(answer=='Yes'):
  request = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  input_text = input("Type your message:\n").lower()
  shift_num = int(input("Type the shift number:\n"))
  ceaser_cipher(direction=request, text=input_text, shift=shift_num)
  answer=input("Do you want to continue Yes/No\n")

