﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define Cap = Character("Зоряний Капітан")
define Wiz = Character(_("Чарівник Центаврів"), color = '#07a2f5')
define Grd = Character("Хоронителька", color = '#fff200')
# define Prc = Character("Princess")
define Zkp = Character("Дід Зуглядач", color = '#0b3b85')

# Variables
define planet = ''
define childhood_acc = 0
define has_dog = False

# Terms
define darkness = '{size=+5}{color=#700}темрява{/color}{/size}'
define by_darkness = '{size=+5}{color=#700}темрявою{/color}{/size}'

# Custom Transitions
define quickfade = Fade(0.2, 0.0, 0.2)
define lightning = Fade(0.2, 0.1, 0.1, color = '#a99')

# The game starts here.

label start:

    "Дивись, що в мене для тебе є…"
    "Уяви собі, що цей шолом від костюму справжнього космічного героя. Він подорожує космічним кораблем між зірками та планетами Чумацього шляху."

    menu:
        "Подорожує космічним кораблем?":
            scene bg ship-int with quickfade
            "Так! В нього є свій власний космічний корабель."
        "Справжній космічний герой?":
            "Так! І звати його – Зоряний Капітан."
            scene bg ship-int with quickfade

    show wizard signal-bad at center with easeinbottom

    "(РАДІО)" "Зоряний Капітане!… пшшшт…"

    show wizard signal-clear at center with dissolve

    Wiz "пшшшт… Зоряний Капітане, це дзвонить Верховний Чарівник з системи Центаврів. До якої планети ви вирушаєте?"

    menu:
        "До планети Альфа":
            $ planet = 'Альфа'
        "До планети Бета":
            $ planet = 'Бета'

    Wiz "Чудово! Побачимося на планеті [planet], де я чекатиму разом із Принцесою та Хоронителькою планети. \Гарного польоту та гіпер-сну. Надобраніч, Зоряний Капітане."

    show guardian signal-bad at right with easeinbottom
    show guardian signal-clear at right with dissolve
    # show guardian signal-clear at right with easeinbottom

    Grd "Надобраніч, сонечко."

    jump catalyst

label catalyst:
    scene black with pixellate

    "І ось, Зоряний Капітан вирушив до планети [planet], що є у системі Центаврів. Його гіпер-сон пройшов спокійно, але посадка - не дуже…"

    scene bg ship-landed with hpunch

    "Зоряний Капітан ще перебував у гіпер-сні, коли його корабель зробив аварійну посадку у космопорті призначення. Він прибув зарано, та його ніхто не очікував у цей час. \nЗокрема одної особи…"

    show guardian default with moveinright

    Grd "Капітане, це Хоронителька. Будь ласка, відповісить."

    menu:
        "Говорить Зоряний Капітан. Що трапилося?":
            $ childhood_acc += 1
        "Будь ласка, ще пʼять хвилиночок…":
            show bg ship-landed with vpunch

    Grd "Немає зовсім часу, Капітане! Щось жахливе трапилося з нашою планетою."
    Grd "Злий чаклун скликав страшну хворобу на нашу неньку. Це через неї небо червоне, це вони заважали кораблеві при посадці."
    Grd "Але Капітане! Принцеса потребує Вашої допомоги!"

    menu:
        "Я переможу злого чаклуна!":
            $ childhood_acc -= 1
        "Я врятую принцесу!":
            $ childhood_acc += 1

    Grd "Звісно, сонечко. Нам дуже пощастило, шо Ви з нами, Капітане. \nНажаль наш Верховний Чарівник не зміг також бути тут. Він мусив вирушати якнайскоріше, щоб захистити місто від тієї хвороби."


    Grd "Нам треба вирушати до безпечного місця. Я зможу принести потрібного палива для корабля, а Ви, Капітане, захищайте Принцесу поки мене нема. Це не займе багато часу"

    show princess default at right with moveinright
    show guardian at offscreenleft with move

    "Хоронителька подался по паливо, а Принцеса піднялася на борт."

    hide princess with dissolve

    "Вперше в своєму житті вона була на справжньому космічному кораблі. Але зараз то викликало в неї не захоплення, а тільки страх."

    scene bg ship-landed with fade

    "Минув деякий час. Густі червоні хмари наближувалися все ближче й ближче до міста. Усе, що залишалося під тіма хмарищами, було наче з’їдено [by_darkness]."
    "Раптом з неба вдарила блискавка. Все навколо висвітлилося лише на момент. \nЦього було достатньо, шоб побачити величезну тінь, що затоїлася за космічним кораблем."

    show dog shadowed with lightning

    "Темна істота" "Аггррххффф"

    menu:
        "Доброго ранку, істота планети [planet]. Мене звати Зоряний Капітан, а тебе як?":
            $ childhood_acc += 1
            jump meet_dog
        "* Вистрелити по істоті звуковою гарматою з корабля. *":
            $ childhood_acc -= 1
            jump lose_dog

    label meet_dog:
        show dog shadowed at left with move

        "Капітан повільно підійшов до Темної істоти та з подивом помітив, як та почала ворушити свома двома хвостами."

        show dog default with dissolve

        "«Диви який гарний песик», подумав Капітан та запронував істоті частину свого сніданку."

        show guardian default at right with moveinright

        Grd "Схоже, ви знайшли нового друга, Капітане! \nМи можемо взяти його з собою на корабель, але треба забиратися звідси."

        $ has_dog = True

        show dog default at offscreenleft
        show guardian default at center
        with move

        jump catalyst_end

    label lose_dog:
        show dog shadowed with vpunch
        show dog default at right with move
        show dog shadowed at offscreenleft with move

        "Звук вибухнув із гармати корабля, розбиваючи тишу наче скло. Від шоку істота відскочила і негайно втекла назад до темряви. Принцеса почала плакати."

        show guardian default at center with moveinright

        Grd "Все добре, Принцесо. Хоронителька вже тут! \nКапітане, то було… але неважливо, нам треба забиратися звідси."

        jump catalyst_end

    label catalyst_end:
        Grd "Ми повинні летіти низько над землею, щоб якнайшвидше дістатися безпечного місця. Я знаю, куди їхати, тож дозвольте мені сісти за кермо."

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











