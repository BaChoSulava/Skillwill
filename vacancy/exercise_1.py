#given words
while True:
    inputed_integer = int(input("Enter integer: "))
    if 1 <= inputed_integer <= 10**5:
        # print("the number is in the limit")
        break
    else:
        print("inputed number exceeds our limit")

list_of_words = []

while True:
    #input words
    for i in range(inputed_integer):
        inputed_word = input(f"inpt word {i+1} time: ").lower()    #ჩაამატე th მერამდენე რომ გამოვიდეს
        list_of_words.append(inputed_word)
    
    #do not exceed 10^6 
    sum_of_lengths = 0
    for word in inputed_word:
        sum_of_lengths += len(word)
    if sum_of_lengths < 10**6:
        # print("the words length are fine!")
        break
    else:
        print("The sum of the lengths of all the words do  exceed 10^6, so enter shorter words!")

#number of occurrences
dict_of_words = {}
for word in list_of_words:
    if word in dict_of_words:
        dict_of_words[word] += 1
    else:
        dict_of_words[word] = 1 

# I line output
print(len(dict_of_words)) 

# II line output
dict_of_words = dict(sorted(dict_of_words.items(), key=lambda item: -item[1]))
for word in dict_of_words:
    print(dict_of_words[word], end=" ")



