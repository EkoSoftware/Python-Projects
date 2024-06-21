from icecream import ic
def myCipher(text, key, salt=59):
    encryption = ""
    
    for i, char in enumerate(text):
        value = ord(char) + ord(key[i])
        if salt: value += salt
        value += 1337
        encryption += chr(value)
    
    return encryption


def myDecipher(text, key, salt=59):
    decryption = ""
    
    for i, char in enumerate(text):
        value = ord(char) - ord(key[i])
        if salt: value -= salt
        value -= 1337
        decryption += chr(value)

    return decryption

# GUI
import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Sipher")



# Fonts
available_fonts = font.families()


normal_font = ("Arial", 12, "normal")
bold_font = ("Arial", 12, "bold")
italic_font = ("Arial", 10, "italic")
custom_font = ("Helvetica", 12, "roman")

# Key
key_var = tk.StringVar(value="")
key_entry_var = tk.StringVar(value="<Enter Encryption Key>")
key_frame = tk.LabelFrame(root)
key_button = tk.Button(key_frame, text="Confirm Key")
key_label_static = tk.Label(key_frame,text="Your key: ")
key_label = tk.Label(key_frame,text="",font=custom_font, )
key_entry = tk.Entry(key_frame,textvariable=key_entry_var,justify='center')
key_entry.bind("<FocusIn>",lambda placeholder: key_entry.delete(0,"end"))


def enter_key():
    if key_entry.get().startswith("Key ca"):
        pass
    elif key_entry.get().startswith("<Ch"):
        pass
    elif key_entry.get():
        key_entry.config(font=italic_font)
        key_var.set(key_entry.get()[:])
        print(f'Key set to: {key_var.get()}')
        key_label.config(text=key_var.get())
        key_entry_var.set("<Change key?>")
    else:
        key_entry_var.set("Key cannot be empty")

key_button.config(command=lambda:enter_key())

# Cipher
text_display = tk.Text(root)
cipher_var = tk.StringVar(value="<Enter Message>")
cipher_frame = tk.LabelFrame(root, text="Cipher")
cipher_entry = tk.Entry(cipher_frame, textvariable=cipher_var, justify='center', borderwidth=10,width=100)
cipher_entry.bind("<FocusIn>", lambda placeholder: cipher_entry.delete(0,"end"))
cipher_button = tk.Button(cipher_frame, text="Enter")
radio_frame = tk.LabelFrame(cipher_frame,text="Setting")
radio_var = tk.BooleanVar(radio_frame,True)
encipher_button = tk.Radiobutton(radio_frame,text="Encryption",variable=radio_var,value=True)
decipher_button = tk.Radiobutton(radio_frame,text="Decryption",variable=radio_var,value=False)



key_frame.pack()
key_button.pack()
key_entry.pack()
key_label_static.pack(side="left",padx=(20, 0))
key_label.pack(side="left", padx=(10, 0))

text_display.pack()
cipher_frame.pack()
radio_frame.pack()
encipher_button.pack(side='left')
decipher_button.pack(side='right')
cipher_button.pack()
cipher_entry.pack()

def enter_button():
    text = cipher_entry.get()
    print("Debug 1")
    
    key = key_var.get()
    key = key[:]
    
    print(f'Debug key: {key}')
    
    while len(key) < len(text):
        key += key
    key = key[:len(text)]            
    print(f"Debug modified key: {key}")
    
    if radio_var.get() == True:
        print("Debug radio_var get")
        message = myCipher(text, key)
        text_display.insert(tk.END, f'Encrypted Message: {message}\n')
        cipher_var.set("")
    else:
        print("Debug radio_var didnt get")
        message = myDecipher(text, key)
        text_display.insert(tk.END, f'Decrypted Message: {message}\n')
    print("Debug 3 : Writing text to display.")
cipher_button.config(command=lambda:enter_button())

#send_button.config(command=lambda:enter_button())


    
while True:
    root.mainloop()

    
    #enter_button()
    
    #enc = myCipher(uinput, key,salt=444)
    #print(f'Encrypted message:\n{enc}')
    #dec = myDecipher(enc, key, salt=444)
    #print(f'Deciphered message:\n{dec}')
    
    #uinput = input("Message to decrypt\n>")
    

    

