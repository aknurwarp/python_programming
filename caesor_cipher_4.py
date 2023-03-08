#from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    if char in alphabet:
       position = alphabet.index(char)
       new_position = position + shift_amount
       end_text += alphabet[new_position]
    else:
       end_text += char
      
  print(f"Here's the {cipher_direction}d result: {end_text}")
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
       
#print(logo)

#TODO-1: Import and print the logo from art.py when the program starts.
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  ask_user = input("Do you want to restart the cipher program, type 'yes' if you want or type 'no'.")
  if ask_user == "no":
    should_continue = False
    print("Goodbye")
  



#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%). 
    
shift = shift % 26  #e.g- 45 + 26 = 1, remainder = 19(this 26 is going to devide shift as many times as need until we get the final point that shift no longer divide fully and left remainder and that number allows(19) to shift what entered shift number(45))

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)