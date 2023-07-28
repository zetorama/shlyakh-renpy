# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define Cap = Character("Star Captain")
define Wiz = Character(_("Wizard of Centaurus"), color = '#07a2f5')
define Grd = Character("Guardian", color = '#fff200')
# define Prc = Character("Princess")
define Zkp = Character("Zookeeper", color = '#0b3b85')

# Variables
define planet = ''
define childhood_acc = 0
define has_dog = False

# Terms
define darkness = '{size=+5}{color=#700}darkness{/color}{/size}'

# Custom Transitions
define quickfade = Fade(0.2, 0.0, 0.2)
define lightning = Fade(0.2, 0.1, 0.1, color = '#a99')

# The game starts here.

label start:

    "Hey kid, look what i've got for you…"
    "Imagine if that's a helmet of famous space hero. Who flies on his ship among stars and planets of Milky Way."

    menu:
        "On a space ship?":
            scene bg ship-int with quickfade
            "Yes! On his space ship!"
        "What's his name?":
            "Star Captain."
            scene bg ship-int with quickfade

    show wizard signal-bad at right with easeinbottom

    "(over radio)" "Star Captain!… pssht…"

    show wizard signal-clear at right with dissolve

    Wiz "Pssht… Star Captain, this is Supreme Wizard calling you from our Centaurus system. Which planet are you traveling to?"

    menu:
        "Planet Alpha":
            $ planet = 'Alpha'
        "Planet Beta":
            $ planet = 'Beta'
        "Planet Gamma":
            $ planet = 'Gamma'

    Wiz "Great! See you on [planet], where i'll be waiting together with Princess and planet’s Guardian. \nHave a smooth flight and a hyper-sleep. Good night, Star Captain."

    show guardian signal-clear at center with easeinbottom

    Grd "Good night, sweetheart."

    jump catalyst

label catalyst:
    scene black with pixellate

    "And so Star Captain went to planet [planet] of Centaurus system. His hyper-sleep was smooth, but landing was not…"

    scene bg ship-landed with hpunch

    # $ renpy.pause(1.0)

    "Star Captain was still in his hyper-sleep, when space ship almost crushed at the cosmoport. Nobody expected to see Captain that early, except just one person."

    show guardian default with moveinright

    Grd "Captain, this is Guardian. Please respond!"

    menu:
        "This is Star Captain. What’s happened?":
            $ childhood_acc += 1
        "Please, five minutes more.":
            show bg ship-landed with vpunch

    Grd "There's no time, Captain! Something bad happened to our planet."
    Grd "Evil mage has summoned an illness on our lands. That’s why skies are red and everyone under it is in danger. \nPrincess needs your help, Captain!"

    menu:
        "I’ll beat the evil mage!":
            $ childhood_acc -= 1
        "I’ll save the princess!":
            $ childhood_acc += 1

    Grd "Of course, sweetheart. We are lucky that you're with us. \nI wish Supreme Wizard was here too, but he left early to protect city from the illness."
    Grd "We should take the ship and go to a safer place. I can bring fuel, and you, Captain, need to keep Princess safe. It won't take long."

    show princess default at right with moveinright
    hide guardian with dissolve

    "Guardian gave a signal, and Princess came out from behind her. Then she boarded a real space ship for the first time in her life. \nBut she was not excited. She was scared."

    scene bg ship-landed with fade

    "Some time has passed. Thick red clouds were getting closer and closer. Everything under was eaten by [darkness]."
    "Suddenly, lightning stroke from the skies. It turned out there was a huge shadow standing just behind the ship."

    show dog shadowed with lightning

    "Shadow" "Agrhh…"

    menu:
        "Hello [planet] creature, my name is Star Captain. What is your name?":
            $ childhood_acc += 1
            jump meet_dog
        "* Shoot at creature with sound blast gun. *":
            $ childhood_acc -= 1
            jump lose_dog

    label meet_dog:
        show dog shadowed at left with move

        "Captain slowly stepped towards shadow and got surprised to notice how it started wiggling with his two tails."

        show dog default with dissolve

        "\"So you must be a good boy\", thought Captain and offered a snack to this creature."

        show guardian default at right with moveinright

        Grd "Looks like you have found a new friend, Captain! \nLet's bring him on the ship with us and get out of here."

        $ has_dog = True

        show dog default at offscreenleft
        show guardian default at center
        with move

        jump catalyst_end

    label lose_dog:
        show dog shadowed with vpunch
        show dog default at right with move
        show dog shadowed at offscreenleft with move

        "Sound has blasted from the ship breaking silence like shattering glass. Out of shock creature has jumped back and immediately retired. Princess started crying."

        show guardian default at center with moveinright

        Grd "It's all good, Princess. Guardian is here! \nCaptain, that was… let's just get out of here."

        jump catalyst_end

    label catalyst_end:
        Grd "We should fly low at the ground to get to a safe place as soon as possible. I know where to go, so let me drive."
        jump break_into_two

label break_into_two:
    scene black with wipeleft
    "Act II"