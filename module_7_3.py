all_words = dict()
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        punctuation_marks = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                single_string = f.read()
                for marks in punctuation_marks:
                    single_string = single_string.replace(marks, '')
        key = file_name
        value = single_string.lower().split()
        all_words[key] = value
        return all_words

    def find(self, word):
        self.word = word
        word_find = dict()
        for file_name in self.file_names:
            words_list = all_words.get(file_name)
            my_word = word.lower()
            words_count = words_list.index(my_word) + 1
            key = file_name
            value = words_count
            word_find[key] = value
            return word_find

    def count(self, word):
        self.word = word
        word_count_dic = dict()
        for file_name in self.file_names:
            words_list = all_words.get(file_name)
            my_word = word.lower()
            word_count = words_list.count(my_word)
            key = file_name
            value = word_count
            word_count_dic[key] = value
            print(word_count_dic)


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
(finder2.count('teXT'))  # 4 слова teXT в тексте всего
