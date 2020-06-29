"""
Created on Thu Sep 12 18:53:13 2019

@author: Dominique Oyco (014605758)
         LAB ASSIGNMENT 1 PART 1 - SIMPLE SUBSTITUTION CIPHER DECRYPTOR
"""
import string as s
import random as r
from ngrams import ngram_score #Courtesy of http://practicalcryptography.com

#NOTE: list() converts strings & tuples into lists
alphabetList = list(s.ascii_lowercase) #returns the alphabet in lowercase form

#BEGIN WITH CAESAR CIPHER
"""
--------------------------
CAESAR CIPHER SECTION
--------------------------
"""

"""
decrypts the ciphertexts to be decoded using Caesar or Substitution
"""
def decrypt(msg):
    method = 'Caesar Cipher'   
    print('Currently Using', method, "...")
    #trims the spaces and calls Shifter function to match the letters
    newMsg = caesarShifter(msg.replace(" ", "")) 

    #If Caesar Cipher doesn't work, Use substitution to decrypt
    if newMsg is "failure":
        newMethod = 'Substitution Cipher'
        print(method, "is unsuccessful. Attempting", newMethod, 
              "(Please be patient this will take a while...)")
        newMsg = substitutionDecrypter(msg)
    return newMsg
    
"""
Performs the shifting for the Caesar Cipher
Returns the shifted letters
"""
def caesarShifter(caesarMsg):
    #Call the bigrams to make the task easier
    #NOTE: A bigram or digram is a sequence of two adjacent 
    #elements from a string of tokens, which are typically letters, syllables, 
    #or words. A bigram is an n-gram for n=2
    bigrams = listOfBigrams()
    bigramCounter = 0
    neededBigramValue = len(caesarMsg) / 5  

    newBigramCounter = 0
    
    #Lists that will be used just for comparison
    decodedWords1 = []
    decodedWords2 = []

    #returns a list of most frequent letters in English alphabet
    frequentLetters = englishFrequentLetters() 
    alphabetNum = getAlphabetNumber() #Get the value when the alphabet key is given
    numberInAlphabet = getNumberAlphabet() #Get the letter when the number is given

    freqLetters = letterFrequency(caesarMsg)#need a dictionary of frequent letters  
    commonLetters = mostFrequentLetters(freqLetters)#need the common letters
    #Grab a common letter from the list starting with the most common one
    referenceLetter = frequentLetters.pop()

    #Iterate through every item in the common letters list because we need to
    #check every letter
    for i in commonLetters:  
        shift = alphabetNum[referenceLetter] - alphabetNum[i] #using Caesar method
        if shift < 0:
            shift += 26  #Positive shifting

        # Start shifting letters
        for encryptedLetter in caesarMsg:
            num = alphabetNum[encryptedLetter] + shift
            if num > 26:
                num -= 26
            decodedWords1.append(numberInAlphabet[num])

        decodedWords1 = ''.join(decodedWords1)  # Convert from list -> str

        #Count the number of bigrams in the newly constructed string
        for j in range(0, len(decodedWords1) - 3):
            if decodedWords1[j:j+2] in bigrams:
                newBigramCounter += 1

        if newBigramCounter > bigramCounter:
            bigramCounter = newBigramCounter
            decodedWords2 = decodedWords1  # decrypted_a/b are strings at this point

        newBigramCounter = 0
        decodedWords1 = []

    if bigramCounter < neededBigramValue:
        return "failure"

    return decodedWords2.upper()

"""
Returns the most commonly appearing bigrams in the English language
Courtesy of:
http://letterfrequency.org/
http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/digraphs.html
"""
def listOfBigrams():
    bigramList = ['th', 'he', 'in', 'er', 'an', 're', 'nd', 'at', 'on', 'nt', 'ha', 'es', 'st',
                  'en', 'ed', 'to', 'it', 'ou', 'ea', 'hi', 'is', 'or', 'ti', 'as', 'te', 'et',
                  'ng', 'of', 'al', 'de', 'se', 'le', 'sa', 'si', 'ar', 've', 'ra', 'ld', 'ur']
    return bigramList

