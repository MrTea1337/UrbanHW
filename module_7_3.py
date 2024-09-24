class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, encoding="utf-8") as file:
                text = file.read().lower()
                for char in punctuation:
                    text = text.replace(char, "")
                all_words[file_name] = text.split()
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        find_words = {}
        for file in all_words:
            find_words[file] = all_words[file].index(word.lower()) + 1
        return find_words

    def count(self, word):
        all_words = self.get_all_words()
        find_words = {}
        for file in all_words:
            count = 0
            for item in all_words[file]:
                if item == word.lower():
                    count += 1
            find_words[file] = count
        return find_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
