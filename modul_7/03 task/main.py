class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                content = file.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    content = content.replace(i, '')
                words = content.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        positions = {}
        for name, words in self.get_all_words().items():
            position = words.index(word) + 1
            positions[name] = position
        return positions

    def count(self, word):
        word = word.lower()
        counts = {}
        for name, words in self.get_all_words().items():
            coun = words.count(word)
            counts[name] = coun
        return counts



finder = WordsFinder('test_file.txt')
print(finder.get_all_words()) # Все слова
print(finder.find('TEXT')) # 3 слово по счёту
print(finder.count('teXT'))