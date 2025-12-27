'''
To search for a patten in a some text
'''

import re

search_word_1 = "apple are more intersting than banana differet types of apples are"
search_word_2 = "A Apple Aman Aelm "
search_word_3 = "  Python"

pattern_1= 'apples'
pattern_2= 'contact'
pattern_3= 'mohamed'

print(re.search(pattern_1,search_word_1).group())
x = re.search('m', search_word_2)
print(x.start())

new_word=search_word_3.strip()
print(new_word)


package_waight=str("100")
new_weight=float(package_waight)
print("The Original weight was:", package_waight)
print("The new package weight is: ", float(new_weight))
print(type(new_weight))
print(type(package_waight))


package_waight=str("100")
type(package_waight)
new_weight=float(package_waight)
print(new_weight, type(new_weight))
print(package_waight, type(package_waight))
