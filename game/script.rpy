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
    # show guardian signal-clear at right with dissolve
    show guardian signal-clear at right with easeinbottom

    Grd "Good night, sweetheart."

    jump catalyst

label catalyst:
    scene black with pixellate

    "And so Star Captain went to planet [planet] of Centaurus system. His hyper-sleep was smooth, but landing was not…"

    scene bg ship-landed with hpunch

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

        "«So you must be a good boy», thought Captain and offered a snack to this creature."

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

    Grd "Ви праві, Дідусю. Мені дуже прикро що так сталося та Вам доведеться залишати своїх тварин на деякий час."

    Zkp "Так так. Отож переночуйте з Принцесою в моїй кімнаті, а ми з Капітаном залишимось тут, поруч з моїми коровками."

    show zookeeper default at center
    show guardian default at offscreenleft
    with move

    Zkp "Отож, Зоряний Капітане, дуже багато чув та чекав зустрітися за інших обставин. Бачу який ти міцний став, Капітане. Мабуть кожного дня бігаєш за своїми мріями, хаха."
    Zkp "Але вже запізно, і дорога була складна, час відпочивати. Розташовувайся зручніше у кораблі."
    Zkp "А мені спочатку треба побажати надобраніч усім моїм тваринкам, та перевірити чи я не забув зачинити всі двері."

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

    "Ніч пройшла, та рано вранці Хоронителька та Принцеса повернулися до кораблю. Але Діда Зуглядача ніде не було видно."

    show guardian and-princess at center
    # show princess default at left
    with moveinleft

    Grd "Майже година пройшла, і мені ніяк не вдається знайти дідуся. Але я побачила хмарищи на підступах, тому нам варто вирушати якнайшвидше."

    show guardian and-princess at left
    # show princess default at offscreenleft
    show zookeeper default at right
    with moveinleft

    Zkp "Заждіть! [darkness] дуже близько, вам не можна вирушати на космічному кораблі!"

    Grd "Що ви таке кажете, Діду?"

    Zkp "Злий чаклун мабуть знає що Принцеса летітиме звідси, і тому його хмарищи оточили нашу деревню. Отож я щойно бачив як вони проковтнули інший корабель."

    Zkp "Але є надія! Ось ці дві гайдамачки зможуть провести вас таємничим шляхом до нашого маленького космопорту."

    show zookeeper default at center
    show locals default at right
    with moveinleft

    Zkp "Там ви зможете сісти на космічний потяг, що довезе вас усіх до іншої планети. Там Принцесі нічого більше не загрожуватиме."

    Grd "Нас усіх? Але як же Ви, Дідусю?"

    Zkp "Як жеж то я покину свою паству? Треба комусь доглядати за моїми тваринками. Але не хвилюйя, в нас є запаси всього потрібного. Отож зараз головне довезти Принцесу до безпеки. Бо вона – це майбутнє нашої планети."

    jump climax_part2

label climax_part2:
    scene bg evacuation with wipeleft
    show creatures at truecenter with dissolve

    "Деревенський космопорт був переповнений усіма можливими істотами. І хоча [darkness] лише оточила деревню, гайдамачки попередили, що треба діяти швидко, але обережно."

    show locals default at right with moveinright

    "Гайдамачка Анфіса" "Тут навіть можуть бути шпигуни злого чаклуна, тому нам треба очепити Принцесу для надійності."

    "Гайдамачка Динька" "Ми повинні дістатися до потягу «Авакація», тільки він зможете пролетіти крізь хмарищи. Але доведеться йти до іншого кінця космічного перону."

    show guardian default at left with moveinleft

    Grd "Здається, саме туди рухаються усі ці істоти."

    # hide locals
    # hide guardian
    # with dissolve

    scene bg evacuation-group at truecenter with dissolve:
        easeout 3.0 zoom 1.2

    "Всі разом вирушили до потягу «Авакація», але пробиратися крізь натовп істот було дуже складно. З кожним кроком Капітан відчував як щільніше стає натовп, як голосніші стають крики, як важче стає дихати."

    scene bg evacuation-group at truecenter with dissolve:
        easeout 4.0 zoom 1.4

    "Побачивши Хоронительку та Принцесу деякі істоти поступалися дорогою, але інші наче скаженіли. Коли до «Авакації» залишалося всього ще декілька кроків, хтось зненацька схопив Капітана, який шов позаду групи."

    show weirdo shadowed at center with vpunch

    "Скаженіла істота" "Але навіщо ти туди йдеш? То несправжня принцеса! [darkness] врятує нас усіх."

    menu:
        "Відпусти негайно, істоте! То справжня Принцеса і ми веземо її до безпеки.":
            "(Cap gets separated)"
        "[darkness] – то лихо і хвороба. Сідай з нами на потяг і там тобі допоможуть!":
            "(Cap gets separated)"

    "Скаженіла істота" "Але, Капітане, ніхто нікуди не їде. Це останній потяг, але в ньому немає більше місця. Але не важливо, бо потяг не пройде крізь хмарищи…"

    # play train-whistle

    "Несподіваний гудок відволік Скаженілого, що дало Капітанові змогу вибратися. Він зміг прошмигнути крізь кілька інших істот, але ні Хоронительки з Принцесою, ані гайдамачок ніде не було бачити."

    hide weirdo with dissolve

    scene bg evacuation-alone at truecenter with dissolve:
        easeout 10.0 zoom 1.6

    "Зоряний Капітан зібрав усі свої почуття разом та крізь усе неможливе зміг розчути плач Принцеси зовсім неподалік. Він намагався піти у тому напрямку, але рухатися стало майже неможливо."

    # play train-double-whistle

    "Коли гудок пролунав вдруге, здалося, що усе навколо почало притягуватися до потягу. Капітан був неспроможній протидіяти течії з істот, яка затягнула його до найближчого вагону."

    "У той самий час потяг почав рухатися, і усі двері автоматично зачинилися. Щонайменш сотня живих істот була невзмозі потрапити до «Авакації»."

    jump break_into_three

