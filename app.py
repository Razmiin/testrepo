sentence = "This is a common interview question"
sentence_lower = sentence.lower()
sentence_set = set(sentence.lower())
sentence_set.remove(' ')
print(sentence_set)
max = (0, 'a')
for word in sentence_set:
    if sentence_lower.count(word) > max[0]:
        max = (sentence_lower.count(word), word)
print(max)
