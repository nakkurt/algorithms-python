# Write a function called char_freq_counter. This function takes in one parameter (a string)
 # and returns a dictionary with the keys being the letters and the values being the count of the letter.

def char_freq_counter(w):
    return {char:w.count(char) for char in w}

