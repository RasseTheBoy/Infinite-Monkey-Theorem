import threading
from datetime   import timedelta
from string     import ascii_lowercase
from random     import choice
from time   import time

# ------------------------------------------------------------

class Monkey:
    def __init__(self, name='Mike'):
        self.name = name

    def find_sentence(self, sentence):
        self.start_time = time()
        self.sentence = sentence.lower()
        self.sentence_len = len(sentence)
        self.generated_sentence_amnt = 0

        while True:
            self.generated_sentence_amnt += 1
            self.generated_sentence = ''
            for indx in range(self.sentence_len):
                generated_char = choice(ascii_char)
                if generated_char == self.sentence[indx]:
                    self.generated_sentence += generated_char
                else:
                    break

            if self.generated_sentence == self.sentence:
                self.end_time = time()
                self.elapsed_time = timedelta(seconds=self.end_time-self.start_time)
                break

        fprint(
f'''Name: {self.name}
Generated sentence: {self.generated_sentence}
Generated amount: {add_space_for_int(self.generated_sentence_amnt)}
Elapsed time: {self.elapsed_time}
'''
        )

# ------------------------------------------------------------

def fprint(text):
    print(f'{text}\n')

def get_input(text, typ=str):
    while True:
        inpt = input(text); print()
        try:
            return typ(inpt)
        except:
            print('Invalid input!')
            fprint('Input needs to be: ' + str(typ).split('\'')[1])

def add_space_for_int(i):
    i = ''.join([x+' ' if (indx+1)%3 == 0 else x for indx, x in enumerate(str(i)[::-1])])[::-1]
    if i[0] == ' ':
        i = ''.join(list(i)[1:])
    return i

# ------------------------------------------------------------

def get_monkey_names():
    with open('monkey_names.txt', 'r') as f:
        lines = list(filter(None, (line.rstrip() for line in f)))
    return lines

# ------------------------------------------------------------

def main():
    fprint('---Infinite Monkey Theorem---')

    monkey_nam_lst = get_monkey_names()
    if not monkey_nam_lst:
        monkey_nam_lst = [f'Mike {x}' for x in range(get_input('Amount of monkeys: ', int))]

    monkey_lst = [Monkey(monkey_nam_lst[x]) for x in range(len(monkey_nam_lst))]

    fprint('- Don\'t use numbers in the sentence -')
    sentence = get_input('Sentence to find: ', str)
    print("Fun fact: The posibility to find your unique string is approximately 1/" +  add_space_for_int(len(ascii_char)**len(sentence)) + '\n')

    thread_lst = [ threading.Thread(target=monkey.find_sentence, args=(sentence,)) for monkey in monkey_lst]
    for th in thread_lst:
        th.start()

# ------------------------------------------------------------

if __name__ == '__main__':
    ascii_char = [x for x in ascii_lowercase + 'åäö ']
    main()
