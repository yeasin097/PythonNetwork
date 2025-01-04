def reverse_sentence(sentence):
    words = sentence.split()  # Split the sentence into words, ignoring extra spaces
    reversed_sentence = ' '.join(reversed(words))  # Reverse the list of words and join them with a single space
    return reversed_sentence

# Test the function
input_sentence = input("Input: ")
output_sentence = reverse_sentence(input_sentence)
print("Output: "+output_sentence)
