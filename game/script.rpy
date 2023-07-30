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
define darkness = '{size=+5}{color=#700}темрява{/color}{/size}'

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

    show wizard signal-bad at center with easeinbottom

    "(over radio)" "Star Captain!… pssht…"

    show wizard signal-clear at center with dissolve

    Wiz "Pssht… Star Captain, this is Supreme Wizard calling you from our Centaurus system. Which planet are you traveling to?"

    menu:
        "Planet Alpha":
            $ planet = 'Alpha'
        "Planet Beta":
            $ planet = 'Beta'
        "Planet Gamma":
            $ planet = 'Gamma'

    Wiz "Great! See you on [planet], where i'll be waiting together with Princess and planet’s Guardian. \nHave a smooth flight and a hyper-sleep. Good night, Star Captain."

    # show guardian signal-bad at right with easeinbottom
    show guardian signal-clear at right with dissolve

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
    scene bg outskirts with wipeleft

    "Отже Зоряний Капітан разом з Хоронителькою та Принцесою вирушили до сховища, залишивши місто позаду."

    show ship gliding at left with moveinright

    "Але [darkness] шла по їх пятах. Злий чаклун дуже хотів знайти Принцесу. Він поширював свої хмарищи якнайдалі, сподіваючись знайти і захопити її якнайскоріше."

    show darkness horizontal at right with moveinright
    show ship gliding at offscreenleft
    show darkness horizontal at offscreenleft
    with moveinright

    # arriving at zoo
    scene bg zoo-ext-night with fade

    "Майже вночі корабель Капітана прибув до деревні, що була відома своїм зоопарком."

    show ship parked-left at left with moveinleft

    "Хоронителька розповіла, що зоопарком керує Дід Зуглядач, і в нього Принцесі буде безпечно залишитись доки лихо не мине."

    show zookeeper default at right with moveinright

    Zkp "Отож почесні гості! Вітаю до нашого гайдамацького куреня."

    jump rising_action

label rising_action:
    scene bg zoo-int-night with quickfade

    "Усередині було багато тварин, і відчувалося дуже затишно."

    show guardian default at left with moveinleft
    Grd "Нарешті ми в безпеці. Принцеса і ми всі дуже дякуємо, Діду, що відразу запроновували їхати до Вас."

    show zookeeper default at right with moveinright
    Zkp "Нажаль, тут неможна довго залишатися. Хмарищи підступають до нашої деревні, і це питання часу доки вони знайдуть Принцесу. Отож спозаранку треба буде вирушати далі."
    Zkp "Переночуйте з Принцесою в моїй кімнаті, а ми з Капітаном залишимось тут, поруч з моїми коровками."

    Grd "(fuck)."

    show zookeeper default at center
    show guardian default at offscreenleft
    with move

    Zkp "Отож, Зоряний Капітане, дуже багато чув та чекав зустрітися за інших обставин. (something funny). Але вже запізно, і дорога була складна, час відпочивати."
    Zkp "Розташовувайся зручніше у кораблі. А мені спочатку треба побажати надобраніч усім моїм тваринкам, та перевірити чи я не забув зачинити всі двері."

    show zookeeper default at offscreenright with move

    scene bg zoo-int-night with quickfade

    "Капітан вже почав засинати, але раптом почув начебто хтось шепоче поруч з корабелем."

    show locals shadowed at center with dissolve

    "Shadows" "пшшш… шпп… хосмішний… шшппп… хорапель…"

    menu:
        "* Keep silence and watch carefully *":
            "(Cap gets noticed)"
        "* Turn on lights and call for Zookeeper *":
            "(Cap gets noticed)"

    show locals shadowed at left
    show zookeeper default at right
    with move

    Zkp "Дивіться, хто знайшовся! Анфіса та Динька, друзі мої. Що ви там робите, га? Збираєте команду сміливих гайдамаків?"

    show locals default at left with dissolve
    show zookeeper default at center with move

    Zkp "Отож не хвилюйся, Зоряний Капітане, то свої. Ми побалакаємо, а ти засинай, онучку. Я залишусь на варті до самого ранку."

    show locals shadowed at offscreenleft
    show zookeeper default at offscreenleft
    with move

    jump climax_part1

label climax_part1:
    scene bg zoo-int-morning with blinds
    show zookeeper default at offscreenright
    show locals default at offscreenright

    "Ніч пройшла спокійно, та рано вранці Хоронителька та Принцеса повернулися до кораблю. Але Діда Зуглядача ніде не було видно."

    show guardian default at center
    show princess default at left
    with moveinleft

    Grd "Майже година пройшла, і мені ніяк не вдається знайти дідуся. Але я побачила хмарищи на підступах, тому нам варто вирушати якнайшвидше."

    show guardian default at left
    show princess default at offscreenleft
    show zookeeper default at right
    with moveinleft

    Zkp "Заждіть! [darkness] дуже близько, вам не можна вирушати на космічному кораблі!"

    Grd "(wtf?)"

    Zkp "Злий чаклун мабуть знає що Принцеса летітиме звідси, і тому його хмарищи оточили нашу деревню. Отож я щойно бачив як вони заковтнули інший корабель."

    Zkp "Але є надія! Ось ці дві гайдамачки зможуть провести вас таємничим шляхом до нашого маленького космопорту."

    show zookeeper default at center
    show locals default at right
    with moveinleft

    Zkp "Там ви зможете сісти на космічний потяг, що довезе вас усіх до іншої планети. Там Принцесі нічого більше не загрожуватиме."

    Grd "Нас усіх? Але як же Ви, Дідусю?"

    Zkp "Як жеж то я покину свою паству? Треба комусь доглядати за моїми тваринками. Але не хвилюйя, в нас є запаси всього потрібного. Отож зараз головне врятувати Принцесу."

    jump climax_part2

label climax_part2:
    scene bg evacuation with wipeleft
    "climax_part2"






