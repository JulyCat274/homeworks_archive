all_words = dict()

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        punctuation_marks = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                for line in f:
                    for marks in punctuation_marks:
                        line = line.replace(marks, '')
                    key = file_name
                    value = line.lower().split()
                    all_words[key] = value
                    print(all_words)


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
#print(finder2.find('TEXT')) # 3 слово по счёту
#(finder2.count('teXT')) # 4 слова teXT в тексте всего



#{'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}
