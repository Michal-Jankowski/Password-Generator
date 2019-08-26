import string
import secrets
import re
import csv
import unicodedata
from tkinter import *
from tkinter.ttk import *


# POLISH CHARACTERS INTO ENGLISH
# LOOKUP AND NAME RECOGNIZE IF IT IS ASCII OR UNICODE
# CHECKS ONLY CHARS
def normalize_char(c):
    try:
        cname = unicodedata.name(c)
        cname = cname[:cname.index(' WITH')]
        return unicodedata.lookup(cname)
    except (ValueError, KeyError):
        return c


# CONCATENATING CHARS INTO WORDS
# CREATING ONE SIMPLE LIST
def normalize(s):
    return ''.join(normalize_char(c) for c in s)


# READING FROM DATABASE POLISH WORDS AND NORMALIZING THEM
def File_Swears_Read(name):
    with open(name + '.csv', newline='', encoding='utf-8') as csvfile:
        readCSV = csv.reader(csvfile)
        for x in readCSV:
            converted_list = ','.join(map(str, x))
    normalized_list = normalize(converted_list)
    return normalized_list


# GENERATE RANDOM PASSWORD
def passwordfunc(size, word):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    size = size
    test = ''.join(secrets.choice(chars) for _ in range(size))

    if (secrets.randbelow(2)) == 0:
        output = test + word
    else:
        output = word + test
    return output


# CHECKING PASSWORD STRENGTH
def password_strength(password):
    """
    Check strenght of the 'password'
    A password is considered strong if:

    8 characters length or more
    1 digir or more
    1 symbol or more
    1 uppercase letter or more
    1 lowercase or more
    """
    # calculating the length
    length_error = len(password) < 8
    # searching for digits
    digit_error = re.search(r"\W", password) is None
    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None
    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None
    # searching for symbols
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password) is None
    # overall result
    password_high_strength = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)
    # missing length
    password_length_ok = not length_error
    # missing digits
    password_digits_ok = not digit_error
    # missing uppercase
    password_uppercase_ok = not uppercase_error
    # missing lowercase
    password_lowercase_ok = not lowercase_error
    # missing symbols
    password_symbol_ok = not symbol_error
    # medium password
    password_medium_strength = not password_high_strength and ((password_length_ok and password_digits_ok)
                                                               or (password_length_ok and password_symbol_ok))
    # weak password
    password_weak_strength = not (bool(password_high_strength) ^ bool(password_medium_strength))
    return {
        'PASSWORD_HIGH': password_high_strength,
        'PASSWORD_MEDIUM': password_medium_strength,
        'PASSWORD_WEAK': password_weak_strength,
        'password_length_ok': password_length_ok,
        'password_uppercase_ok': password_uppercase_ok,
        'password_lowercase_ok': password_lowercase_ok,
        'password_digits_ok': password_digits_ok,
        'password_symbol_ok': password_symbol_ok,
        'length_error': length_error,
        'digit_error': digit_error,
        'uppercase_error': uppercase_error,
        'lowercase_error': lowercase_error,
        'symbol_error': symbol_error,

    }


# GENERATE RANDOM POLISH WORD
def Generaterandompolishword(dupa):
    splited_string = dupa.split(',')
    splited_random_string = secrets.choice(splited_string)
    return splited_random_string


def PrintPassword():
    password_example = passwordfunc(8, Generaterandompolishword(dupa))
    # print(Generaterandompolishword(dupa))
    # print(password_strength((password_example_1)))
    # print(password_strength((password_example_1)))






dupa = File_Swears_Read('baza')

#print(password_example_1)
#print(password_strength((password_example_1)))



root = Tk()
root.title("Generuj Hasło!")
root.geometry('350x200')
welcome = Label(root, text="Witaj")
welcome.grid(column=1, row=0)

def clicked():
    password_example_1 = passwordfunc(8, Generaterandompolishword(dupa))
    welcome2 = "Wygenerowane hasło :  " + password_example_1
    welcome.configure(text=welcome2)
    w = Text(root, height=1, borderwidth=0)
    w.insert(1.0, passwordfunc(8, Generaterandompolishword(dupa)))
    w.configure(state="disabled")
    # if tkinter is 8.5 or above you'll want the selection background
    # to appear like it does when the widget is activated
    # comment this out for older versions of Tkinter
    w.configure(inactiveselectbackground=w.cget("selectbackground"))
    w.grid()


przycisk = Button(root, text="Naciśnij przycisk", command=clicked)
przycisk.grid(column=1, row=1)
root.mainloop()