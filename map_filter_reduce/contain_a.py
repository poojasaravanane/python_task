# filter the string which contain a
words = ["apple", "sky", "blue", "cat", "dog", "tree"]
word = list(filter(lambda w: 'a'in w, words))
print(word) 
