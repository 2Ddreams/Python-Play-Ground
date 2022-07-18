word_bank = ["apple", "orange", "banana", "cherry", "pear", "pineapple", "peach"]

prediction_dict = {}

word_input = input("Word: ")

word_index_counter = 0

input_index_counter = 0

prediction_points = 0



for i in range(len(word_bank)):
    for i in word_input.lower():
        print(i)
        if i in word_bank[word_index_counter]:
            prediction_points += 1
        word_bank_word = word_bank[word_index_counter]
        if word_input.lower() in word_bank_word.lower():
            prediction_points += 1
        for i in word_bank_word.lower():
            if word_bank_word[input_index_counter] == word_input[input_index_counter]:
                prediction_points +=1
                input_index_counter += 1
        prediction_dict[word_bank_word] = prediction_points
        prediction_points = 0
        input_index_counter = 0
    word_index_counter += 1

text_predicted = max(prediction_dict, key = prediction_dict.get)
print(prediction_dict)    
print(text_predicted)