"""
Yay, someone found this easter egg. Gratz!

NOTE: there is no flag here,
      but you can ask the organizer of this challenge
      for a shot of vodka [if its still there!] ;)

          .?77777777777777$.
          777..777777777777$+
         .77    7777777777$$$
         .777 .7777777777$$$$
         .7777777777777$$$$$$
         ..........:77$$$$$$$
  .77777777777777777$$$$$$$$$.=======.
 777777777777777777$$$$$$$$$$.========
7777777777777777$$$$$$$$$$$$$.=========
77777777777777$$$$$$$$$$$$$$$.=========
777777777777$$$$$$$$$$$$$$$$ :========+.
77777777777$$$$$$$$$$$$$$+..=========++~
777777777$$..~=====================+++++
77777777$~.~~~~=~=================+++++.
777777$$$.~~~===================+++++++.
77777$$$$.~~==================++++++++:
 7$$$$$$$.==================++++++++++.
 .,$$$$$$.================++++++++++~.
         .=========~.........
         .=============++++++
         .===========+++..+++
         .==========+++.  .++
          ,=======++++++,,++,
          ..=====+++++++++=.
   __________        __  __                   _         ________  ___   __
  / ____/ __ \__  __/ /_/ /_  ____  ____     (_)____   / ____/ / / / | / /
 / /   / /_/ / / / / __/ __ \/ __ \/ __ \   / / ___/  / /_  / / / /  |/ /
/ /___/ ____/ /_/ / /_/ / / / /_/ / / / /  / (__  )  / __/ / /_/ / /|  /
\____/_/    \__, /\__/_/ /_/\____/_/ /_/  /_/____/  /_/    \____/_/ |_/
           /____/


>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

import os
import sys

print('~~ May the Witchers be with you. Always.')

started = False
filtered = False

with open(__file__) as f:
    print('~'*30)
    for line in f:
        if 'import os' in line:
            started = True
        elif not started:
            continue

        if line == '#end-of-filter\n':
            filtered = False

        elif filtered:
            continue

        print(line, end='')
        if 'class Challenge:\n' in line:
            filtered = True
            print('# [ filtered ]')
    print('~'*30)

def disconnect_code():
    print(
        'I am closin\' the', __file__, 'file so it aint too eazy; you know, for your own fun.\n'
    )
    os.close(100)


LOL_NO = "I won't give you flag like this"
LOL_MEH = "Meh, you need a bit more here"

print("Flags have a format of FLAG{[A-Za-z0-9_]+}")

class Challenge:
    def first_level(self):
        return 'That was just a begining. First flag: FLAG{easy_peasy_lemon_squeezy}'

    def second_level(self):
        raise Exception(LOL_NO)

        def a():
            """
            Never gonna give you up
            Never gonna let you down
            Never gonna run around and desert you
            Never gonna make you cry
            Never gonna say goodbye
            Never gonna tell a lie and hurt you
            """
        def b():
            """
            Never gonna give you up
            Never gonna let you down
            Never gonna run around and desert you
            Never gonna make you cry
            Never gonna say goodbye
            Never gonna tell a lie and hurt you
            """
        def c():
            """
            Never gonna give you up
            Never gonna let you down
            Never gonna run around and desert you
            Never gonna make you cry
            Never gonna say goodbye
            Never gonna tell a lie and hurt you
            """
        def d():
            """
            Never gonna give you up
            Never gonna let you down
            Never gonna run around and desert you
            Never gonna make you cry
            Never gonna say goodbye
            Never gonna tell a lie and hurt you
            """
            def e():
                return 'Lets play moar =). Second flag: FLAG{this_was_also_easy}'
        def f():
            """
            Never gonna give you up
            Never gonna let you down
            Never gonna run around and desert you
            Never gonna make you cry
            Never gonna say goodbye
            Never gonna tell a lie and hurt you
            """

        return LOL_MEH

    def third_level(self):
        raise Exception(LOL_NO)
        
        key = [3, 1, 3, 3, 7]
        ciphertext = '^DGMH[t@Or]CH]r^JZvEHYM'

        flag = ''.join(chr(ord(ciphertext[i]) ^ key[i%len(key)] ^ 42) for i in range(len(ciphertext)))

        return 'This could be deducted... MOOAAR. Third flag: FLAG{%s}' % flag

#end-of-filter


def run():
    assert __file__ == '/proc/self/fd/100'  # Disconnect3d's magic

    disconnect_code()

    print('\n\n\nOkay. Now you can show off your skills. gl hf')

    while True:
        msg = input('msg: ')[:300]  # you don't need that many, but feel free...

        print(eval(msg))            # YOLO. gl hf


if __name__ == '__main__':
    run()

