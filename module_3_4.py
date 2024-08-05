def single_root_words(root_word, *other_words):
    same_words = []
    result2 = same_words

    for item in other_words:
        if root_word.lower() in item.lower():
            same_words.append(item)

    for item in other_words:
        if item.lower() in root_word.lower():
            same_words.append(item)
    return result2

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)



