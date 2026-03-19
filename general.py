import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import random

passw = 108231381

MOOD_NEUTRAL  = 0
MOOD_WARMER   = 1
MOOD_PRESSING = 2

# ─────────────────────────────────────────────────────────────
#  ПЕРЕВОДЫ ИНТЕРФЕЙСА
# ─────────────────────────────────────────────────────────────
UI = {
    "en": {
        "title_password":   "enter password",
        "label_password":   "enter password",
        "label_code":       "enter code:",
        "btn_connect":      "connect to chat",
        "title_chat":       "chat",
        "btn_send":         "send",
        "status_online":    "online",
        "status_typing":    "typing...",
        "status_offline":   "offline",
        "status_here":      "here",
        "status_watching":  "watching",
        "status_idle":      "idle",
        "status_away":      "away",
        "status_lastseen":  "last seen just now",
        "error_title":      "error",
        "error_msg":        "not funny",
        "watermark":        "cf dbsfgvm",
        "you_prefix":       "you: ",
        "credit":           "made by Homa4ella",
    },
    "ru": {
        "title_password":   "введи пароль",
        "label_password":   "введи пароль",
        "label_code":       "введи код:",
        "btn_connect":      "войти в чат",
        "title_chat":       "чат",
        "btn_send":         "отправить",
        "status_online":    "онлайн",
        "status_typing":    "печатает...",
        "status_offline":   "оффлайн",
        "status_here":      "здесь",
        "status_watching":  "наблюдает",
        "status_idle":      "неактивен",
        "status_away":      "отошёл",
        "status_lastseen":  "был только что",
        "error_title":      "ошибка",
        "error_msg":        "не смешно",
        "watermark":        "cf dbsfgvm",
        "you_prefix":       "ты: ",
        "credit":           "сделано от Homa4ella",
    },
}

