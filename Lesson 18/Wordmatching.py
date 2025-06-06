def word_match(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("list of words with the same first and last letters", lst)
    return ctr
count = word_match(['abc' , 'cfc' , 'aba' , 'xyz' , '1221'])
print("Number of words having same first and last letter:" , count)