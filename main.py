import json
import os

play = True


def main():
    if os.path.exists('data.json'):
        with open('data.json','r') as data_file:
            word_dict = json.load(data_file)

    else:
        word_dict ={}

    while True:
        user_word = input('Create a word (or type "stop" to exit): ')
        if user_word.lower() == 'stop':
            break

        user_meaning = input("Tell us its meaning: ")
        word_dict[user_word] = user_meaning

        #save current data to  our file
        with open('data.json', 'w') as data_file:
            json.dump(word_dict, data_file, indent=4)

def search():


    with open('data.json','r') as file:
        data = json.load(file)

    #Ask user for the word:
    words_to_search = input('What word would you like to search?:')
    if words_to_search in data:
        print(f"{words_to_search} : {data[words_to_search]}")
    else:
        print('The given word is not in your dictionary. Go ahead and create it')

def start():
    global play
    starting_question = input('What would you like to do?: Create or Search:').lower()
    if starting_question == 'create':
        main()
    elif starting_question == 'search':
        search()
    elif starting_question =='stop':
        play = False
    else:
        print('please type in correct option')

while play:
 start()