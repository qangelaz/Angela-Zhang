

def explore():
    j = int(raw_input("You want to... \n1.Go into the cave \n2. Keep exploring in the forest"))
    if j == 1:
        raw_input("You decide to Go into the cave")
        raw_input("You decide to eat something first. Slowly, you move toward the steak on the table")
        raw_input("'WHO IS THAT' you hear a yelling by a man ")
        raw_input(' "I was missing in the forest, would you help me please?" ')
        raw_input("Fortunately, the man is willing to help.congratulation!! "
                  "You have go out of the forest, you are save!!")

    if j == 2:
        raw_input("You still want to explrore theforest")
        raw_input("unfortunately, you get lost in the forest, you are found died by a river 3 days later. GAME OVER")


def cave():
    e = int(raw_input("You want to do .... \n1. Eat first \n2.Leave a note first and leave the cave"))
    if e == 1:
        raw_input("You decide to eat something first. Slowly, you move toward the steak on the table")
        raw_input("'WHO IS THAT' you hear a yelling by a man ")
        raw_input(' "I was missing in the forest, would you help me please?" ')
        raw_input("Fortunately, the man is willing to help.congratulation!! "
                  "You have go out of the forest, you are save!!")


    if e == 2:
        raw_input("You decide to leave a note to your mom first.")
        raw_input("unfortunately, you get lost in the forest, you are found died by a river 3 days later. GAME OVER")



def stay():
    d = int(raw_input("What would you want to do? "
                      "\n1.choose to go into a cave to wait \n2. choose to explore the forest by yourself"))
    if d == 1:
        raw_input("You decide to go inside a cave that near you.")
        raw_input("Luckily,the cave is save enough for you to stay. "
                  "you find out that there maybe some people ince live here. "
                  "You notice that there is pen and paper for you to leave notes. "
                  "There are also a big piece of steak on the table that you can eat "
                  " What do you want to do first? ")
        cave()
    elif d == 2:
        raw_input("You decide to explore the forest by yourself.")
        raw_input("However, you feel very hungry suddenly, you notice that there is a cave that is near you, "
                  "the cave has a piece of meat inside. what do you want to do? ")
        explore()

def first_decision():
    c = int(raw_input("What do you want to do? "
                      "\n1.wait until there is a man come for help \n2. Try to get out by yourself"))
    if c == 1:
        raw_input("You decided to wait for  help .")
        raw_input("You sit down under a big tree ")
        raw_input("After 15 minutes, you find out there are only ants around you")
        raw_input("you are stilling waiting, but no one come...")
        stay()
    else:
        if c == 2:
            raw_input("You decided to get out by yourself.")
            raw_input("You find out that there is a route in thr forest that may help you")
            raw_input("You stand up and walk alone that route")
            raw_input("Congratulation! You become an independent person! "
                      "However, you soon discover that there is a tiger sleeping on that route.You can decide...")
            tiger()

def tiger():
    a = int(raw_input("you can  \n1.climb on a tree\n2.Still walk on that route, bur walk as quickly as possible"))
    if a == 1:
        raw_input("You look around, find our that there a tall tree for you to hide.")
        raw_input("you climb on a tree. After few minutes, the tiger leave. "
                  "You are free now and your adventure had begun! ")
        a_1()
    else:
        if a == 2:
            raw_input("you walk as quietly as you can..")
            raw_input("The tiger did not notice you, you continue walking on the route..")
            a_2()
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")


def a_1():
    raw_input("now you are in the right route.You saw a hungry dog is staring at you viciously. "
              "He opened his mouth, the saliva flow down from the tongue and dropped to the ground. ")
    b = int(raw_input("\n1.  climb toward him and have a fight \n2.run"))
    if b == 1:
        raw_input("you proved that you are a brave man! You run toward the dog and want to have a fight with the dog. "
                  "The dog is also very exciting with the fighting")
        b_1()
    else:
        if b == 2:
            raw_input(
                "You turn around as quick as you can, however, the dog is still chasing you..")
            b_2()
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")


