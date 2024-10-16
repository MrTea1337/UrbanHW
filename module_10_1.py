from time import sleep
from datetime import datetime
from threading import Thread

start_time = datetime.now()


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding="UTF-8") as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i} \n")
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = datetime.now()
print(end_time - start_time)

start_time = datetime.now()
func5 = Thread(target=write_words, args=(10, 'example5.txt'))
func6 = Thread(target=write_words, args=(30, 'example6.txt'))
func7 = Thread(target=write_words, args=(200, 'example7.txt'))
func8 = Thread(target=write_words, args=(100, 'example8.txt'))

func5.start()
func6.start()
func7.start()
func8.start()

func5.join()
func6.join()
func7.join()
func8.join()

end_time = datetime.now()
print(end_time - start_time)


