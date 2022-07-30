import random
import copy
from PIL import Image, ImageFont, ImageDraw

portuguese_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y" ,"Z","Á","É","Í","Ó","Ú"]

columns_and_lines_quantity = 25
number_words = 15

pannel = [[0 for x in range(columns_and_lines_quantity)] for y in range(columns_and_lines_quantity)]
random_words = []

with open("words.txt", 'r') as word_list:
    word_list = word_list.read().splitlines()
    for i in range(number_words):
        random_words.append((random.choice(word_list).upper()))
    

def vertical_collision_detection(word,initial_x,initial_y):
    letter_index = 0
    collision_detected = False
    for i in range(initial_y,initial_y+len(word)):
        if (pannel[initial_x][i] != 0 and pannel[initial_x][i] != word[letter_index]):
            collision_detected = True
        letter_index+=1
    return collision_detected   

def horizontal_collision_detection(word,initial_x,initial_y):
    letter_index = 0
    collision_detected = False
    for i in range(initial_x,initial_x+len(word)):
            if (pannel[i][initial_y] != 0 and pannel[i][initial_y] != word[letter_index]):
                collision_detected = True
            letter_index+=1
    return collision_detected  

def word_placement(word):
    vertical_horizontal = ["v","h"]
    orientation = random.choice(vertical_horizontal)
    initial_x = 0
    initial_y = 0
    if (orientation == "v"):
        initial_x = random.randint(0,columns_and_lines_quantity - 1)
        initial_y = random.randint(0,columns_and_lines_quantity - len(word))
        letter_index = 0
        if (not vertical_collision_detection(word,initial_x,initial_y)):
            for i in range(initial_y,initial_y+len(word)):
                pannel[initial_x][i] = word[letter_index]
                letter_index+=1
        else:
            word_placement(word)

    elif (orientation == "h"):
        initial_x = random.randint(0,columns_and_lines_quantity - len(word))
        initial_y = random.randint(0,columns_and_lines_quantity - 1)
        letter_index = 0
        if (not horizontal_collision_detection(word,initial_x,initial_y)):
            for i in range(initial_x,initial_x+len(word)):
                pannel[i][initial_y] = word[letter_index]
                letter_index+=1
        else:
            word_placement(word)

    

for word in random_words:
    word_placement(word)

cheat_pannel = copy.deepcopy(pannel)

for i in range(columns_and_lines_quantity):
    for j in range(columns_and_lines_quantity):
        if pannel[i][j] == 0:
            pannel[i][j] = random.choice(portuguese_alphabet)


with open("caca_palavras.txt", "w") as caca_palavras:
    for row in pannel:
        caca_palavras.write(' '.join([str(a) for a in row]) + '\n')

    caca_palavras.write("\n---PALAVRAS CHAVE----\n\n")
    caca_palavras.write(' '.join([str(a) for a in random_words]) + '\n')

    caca_palavras.write("\n----RESPOSTAS----\n\n")

    for row in cheat_pannel:
        caca_palavras.write(' '.join([str(a) for a in row]) + '\n')


filename = "caca_palavras.png"
fnt = ImageFont.truetype("consola.ttf",50, encoding="unic")
page_width = 2480
page_heigth = 1748
image = Image.new(mode = "RGB", size = (page_heigth,page_width ), color = "white")
draw = ImageDraw.Draw(image)
height_offset = 10
width_offset = (page_width/2) - 1000
draw.text((width_offset,height_offset),"Caça Palavras By Relâmpago Marquim", font=fnt, fill=(0,0,0))
height_offset += 100
for row in pannel:
    draw.text((width_offset,height_offset),' '.join([str(a) for a in row]), font=fnt, fill=(0,0,0))
    height_offset+=50

height_offset+=50

fnt = ImageFont.truetype("consola.ttf",40, encoding="unic")
for word in random_words:
    draw.text((width_offset,height_offset),word, font=fnt, fill=(0,0,0))
    height_offset+=40
height_offset+=50

fnt = ImageFont.truetype("consola.ttf",15, encoding="unic")

for row in cheat_pannel:
    row = ' '.join([str(a) for a in row]).replace("0", "-")
    draw.text((width_offset,height_offset),row, font=fnt, fill=(0,0,0))
    height_offset+=15

image.save(filename)

