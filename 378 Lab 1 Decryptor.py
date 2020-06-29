#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:42:30 2019

@author: Dominique Oyco (014605758)
         LAB ASSIGNMENT 1 PART B - DECRYPTOR
"""

import string as s

#NOTE: list() converts strings & tuples into lists
alphabetList = list(s.ascii_lowercase) #returns the alphabet in lowercase form

"""
decrypts the plaintext message by using a key
"""

#DECRYPTING METHODS - SUBSTITUTION & CAESAR CIPHER
def decrypt(msg, key):
    msgToUse = list(msg)
    keyToUse = list(key)
    newMsgToUse = list(trimAndConvert(msgToUse))
    decryptedMsg = " " #stores the new encrypted message
    
    #Encrypts the message by going through the key and iterate through every
    #single alphabet in the sentence of the message 
    #and then searching for index of the corresponding alphabet on the key,
    #matching it and translates it to the new alphabet. The end product will
    #be the encrypted message
    for i in range(0, len(newMsgToUse)):
        decryptedMsg += alphabetList[keyToUse.index(newMsgToUse[i])]        
    return decryptedMsg
    
"""
Trims the words on the plaintext from any spaces and punctuations and it also
converts any uppercase letters into lowercase letters
"""
def trimAndConvert(msg):
    newMsg = '' #will be used to store the new message    
    #iterates through the entire message to see if there if are non-alphabet
    #characters (i.e. punctuations & whitespaces). If there are non-alphabet 
    #chars, it gets rid of it and put the alphabet on a new message where all 
    #the letters will be converted into lowercase letters
    for j in range(0, len(msg)):
        if(msg[j].isalpha()):
            newMsg += msg[j]
    
    #convert the letters into lowercase just in case there is an uppercase 
    #letter
    newMsg = newMsg.lower() #NOTE: lower() converts lowercase to uppercase
    return newMsg    
    
def main():
    print('\nPlease check the created txt file on the same folder as this file for the results!') 
    #Want the message to be in lowercase
    ciphertext = input("Please enter the message to decode: ").lower()
    msgKey = input("Please enter the key: ").lower()    
    writeTitle = open("Decryptor Results.txt", "a+")
    print("KEY USED: ", msgKey, file=writeTitle)
    print("\nDECODED MESSAGE: ", file=writeTitle)
    writeTitle.close
           
    #THE PLAINTEXT MESSAGE   
    with open("Decryptor Results.txt", "a+") as text_file:
        decodedMessage = decrypt(ciphertext, msgKey)
        print("The decoded message is", decodedMessage, "\n", file=writeTitle)
    text_file.close
    decodedMessage = decrypt(ciphertext, msgKey)
        
    return 

main()
