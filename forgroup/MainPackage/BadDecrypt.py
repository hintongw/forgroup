#Name:Team Jared Butler                                                   #
#email: halverhc@mail.uc.edu, hintongw@mail.uc.edu,Stewasu@mail.Uc.edu    #                                          #
#Assignment Title: Final Assignment                                       #
#Course: IS 4010                                                          #
#Semester/Year: Spring 2023                                               #
#Brief Description: Old version of decryption method                      #
#                                                                         #
#Anything else that's relevant: no                                        #
#Citations:  GPT3                                                         #
###########################################################################

import json

# Function to decrypt the location data
def BADdecrypt_location():
    with open('EncryptedGroupHints Spring 2023 Section 002.json', 'r') as f:
        encrypted_data = json.load(f)

    # Get the encrypted string for Jared Butler
    encrypted_string = encrypted_data['Jared Butler']

    # Load the English words list
    with open('english.txt', 'r') as f:
        english_words = f.read().splitlines()

    # Convert each index to an integer and retrieve the corresponding English word
    decrypted_string = ''
    for index in encrypted_string:
        try:
            decrypted_string += english_words[int(index)]
        except IndexError:
            print(f'Error: Invalid index {index} in the encrypted data.')
            return None
        except ValueError:
            print(f'Error: Invalid index {index} in the encrypted data.')
            return None
    #print(f'The first attempt at the decrypted location was: {decrypted_string}')

    return ((f'Attempt 01 was: {decrypted_string}'))