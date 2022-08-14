import random


class HangMan:

    def __init__(self):
        self.tries = 6
        self.word = self.get_word()
        self.word_template = '_' * len(self.word)
        self.guessed_letters = []

    def start(self):
        print("Угадайте слово, прежде чем рисунок виселицы будет завершен!")
        print('----------------------------------')

        self.display_hangman(self.tries)
        print(self.word_template)
        self.get_guess()

        print('До новых встреч!')

    def get_template(self):
        word_template = ''
        for i in self.word:
            if i in self.guessed_letters:
                word_template += i
            else:
                word_template += '_'
        return word_template

    def get_guess(self):
        while self.tries > 0:
            print("Введите букву или слово!")
            letter = input().upper()

            if len(letter) == 1:
                if letter in self.word:
                    print('Вы угадали букву:')
                    self.guessed_letters.append(letter)
                    word_template = self.get_template()
                    print(word_template)
                    if '_' not in word_template:
                        print("Ура! Вы выиграли!")
                        break
                else:
                    print('Вы не угадали букву!')
                    self.tries -= 1
                    self.display_hangman(self.tries)
            elif self.word == letter:
                print("Вы угадали слово и выиграли!")
                break
            else:
                self.tries -= 1
                print("Вы не угадали слово!")

        if self.tries == 0:
            print(f"Вы проиграли, слово было {self.word}.")

    @staticmethod
    def get_word():
        words_list = ['человек', 'работа', 'вопрос', 'сторона', 'страна', 'случай', 'голова',
                      'ребенок', 'система', 'отношение', 'женщина', 'деньги', 'машина', 'проблема',
                      'решение', 'история', 'власть', 'тысяча', 'возможность', 'результат',
                      'область', 'статья', 'компания', 'группа', 'развитие', 'процесс', 'условие',
                      'средство', 'начало', 'уровень', 'минута', 'качество', 'дорога', 'действие',
                      'государство', 'любовь', 'взгляд', 'общество', 'деятельность', 'организация',
                      'президент', 'комната', 'порядок', 'момент', 'письмо', 'помощь', 'ситуация',
                      'состояние', 'квартира', 'внимание', 'смерть', 'программа', 'задача',
                      'предприятие', 'разговор', 'правительство', 'производство', 'информация',
                      'положение', 'интерес', 'федерация', 'правило', 'управление', 'мужчина',
                      'партия', 'сердце', 'движение', 'материал', 'неделя', 'чувство', 'газета',
                      'причина', 'основа', 'товарищ', 'культура', 'данные', 'мнение', 'документ',
                      'институт', 'проект', 'встреча', 'директор', 'служба', 'судьба', 'девушка',
                      'очередь', 'состав', 'количество', 'событие', 'объект', 'создание', 'значение',
                      'период', 'искусство', 'структура', 'пример', 'исследование', 'гражданин',
                      'начальник', 'принцип', 'воздух', 'характер', 'борьба', 'использование',
                      'размер', 'образование', 'мальчик', 'представитель', 'участие', 'девочка',
                      'политика', 'картина', 'доллар', 'территория', 'изменение', 'направление',
                      'рисунок', 'течение', 'церковь', 'население', 'большинство', 'музыка',
                      'правда', 'свобода', 'память', 'команда', 'договор', 'дерево', 'хозяин',
                      'природа', 'телефон', 'позиция', 'писатель', 'самолет', 'солнце', 'спектакль',
                      'способ', 'журнал', 'руководитель', 'специалист', 'оценка', 'регион', 'процент',
                      'родитель', 'требование', 'основание', 'половина', 'анализ', 'автомобиль',
                      'экономика', 'литература', 'бумага', 'степень', 'господин', 'надежда',
                      'предмет', 'руководство', 'площадь', 'режиссер', 'поверхность', 'ощущение',
                      'станция', 'революция', 'колено', 'министерство', 'стекло']
        return random.choice(words_list).upper()

    @staticmethod
    def display_hangman(tries):
        stages = [
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            ''',
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            ''',
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            ''',
            '''
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            ''',
            '''
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            ''',
            '''
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            ''',
            '''
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            '''
        ]
        print(stages[tries])


game = HangMan()
game.start()

