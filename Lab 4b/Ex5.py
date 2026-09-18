# Ask the user for a sentence using input ()
# Turn the sentence into a list of words using the split() method
# Reverse the list
# Join the reversed list back into a sentence using the join() method

sentence = input("Enter a sentence: ")
words = sentence.split()
words.reverse()
reversed_sentence = " ".join(words)
print("Reversed sentence:", reversed_sentence)

joined_sentence = sentence + " " + reversed_sentence
print("Joined sentence:", joined_sentence)


