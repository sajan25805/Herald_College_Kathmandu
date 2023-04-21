with open('sajan.txt', 'r') as file:
    # Initialize variables for the longest, shortest and equal length words
    longest_word = ''
    shortest_word = ''
    equal_length_words = []

    # Loop through each line in the file
    for line in file:
        # Split the line into individual words
        words = line.split()
        print("line",line)

        print("words",words)

        # Loop through each word in the line
        for word in words:
            # Check if the word is longer than the current longest word
            if len(word) > len(longest_word):
                longest_word = word

            # Check if the word is shorter than the current shortest word or if it's the first word encountered
            if len(word) < len(shortest_word) or not shortest_word:
                shortest_word = word

            # Check if the word has the same length as the longest word
            if len(word) == len(longest_word) and word not in equal_length_words:
                equal_length_words.append(word)

    # Print the longest, shortest and equal length words
    print('Longest word:', longest_word)
    print('Shortest word:', shortest_word)
    if equal_length_words:
        print('Equal length words:', equal_length_words)
    else:
        print('No equal length words found.')