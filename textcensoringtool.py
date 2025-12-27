'''
to show how we can hide the text with astrix
'''

word_to_display=input("Please enter the text: \n")
censor_word=input("Please enter the word to sensor: \n")
print(censor_word)

censor_word_length=len(censor_word[6:100])
print(censor_word_length)
''' 
#below is to exclude the first character and add a star to the remining characters
censor_word=censor_word[0] + "*" * (len(censor_word) -1)
#print(censor_word)
#print("This is your new passowred:", word_to_display + censor_word)
print(censor_word)
# start_index= word_to_siaplay.find(censor_word)
# print(start_index)
'''