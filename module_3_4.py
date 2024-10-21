def single_root_words(root_word, *other_words):
    same_words = []
    for i  in range(len(other_words)):
        if i in root_word:
            same_words.append(i)
    print(same_words)


other_words_1 = ['airline', 'driver', 'airport', 'airmail', 'airdrop', 'hat']
single_root_words(*other_words_1, root_word = 'air')