"""returns a dictionary where accessing the letter as a key will provide its frequency
{letter:# of times it appears}
"""    
def letterFrequency(self):
    freqLetters = {ltr: 0 for ltr in list(s.ascii_lowercase)}
    for k in self:
        # Only check for letters
        if k in freqLetters:
            freqLetters[k] += 1
    return freqLetters

"""
Returns a dictionary in the format of {key = letter : value = number}
Access a certain letter in the alphabet and get their corresponding number
"""
def getAlphabetNumber():
    return {ltr: (int(num) + 1) for num, ltr in enumerate(list(s.ascii_lowercase))}

"""
Returns a dictionary in the format of {key = number : value = letter}
Access a number and get their corresponding value in the alphabet
"""
def getNumberAlphabet():
    return {(int(num) + 1): ltr for num, ltr in enumerate(list(s.ascii_lowercase))}

"""
Takes in a dictionary of letters and their frequency (see letterFrequency())
and checks to see the letters that are the most frequent and store them on a 
new list
Returns a list containing the letters that frequently appear the most
"""
def mostFrequentLetters(letters):
    mostFrequent = [] #list that will contain the most frequent letters
    for l in letters:
        if letters[l] != 0:
            mostFrequent.append(l)

    return mostFrequent

"""
Returns a list of letters that are appear more frequently on the English alphabet
courtesy of http://letterfrequency.org/
"""
def englishFrequentLetters():
    return ['z','q','x','j','k','v','b','p','y','g','f','w','m','u','c','l',
            'd','r','h','s','n','i','o','a','t','e']

"""
Generates a list of random alphabet letters in uppercase form
Return the list containing random alphabet letters
"""
def randomAlphabetLetters():
    randomAlphabet = []

    #generating random alphabet and storing them to the list
    #NOTE: .choice() returns a random item from a list, tuple, or string
    while len(randomAlphabet) is not 26:
        letter = r.choice(list(s.ascii_uppercase))
        if letter not in randomAlphabet:
            randomAlphabet.append(letter)
    return randomAlphabet

#SUBSTITUTION CIPHER SECTION- if Caesar Cipher fails, use this method instead!
"""
--------------------------
SUBSTITUTION CIPHER SECTION
--------------------------
"""

