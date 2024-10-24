def single_root_words(root_word, *other_words):
    same_words = []
    word = root_word.lower()
    for i in other_words:
        if i.lower() in word or word in i.lower():
            same_words.append(i)
    return same_words

result = single_root_words('air','airline', 'driver', 'airport', 'airmail', 'airdrop', 'hat' )
print(result)
words_ = ['airline', 'driver', 'airport', 'airmail', 'airdrop', 'hat']

single_root_words('air' ,*words_)



