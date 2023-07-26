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

# Custom Transitions
define quickfade = Fade(0.2, 0.0, 0.2)

# The game starts here.

label start:

    "Hey kid, look what i've got for you…"
    "Imagine if that's a helmet of famous space hero. Who flies on his ship among stars and planets of Milky Way."

    menu:
        "On a space ship?":
            scene bg ship-int with quickfade
            "Yes! On his space ship!"
        "What's his name?":
            scene bg ship-int with quickfade

    show wizard signal-bad at right with easeinbottom

    "(over radio)" "Star Captain!… pssht…"

    show wizard signal-clear at right with dissolve

    Wiz "Pssht… Star Captain, this is Supreme Wizard calling from Centaurus system. Which planet are you traveling to?"

    menu:
        "Planet Alpha":
            $ planet = 'Alpha'
        "Planet Beta":
            $ planet = 'Beta'
        "Planet Gamma":
            $ planet = 'Gamma'

    Wiz "Great! See you on [planet], where i'll be waiting together with Princess and our planet’s Guardian. \nHave a smooth flight and a hyper-sleep. Good night, Star Captain."

    show guardian signal-clear at center with easeinbottom

    Grd "Good night, sweetheart."

    jump catalyst

label catalyst:
    scene black with pixellate

    "And so Star Captain went to planet [planet] of Centaurus system. His hyper-sleep was smooth, but landing was not…"

    scene bg ship-landed with hpunch

    $ renpy.pause(1.0)

    show guardian default with ease

    Grd "Captain, this is Guardian. Please respond!"

    menu:
        "This is Star Captain. What’s happened?":
            $ childhood_acc += 1
        "Please, five minutes more.":
            show bg ship-landed with vpunch

    Grd "There's no time, Captain! Something bad happened to our planet."
    Grd "Evil mage has summoned bad illness on us. That’s why the skies are red. \nPrincess needs your help, Captain!"

    menu:
        "I’ll beat the evil mage!":
            $ childhood_acc -= 1
        "I’ll save the princess!":
            $ childhood_acc += 1

    Grd "Of course, sweetheart. Our Wizard is holding that illness from advancing, but we need to move quickly!"
    Grd "Unfortunately space ship is damaged, but it still can glide. \nI can refuel the ship, but you need to keep Princess safe."

    hide guardian with dissolve

    "Guardian went to pick up the fuel, leaving Princess with Captain. It's her first time on a real space ship, but she is not excited. She is scared."

    scene bg ship-landed with fade

    "Huge cloud is getting closer to cosmoport slowly, putting everything into {color=#a00}darkness{/color}."
    "Suddenly, lightning strikes from skies. It reveals a huge shadow that is standing just behind the ship."

    show dog default with quickfade

    "Shadow" "Agrhh…"