"""
Decodes the message using the Substitution Cipher
Returns the decrypted message
"""
def substitutionDecrypter(encryptedMsg):
    #test values
    zero = 0
    low = 1000
    high = 2000
    referenceScore = 10
    resetValue = 3 #once this value is reach, reset the scores
    
    #Removes non-alphabet characters such as spaces or punctuation from the encrypted message
    #NOTE: .join() concatenates elements in a string, tuple, or list
    encryptedMsg = ''.join(c for c in (encryptedMsg.replace(' ','').upper()) if c.isalpha())
    decryptedMsg = '' #stores the decrypted message
    potentialMsg = '' #stores the message that could potentially be the real decoded message

    #1. Counts the iteration since a lower fitness score was achieved
    iterationCounter = zero
    iterationUpdate = low if len(encryptedMsg) < low else high
    
    #2. Fitness scores indicate how close the encryption is to containing real English words
    #NOTE: Fitness scores are in ngrams.py
    #NOTE: dictionaryOfWords.txt contains the words ranked by their frequencies
    fitnessScore = ngram_score('dictionaryOfWords.txt')
    scoreForReference = referenceScore
    lowestScore = scoreForReference

    #3. Need the alphabet in random order so call the function above that returns
    #   a list of random alphabet letters
    randomAlphabet = randomAlphabetLetters()

    #attempting the substitution
    for m in range(iterationUpdate):
        #check if the reset cap is reached, if it's reached, reset the scores
        if iterationCounter >= resetValue: 
            scoreForReference = referenceScore
            iterationCounter = zero

        for n in range(len(randomAlphabet) - 1):
            checkLetters = randomAlphabet[n + 1:] #swap the remaining values

            #SWAPPING LETTERS SECTION:
            while len(checkLetters) > 0: 
                #generate a random integer and then use the int as an index to
                #the list of letters to check and then get the index of that 
                #particular letter from the random alphabet letters list
                #swap the random letter with the letter at index n
                randInt = r.randint(0, len(checkLetters) - 1)
                randLetter = checkLetters.pop(randInt)
                randomIndex = randomAlphabet.index(randLetter)
                randomAlphabet[n], randomAlphabet[randomIndex] = randomAlphabet[randomIndex], randomAlphabet[n]
                
                #Creating a map to check if fitness score of the new message is
                #lower than the previous message
                #KEY: letters in the random alphabet list
                #VALUE: alphabet in order
                encryptedMessageMap = {encryptedLetter: letterInAlphabet 
                                       for encryptedLetter, letterInAlphabet 
                                       in zip(randomAlphabet, 
                                              list(s.ascii_uppercase))}
                encryptedMessageContainer = ''

                for o in range(len(encryptedMsg)):
                    encryptedMessageContainer += encryptedMessageMap.get(encryptedMsg[o])
                potentialMsg = encryptedMessageContainer

                #check if updated score is lower that the previous score
                #score needs to be really low
                updatedScore = fitnessScore.score(potentialMsg)
                if updatedScore < scoreForReference:
                    scoreForReference = updatedScore
                else:
                    randomAlphabet[n], randomAlphabet[randomIndex] = randomAlphabet[randomIndex], randomAlphabet[n]

        #if the previous score is lower than the lowest score, then
        #the potential message is indeed the decrypted message
        if scoreForReference < lowestScore:
            lowestScore = scoreForReference
            iterationCounter = 0
            decryptedMsg = potentialMsg
        else:
            iterationCounter += 1

    return decryptedMsg

def main():
    #Ciphertexts needed to be decoded
    ciphertxt1 = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"
    ciphertxt2 = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi"\
                    "oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv"\
                    "xcdzq zoczn zxjiy"
    ciphertxt3 = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls"\
                    "iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae"
    ciphertxt4 = "iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn"\
                    "jbeuq iihed yzhni ifnun sayiz yudhe sqshu qesqa iluym"\
                    "qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq"\
                    "vayzq shsnj jejjz nshna hnmyt isnae sqfun dqzew qiead"\
                    "zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij"\
                    "qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq"\
                    "uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz"

    writeTitle = open("Part 1 Decryption Results.txt", "a+") #check this file
    print("DECODED MESSAGES: ", file=writeTitle)
    writeTitle.close
           
    #THE PLAINTEXT MESSAGE   
    print("NOTE: CHECK THE TXT FILE ONCE IT IS FINISHED RUNNING.")
    print("THE TXT FILE WILL BE EMPTY IF IT'S STILL RUNNING")
    print("AND WILL BE FILLED UP ONCE ITS FINISHED RUNNING\n")
    
    with open("Part 1 Decryption Results.txt", "a+") as text_file:
        print("Attempting to decrypt", ciphertxt1)
        decodedMessage1 = decrypt(ciphertxt1)
        print("The decoded message the first ciphertext is", 
              decodedMessage1, "\n", file=writeTitle)
        
        print("Attempting to decrypt", ciphertxt2)
        decodedMessage2 = decrypt(ciphertxt2)
        print("The decoded message the second ciphertext is", 
              decodedMessage2, "\n", file=writeTitle)
        
        print("Attempting to decrypt", ciphertxt3)
        decodedMessage3 = decrypt(ciphertxt3)
        print("The decoded message the third ciphertext is", 
              decodedMessage3, "\n", file=writeTitle)
        
        print("Attempting to decrypt", ciphertxt4)
        decodedMessage4 = decrypt(ciphertxt4)
        print("The decoded message the fourth ciphertext is", 
              decodedMessage4, "\n", file=writeTitle)
    text_file.close
main()