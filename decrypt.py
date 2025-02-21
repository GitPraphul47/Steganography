import cv2
import os
import string
# read the encrypted image 
img = cv2.imread("encryptedImage.png") 

# initialize the empty dictionary
c = {}

# entering the ASCII values in the distionaries as key value pair 
for i in range(255):  
    c[i] = chr(i) # maps character according to their ascii values 

# reteiving the original password and message length 
with open("password.txt", "r") as f:
    lines = f.readlines()
    password = lines[0].strip()  # First line: password
    msg_length = int(lines[1].strip())  # Second line: message length

# created an empty string to store the decrypted message
message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for Decryption : ")
if password == pas:
    for i in range(msg_length):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decrypted message : ", message)
else:
    print("YOU ARE NOT authorized person")