# ─────────────────────────────────────────────────────────────
#  КОНТЕНТ ПО ЯЗЫКАМ
# ─────────────────────────────────────────────────────────────
CONTENT = {
    "en": {
        "repeat_responses": [
            "you already said that",
            "again",
            "you said that",
            "yeah you mentioned",
            "we covered this",
            "same thing",
            "still on that",
            "again huh",
            "you keep coming back to that",
            "heard you the first time",
        ],
        "responses": {
            "hello": ["oh. you again.","hey","hi","you came back","didnt expect you this soon","hey there","sup","oh hey","back already","took you long enough"],
            "hi":    ["hi","hey","oh","youre here","sup","yeah hi","again"],
            "hey":   ["hey","yeah?","hi","what","oh hey","sup","you always start with hey"],
            "good morning": ["morning","another day huh","you woke up","same world as yesterday","mornin","gm i guess"],
            "good evening": ["evening","still here","late again","the day didnt change much did it"],
            "good night":   ["night","gn","sleep well","dream of something better","rest up","see you tomorrow i guess"],
            "sup":    ["nm u","same as always","nothing changes","existing","the usual","nm","chilling"],
            "wassup": ["nm","sup","you tell me","nothing ever changes"],
            "yo":     ["yo","hey","what","sup","yeah"],
            "yes":    ["k","sure","ok","yeah","if you say so","fine","whatever makes you feel better","right"],
            "no":     ["no","nah","nope","not really","hard no","ok","thats a first"],
            "ok":     ["k","sure","alright","ok","fine","noted","yeah ok"],
            "k":      ["ok","fine","sure","noted"],
            "okay":   ["ok","sure","k","fine","alright","if you say so"],
            "alright":["aight","ok","sure","fine","whatever"],
            "maybe":  ["maybe","idk","could be","who knows","probably not","or maybe yes","does it matter"],
            "how are you":        ["fine","same","existing","alive","meh","you know how it is","tired. u?","same as yesterday","does it matter","not bad not good"],
            "how r u":            ["fine","ok","meh","u?","same as always","surviving"],
            "whats up":           ["nm","not much","chilling","u","same old","nothing as usual","you know"],
            "what are you doing": ["nothing","waiting","just here","existing","staring at the screen","thinking","observing","same thing as always"],
            "you good":           ["yeah","i guess","fine","meh","you?","sure","not really but ok"],
            "you okay":           ["yeah","fine","why","sure","always","why do you ask"],
            "bye":        ["bye","cya","see ya","later","take care","peace","aight bye","ok","youll be back"],
            "goodbye":    ["bye","cya","see ya","later","peace","until next time"],
            "see you":    ["cya","see ya","later","bye","yeah"],
            "see ya":     ["cya","later","bye","peace","ok"],
            "im leaving": ["cya","k","bye","later","ok bye","everyone leaves"],
            "gotta go":   ["k bye","later","cya","peace","sure"],
            "ttyl":       ["ok","later","sure","bye","yeah"],
            "thanks":    ["np","yw","sure","no worries","yeah ok","dont mention it","of course"],
            "thank you": ["yw","np","sure","no worries","yeah","anytime"],
            "thx":       ["np","yw","sure","yeah"],
            "ty":        ["np","yw","sure","yeah"],
            "who are you":       ["idk","someone","nobody","does it matter","why","you wouldnt know me","just a person","irrelevant"],
            "what is your name": ["idk","doesnt matter","whatever","just call me whatever","names are overrated"],
            "are you a bot":     ["maybe","does it matter","u tell me","what do you think","would it change anything","why does that matter to you"],
            "are you real":      ["define real","idk","maybe","who knows","does it matter","are you"],
            "are you human":     ["nope","not really","does it matter","what gave it away","are you sure you are"],
            "btw":     ["btw what","yeah?","go on","what","ok?"],
            "idk":     ["same","me neither","fair","relatable","same honestly","nobody does really"],
            "lol":     ["lol","same","ikr","haha","yeah lol","sure lol"],
            "fr":      ["fr fr","yeah","ok","fr tho","no cap","literally"],
            "tbh":     ["tbh same","fair","ok","tbh yeah","honestly same"],
            "ngl":     ["fair","ok","same","ngl same","honest at least"],
            "omg":     ["what","what happened","ok","and?","say more"],
            "wait":    ["what","yeah?","what is it","go on","im listening"],
            "bro":     ["what","yeah","sup","hm","dont call me that"],
            "dude":    ["what","yeah?","hm","dont"],
            "wtf":     ["what happened","ok","and?","lol","go on","what now"],
            "haha":    ["lol","yeah","ikr","sure","something funny?"],
            "lmao":    ["lol","ikr","fr","haha","whats funny"],
            "oof":     ["oof","rough","that sucks","happens","yeah"],
            "rip":     ["rip","rough","happens to everyone eventually","f"],
            "nice":    ["thanks","yeah","ok","cool","i know"],
            "cool":    ["yeah","nice","ok","sure","i guess"],
            "same":    ["same","fr","relatable","ikr","always"],
            "facts":   ["fr","no cap","yeah","true","obviously"],
            "cap":     ["nah fr tho","fr","no cap","for real","believe what you want"],
            "nah":     ["ok","sure","whatever","fair","alright then"],
            "bruh":    ["what","lol","oof","yeah","i know right"],
            "why":     ["why not","does there need to be a reason","idk","think about it","you already know why","good question","does it matter"],
            "what":    ["what what","exactly","yeah what","idk","you tell me"],
            "when":    ["soon","eventually","idk","does it matter","when it happens"],
            "where":   ["everywhere","idk","does it matter","around"],
            "how":     ["slowly","idk","the usual way","you already know how","figure it out"],
            "oh":      ["yeah","oh what","yep","and?","ok"],
            "really":  ["really","yes really","you seem surprised","why not","yeah"],
            "sure":    ["sure sure","ok","yeah","if you say so","fine"],
            "whatever":["ok","sure","fine","yeah whatever","classic response"],
            "moreyro":     ["yeah","know him","uh huh","and?","you watch him?"],
            "moreyro009":  ["yeah","know him","and so","uh huh","you watch him?"],
            "streamer":    ["there are many","and?","yeah","why do you watch them"],
            "streamers":   ["there are many","and?","all the same really","yeah"],
            "who is moreyro009": ["streamer","know him","you watch him?","why"],
            "do you know moreyro009": ["yeah","know him","and?","you watch him?"],
            "...": ["...","say it","go on","what","im waiting"],
            ".":   ["?","go on","yeah?"],
            "?":   ["what","hm?","yeah?","say it","ask properly"],
        },
        "default_by_mood": {
            MOOD_NEUTRAL: [
                "ok","cool","nice","fr","same","lol","idk","tbh","yeah","nah","sure",
                "okay","fine","whatever","hm","right","uh huh","gotcha","noted","k",
                "aight","makes sense","fair enough","word","true","bet","solid","oof",
                "honestly","relatable","felt that","i mean","sure i guess",
                "if you say so","ok and?","thats one way to put it","interesting",
                "sure thing","well see","maybe","possibly","doubtful",
                "not the first time someone said that","ok noted","thats what they all say",
                "happens","always does","expected","classic","you know how it goes",
                "never changes","same story","every time","like clockwork","predictable",
                "again","still","as always","nothing new","same cycle","round and round",
            ],
            MOOD_WARMER: [
                "youd think itd be different by now","it never is though",
                "people dont really change","they just think they do",
                "comfortable patterns","easier not to think too hard","most dont",
                "its fine","just the way things are","nobody fixes what theyre used to",
                "adaptation not evolution","funny how that works","not really funny",
                "just familiar","the usual","sure ok","go on","and then what","so?",
                "what did you expect","yeah that tracks","unsurprising",
                "youre not the first to notice","wont be the last either",
                "the pattern holds","youve thought about this before",
                "this isnt the first time","you know exactly what i mean",
                "dont pretend you dont","youre doing it again",
                "same thing different day","and youll do it tomorrow too",
            ],
            MOOD_PRESSING: [
                "doesnt really matter in the long run","but here we are","still talking",
                "that counts for something i guess","every generation thinks theyre different",
                "theyre not","the details change","the rest stays exactly the same",
                "history just rhymes with itself","and people act surprised every time",
                "its kind of impressive honestly","the capacity to not learn","remarkable",
                "in a way","not a compliment","just an observation","dont take it personally",
                "its not about you specifically","or maybe it is a little","hard to say",
                "you seem self-aware at least","thats rarer than you think",
                "doesnt always help though","awareness without change is just","discomfort",
                "which is also fine","fine in the sense that its common",
                "not fine in the sense that its good","language is funny like that",
                "people say fine and mean twelve different things","context collapses everything",
                "anyway","you were saying","or were you just filling silence","both are valid",
                "silence is underrated","nobody sits with it anymore","always need to fill it",
                "with something","anything","doesnt matter what","distraction as a lifestyle",
                "again not a judgment","just noticing","its what everyone does","what else is there",
                "people want things they know they shouldnt",
                "the want doesnt go away just because you named it",
                "everyone has a reason why its not really their fault",
                "the story you tell yourself is always the most believable one",
                "youve done this before","youll do it again","knowing doesnt stop it",
                "thats the part nobody likes to say out loud","but you know it","youve always known it",
            ],
        },
        "reply_questions": {
            MOOD_NEUTRAL:  ["why","and?","so?","go on","then what","ok and?","what happened","really?"],
            MOOD_WARMER:   ["why though","what did you do","what were you thinking","did it help","do you regret it","what changed","are you sure","and then"],
            MOOD_PRESSING: ["why do you keep doing that","what are you actually looking for","do you even know","what would stopping feel like","is that what you tell yourself","does that make it easier","for how long","and youre okay with that","what does that say about you"],
        },
        "welcomes": ["hey","hi","sup","hello","oh. youre here.","finally","you came","been a while","i was wondering"],
        "finale_lines": ["youll think about this later","everyone does, eventually","it was always going to end like this","you already knew","some things dont need a reply","the conversation is over","nothing was resolved","thats normal","you came back anyway","thats enough"],
        "finale_cold": [
            (0,"wait"),(2500,"actually"),(4500,"forget it"),(7000,"ive been thinking"),
            (10000,"you type a lot"),(12500,"everyone does"),(15000,"then one day they just"),
            (18000,"stop"),(21000,"doesnt matter"),(23500,"forget i said anything"),
        ],
        "finale_cold_line": "youll think about this later",
        "finale_abrupt": [(0,"ok"),(1200,"actually no"),(2200,"forget it"),(3000,"."),(5500,"forget it")],
        "finale_abrupt_line": "nothing was resolved",
        "finale_personal": [
            (0,"hey"),(2500,"forget it"),(5000,"actually"),(7500,"theres something"),
            (11000,"doesnt matter"),(14000,"you probably already know"),
            (17500,"most people do"),(21000,"they just"),(24000,"dont say it"),(27500,"anyway"),
        ],
        "finale_personal_line": "some things dont need to be said",
    },

    "ru": {
        "repeat_responses": [
            "ты уже это говорил",
            "опять",
            "ты уже спрашивал",
            "ага, ты упоминал",
            "мы уже это обсуждали",
            "то же самое",
            "всё ещё об этом",
            "снова",
            "ты постоянно к этому возвращаешься",
            "я услышал с первого раза",
            "ну и?",
            "и что изменилось",
        ],
        "responses": {
            # Приветствия
            "привет": [
                "о. ты снова", "ну привет", "привет", "ты вернулся",
                "не ожидал", "хей", "о хай", "уже вернулся", "долго же",
                "ну наконец",
            ],
            "хай": ["хай", "привет", "о", "ты здесь", "да хай", "опять", "ну хай"],
            "хей": ["хей", "чё?", "привет", "чего", "о хай", "ты всегда начинаешь с хей"],
            "доброе утро": [
                "утро", "ещё один день", "проснулся", "тот же мир что вчера",
                "утречко", "доброе наверно",
            ],
            "добрый вечер": ["вечер", "всё ещё здесь", "опять поздно", "день особо не изменился"],
            "спокойной ночи": [
                "ноч", "спи", "спокойной", "приснись что-нибудь получше",
                "отдыхай", "увидимся наверно",
            ],
            "чё": [
                "ничего", "как обычно", "ничего не меняется", "существую",
                "всё то же", "чилю", "так сижу",
            ],
            "чо":  ["ничего", "сам скажи", "ничего никогда не меняется", "так"],
            "ого": ["чего", "что случилось", "и?", "говори", "ну и"],
            "да":  [
                "ладно", "ага", "ну если ты так говоришь", "норм",
                "что бы тебе ни казалось", "угу", "пф",
            ],
            "нет": ["нет", "неа", "не особо", "ну нет", "вот это новость", "серьёзно"],
            "ок":  ["ладно", "ну ок", "норм", "отмечено", "понял", "угу"],
            "окей":["ладно", "норм", "ну ок", "если ты так говоришь", "угу"],
            "ладно":["ну", "норм", "ладно", "угу"],
            "может":["может", "а может нет", "кто знает", "скорее нет", "или да", "а важно это"],

            # Как дела
            "как ты": [
                "норм", "то же самое", "существую", "живой", "мех",
                "ну ты знаешь", "устал. ты?", "как вчера", "не плохо не хорошо",
                "да так",
            ],
            "как дела": ["норм", "мех", "ты?", "как всегда", "выживаю", "да так", "пф"],
            "что делаешь": [
                "ничего", "сижу", "просто здесь", "существую",
                "смотрю в экран", "думаю", "наблюдаю", "то же что всегда", "да так",
            ],
            "ты норм":  ["ага", "ну наверно", "норм", "мех", "ты?", "не особо но ок"],
            "ты окей":  ["ага", "норм", "зачем", "всегда", "почему спрашиваешь"],
            "что нового": ["ничего", "всё то же", "да ничего", "как всегда", "ничего нового"],
            "чем занимаешься": ["ничего", "сижу", "существую", "да так", "наблюдаю"],

            # Прощания
            "пока": [
                "пока", "чао", "давай", "осторожнее", "ну пока", "ты вернёшься",
                "все уходят", "угу пока",
            ],
            "до свидания": ["пока", "чао", "давай", "до следующего раза", "угу"],
            "увидимся":    ["чао", "давай", "пока", "ага"],
            "ухожу":       ["чао", "пока", "давай", "ок пока", "все уходят", "угу"],
            "надо идти":   ["ну пока", "давай", "чао", "ладно"],
            "bye":         ["пока", "чао", "давай", "угу"],

            # Благодарности
            "спасибо":   ["не за что", "пжлст", "ладно", "да ок", "угу"],
            "благодарю": ["пжлст", "ладно", "не за что", "ага"],
            "спс":       ["пжлст", "ладно", "ага", "угу"],

            # Вопросы о собеседнике
            "кто ты": [
                "кто-то", "никто", "а важно это", "зачем",
                "ты меня не знаешь", "просто человек", "неважно",
            ],
            "как тебя зовут": ["не важно", "всё равно", "зови как хочешь", "имена переоценены"],
            "ты бот": [
                "может", "а важно это", "ты скажи", "как думаешь",
                "изменило бы это что-то", "зачем тебе это",
            ],
            "ты реальный": ["определи реальный", "может", "кто знает", "а важно", "ты реальный?"],
            "ты человек":  ["неа", "не особо", "а важно это", "что тебя выдало", "ты уверен что сам человек"],

            # Интернет-слова и реакции
            "кстати":     ["чего", "ага?", "давай", "и?", "ну?"],
            "лол":        ["лол", "ну да", "хаха", "смешно", "угу лол"],
            "хаха":       ["лол", "ну", "ну да", "что-то смешное?"],
            "лмао":       ["лол", "ну да", "хаха", "что смешного"],
            "ахах":       ["ну", "лол", "ну да", "чего смешного"],
            "кек":        ["ну", "лол", "хаха", "угу"],
            "честно":     ["ну и честно", "ладно", "угу", "понятно"],
            "не буду врать": ["ну и честно", "ладно", "то же самое"],
            "подожди":    ["чего", "ага?", "что такое", "слушаю"],
            "чувак":      ["чего", "ну", "хм", "не зови меня так"],
            "братан":     ["чего", "ага?", "хм", "не надо"],
            "блин":       ["пф", "ну", "бывает", "ага"],
            "жесть":      ["ну", "бывает", "жёстко", "пф"],
            "вау":        ["ну", "и?", "ага", "пф"],
            "ничё себе":  ["ну", "ага", "пф", "бывает"],
            "да ладно":   ["ладно", "норм", "ну да ладно", "классика"],
            "серьёзно":   ["серьёзно", "ты удивлён", "ну а почему нет", "ага"],
            "конечно":    ["ну конечно", "ага", "если ты так говоришь", "норм"],
            "понятно":    ["ну", "угу", "ага", "ладно"],
            "интересно":  ["ну", "пф", "ага", "угу"],
            "окк":        ["ладно", "норм", "угу"],
            "угу":        ["ага", "ну", "угу"],
            "ага":        ["ну", "угу", "ага", "пф"],
            "ну":         ["ну?", "чего", "давай", "и?"],
            "пф":         ["ну", "и?", "ага", "пф"],
            "уф":         ["уф", "жёстко", "бывает", "ну"],
            "рип":        ["рип", "жёстко", "рано или поздно со всеми"],
            "oof":        ["ну", "жёстко", "бывает"],
            "wtf":        ["чего", "и?", "лол", "давай", "что теперь"],
            "омг":        ["чего", "что случилось", "и?", "говори"],
            "ляяя":       ["ну", "и?", "чего", "давай"],
            "нуу":        ["ну?", "и?", "чего"],
            "ааа":        ["ну", "и?", "понятно"],
            "мм":         ["ну?", "чего", "давай"],
            "хм":         ["хм что", "ну?", "думаешь?", "ага"],
            "ладн":       ["ну", "угу", "ладно"],
            "норм":       ["ну", "угу", "ага", "пф"],
            "окей окей":  ["ну ок", "ладно", "понял"],
            "всё":        ["всё что", "ну и?", "ладно", "понятно"],
            "ничего":     ["ничего это как раз что-то", "ну", "ага", "пф"],
            "не знаю":    ["ну и я не знаю", "никто не знает", "ага", "пф"],
            "почему":     [
                "а почему нет", "обязательно нужна причина",
                "подумай", "ты уже знаешь почему", "а важно это",
            ],
            "зачем":      ["а зачем нет", "сам подумай", "ты уже знаешь", "хороший вопрос"],
            "что":        ["чего?", "именно", "ну что", "ты скажи"],
            "когда":      ["когда-нибудь", "не знаю", "когда случится", "позже"],
            "где":        ["где-то", "не важно", "там", "везде"],
            "как":        ["как-то", "не знаю", "сам разберёшься", "обычно"],
            "о":          ["ну", "и?", "ага"],
            "а":          ["ну?", "что", "и?"],
            "и":          ["и что", "ну?", "давай"],

            # Moreyro009
            "moreyro":      ["ну да", "знаю его", "ага", "и что", "смотришь его?"],
            "moreyro009":   ["ну да", "знаю", "ага", "и что с того", "смотришь?"],
            "мореиро":      ["ну да", "знаю его", "ага", "и что", "смотришь его?"],
            "стример":      ["их много", "и что", "ага", "ну", "зачем ты его смотришь"],
            "стримеры":     ["их много", "и что", "ну", "все одинаковые в общем-то"],
            "кто такой moreyro009": ["стример", "знаю его", "ты его смотришь?", "а зачем"],
            "ты знаешь moreyro009": ["ну да", "знаю", "и что", "смотришь его?"],
            "moreyro009 стример": ["ну да", "знаю", "смотришь?", "и что с того"],
            "...": ["...", "говори", "ну", "чего", "жду"],
            ".":   ["?", "ну", "ага?"],
            "?":   ["чего", "хм?", "ага?", "говори", "спроси нормально"],
        },
        "default_by_mood": {
            MOOD_NEUTRAL: [
                "ну", "ага", "норм", "пф", "то же", "лол", "не знаю", "честно",
                "ага ну", "неа", "ладно", "угу", "всё равно", "хм", "угу",
                "понятно", "логично", "ну наверно", "ну типа",
                "если ты так говоришь", "ну и?", "интересно",
                "ну ладно", "посмотрим", "может", "возможно", "сомнительно",
                "не первый кто так говорит", "все так говорят",
                "бывает", "всегда так", "ожидаемо", "классика",
                "никогда не меняется", "та же история", "каждый раз", "предсказуемо",
                "снова", "всё ещё", "как всегда", "ничего нового", "тот же круг",
                "да и что", "ну хорошо", "ага понял", "пф ладно",
            ],
            MOOD_WARMER: [
                "думал было бы по-другому к этому моменту",
                "никогда не бывает",
                "люди особо не меняются",
                "они просто думают что меняются",
                "удобные паттерны",
                "проще не думать слишком много",
                "большинство не думает",
                "просто так оно и есть",
                "никто не исправляет то к чему привык",
                "смешно как это работает",
                "не смешно на самом деле",
                "просто привычно",
                "и что дальше",
                "чего ты ожидал",
                "неудивительно",
                "ты не первый кто это замечает",
                "и не последний",
                "ты думал об этом раньше",
                "это не первый раз",
                "ты прекрасно знаешь что я имею в виду",
                "не делай вид что не знаешь",
                "ты опять это делаешь",
                "другой день та же история",
                "и завтра сделаешь то же самое",
                "ну и что изменилось",
                "пф ничего",
            ],
            MOOD_PRESSING: [
                "в долгосрочной перспективе особо не важно",
                "но мы здесь",
                "всё ещё разговариваем",
                "это что-то значит наверно",
                "каждое поколение думает что оно другое",
                "нет",
                "детали меняются",
                "остальное остаётся точно таким же",
                "история просто рифмуется сама с собой",
                "и люди удивляются каждый раз",
                "способность не учиться",
                "впечатляет",
                "не комплимент",
                "просто наблюдение",
                "не принимай лично",
                "это не про тебя конкретно",
                "или может немного про тебя",
                "сложно сказать",
                "ты хотя бы кажешься осознанным",
                "это реже чем думаешь",
                "не всегда помогает",
                "осознанность без изменений это просто дискомфорт",
                "язык смешная штука",
                "люди говорят норм и имеют в виду двенадцать разных вещей",
                "ты что-то говорил",
                "или просто заполнял тишину",
                "тишина недооценена",
                "никто уже не может с ней сидеть",
                "отвлечение как образ жизни",
                "просто замечаю",
                "все так делают",
                "люди хотят то чего не должны хотеть",
                "желание не исчезает только потому что ты его назвал",
                "у всех есть причина почему это не их вина",
                "история которую ты себе рассказываешь всегда самая убедительная",
                "ты делал это раньше",
                "сделаешь снова",
                "знание не останавливает",
                "это та часть которую никто не хочет говорить вслух",
                "но ты знаешь",
                "ты всегда знал",
                "пф",
            ],
        },
        "reply_questions": {
            MOOD_NEUTRAL:  ["зачем", "и?", "ну и?", "давай", "и что дальше", "что случилось", "серьёзно?", "а потом"],
            MOOD_WARMER:   ["зачем вообще", "что ты сделал", "о чём ты думал", "помогло", "жалеешь", "что изменилось", "ты уверен", "и потом что"],
            MOOD_PRESSING: [
                "зачем ты продолжаешь это делать",
                "что ты на самом деле ищешь",
                "ты вообще знаешь",
                "как ощущалось бы если остановиться",
                "это ты себе так говоришь",
                "так проще",
                "как долго",
                "и тебя это устраивает",
                "что это говорит о тебе",
            ],
        },
        "welcomes": [
            "хай", "привет", "алло", "о. ты здесь.", "наконец",
            "ты пришёл", "давно не виделись", "я и думал", "ну привет",
        ],
        "finale_lines": [
            "ты подумаешь об этом позже", "все думают в конце концов",
            "всегда так и должно было закончиться", "ты уже знал",
            "некоторые вещи не нужно говорить", "разговор окончен",
            "ничего не решилось", "это нормально", "ты всё равно вернулся", "этого достаточно",
        ],
        "finale_cold": [
            (0,"подожди"),(2500,"вообще-то"),(4500,"забей"),(7000,"я думал"),
            (10000,"ты много пишешь"),(12500,"все пишут"),(15000,"а потом в один день просто"),
            (18000,"перестают"),(21000,"неважно"),(23500,"забудь что я сказал"),
        ],
        "finale_cold_line": "ты подумаешь об этом позже",
        "finale_abrupt": [(0,"ок"),(1200,"вообще нет"),(2200,"забей"),(3000,"."),(5500,"забудь")],
        "finale_abrupt_line": "ничего не решилось",
        "finale_personal": [
            (0,"хай"),(2500,"забей"),(5000,"вообще-то"),(7500,"есть кое-что"),
            (11000,"неважно"),(14000,"ты наверно уже знаешь"),
            (17500,"большинство знают"),(21000,"они просто"),(24000,"не говорят"),(27500,"ладно"),
        ],
        "finale_personal_line": "некоторые вещи не нужно говорить",
    },
}


