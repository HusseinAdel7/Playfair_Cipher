import os.path
from sys import platform
import os 
import string
from termcolor import colored
from Crypto.Cipher import DES3
from Crypto.Util import Counter
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random 
from Crypto.Cipher import DES3


os.system('clear') 

print ("\n\n\t\t\t    ------------------")
print(colored('\t\t\t      Cryptography ', 'yellow'))
print ("\t\t\t    ------------------")
print(colored('\n\t\t     * Written by : ', 'green'),end="")
print(colored(' Hussein Adel', 'white'),end="")
print ("\n\t\t\t\t     ------------\n")
print (" ===========================================================================\n")
print (colored('\t\t\t\t  ------------','white'))
print(colored('\t\t\t\t    Hello \U0001f600 ', 'yellow'))
print (colored('\t\t\t\t  ------------\n','white'))

#------------------------------------------------------------------------  
#========================================================================
# Auto Key Cipher 


def key_generation(key):                               # this functiuon  is for generating the key for encryption and decryption
    main=string.ascii_lowercase.replace('j','.')       # removing the j letter 
    key=key.lower()
    key_matrix=['' for i in range(5)]                  # create five empty raws 
    i=0;j=0                                            # raw , coulmn
    for c in key:
        if c in main:
            key_matrix[i]+=c
            main=main.replace(c,'.')                   # once addiding the letter in key_matrix we replace it by '.' to avoid repitition 
            j+=1
            if(j>4):                                   # in one raw 4 char
                i+=1  
                j=0
    for c in main:                                     # filling the rest of the key_matrix with the rest of unused char
        if c!='.':
            key_matrix[i]+=c
            j+=1
            if j>4:
                i+=1
                j=0                                    # key = playfairexample
    return(key_matrix)                                 # ['playf', 'irexb', 'cdghk', 'mnoqs', 'tuvwz']


def playfair_Encryption(plain_text):
    plain_text_pairs=[]
    cipher_text_pairs=[]
    plain_text=plain_text.replace(" ","")
    plain_text=plain_text.lower()
    i=0
    while i<len(plain_text):                           # this block for preparing the plain text and divide it in pairs
        a=plain_text[i]
        b=''
        if((i+1)==len(plain_text)):                    # to add x at the end of the string if there is one letter left
            b='x'
        else:
            b=plain_text[i+1]
        if(a!=b):                                      # to chceck if the pairs are not the same 
            plain_text_pairs.append(a+b)
            i+=2
        else:
            plain_text_pairs.append(a+'x')
            i+=1                                       #  palin text = husseinadel
    print("plain text pairs: ",plain_text_pairs)       #  plain text pairs:  ['hu', 'sx', 'se', 'in', 'ad', 'el']

    for pair in plain_text_pairs:                      #  plain text pairs:  ['pa', 'sx', 'se', 'in', 'ad', 'el']
        flag=False
        for row in key_matrix:                         #  key_matrix = ['playf', 'irexb', 'cdghk', 'mnoqs', 'tuvwz']
            if(pair[0] in row and pair[1] in row):
                j0=row.find(pair[0])                   #  finding the index of the letters  
                j1=row.find(pair[1])
                cipher_text_pair=row[(j0+1)%5]+row[(j1+1)%5] 
                cipher_text_pairs.append(cipher_text_pair)
                flag=True
        if flag:
            continue   

        for j in range(5):
            col="".join([key_matrix[i][j] for i in range(5)])       # to retrieve the coloums 
            if(pair[0] in col and pair[1] in col):                  # then the same thing as the row
                i0=col.find(pair[0])
                i1=col.find(pair[1])
                cipher_text_pair=col[(i0+1)%5]+col[(i1+1)%5]
                cipher_text_pairs.append(cipher_text_pair)
                flag=True
        if flag:
            continue

        i0=0
        i1=0
        j0=0
        j1=0
        for i in range(5):
            row=key_matrix[i]
            if(pair[0] in row):
                i0=i
                j0=row.find(pair[0])
            if(pair[1] in row):
                i1=i
                j1=row.find(pair[1])
        cipher_text_pair=key_matrix[i0][j1]+key_matrix[i1][j0]      # the coordinate
        cipher_text_pairs.append(cipher_text_pair)
    return "".join(cipher_text_pairs)

def playfair_Decryption(plain_text):
    plain_text_pairs=[]
    cipher_text_pairs=[]
    plain_text=plain_text.replace(" ","")
    plain_text=plain_text.lower()
    i=0
    while i<len(plain_text):                           # this block for preparing the plain text and divide it in pairs
        a=plain_text[i]
        b=''
        if((i+1)==len(plain_text)):                    # to add x at the end of the string if there is one letter left
            b='x'
        else:
            b=plain_text[i+1]
        if(a!=b):                                      # to chceck if the pairs are not the same 
            plain_text_pairs.append(a+b)
            i+=2
        else:
            plain_text_pairs.append(a+'x')
            i+=1                                       #  palin text = husseinadel
    print("plain text pairs: ",plain_text_pairs)       #  plain text pairs:  ['hu', 'sx', 'se', 'in', 'ad', 'el']

    for pair in plain_text_pairs:                      #  plain text pairs:  ['pa', 'sx', 'se', 'in', 'ad', 'el']
        flag=False
        for row in key_matrix:                         #  key_matrix = ['playf', 'irexb', 'cdghk', 'mnoqs', 'tuvwz']
            if(pair[0] in row and pair[1] in row):
                j0=row.find(pair[0])                   #  finding the index of the letters  
                j1=row.find(pair[1])
                cipher_text_pair=row[(j0+4)%5]+row[(j1+4)%5]
                cipher_text_pairs.append(cipher_text_pair)
                flag=True
        if flag:
            continue   

        for j in range(5):
            col="".join([key_matrix[i][j] for i in range(5)])       # to retrieve the coloums 
            if(pair[0] in col and pair[1] in col):                  # then the same thing as the row
                i0=col.find(pair[0])
                i1=col.find(pair[1])
                cipher_text_pair=col[(i0+4)%5]+col[(i1+4)%5]
                cipher_text_pairs.append(cipher_text_pair)
                flag=True
        if flag:
            continue

        i0=0
        i1=0
        j0=0
        j1=0
        for i in range(5):
            row=key_matrix[i]
            if(pair[0] in row):
                i0=i
                j0=row.find(pair[0])
            if(pair[1] in row):
                i1=i
                j1=row.find(pair[1])
        cipher_text_pair=key_matrix[i0][j1]+key_matrix[i1][j0]      # the coordinate
        cipher_text_pairs.append(cipher_text_pair)
    return "".join(cipher_text_pairs)




choose =int(input(colored("\n1- Encryption\n2- Decryption\n\nChoice '1' or '2': ", 'white')))
if choose ==1:
    plain_Text =str(input(colored("\nEnter Your Message That You Wanna encrypt :  " , 'green')))
    secret_Key= input(colored("Enter The Secret key : " , 'green'))
    key_matrix=key_generation(secret_Key)
    print(playfair_Encryption(plain_Text))

if choose ==2:
    plain_Text =str(input(colored("\nEnter Your Message That You Wanna decrypt :  " , 'green')))
    secret_Key= input(colored("Enter The Secret key : " , 'green'))
    key_matrix=key_generation(secret_Key)
    print(playfair_Decryption(plain_Text))
#---------------------------------------------------------------------------------------
print (colored('\n\n\t\t\t\t  ----------','white'))
print(colored('\t\t\t\t    Done \U0001f600 ', 'yellow'))
print (colored('\t\t\t\t  ----------\n','white'))

