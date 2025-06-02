#Write a Python program to count the occurrences of each word in a given sentence.
 
def count_words(sentence):
    words = sentence.lower().split()

    word_count ={}
    for word in words:
        word = word.strip("., 1?") 

        if word in word_count: 
            word_count[word] += 1 
        else: 
            word_count[word] = 1 
    return word_count 

sentence = input("Enter the sentence: ")
print(count_words(sentence))

# sentence = "Hello world! Hello everyone. This is a world of coding." 
# print(count_words(sentence))
