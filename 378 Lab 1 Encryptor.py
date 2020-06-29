#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 18:56:05 2019

@author: Dominique Oyco (014605758)
         LAB ASSIGNMENT 1 PART A - ENCRYPTOR
"""
import string as s

#NOTE: list() converts strings & tuples into lists
alphabetList = list(s.ascii_lowercase) #returns the alphabet in lowercase form
    
"""
encrypts the plaintext message by using a key
"""
def encrypt(msg, key):
    msgToUse = list(msg)
    keyToUse = list(key)
    newMsgToUse = list(trimAndConvert(msgToUse))
    encryptedMsg = " " #stores the new encrypted message
    
    #Encrypts the message by going through the key and iterate through every
    #single alphabet in the sentence of the message 
    #and then searching for index of the corresponding alphabet on the key,
    #matching it and translates it to the new alphabet. The end product will
    #be the encrypted message
    for i in range(1, len(newMsgToUse)):
        encryptedMsg += keyToUse[alphabetList.index(newMsgToUse[i-1])]        
    return encryptedMsg
    
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
    encryptingKey = 'rtkljhmpqasvybezocwnxugfdi'
    writeKey = open("Encryptor Results.txt", "a+")
    print("KEY TO DECRYPT: ", encryptingKey, file=writeKey)
    print("\nENCRYPTED MESSAGES: ", file=writeKey)
    writeKey.close
        
    #OPEN AN EXTERNAL FILE THAT HAS THE MESSAGES PROVIDED FOR TESTING PURPOSES
    filePlaintxt = open("Part2Plaintexts.txt", "r")
    messages = list(filePlaintxt)
    text = ""
        
    #Print the original plaintext and encrypted plaintext in a txt file
    for k in range(0, len(messages)):
        #open/create a txt file and append (a) the text
        text = messages[k]
        print(text)  
        
    print('\nPlease check the created txt file on the same folder as this file for the results!')     
    for l in range(0, len(messages)):
        #open/create a txt file and append (a) the encrypted messages
        
        #The created txt file will contain the encrypted message that can be 
        #used on the decryptor
        with open("Encryptor Results.txt", "a") as text_file:
            text = messages[l]
            text = trimAndConvert(text) 
            encryptedMessages = encrypt(text, encryptingKey)
            print(encryptedMessages, file=writeKey) 
        text_file.close    
    return 

main()
    