import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')
pp_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    name = input('What is your name?').upper()
    try:
        phonetic_code = [pp_dict[letr] for letr in name]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic()
    else:
        print(phonetic_code)


generate_phonetic()
