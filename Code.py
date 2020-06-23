Words_to_Translate = input("Enter The text to Translate: ")
word_l = Words_to_Translate.split()
final = []

def Translated_Words(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        New_word = word[2::] + "x" + word[0:2] 
    else:
        New_word = word[2::] + "y" + word[0:2]
    return New_word

for word in word_l:
    new_Words = Translated_Words(word)
    #print(new_Words)
    final.append(new_Words)


output = " ".join(final)
print (output)
