def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    word_list = phrase.split(' ')
    for word in word_list:
        #print(word)
        index = word_list.index(word)
        letter_list = []
        letter_list[:0] = word
        #print(letter_list)
        letter_list[0] = word[0].upper()
        #print(word[0].upper())
        for letter in letter_list[1:]:
            letter_index = letter_list.index(letter)
            letter_list[letter_index] = letter.lower()
        
        word = ''.join(letter_list)
        
        word_list[index] = word
        
    return ' '.join(word_list)
#titleize('this is awesome')