label break_into_three:
    scene bg trains with fade

    "Потяг набрав швидкості, та взмив до неба. Потім ще один, і ще один. Три «Авакації» покинули космопорт та прорвалися крізь хмарищи. Наступна зупинка повинна бути вже в безпеці."

    jump finale_action

label finale_action:
    scene bg train-int-blue with quickfade

    show passengers shadowed at center

    "Капітан стояв у вагоні все ще невзмозі порухатися. Він був оточений десятками різних істот, але відчуввалося наче він залишився один у всему всесвіті."

    "Де поділися його друзі? Чи потрапили Хоронителька та Принцеса до «Авакації»? Якби ж тут був Чарівник Кентаврів, то він знав би що робити."

    show bg train-int-blue with hpunch

    "Раптом хтось покликав Капітана. Йому здалося, що він впізнав голос Хоронительки. Але то була не вона."

    show stuardess default at center with move

    "Бортпровідниця Любка" "Капітане! Зоряний Капітане, це так чудово, що я вас впізнала! Ми щойно отримали сігнал про допомогу від іншого потягу, «Авакації-3». Тільки Ви, Капітане, здатні їм допомогти."

    menu:
        "Звісно я допоможу! Недарма мене кличуть Зоряний Капітане.":
            "Бортпровідниця Любка" "(let's go!)"
        "Але що я можу зробити? Як дістатися іншого потягу?":
            "Бортпровідниця Любка" "(no worries!)"

    "Бортпровідниця Любка" "До того потягу потрапили хворі істоти, і їм негайно потрібно випити чарівного зілля. Але чомусь в них його немає."
    "Бортпровідниця Любка" "Проте в нас ще залишилося зілля! Та ось ще є ракетний ранець, щоб дістатися до іншого потягу. Я вірю, Капітане, що Ви здатні опанувати силу вітру."
    "Бортпровідниця Любка" "А нумо, розступіться, народе!"

    scene bg train-int-blue at right with dissolve:
        easeout 10.0 zoom 1.4

    "І ось Зоряний Капітан, взявши склянку зілля, ракетний ранець та усю свою хоробрість вирушив до єдиного шлюза у потязі. Почувши Бортпровідницю, усі істоти всередині почали розступатися як могли."

    scene bg trains at left with dissolve:
        easeout 10.0 zoom 1.4

    pause 1.0

    "Для Капітана то був не перший політ із ракетним ранцем, але потяги ще не вийшли з атмосфери, і тому шли на повному ходу. Це було дуже небезпечно."

    # show flying cap

    pause 1.0

    "Але він впорався."

    show bg train-int-yellow with hpunch

    show passengers shadowed at center

    show stuardess default at center with move

    "Бортпровідниця Вірка" "Зоряний Капітане! Я Бортпровідниця Вірка, вітаю Вас на борту «Авакації-3». Я щойно розподілила чарівне зілля, і усім хворим вже стало краще!"
    "Бортпровідниця Вірка" "Ох недарма вас кличуть Зоряним Капітаном. Ми усі вам дуже вдячні! Чудова робота, Капітане!"

    "І раптом…"

    show guardian and-princess at left with moveinleft

    Grd "Чудова робота, сонечко!"

    pause 1.0

    jump resolution

label resolution:
    scene black with fade
    scene bg safe-station at center with fade:
        easeout 15.0 zoom 1.2

    "Наступного дня Зоряний Капітан, Хоронителька та Принцеса дісталися до іншої планети, де злий чаклун більше не загрожуватиме їм."
    "Втомлені та виснажені, вони рухалися без якогось визначеного напрямку разом із сотнями інших виснажених істот."
    "В цей момент ніхто не розумів, що з ними усіма буде далі. Але всі думки були лише про те, що буде далі із їх рідною планетою [planet]."

    show black with pixellate

    "Кінець."

    "Присвячується усім Зоряним Капітанам і Принцесам, шо втратили своє дитинство внаслідок рашістскької агресії."

    pause 1.0
    return