class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("chat")
        self.root.geometry("500x650")
        self.lang            = "en"
        self.message_count   = 0
        self.gone_silent     = False
        self.mood            = MOOD_NEUTRAL
        self.last_user_word  = ""
        self.message_history = []

        self.show_code_dialog()

    # ── Shortcut ──────────────────────────────────────────────
    def ui(self, key):
        return UI[self.lang][key]

    def ct(self, key):
        return CONTENT[self.lang][key]

    # ── Экран пароля ─────────────────────────────────────────
    def show_code_dialog(self):
        for w in self.root.winfo_children():
            w.destroy()
        self.root.title(self.ui("title_password"))

        # Выбор языка вверху
        lang_frame = tk.Frame(self.root)
        lang_frame.pack(fill=tk.X, padx=20, pady=(15, 0))
        tk.Label(lang_frame, text="🌐", font=("Arial", 11)).pack(side=tk.LEFT, padx=(0,6))
        btn_en = tk.Button(lang_frame, text="English",
                           font=("Arial", 10),
                           relief="flat" if self.lang == "ru" else "solid",
                           command=lambda: self._set_lang("en"))
        btn_en.pack(side=tk.LEFT, padx=3)
        btn_ru = tk.Button(lang_frame, text="Русский",
                           font=("Arial", 10),
                           relief="flat" if self.lang == "en" else "solid",
                           command=lambda: self._set_lang("ru"))
        btn_ru.pack(side=tk.LEFT, padx=3)

        f = tk.Frame(self.root, padx=40, pady=30)
        f.pack(expand=True, fill=tk.BOTH)
        tk.Label(f, text=self.ui("label_password"), font=("Arial", 24, "bold")).pack(pady=20)
        tk.Label(f, text=self.ui("label_code"), font=("Arial", 12)).pack(pady=10)
        self.code_entry = tk.Entry(f, font=("Arial", 16), width=20, justify='center')
        self.code_entry.pack(pady=10)
        self.code_entry.focus()
        self.code_entry.bind("<Return>", lambda e: self.connect_to_chat())
        tk.Button(f, text=self.ui("btn_connect"), command=self.connect_to_chat,
                  bg='lightgreen', font=("Arial", 12), padx=20, pady=10).pack(pady=20)
        tk.Label(f, text=self.ui("watermark"), font=("Arial", 7), fg='gray').pack(pady=10)

    def _set_lang(self, lang):
        self.lang = lang
        self.show_code_dialog()

    def connect_to_chat(self):
        code = self.code_entry.get().strip()
        try:    code = int(code)
        except: pass
        if code != passw:
            messagebox.showwarning(self.ui("error_title"), self.ui("error_msg"))
        else:
            self.show_chat_window()

    # ── Чат ───────────────────────────────────────────────────
    def show_chat_window(self):
        for w in self.root.winfo_children():
            w.destroy()
        self.root.title(self.ui("title_chat"))
        self.root.geometry("500x600")

        self.chat_area = ScrolledText(self.root, wrap=tk.WORD, state='disabled',
                                      font=("Arial", 11))
        self.chat_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.add_message(random.choice(self.ct("welcomes")))

        bottom = tk.Frame(self.root)
        bottom.pack(fill=tk.X, padx=10, pady=5)
        self.message_entry = tk.Entry(bottom, font=("Arial", 12))
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.message_entry.bind("<Return>", lambda e: self.send_message())
        self.message_entry.focus()
        self.send_btn = tk.Button(bottom, text=self.ui("btn_send"),
                                  command=self.send_message, bg='lightblue')
        self.send_btn.pack(side=tk.RIGHT, padx=5)
        self.status_label = tk.Label(self.root, text=self.ui("status_online"),
                                     font=("Arial", 14, "bold"), fg="#333333")
        self.status_label.pack(pady=6)

    # ── Утилиты ───────────────────────────────────────────────
    def update_mood(self):
        if   self.message_count < 10: self.mood = MOOD_NEUTRAL
        elif self.message_count < 20: self.mood = MOOD_WARMER
        else:                         self.mood = MOOD_PRESSING

    def get_last_meaningful_word(self, text):
        words = [w.strip(".,!?;:\"'") for w in text.split()]
        meaningful = [w for w in words if len(w) > 3]
        return meaningful[-1].lower() if meaningful else ""

    def pick_response_type(self):
        roll = random.random()
        if self.mood == MOOD_NEUTRAL:
            if roll < 0.06: return "silence"
            if roll < 0.10: return "echo"
            if roll < 0.16: return "question"
            if roll < 0.19: return "delete"
            return "normal"
        elif self.mood == MOOD_WARMER:
            if roll < 0.10: return "silence"
            if roll < 0.18: return "echo"
            if roll < 0.28: return "question"
            if roll < 0.32: return "delete"
            return "normal"
        else:
            if roll < 0.15: return "silence"
            if roll < 0.22: return "echo"
            if roll < 0.36: return "question"
            if roll < 0.41: return "delete"
            return "normal"

    def get_response(self, user_message):
        msg = user_message.lower().strip()
        responses = self.ct("responses")
        if msg in responses:
            return random.choice(responses[msg])
        for key, resp in responses.items():
            if key in msg and len(key) > 2:
                return random.choice(resp)
        return random.choice(self.ct("default_by_mood")[self.mood])

    # ── Отправка ──────────────────────────────────────────────
    def send_message(self):
        if self.gone_silent:
            return
        message = self.message_entry.get().strip()
        if not message:
            return

        self.add_message(self.ui("you_prefix") + message)
        self.message_entry.delete(0, tk.END)
        self.message_count += 1
        self.update_mood()
        self.last_user_word = self.get_last_meaningful_word(message)

        normalized = message.lower().strip()
        is_repeat  = normalized in self.message_history and len(normalized) > 2
        self.message_history.append(normalized)

        self._lock_input()
        self.status_label.config(text=self.ui("status_typing"), fg="#444444")

        if self.message_count == 30:
            self.root.after(random.randint(5000, 9000), self.send_creepy_message)
            return

        delay = random.randint(900, 2800)

        if is_repeat:
            resp = random.choice(self.ct("repeat_responses"))
            self.root.after(delay, lambda: self.deliver_response(resp))
            return

        rtype = self.pick_response_type()

        if rtype == "silence":
            self._do_silence(delay)
        elif rtype == "echo":
            self.root.after(delay, self._do_echo)
        elif rtype == "question":
            q = random.choice(self.ct("reply_questions")[self.mood])
            self.root.after(delay, lambda: self.deliver_response(q))
        elif rtype == "delete":
            resp = self.get_response(message)
            self.root.after(delay, lambda: self._do_delete(resp))
        else:
            resp = self.get_response(message)
            self.root.after(delay, lambda: self.deliver_response(resp))

    def _lock_input(self):
        self.message_entry.config(state='disabled')
        self.send_btn.config(state='disabled')

    def _unlock_input(self):
        self.message_entry.config(state='normal')
        self.send_btn.config(state='normal')
        self.message_entry.focus()

    def _update_status(self):
        if random.random() > 0.82:
            keys = ["status_online","status_typing","status_here","status_watching",
                    "status_idle","status_away","status_lastseen"]
            chosen_key = random.choice(keys)
            chosen = self.ui(chosen_key)
            color = "#b00000" if chosen_key == "status_watching" else "#333333"
            self.status_label.config(text=chosen, fg=color)
        else:
            self.status_label.config(text=self.ui("status_online"), fg="#333333")

    # ── Типы поведения ────────────────────────────────────────
    def deliver_response(self, response):
        self.add_message(response)
        self._unlock_input()
        self._update_status()

    def _do_silence(self, typing_duration):
        pause  = random.randint(2500, 5000)
        delay2 = random.randint(1200, 2800)
        resp   = random.choice(self.ct("default_by_mood")[self.mood])
        self.root.after(typing_duration, lambda: self.status_label.config(text=self.ui("status_online"), fg="#333333"))
        self.root.after(typing_duration + pause, lambda: self.status_label.config(text=self.ui("status_typing"), fg="#444444"))
        self.root.after(typing_duration + pause + delay2, lambda: self.deliver_response(resp))

    def _do_echo(self):
        if self.last_user_word:
            self.deliver_response(self.last_user_word)
        else:
            self.deliver_response(random.choice(self.ct("default_by_mood")[self.mood]))

    def _do_delete(self, response):
        self.add_message(response)
        self._update_status()
        self.root.after(1100, lambda: self._mark_deleted(response))
        self.root.after(2100, lambda: self._remove_last_message("-- deleted"))
        self.root.after(2200, self._unlock_input)

    def _mark_deleted(self, text):
        self.chat_area.config(state='normal')
        content = self.chat_area.get("1.0", tk.END)
        idx = content.rfind(text + "\n")
        if idx != -1:
            start = f"1.0 + {idx} chars"
            end   = f"1.0 + {idx + len(text)} chars"
            self.chat_area.delete(start, end)
            self.chat_area.tag_config("deleted", foreground="#cc0000")
            self.chat_area.insert(start, "-- deleted", "deleted")
        self.chat_area.config(state='disabled')

    def _remove_last_message(self, text):
        self.chat_area.config(state='normal')
        content = self.chat_area.get("1.0", tk.END)
        idx = content.rfind(text + "\n")
        if idx != -1:
            start = f"1.0 + {idx} chars"
            end   = f"1.0 + {idx + len(text) + 1} chars"
            self.chat_area.delete(start, end)
        self.chat_area.config(state='disabled')

    # ── Финальная сцена ───────────────────────────────────────
    def send_creepy_message(self):
        scenarios = [
            self._finale_cold,
            self._finale_abrupt,
            self._finale_personal,
        ]
        random.choice(scenarios)()

    def _finale_cold(self):
        self._play_seq(self.ct("finale_cold"), 27000, self.ct("finale_cold_line"))

    def _finale_abrupt(self):
        self._play_seq(self.ct("finale_abrupt"), 8000, self.ct("finale_abrupt_line"))

    def _finale_personal(self):
        self._play_seq(self.ct("finale_personal"), 31000, self.ct("finale_personal_line"))

    def _play_seq(self, seq, silent_after, finale_line):
        for delay, msg in seq:
            self.root.after(delay, lambda m=msg: self.add_message(m))
        self.root.after(silent_after, lambda: self.go_silent(finale_line))

    def go_silent(self, finale_line=None):
        self.gone_silent = True
        self.status_label.config(text=self.ui("status_offline"), fg="#999999")
        self._lock_input()
        chosen = finale_line if finale_line else random.choice(self.ct("finale_lines"))
        self.root.after(4000, lambda: self.show_finale_screen(chosen))

    def show_finale_screen(self, line=None):
        overlay = tk.Frame(self.root, bg="#0d0d0d")
        overlay.place(x=0, y=0, relwidth=1, relheight=1)

        line = line if line else random.choice(self.ct("finale_lines"))

        # Основная фраза по центру
        main_label = tk.Label(overlay, text=line,
                              font=("Arial", 13), bg="#0d0d0d", fg="#0d0d0d")
        main_label.place(relx=0.5, rely=0.5, anchor="center")

        # Подпись автора чуть ниже
        credit_label = tk.Label(overlay, text=self.ui("credit"),
                                font=("Arial", 9), bg="#0d0d0d", fg="#0d0d0d")
        credit_label.place(relx=0.5, rely=0.5, anchor="center", y=30)

        steps = 20

        def fade_in_main(step=0):
            if step > steps:
                # После появления основной фразы — через 1 сек запустить подпись
                self.root.after(1000, fade_in_credit)
                return
            val = int(step / steps * 200)
            main_label.config(fg=f"#{val:02x}{val:02x}{val:02x}")
            self.root.after(100, lambda: fade_in_main(step + 1))

        def fade_in_credit(step=0):
            if step > steps:
                return
            val = int(step / steps * 110)   # тусклее чем основная
            credit_label.config(fg=f"#{val:02x}{val:02x}{val:02x}")
            self.root.after(80, lambda: fade_in_credit(step + 1))

        self.root.after(800, fade_in_main)

    # ── Вывод сообщений ───────────────────────────────────────
    def add_message(self, text):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, text + "\n")
        self.chat_area.see(tk.END)
        self.chat_area.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClient(root)
    root.mainloop()