def b_1():
    raw_input("You are going to make an very important decision. "
              "You are also trembling because the dog are barking at you ")
    j = int(raw_input("now you have two decision: "
                      "\n1. You can pretend you are die and wait till the dog ran away."
                      " \n2. You can bark back to the dog: 'go away!  ' "))
    if j == 1:
        raw_input("You stop moving and start controlling your breath rate. "
                  "You are so afraid the dog will come near you and step on you.")
        j_1()
    else:
        if j == 2:
            raw_input("The dog look at you like looking at a idiot. He do not even understand what you are saying. "
                      "How could a dog understand you.")
            j_2()
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")


def j_1():
    p = raw_input("you can now decided \n1. to peek and see how is going with the dog "
                  "\n. slowly moving yourself and tried to run away.")
    if p == 1:
        p_1()
    else:
        if p == 2:
            p_2()
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")


def p_1():
    raw_input("when you peek at to dog, the dog saw you. "
              "The dog understand that you are pretending you are died...THE END.")


def p_2():
    raw_input("THE END")


def j_2():
    raw_input("After you use all your braveness to yell out the words, you run toward the dog and give him a bite.")
    w = int(raw_input("you can decided \n1. climb on his back and tried to control him \n2.Yelled:'sit!!!'"))
    if w == 1:
        raw_input("you climb on his back, but the dog is so strong that he shake you off his back. then you died. "
                  "THE END.")
    else:
        if w == 2:
            raw_input("congratulation!! The dog has been trained before. The dog become very polite to you. "
                      "It helps you go out of the forest!! ")
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")


def b_2():
    raw_input("You turn around yourself and going to run away. "
              "You moved as fast as you can, and trying to escape from this scary scene.")
    qq = int(raw_input("you can decide \n1. Keep running until the dog is far away from you. \n2. hide into the forest"))
    if qq == 1:
        raw_input("you are running so slow that the dog can even win you by walking, and then you died. THE END.")

    else:
        if qq == 2:
            raw_input("The forest is a good place for you to hide! However, you miss your way in the forest.. THE END.")
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")


def a_2():
    raw_input("you are very happy and feel proud of yourself.Suddenly, you feel hungry, it is time to eat ")
    f = int(raw_input("you can decide "
                      "\n1. check if there is any snacks you may take with you"
                      " \n2. You can climb on the tall apple tree"))
    if f == 1:
        raw_input("Aha, you find out that there is a bar of chocolate inside you clothes."
                  " However, it is the only snacks that you have with you. I are hesitating about eat this or not.  ")
        f_1()
    else:
        if f == 2:
            raw_input("you climb on the tree and saw a big apple !!"
                      " You are so excited that you find something good to eat."
                      "But the apple is at the top of the tree, it is dangerous for you to climb higher. ")
            f_2()
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")


def f_1():
    raw_input("You are thinking about wherther to eat this or not, the chocolate bar looks very delicious")
    i = int(raw_input("you can choose to.. \n1. do not eat it \n2. eat!!"))
    if i == 1:
        i_1()
    else:
        if i == 2:
            i_2()
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")


def i_1():
    raw_input("You do not have any energy without eat the chocolate bar. "
              "The tiger comes back but you could not run away. THE END.")


def i_2():
    raw_input("congratulation!! You have enough energy to go out of the forest, you are save!! ")


def f_2():
    raw_input(
        "You start climbing up to reach the apple, suddenly, wind blows very hard are the whole tree is shaking.")
    u = int(raw_input("and now there are two choices: "
                      "\n1. continue to climb \n2. give up of climbing, you continue to walk on the route"))


    if u == 1:
        raw_input("The wind blows so hard that the tree is shaking. You are blew out of the high tree.. THE END.")

    else:
        if u == 2:
            raw_input("You do not have any energy without eat the chocolate bar. "
                      "The tiger comes back but you could not run away.THE END.")
        else:
            raw_input("Please type either 1 or 2, otherwise you will start from the top.")



def main():
    raw_input('*** BEFORE YOU START *** Please hit "ok" if there is text only.'
              ' Otherwise, enter a number when making your choices. ')
    raw_input("When you wake up, you find yourself alone in the forest you want to ... ")
    first_decision()

main()


