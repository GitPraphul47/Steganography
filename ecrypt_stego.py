import cv2
import os
import string

# provide image path
img = cv2.imread("my_image.jpg")
# inputh the secret message 
msg = input("Enter secret message:")
# input the password 
password = input("Enter a passcode:")
# intialize the empty dictionaries 
d = {} 

# entering the ASCII values in the distionaries as key value pair 
for i in range(255):
    d[chr(i)] = i # maps ascii values  according to characters  

#  initialing variable m,n for pixel postions and color(z)
m,n,z = 0,0,0

# now loops through the secret message 
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3
# saving the password in text file 
with open("password.txt", "w") as f:
    f.write(f"{password}\n{len(msg)}")  # Save password and message length
cv2.imwrite("encryptedImage.png", img) #saving the encrypted message 
os.system("start encryptedImage.png")


''' here i have created a txt file for original password and password length because
   originally the only both user would know the password so they can verify 
   but here for the decryption file have also have to know the password by some means thats why 
   i have created the text file 

   in this code i have changed the saving format of image from jpeg to png because in the 
   jpg format the pixel values were being altered after the encryption was done  
   '''
