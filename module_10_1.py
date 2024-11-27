import threading
import time
from time import sleep

def write_words(word_cpunt, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for word in range(1, word_cpunt + 1):
            f.write(f'Какое-то слово № {word}\n')
            time.sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')

started_module1 = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_module1 = time.time()
difference1 = end_module1 - started_module1
print(f'Работа потоков {difference1}')

started_module2 = time.time()
thread5 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread6 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread7 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread8 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread5.join()
thread6.join()
thread7.join()
thread8.join()
end_module2 = time.time()
difference2 = end_module2 - started_module2
print(f'Работа потоков {difference2}')