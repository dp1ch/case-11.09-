"""Case-study "Dictionaries"
Developers:
 Pichuev Denis - 51%   
 Dyakovich Alexander - 60%
 Trushkin Nikita - 20%
"""
import json
def save_tree(tree_elem):
    #загрузка json  из файла
    with open("tree_file.json", "w") as tree_file:
        json.dump(tree_elem, tree_file)
    return 1


def add_leaf(i):
    print("Сдаюсь,что это?")
    new_leaf = input().lower()
    while new_leaf + '?' in tree:
        print('Такой вариант ответа уже есть') # Такой лист уже есть в словаре
        new_leaf = input("Что это?").lower() 
    print("Каким вопросом ответ: ", '"', i[:-1], '"' " отделить от ответа: ", '"', new_leaf, '"', "?", sep='')
    new_quest = input().lower()
    if "?" not in new_quest:
      new_quest+="?"
    while new_quest in tree:
        print('Такой вопрос уже есть') #  такой ключ уже есть в словаре
        new_quest = input("Введите новый вопрос ").lower()
    for elem in tree.keys():
      #находим ключ предка - меняем значение на новый вопрос пользователя
      if tree[elem]["нет"]==i:
        tree[elem]["нет"] = new_quest
      if tree[elem]["да"]==i:
        tree[elem]["да"] = new_quest
      #добавляем новые листья без потомков, новый вопрос указывает на листья
    tree[new_quest] = {"да": new_leaf+"?", "нет":i}
    tree[new_leaf+"?"] = {"да":False,"нет":False}
    tree[i] = {"да":False,"нет":False}
    return 1

def run_tree(i="живое?"):
    if not (tree[i]["да"] or tree[i]["нет"]): # если мы предполагаем ответ
        print("Вы загадали:", i)
        ans = input().lower()
        while ans not in ("да", "нет"): # проверка на неправильность ввода
            ans = input().lower()
        if ans.lower() == "да":
            print("Победа!")
            end_game()
            return 1
        else:
            add_leaf(i) # если ответ неверный идем в добавление вопросов и ответов
            end_game() #предлагаем пользователю завершить игру или сыграть ещё раз
            return tree
    print("Вопрос: ",i)
    resp = input().lower()
    while resp not in ("да", "нет"):
        print("Ой, вы видимо промахнулись, попробуйте ввести ваш ответ еще раз")
        print("Вопрос: ",i)
        resp = input().lower()
    #повторяем, пока пользователь не даст подходящий ответ и переходим к потомку
    if resp == "да":
        return run_tree(tree[i]["да"])
    else:
        return run_tree(tree[i]["нет"])
def init():
    global tree # делаем глобальной
    with open("tree_file.json", "r") as tree_file:
        tree = json.load(tree_file)
    return 1

def end_game():
    print("Если вы хотите сыграть еще раз нажмите 1", "Для выхода из игры нажмите 2," , "Для вывода дерева и выхода из игры нажмите 3", sep="\n")
    game = input()
    while game not in ("1", "2", "3"):
        print("Ой, вы видимо промахнулись, попробуйте ввести цифру еще раз")
        game = input()
    while game in ("1", "2", "3"):
        if game == "1":
          save_tree(tree)  
          main()
          return 0
        if game == "3":
          q=0
          for a in tree.items():
            q+=1
            print(q,":",a[:-1])
          print("Игра окончена, до новых встреч!")
          save_tree(tree)
          return 0
        else:
            print("Игра окончена, до новых встреч!")
            save_tree(tree)
            return 0
      
def main():
  init() # Загрузка json  файла
  run_tree()  # Старт

main()#Старт игры
