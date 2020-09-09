import time
import pyautogui
import webbrowser


# Setting all the song notes as variables (So I don't need to write them every time)
sadThemeUp = '4-6-4-3      4-6-3-2   2-4-2-1      2-6-5   2-6-5   4-2 4-5-4-3 3-5-3-1 8-0-8-7+J'
despacito = '8   7   63  3333  6666  6564  4444 66667 8 5 5555 888 99 7  8 7 6 3'
fortniteDefault = '3 3 5 6 5    3 5 6 5 3 2 3 6 5 3 2 3'
ussr = '8      5 8    5 6 7   3 3 6   5 4 5   1 1   2    2 3 4    4 5 6    7 8 9  ' \
        '  5 5 0    9 8 9    5 5 8    7 6 7    3 3 6    5 4 5    1 1 8    7 6 5'
gravityFalls = '2346561 2343 5654 4446654 6665654 4446654 666 888 4446654'

# Intro
print('Hello, and welcome to Youtube Piano. Please use the number keys to select a song.')
time.sleep(0.5)
song = input('Would you like to play? You can play you can play we have '
             '1: Sad theme from up, 2: Despacito, \n3: Fortnite Default Dance, '
             '4: National Anthem of USSR, 5: Gravity Falls Theme, 6: Custom. ')


# Turns notes into keypress
def play(music):
    for x in music:
        if x == '-':
            time.sleep(0.1)

        elif x == '+':
            pass

        elif x == ' ':
            time.sleep(0.3)

        else:
            pyautogui.keyDown(x)
            time.sleep(0.05)
            pyautogui.keyUp(x)


# Opening the youtube video
if song != '6':
    webbrowser.open('https://www.youtube.com/watch?v=eQ-eE8Ai_8g&ab_channel=SethSandler')
    time.sleep(10)

# Plays the music
if song == '1':
    play(sadThemeUp)

elif song == '2':
    play(despacito)

elif song == '3':
    play(fortniteDefault)

elif song == '4':
    play(ussr)

elif song == '5':
    play(gravityFalls)

elif song == '6':
    print('To make a custom song, put in the numbers assigned to keys. '
          '\nAdding a space will wait .3 seconds. Adding a dash will wait .1 seconds.'
          '\nAdding a j will make the previous key sharp.')
    time.sleep(1)
    customSong = input('Please enter the keys to be played ')
    webbrowser.open('https://www.youtube.com/watch?v=eQ-eE8Ai_8g&ab_channel=SethSandler')
    time.sleep(10)
    play(customSong)
