import pygame
import draw
import random
import cmpt120image


# img = cmpt120image.getImage('images/child.png')
###############################################################
# Keep this block at the beginning of your code. Do not modify.
def initEnv():
  print("\nWelcome! Before we start...")
  env = input(
    "Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
  while env not in "mri":
    print("Environment not recognized, type again.")
    env = input(
      "Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
  print("Great! Have fun!\n")
  return env


# Use the playSound() function below to play sounds.
# soundfilename does not include the .wav extension,
# e.g. playSound(apples,ENV) plays apples.wav
def playSound(soundfilename, env):
  if env == "m":
    exec("sounds." + soundfilename + ".play()")
  elif env == "r":
    from replit import audio
    audio.play_file("sounds/" + soundfilename + ".wav")
  elif env == "i":
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/" + soundfilename + ".wav")
    pygame.mixer.music.play()


ENV = initEnv()
##############################################################
global number
number = 3
file = open('blackfoot.csv')
wi = cmpt120image.getWhiteImage(400, 300)
pic = []
for line in file:
  pic.append(line.strip())


def Show_Menu():
  print('MAIN MENU')
  print('1. Learn - Word Flashcards')
  print('2. Play - Seek and Find Game')
  print('3. Settings - Change Difficulty')
  print('4. Exit')
  print('\n')
  choice = input('Choose an option: ')
  choice = choice.strip(',.?!: *')
  if choice == '1':
    Part_One()
  elif choice == '2':
    Part_Two()
  elif choice == '3':
    Part_Three()
  elif choice == '4':
    Part_Four()
  else:
    print("That is not an option please select another option" + '\n')
    Show_Menu()


def Part_One():
  print('\n' + 'LEARN' + '\n')
  for i in range(int(number)):
    wi = cmpt120image.getWhiteImage(400, 300)
    w = random.choice(range(1,300))
    h = random.choice(range(1,200))
    picture = cmpt120image.getImage('images/' + pic[i] + '.png')
    h = draw.drawItem(wi, picture, w, h)
    cmpt120image.showImage(h)
    playSound(pic[i], ENV)
    test = input(str(i + 1) + ". press enter to continue")

  print('\n')
  Show_Menu()

def Round():
  im = cmpt120image.getWhiteImage(400, 300)
  words = []

  if len(words) == 0:
    for u in range(number):
      words.append(pic[u])
    random.shuffle(words)

  word_dict = {}
  for i in range(3):
    n = random.choice(range(1, 4))
    q = random.choice(range(1,4))
    show_pic = cmpt120image.getImage('images/' + words[i] + '.png')
    draw.recolorImage(show_pic,[25,255,39])
    
    if q == 1:
      show_pic = draw.mirror(show_pic)
    if q == 2:
      show_pic = draw.minify(show_pic)
    if q == 3:
      show_pic = draw.minify(show_pic)
      show_pic = draw.mirror(show_pic)
      
    dist_item = draw.distributeItems(im, show_pic, n)
    cmpt120image.showImage(dist_item)
    word_dict[words[i]] = n
  random_sound = random.choice(range(0, 2))
  playSound(words[random_sound], ENV)
  newword = words[random_sound]
  global ans
  ans = word_dict[newword]
  dict.clear(word_dict)


def Part_Two():
  print('\n' + 'PLAY' + '\n')
  print(
    'This is a seek and find game. You will hear a word. Count how many of that word you find!'
    + '\n')
  how_many = input('How many rounds would you like to play: ')

  
  if how_many.isdigit():
    for i in range(int(how_many)):
      Round()
      user = input('Listen to the word, How many of that word can you find ')
      if int(user) == ans:
        print('correct!')
      else:
        print('sorry, wrong answer')
    Show_Menu()
  else:
    print('That is not a valid input please choose another option')
    Part_Two()
    


def Part_Three():
  global number
  print('You are currently learning ' + str(number) + ' words')
  word_num = input('How many words would you like to learn (3-12)? ')

  
  if int(word_num) in range(3,13):
    number = word_num
    Show_Menu()
  
  else:
    print('That is not a valid input, please choose a number between 3-12'+ '\n')
    Part_Three()
  

  
  

  Show_Menu()


def Part_Four():
  exit()


Show_Menu()
