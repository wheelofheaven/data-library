#!/usr/bin/env python3
"""Split long paragraphs in data-library chapter JSON, renumbering n + refId in-place.

Splits are defined per (book, chapter, paragraph_n) with per-language marker
strings; the marker is the LAST text of a piece (so the split happens just after
the marker). Markers must be unique substrings within the paragraph.
"""

import json
import sys
from pathlib import Path

LIB = Path(__file__).resolve().parent.parent  # data-library/ (this script lives in data-library/scripts/)

# (book_slug, chapter_n, paragraph_n) -> list of split markers per language.
# Each markers dict yields N+1 pieces from N markers.
SPLITS = {
    ('the-book-which-tells-the-truth', 1, 3): [
        # split 1: end of geographic/atmospheric setup
        {
            'fr': 'le long de ces pentes abruptes.',
            'en': 'down those steep slopes.',
            'de': 'diese steilen Hänge hinabzugleiten.',
            'es': 'por aquellas pendientes abruptas.',
            'ru': 'по этим крутым склонам.',
            'ja': '滑り降りて楽しんだことか。',
            'ko': '즐긴 것이 몇 번이었던가.',
            'zh': '沿着这些陡峭的山坡滑下取乐。',
            'zh-Hant': '沿着這些陡峭的山坡滑下取樂。',
        },
        # split 2: end of visual description of craft
        {
            'fr': 'sans cligner des yeux.',
            'en': 'without blinking.',
            'de': 'ohne mit den Augen zu blinzeln.',
            'es': 'sin parpadear.',
            'ru': 'не моргая.',
            'ja': '見ていられなかった。',
            'ko': '바라볼 수 없었다.',
            'zh': '我看着它时不得不眨眼。',
            'zh-Hant': '我看着它時不得不眨眼。',
        },
    ],
    ('the-book-which-tells-the-truth', 5, 3): [
        {
            'fr': "ne servant plus à rien.",
            'en': "no longer serving any purpose.",
            'de': "zu nichts mehr dienen.",
            'es': "no sirviendo ya para nada.",
            'ru': "более ни на что не служа.",
            'ja': "何の役にも立たず、崩れ落ちるでしょう。",
            'ko': "아무 데도 쓸모없이 무너질 것입니다.",
            'zh': "不再有任何用处。",
            'zh-Hant': "不再有任何用處。",
        },
    ],
    ('the-book-which-tells-the-truth', 5, 50): [
        {
            'fr': "«hauteur de ses talons» est de 30 millions de «parasanges».",
            'en': "«height of his heels» is 30 million «parasangs».",
            'de': "«Höhe seiner Fersen» 30 Millionen «Parasangen» beträgt.",
            'es': "«altura de sus talones» es de 30 millones de «parasangas».",
            'ru': "«высота его пят» составляет 30 миллионов «парасангов».",
            'ja': "「その踵の高さ」が三千万「パラサング」であると言われています。",
            'ko': "「그 발꿈치의 높이」가 삼천만 「파라상」이라고 말해져 있습니다.",
            'zh': "「他脚跟的高度」是三千万「帕拉桑」。",
            'zh-Hant': "「他腳跟的高度」是三千萬「帕拉桑」。",
        },
        {
            'fr': "26 000 ans avant d’arriver jusqu’à nous.",
            'en': "26,000 years before arriving up to us.",
            'de': "26.000 Jahre brauchen, bevor Sie bis zu uns gelangen.",
            'es': "26.000 años antes de llegar hasta nosotros.",
            'ru': "около 26 000 лет, прежде чем добраться до нас.",
            'ja': "約二万六千年かかるでしょう。",
            'ko': "약 이만 육천 년이 걸릴 것입니다.",
            'zh': "将近两万六千年才能到达我们这里。",
            'zh-Hant': "將近兩萬六千年才能到達我們這裏。",
        },
    ],
    ('the-book-which-tells-the-truth', 5, 53): [
        {
            'fr': "panique meurtrière et dangereuse.",
            'en': "deadly and dangerous panic.",
            'de': "mörderische und gefährliche Panik zu schaffen.",
            'es': "pánico mortífero y peligroso.",
            'ru': "смертоносную и опасную панику.",
            'ja': "殺人的で危険なパニックを生む危険もなしに、あえて姿を見せるために、われわれが何者かを彼らに教えねばなりません。",
            'ko': "살인적이고 위험한 공황을 일으킬 위험도 없이, 감히 모습을 보이기 위하여, 우리가 누구인지를 그들에게 가르쳐야 합니다.",
            'zh': "致命而危险的恐慌的风险。",
            'zh-Hant': "致命而危險的恐慌的風險。",
        },
        {
            'fr': "Dans les deux sens, c’est infini.",
            'en': "In both directions, it is infinite.",
            'de': "In beiden Richtungen ist es unendlich.",
            'es': "En los dos sentidos, es infinito.",
            'ru': "В обоих направлениях это бесконечно.",
            'ja': "両方向に、それは無限です。",
            'ko': "두 방향으로, 그것은 무한합니다.",
            'zh': "两个方向上，都是无限的。",
            'zh-Hant': "兩個方向上，都是無限的。",
        },
        {
            'fr': "nous avons pu prendre la relève et vous créer.",
            'en': "we were able to take over and create you.",
            'de': "konnten wir die Stafette übernehmen und Sie schaffen.",
            'es': "hemos podido tomar el relevo y crearlos.",
            'ru': "мы смогли принять эстафету и создать вас.",
            'ja': "われわれは引き継ぎ、あなたがたを創造することができました。",
            'ko': "우리는 이어받아 여러분을 창조할 수 있었습니다.",
            'zh': "我们得以接棒并创造您们。",
            'zh-Hant': "我們得以接棒並創造您們。",
        },
    ],
    ('the-book-which-tells-the-truth', 5, 56): [
        {
            'fr': "comme cela est écrit dans la Genèse biblique.",
            'en': "as it is written in the biblical Genesis.",
            'de': "wie es in der biblischen Genesis geschrieben steht.",
            'es': "como está escrito en el Génesis bíblico.",
            'ru': "как это написано в библейском Бытии.",
            'ja': "聖書の創世記に書かれているように、彼をわれわれの像に作りました。",
            'ko': "성경의 창세기에 기록된 대로, 그를 우리의 형상으로 만들었습니다.",
            'zh': "如圣经创世记所写的。",
            'zh-Hant': "如聖經創世記所寫的。",
        },
        {
            'fr': "ne répondant qu’à leurs besoins ou à leurs fonctions.",
            'en': "answering only to their needs or their functions.",
            'de': "der nur ihren Bedürfnissen oder ihren Funktionen entspräche.",
            'es': "que respondiera solo a sus necesidades o a sus funciones.",
            'ru': "отвечающее лишь их потребностям или их функциям.",
            'ja': "その必要やその機能にしか応えない体を持たねばならないなら、かなり醜いでしょう。",
            'ko': "그 필요나 그 기능에만 응하는 몸을 가져야 한다면, 꽤 추할 것입니다.",
            'zh': "只回应其需要或其功能的身体。",
            'zh-Hant': "只回應其需要或其功能的身體。",
        },
        {
            'fr': "C’est au moins ce que nous attendons pour vous venir en aide.",
            'en': "That is at least what we await in order to come to your aid.",
            'de': "Das ist zumindest, was wir erwarten, um Ihnen zu Hilfe zu kommen.",
            'es': "Es al menos lo que esperamos para venir en su ayuda.",
            'ru': "По крайней мере, это то, чего мы ждём, чтобы прийти вам на помощь.",
            'ja': "少なくともそれが、あなたがたに助けに来るためにわれわれが待っていることです。",
            'ko': "적어도 그것이, 여러분에게 도우러 오기 위하여 우리가 기다리는 것입니다.",
            'zh': "这至少是我们为前来帮助您们而等待的。",
            'zh-Hant': "這至少是我們爲前來幫助您們而等待的。",
        },
    ],
    ('the-book-which-tells-the-truth', 6, 5): [
        {
            'fr': "paysans même pas spécialisés qui ont une intelligence de plus de 50% supérieure à la moyenne...",
            'en': "peasants not even specialized who have an intelligence more than 50% superior to the average…",
            'de': "Bauern, nicht einmal Spezialisten, die eine um mehr als 50% über dem Durchschnitt liegende Intelligenz haben…",
            'es': "campesinos ni siquiera especializados que tienen una inteligencia más de un 50% superior a la media…",
            'ru': "крестьяне, даже не специалисты, у которых разум более чем на 50% выше среднего…",
            'ja': "専門家でさえない労働者や農民で、平均より50%以上高い知性を持つ者たちがいます……",
            'ko': "전문가도 아닌 노동자나 농민으로 평균보다 50% 이상 높은 지성을 가진 자들이 있습니다……",
            'zh': "甚至不是专门人才，却有比平均高百分之五十以上的智力……",
            'zh-Hant': "甚至不是專門人才，卻有比平均高百分之五十以上的智力……",
        },
    ],
    ('the-book-which-tells-the-truth', 6, 7): [
        {
            'fr': "Ceci n’empêche pas le mérite de chacun d’être récompensé.",
            'en': "This does not prevent the merit of each from being rewarded.",
            'de': "Das verhindert nicht, dass das Verdienst eines jeden belohnt werde.",
            'es': "Esto no impide que el mérito de cada uno sea recompensado.",
            'ru': "Это не мешает заслуге каждого быть вознаграждённой.",
            'ja': "これは各人の功績が報いられることを妨げません。",
            'ko': "이것은 각 사람의 공로가 보상받는 것을 막지 않습니다.",
            'zh': "这并不妨碍各人的功劳得到奖赏。",
            'zh-Hant': "這並不妨礙各人的功勞得到獎賞。",
        },
        {
            'fr': "À chacun son mérite.",
            'en': "To each his merit.",
            'de': "Jedem sein Verdienst.",
            'es': "A cada cual su mérito.",
            'ru': "Каждому его заслуга.",
            'ja': "各人にその功績を。",
            'ko': "각 사람에게 그 공로를.",
            'zh': "各人有其功劳。",
            'zh-Hant': "各人有其功勞。",
        },
    ],
    ('the-book-which-tells-the-truth', 6, 18): [
        {
            'fr': "surveillance militaire directe ou effectuée par radar.",
            'en': "military surveillance, direct or carried out by radar.",
            'de': "militärischen Überwachung, direkter oder durch Radar durchgeführter, unterworfen sein.",
            'es': "vigilancia militar directa o efectuada por radar.",
            'ru': "военному наблюдению, прямому или осуществляемому радаром.",
            'ja': "軍事的監視、直接の、またはレーダーによって行われるものに付されてはなりません。",
            'ko': "군사적 감시, 직접의 것이든 레이더로 행해지는 것이든 그것에 부쳐져서는 안 됩니다.",
            'zh': "不得受到军事监视，无论是直接的还是用雷达进行的。",
            'zh-Hant': "不得受到軍事監視，無論是直接的還是用雷達進行的。",
        },
    ],
    ('the-book-which-tells-the-truth', 7, 30): [
        {
            'fr': "seuls les génies ont droit à cette éternité.",
            'en': "only the geniuses have a right to this eternity.",
            'de': "nur die Genies ein Recht auf diese Ewigkeit.",
            'es': "únicamente los genios tienen derecho a esta eternidad.",
            'ru': "лишь гении имеют право на эту вечность.",
            'ja': "天才たちだけがこの永遠への権利を持ちます。",
            'ko': "천재들만이 이 영원에 대한 권리를 가집니다.",
            'zh': "唯有天才有权得到这种永恒。",
            'zh-Hant': "唯有天才有權得到這種永恆。",
        },
    ],
    ('the-book-which-tells-the-truth', 7, 49): [
        {
            'fr': "respecter leur envie de mourir ou de jouer avec la mort dans le cadre des spécialités bien définies.",
            'en': "respect their desire to die or to play with death within the framework of well-defined specialties.",
            'de': "auch ihren Wunsch achten zu sterben oder mit dem Tod zu spielen im Rahmen wohldefinierter Spezialitäten.",
            'es': "respetar también su deseo de morir o de jugar con la muerte en el marco de especialidades bien definidas.",
            'ru': "уважать их желание умереть или играть со смертью в рамках чётко определённых специальностей.",
            'ja': "死ぬあるいは死と戯れる彼らの欲望もまた尊重せねばなりません。",
            'ko': "죽거나 죽음과 노는 그들의 욕망도 존중해야 합니다.",
            'zh': "尊重他们在明确界定的专门项目框架内死或与死嬉戏的愿望。",
            'zh-Hant': "尊重他們在明確界定的專門項目框架內死或與死嬉戲的願望。",
        },
    ],
    # === ETTMTTP ch1-3 ===
    # Markers derived via FR-anchor + relative-position heuristic (scripts/find_split_markers.py).
    # JA/KO/ZH may drift ~1 sentence vs FR/EN due to different sentence structure;
    # acceptable for audiobook (each lang reads its own file).
    ('extraterrestrials-took-me-to-their-planet', 1, 3): [
        {
            'fr': "Peu quand on pense aux quatre milliards d'hommes qui peuplent la Terre, et beaucoup quand on pense au peu de gens qui avaient, au bout de deux ans, décidé de suivre celui qui, il y a deux mille ans, avait également eu la lourde charge d'être initié et d'initier les primitifs de son époque.",
            'en': "Little, when one thinks of the four billion people who populate the Earth; and a great deal, when one thinks of the few people who had, after two years, decided to follow the one who, two thousand years ago, had likewise had the heavy charge of being initiated and of initiating the primitive people of his time.",
            'de': "Wenig, wenn man an die vier Milliarden Menschen denkt, die die Erde bevölkern, und viel, wenn man an die wenigen Leute denkt, die nach zwei Jahren beschlossen hatten, jenem zu folgen, der vor zweitausend Jahren ebenfalls die schwere Last gehabt hatte, eingeweiht zu werden und die Primitiven seiner Zeit einzuweihen.",
            'es': "Poco cuando se piensa en los cuatro mil millones de hombres que pueblan la Tierra, y mucho cuando se piensa en la poca gente que había, al cabo de dos años, decidido seguir a aquel que, hace dos mil años, había tenido igualmente la pesada carga de ser iniciado y de iniciar a los primitivos de su época.",
            'ru': "Мало, когда думаешь о четырёх миллиардах людей, населяющих Землю, и много, когда думаешь о тех немногих людях, которые по прошествии двух лет решили последовать за тем, кто две тысячи лет назад также имел тяжкое бремя быть посвящённым и посвящать первобытных людей своей эпохи.",
            'ja': "この七百人、彼らは誰なのか。",
            'ko': "이 칠백 명, 그들은 누구인가?",
            'zh': "少，当人想到居住在地球上的四十亿人；多，当人想到那些为数不多的人，他们在两年之末决定追随那位在两千年前同样背负了被启蒙并启蒙其时代原始人这一沉重职责的人。",
            'zh-Hant': "少，當人想到居住在地球上的四十億人；多，當人想到那些爲數不多的人，他們在兩年之末決定追隨那位在兩千年前同樣揹負了被啓蒙並啓蒙其時代原始人這一沉重職責的人。",
        },
    ],
    ('extraterrestrials-took-me-to-their-planet', 1, 66): [
        {
            'fr': "J'écrivis une lettre recommandée à l'éditeur qui me répondit que le manuscrit me serait renvoyé mais qu'on ne l'avait toujours pas retrouvé.",
            'en': "I wrote a registered letter to the publisher who answered me that the manuscript would be sent back to me but that it had still not been found.",
            'de': "Ich schrieb einen Einschreibbrief an den Verleger, der mir antwortete, dass das Manuskript mir zurückgeschickt würde, aber dass man es immer noch nicht gefunden habe.",
            'es': "Escribí una carta certificada al editor que me respondió que el manuscrito me sería reenviado pero que aún no lo habían encontrado.",
            'ru': "Я написал заказное письмо издателю, который ответил мне, что рукопись будет мне выслана, но что её всё ещё не нашли.",
            'ja': "私は出版者に書留状を書き、彼は原稿が私に送り返されるだろうが、それがまだ見つかっていないと答えた。",
            'ko': "나는 출판자에게 등기 편지를 썼고, 그는 원고가 나에게 돌려보내질 것이지만 그것을 아직 찾지 못했다고 답했다.",
            'zh': "我给出版商写了一封挂号信，他回答我说原稿会寄还给我，但仍未找到。",
            'zh-Hant': "我給出版商寫了一封掛號信，他回答我說原稿會寄還給我，但仍未找到。",
        },
    ],
    ('extraterrestrials-took-me-to-their-planet', 1, 74): [
        {
            'fr': "J'ai vu également des journalistes faire vraiment et bien leur métier, qui consiste à informer leur public en écrivant ou en disant exactement ce qu'ils ont vu ou ce qu'ils ont lu, et d'autres rapporter, comme ceux du journal Le Point, des choses mensongères et, même après des lettres recommandées leur rappelant que, conformément au droit de réponse, ils doivent rectifier l'article diffamatoire, ne pas rectifier exactement ces écrits ; d'autres encore, comme ceux du journal La Montagne, tout simplement refuser d'annoncer à leur lecteurs que je donnais une conférence à Clermont-Ferrand, abusant d'autre part du fait que ce journal est le seul quotidien de la région.",
            'en': "I have also seen journalists really and well do their job, which consists in informing their public by writing or saying exactly what they have seen or what they have read, and others report, like those of the newspaper Le Point, mendacious things and, even after registered letters reminding them that, in conformity with the right of reply, they must rectify the defamatory article, not rectify these writings exactly; others still, like those of the newspaper La Montagne, simply refuse to announce to their readers that I was giving a lecture at Clermont-Ferrand, abusing moreover the fact that this newspaper is the only daily of the region.",
            'de': "Ich habe auch Journalisten wirklich und gut ihren Beruf ausüben sehen, der darin besteht, ihr Publikum zu informieren, indem sie genau das schreiben oder sagen, was sie gesehen oder was sie gelesen haben, und andere, wie jene der Zeitung Le Point, lügnerische Dinge berichten und, selbst nach Einschreibbriefen, die sie daran erinnerten, dass sie gemäß dem Recht auf Gegendarstellung den verleumderischen Artikel berichtigen müssen, diese Schriften nicht genau berichtigen; wieder andere, wie jene der Zeitung La Montagne, sich einfach weigern, ihren Lesern anzukündigen, dass ich in Clermont-Ferrand einen Vortrag hielt, wobei sie andererseits die Tatsache missbrauchen, dass diese Zeitung die einzige Tageszeitung der Region ist.",
            'es': "He visto también a periodistas ejercer verdadera y bien su oficio, que consiste en informar a su público escribiendo o diciendo exactamente lo que han visto o lo que han leído, y a otros relatar, como los del periódico Le Point, cosas mentirosas y, incluso después de cartas certificadas que les recordaban que, conforme al derecho de respuesta, deben rectificar el artículo difamatorio, no rectificar exactamente estos escritos; otros aún, como los del periódico La Montagne, simplemente negarse a anunciar a sus lectores que daba una conferencia en Clermont-Ferrand, abusando por otra parte del hecho de que este periódico es el único diario de la región.",
            'ru': "Я видел также журналистов, по-настоящему и хорошо исполнявших своё ремесло, которое состоит в информировании своей публики, записывая или говоря точно то, что они видели или что они прочли, и других, сообщавших, как те из газеты Le Point, лживые вещи и, даже после заказных писем, напоминавших им, что, сообразно праву на ответ, они должны исправить клеветническую статью, не исправлявших точно эти писания; других ещё, как те из газеты La Montagne, просто отказывавшихся объявить своим читателям, что я давал доклад в Клермон-Ферране, злоупотребляя, с другой стороны, тем фактом, что эта газета — единственная ежедневная газета региона.",
            'ja': "さらに他の者たち、La Montagne 紙の者たちのように、私がクレルモン＝フェランで講演を行うことを読者に告知することを単に拒み、他方でこの新聞が地域唯一の日刊紙であるという事実を濫用する者を。",
            'ko': "또 다른 이들, La Montagne 지의 자들처럼, 내가 클레르몽페랑에서 강연을 한다고 독자들에게 알리기를 단지 거부하고, 다른 한편 이 신문이 지역 유일의 일간지라는 사실을 남용하는 자를.",
            'zh': "我也看到一些记者真正而出色地从事他们的职业，那职业在于通过准确地写出或说出他们所见或所读来告知他们的公众；以及另一些人，像《Le Point》报的那些人，报道虚假之事，甚至在挂号信提醒他们依据答辩权必须更正那篇诽谤文章之后，仍不准确地更正这些文字；还有另一些人，像《La Montagne》报的那些人，干脆拒绝向他们的读者宣告我在克莱蒙费朗做一场演讲，另一方面滥用这份报纸是该地区唯一日报这一事实。",
            'zh-Hant': "我也看到一些記者真正而出色地從事他們的職業，那職業在於通過準確地寫出或說出他們所見或所讀來告知他們的公衆；以及另一些人，像《Le Point》報的那些人，報道虛假之事，甚至在掛號信提醒他們依據答辯權必須更正那篇誹謗文章之後，仍不準確地更正這些文字；還有另一些人，像《La Montagne》報的那些人，乾脆拒絕向他們的讀者宣告我在克萊蒙費朗做一場演講，另一方面濫用這份報紙是該地區唯一日報這一事實。",
        },
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 1): [
        {
            'fr': "Une association type loi de 1901 était par définition en opposition avec le message, tout au moins sous la forme où nous l'avions structurée puisqu'il y avait vote de tous les membres et donc non respect de la géniocratie qui aurait voulu que seuls les membres les plus intelligents puissent prendre part aux décisions.",
            'en': "An association of the 1901-law type was by definition in opposition to the message, at least in the form in which we had structured it, since there was a vote of all the members and therefore no respect for geniocracy, which would have required that only the most intelligent members be able to take part in decisions.",
            'de': "Eine Vereinigung vom Typ des Gesetzes von 1901 stand per Definition im Widerspruch zur Botschaft, zumindest in der Form, in der wir sie strukturiert hatten, da es eine Abstimmung aller Mitglieder gab und somit keine Achtung der Geniokratie, die gewollt hätte, dass nur die intelligentesten Mitglieder an den Entscheidungen teilnehmen können.",
            'es': "Una asociación del tipo ley de 1901 estaba por definición en oposición con el mensaje, al menos bajo la forma en que la habíamos estructurado, puesto que había voto de todos los miembros y por tanto no respeto de la geniocracia, que habría querido que solo los miembros más inteligentes pudieran tomar parte en las decisiones.",
            'ru': "Ассоциация типа закона 1901 года была по определению в противоречии с посланием, по крайней мере в той форме, в какой мы её структурировали, поскольку имелось голосование всех членов и, следовательно, несоблюдение гениократии, которая желала бы, чтобы только самые умные члены могли принимать участие в решениях.",
            'ja': "少なくとも私たちが構成した形においては、全会員の投票があり、したがって最も知的な会員のみが決定に参加できることを求める天才政治の不尊重があったからである。",
            'ko': "적어도 우리가 그것을 구성한 형태에서는, 모든 회원의 투표가 있었고 따라서 가장 지적인 회원들만이 결정에 참여할 수 있기를 바라는 천재정치의 불존중이 있었기 때문이다.",
            'zh': "1901年法类型的协会按定义与信息相对立，至少在我们所构建的形式下是如此，因为有全体成员的投票，因而不尊重天才政治，而天才政治本应要求只有最有智慧的成员才能参与决策。",
            'zh-Hant': "1901年法類型的協會按定義與信息相對立，至少在我們所構建的形式下是如此，因爲有全體成員的投票，因而不尊重天才政治，而天才政治本應要求只有最有智慧的成員才能參與決策。",
        },
        {
            'fr': "Dans cette société cherchant par tous les moyens à fermer les esprits à coup de religions déistes, d'éducation soporifique, d'émissions de télévision anti-pensée et de batailles politiques étroites, j'allais donc essayer de former, par une initiation, des personnes qui pourraient partir sur les routes du monde pour tenter d'ouvrir à leur tour des esprits.",
            'en': "In this society seeking by all means to close minds with deistic religions, soporific education, anti-thought television programmes and narrow political battles, I was therefore going to try to form, through an initiation, people who could set out on the roads of the world to attempt in their turn to open minds.",
            'de': "In dieser Gesellschaft, die mit allen Mitteln versucht, die Geister zu verschließen, mit deistischen Religionen, einschläfernder Erziehung, denkfeindlichen Fernsehsendungen und engen politischen Kämpfen, würde ich also versuchen, durch eine Einweihung Personen auszubilden, die sich auf die Straßen der Welt aufmachen könnten, um ihrerseits zu versuchen, Geister zu öffnen.",
            'es': "En esta sociedad que busca por todos los medios cerrar las mentes a golpe de religiones deístas, de educación soporífera, de emisiones de televisión antipensamiento y de mezquinas batallas políticas, iba pues a intentar formar, por una iniciación, a personas que pudieran partir por las rutas del mundo para intentar a su vez abrir mentes.",
            'ru': "В этом обществе, стремящемся всеми средствами закрыть умы посредством деистических религий, усыпляющего воспитания, противомыслительных телепередач и узких политических битв, я собирался, таким образом, попытаться сформировать через посвящение людей, которые могли бы отправиться по дорогам мира, чтобы попытаться в свою очередь открывать умы.",
            'ja': "有神論的宗教、眠気を誘う教育、思考に反するテレビ番組、狭量な政治闘争によってあらゆる手段で精神を閉ざそうとするこの社会において、私はしたがって、ある入門を通じて、世界の道へと旅立ち、今度は自ら精神を開こうと試みうる人々を養成しようとしていた。",
            'ko': "유신론적 종교, 졸리게 하는 교육, 사고에 반하는 텔레비전 방송, 편협한 정치 투쟁으로 온갖 수단을 다해 정신을 닫으려 하는 이 사회에서, 그러므로 나는 어떤 입문을 통해, 세계의 길로 떠나 이번에는 스스로 정신을 열려고 시도할 수 있는 사람들을 양성하려 했다.",
            'zh': "在这个用一切手段——有神论的宗教、催眠般的教育、反思考的电视节目、狭隘的政治斗争——试图封闭精神的社会里，因此我将试图通过一种入门，培养能够踏上世界的道路、反过来试图敞开精神的人。",
            'zh-Hant': "在這個用一切手段——有神論的宗教、催眠般的教育、反思考的電視節目、狹隘的政治鬥爭——試圖封閉精神的社會里，因此我將試圖通過一種入門，培養能夠踏上世界的道路、反過來試圖敞開精神的人。",
        },
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 2): [
        {
            'fr': "François vint nous rejoindre fin juillet et nous commençâmes à envisager mon déménagement pour le lendemain de la réunion du 6 août à Clermont-Ferrand.",
            'en': "François came to join us at the end of July and we began to envisage my move for the day after the meeting of 6 August at Clermont-Ferrand.",
            'de': "August in Clermont-Ferrand ins Auge zu fassen.",
            'es': "François vino a reunirse con nosotros a finales de julio y comenzamos a considerar mi mudanza para el día siguiente de la reunión del 6 de agosto en Clermont-Ferrand.",
            'ru': "Франсуа приехал к нам в конце июля, и мы начали обдумывать мой переезд на день после собрания 6 августа в Клермон-Ферране.",
            'ja': "Françoisは7月末に私たちに合流しに来て、私たちはクレルモン=フェランでの8月6日の集まりの翌日に私の引っ越しを行うことを考慮し始めた。",
            'ko': "François는 7월 말에 우리에게 합류하러 왔고, 우리는 클레르몽페랑에서의 8월 6일 모임 다음 날에 내 이사를 행하는 것을 고려하기 시작했다.",
            'zh': "François于7月底来与我们会合，我们开始考虑在克莱蒙费朗8月6日聚会的次日进行我的搬迁。",
            'zh-Hant': "François於7月底來與我們會合，我們開始考慮在克萊蒙費朗8月6日聚會的次日進行我的搬遷。",
        },
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 11): [
        {
            'fr': "La voix me dit alors qu'en suivant les flèches peintes sur le sol, j'arriverais dans une autre pièce où un bain m'attendait.",
            'en': "The voice then told me that by following the arrows painted on the floor, I would arrive in another room where a bath awaited me.",
            'de': "Die Stimme sagte mir dann, dass ich, wenn ich den auf dem Boden gemalten Pfeilen folgte, in einen anderen Raum gelangen würde, wo ein Bad mich erwartete.",
            'es': "La voz me dijo entonces que siguiendo las flechas pintadas en el suelo, llegaría a otra sala donde un baño me esperaba.",
            'ru': "В следующем помещении я нашёл действительно ванну, встроенную в пол.",
            'ja': "次の部屋で、私は実際に床に埋め込まれた浴槽を見つけた。",
            'ko': "다음 방에서, 나는 실제로 바닥에 박힌 욕조를 발견했다.",
            'zh': "在下一个房间里，我确实找到一个嵌入地板的浴缸。",
            'zh-Hant': "在下一個房間裏，我確實找到一個嵌入地板的浴缸。",
        },
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 22): [
        {
            'fr': "Au contraire, cela les amènerait très vite à suivre la voie tracée par votre pays en l'imitant.",
            'en': "On the contrary, that would bring them very quickly to follow the path traced by your country by imitating it.",
            'de': "Im Gegenteil, das würde sie sehr schnell dazu bringen, dem von Ihrem Land vorgezeichneten Weg zu folgen, indem sie es nachahmen.",
            'es': "Al contrario, eso los llevaría muy rápido a seguir la vía trazada por su país imitándolo.",
            'ru': "Напротив, это привело бы их очень быстро к тому, чтобы следовать по пути, начертанному вашей страной, подражая ей.",
            'ja': "反対に、それは彼らをごく速やかに、それを模倣することであなたがたの国によって描かれた道に従うよう導くでしょう。",
            'ko': "반대로, 그것은 그들을 아주 빠르게, 그것을 모방함으로써 당신들 나라가 그린 길을 따르도록 이끌 것입니다.",
            'zh': "相反，这会很快引导它们效仿、遵循你们国家所描绘的道路。",
            'zh-Hant': "相反，這會很快引導它們效仿、遵循你們國家所描繪的道路。",
        },
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 25): [
        {
            'fr': "Vous savez également que nous avons découvert que sur l'infiniment petit il y a de la vie intelligente organisée, très certainement aussi évoluée que nous et comparable à ce que nous sommes nous-mêmes ; cela nous avons pu le prouver.",
            'en': "You also know that we have discovered that on the infinitely small there is organized intelligent life, very certainly as evolved as we and comparable to what we ourselves are; that we have been able to prove.",
            'de': "Sie wissen auch, dass wir entdeckt haben, dass es im unendlich Kleinen organisiertes intelligentes Leben gibt, ganz gewiss so entwickelt wie wir und vergleichbar mit dem, was wir selbst sind; das haben wir beweisen können.",
            'es': "Saben igualmente que hemos descubierto que en lo infinitamente pequeño hay vida inteligente organizada, muy ciertamente tan evolucionada como nosotros y comparable a lo que nosotros mismos somos; eso lo hemos podido probar.",
            'ru': "Вы знаете также, что мы открыли, что в бесконечно малом есть организованная разумная жизнь, совершенно наверняка столь же развитая, как мы, и сравнимая с тем, что мы сами есть; это мы смогли доказать.",
            'ja': "あなたはまた、無限に小さなものの上に組織された知的生命があり、ごく確実に私たちと同じく進化し、私たち自身があるものに比肩しうることを私たちが発見したことをご存じです。",
            'ko': "당신은 또한, 무한히 작은 것 위에 조직된 지적 생명이 있고, 아주 확실히 우리만큼 진화했으며 우리 자신이 그러한 것에 비견될 수 있음을 우리가 발견했음을 아십니다.",
            'zh': "您同样知道，我们已发现，在无限小之中有有组织的智慧生命，非常确定地与我们一样进化，并可与我们自身所是的相比；这我们已能证明。",
            'zh-Hant': "您同樣知道，我們已發現，在無限小之中有有組織的智慧生命，非常確定地與我們一樣進化，並可與我們自身所是的相比；這我們已能證明。",
        },
        {
            'fr': "En ce moment dans un atome de votre bras, des millions de mondes naissent et d'autres meurent, croyant ou non à un dieu et à une âme et tandis qu'un millénaire s'écoule, l'être gigantesque dont le soleil est un atome n'a eu que le temps de faire un pas.",
            'en': "At this moment in an atom of your arm, millions of worlds are being born and others are dying, believing or not in a god and a soul and while a millennium elapses, the gigantic being of which the sun is an atom has had only the time to take one step.",
            'de': "In diesem Augenblick werden in einem Atom Ihres Arms Millionen von Welten geboren, und andere sterben, ob sie an einen Gott und an eine Seele glauben oder nicht, und während ein Jahrtausend verstreicht, hat das gigantische Wesen, dessen Atom die Sonne ist, nur die Zeit gehabt, einen Schritt zu tun.",
            'es': "En este momento en un átomo de su brazo, millones de mundos nacen y otros mueren, creyendo o no en un dios y en un alma y mientras un milenio transcurre, el ser gigantesco del cual el sol es un átomo no ha tenido más que el tiempo de dar un paso.",
            'ru': "В этот момент в атоме вашей руки рождаются миллионы миров и другие умирают, веря или не веря в бога и в душу, и пока тысячелетие протекает, гигантское существо, атомом которого является солнце, имело лишь время сделать один шаг.",
            'ja': "この瞬間あなたの腕の一つの原子の中で、神と魂を信じるか否かにかかわらず、何百万もの世界が生まれ、他のものが死んでいき、そして一千年があなたにとって過ぎ去る間に、太陽がその一原子である巨大な存在は一歩を踏み出す時間しかなかったのです。",
            'ko': "이 순간 당신 팔의 한 원자 안에서, 신과 영혼을 믿든 안 믿든, 수백만 개의 세계가 태어나고 다른 것들이 죽어 가며, 그리고 천 년이 당신에게 흐르는 동안, 태양이 그 한 원자인 거대한 존재는 한 걸음을 내디딜 시간밖에 갖지 못했습니다.",
            'zh': "此刻在您手臂的一个原子里，数百万个世界正在诞生，另一些正在死去，无论信或不信一位神和一个灵魂，而当一千年对您流逝时，太阳是其一个原子的那个巨大存在只有时间迈出一步。",
            'zh-Hant': "此刻在您手臂的一個原子裏，數百萬個世界正在誕生，另一些正在死去，無論信或不信一位神和一個靈魂，而當一千年對您流逝時，太陽是其一個原子的那個巨大存在只有時間邁出一步。",
        },
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 30): [
        {
            'fr': "Ces machines fantastiques qui font le travail de cinq cents personnes doivent permettre à ces cinq cents personnes de vivre au lieu de servir à engraisser une seule personne:",
            'en': "the boss.",
            'de': "den Chef.",
            'es': "Esas máquinas fantásticas que hacen el trabajo de quinientas personas deben permitir a esas quinientas personas vivir en lugar de servir para engordar a una sola persona:",
            'ru': "Эти фантастические машины, которые делают работу пятисот человек, должны позволить этим пятистам человекам жить, вместо того чтобы служить тому, чтобы откармливать одного-единственного человека:",
            'ja': "いかなる人も他人の奉仕にあってはならず、賃金と引き換えに他人のために働いてもなりません。",
            'ko': "어떤 인간도 다른 사람의 봉사에 있어서도 안 되고 임금과 맞바꿔 다른 사람을 위해 일해서도 안 됩니다.",
            'zh': "任何人都不应处于另一人的服务之中，也不应为换取薪水而为另一人工作。",
            'zh-Hant': "任何人都不應處於另一人的服務之中，也不應爲換取薪水而爲另一人工作。",
        },
        {
            'fr': "Mais vous n'êtes plus des primitifs maintenant !",
            'en': "But you are no longer primitives now!",
            'de': "Aber Sie sind jetzt keine Primitiven mehr!",
            'es': "¡Pero ustedes ya no son primitivos ahora!",
            'ru': "Эти три термина, труд-семья-родина, к тому же всегда поддерживались первобытными религиями.",
            'ja': "しかしあなたがたはもはや今や原始人ではありません！",
            'ko': "그러나 당신들은 더 이상 이제 원시인이 아닙니다!",
            'zh': "这三个词，劳动-家庭-祖国，此外一直都被原始的宗教所支持。",
            'zh-Hant': "這三個詞，勞動-家庭-祖國，此外一直都被原始的宗教所支持。",
        },
        {
            'fr': "Enfin, ne vous laissez pas avoir par ceux qui vous disent que le service militaire permet d'apprendre à se servir d'un fusil et que \"ça peut toujours servir\" tout en entassant des missiles nucléaires ; ils veulent vous apprendre la violence, vous apprendre à ne pas être effrayé de tuer un homme comme vous sous prétexte qu'il porte un autre uniforme, faire en sorte que cela devienne pour vous un geste machinal, à force de manoeuvres contre des cibles d'entraînement.",
            'en': "Finally, do not let yourselves be had by those who tell you that military service permits learning to use a rifle and that \"it can always serve\" all the while piling up nuclear missiles; they want to teach you violence, to teach you not to be frightened of killing a man like yourself under pretext that he wears another uniform, to make it so that this becomes for you a mechanical gesture, by dint of manoeuvres against training targets.",
            'de': "Lassen Sie sich nicht von denen hereinlegen, die Ihnen sagen, man müsse für das Vaterland kämpfen!",
            'es': "Por fin, no se dejen engañar por aquellos que les dicen que el servicio militar permite aprender a servirse de un fusil y que \"eso siempre puede servir\" mientras amontonan misiles nucleares; quieren enseñarles la violencia, enseñarles a no estar asustados de matar a un hombre como ustedes bajo pretexto de que lleva otro uniforme, hacer de modo que eso se vuelva para ustedes un gesto maquinal, a fuerza de maniobras contra blancos de entrenamiento.",
            'ru': "Наконец, не давайте провести себя тем, кто говорит вам, что военная служба позволяет научиться пользоваться ружьём и что «это всегда может пригодиться», нагромождая при этом ядерные ракеты; они хотят научить вас насилию, научить вас не пугаться убить человека, как вы, под предлогом того, что он носит другую форму, сделать так, чтобы это стало для вас машинальным жестом, в силу манёвров против учебных мишеней.",
            'ja': "祖国のために戦わねばならないとあなたがたに言う者たちにだまされてはなりません！",
            'ko': "그들은 당신들에게 폭력을 가르치고, 그가 다른 제복을 입었다는 구실로 당신들 자신과 같은 인간을 죽이는 것을 두려워하지 않도록 당신들에게 가르치고, 훈련 표적에 대한 연습을 거듭함으로써, 그것이 당신들에게 기계적인 몸짓이 되도록 하고 싶어 합니다.",
            'zh': "最后，不要被那些一边堆积核导弹一边对你们说兵役能让人学会使用步枪、‘这总能派上用场’的人骗了；他们想教你们暴力，教你们不要害怕以他穿着另一种制服为借口去杀一个像你们自己一样的人，通过对训练靶子的反复演习，使这对你们成为一个机械的举动。",
            'zh-Hant': "最後，不要被那些一邊堆積核導彈一邊對你們說兵役能讓人學會使用步槍、‘這總能派上用場’的人騙了；他們想教你們暴力，教你們不要害怕以他穿着另一種制服爲藉口去殺一個像你們自己一樣的人，通過對訓練靶子的反覆演習，使這對你們成爲一個機械的舉動。",
        },
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 31): [
        {
            'fr': "Mais vous pouvez vraiment considérer que la télévision est le système nerveux de l'humanité, qui permet à chacun de prendre conscience de l'existence des autres, de les voir vivre et qui évite ainsi de se faire, sur leur compte, des idées fausses qui amènent une crainte de \"l'étranger\".",
            'en': "But you can truly consider that television is the nervous system of humanity, which permits each one to take consciousness of the existence of others, to see them live and which thus avoids forming, on their account, false ideas which bring a fear of \"the foreigner\".",
            'de': "Aber Sie können wirklich das Fernsehen als das Nervensystem der Menschheit betrachten, das jedem erlaubt, sich der Existenz der anderen bewusst zu werden, sie leben zu sehen, und das so vermeidet, sich auf ihre Rechnung falsche Vorstellungen zu machen, die eine Furcht vor dem \"Fremden\" mit sich bringen.",
            'es': "Pero ustedes pueden realmente considerar que la televisión es el sistema nervioso de la humanidad, que permite a cada uno tomar conciencia de la existencia de los demás, verlos vivir y que evita así formarse, a costa de ellos, ideas falsas que llevan a un temor del \"extranjero\".",
            'ru': "Но вы можете действительно считать, что телевидение — это нервная система человечества, которая позволяет каждому осознавать существование других, видеть их живущими и которая избегает таким образом составлять о них ложные представления, приводящие к страху «чужого».",
            'ja': "しかしあなたがたは本当に、テレビが人類の神経系であり、各々が他者の存在を意識し、彼らが生きているのを見ることを可能にし、こうして彼らについて『よそ者』への恐れをもたらす誤った観念を作ることを避けさせると考えることができます。",
            'ko': "그러나 당신들은 정말로, 텔레비전이 인류의 신경계이며, 저마다가 타자의 존재를 의식하고 그들이 사는 것을 보는 것을 가능하게 하고, 이렇게 그들에 대해 『외국인』에 대한 두려움을 가져오는 그릇된 관념을 만드는 것을 피하게 한다고 여길 수 있습니다.",
            'zh': "但你们真的能认为，电视是人类的神经系统，它使每一个人能意识到他人的存在，看见他们生活，从而避免对他们形成带来对‘外人’恐惧的错误观念。",
            'zh-Hant': "但你們真的能認爲，電視是人類的神經系統，它使每一個人能意識到他人的存在，看見他們生活，從而避免對他們形成帶來對‘外人’恐懼的錯誤觀念。",
        },
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 33): [
        {
            'fr': "Je pus découvrir un paysage merveilleux,paradisiaque, et je ne trouve en fait aucun qualificatif pour décrire l'enchantement procuré par la vision de fleurs immenses, toutes plus belles les unes que les autres, au milieu desquelles se promenaient des animaux inimaginables, oiseaux aux plumages multicolores, écureuils roses et bleus à la tête d'oursons grimpant dans les branches d'arbres portant des fruits énormes en même temps que des fleurs gigantesques.",
            'en': "I could discover a marvellous, paradisiacal landscape, and I find in fact no qualifier to describe the enchantment procured by the vision of immense flowers, each more beautiful than the last, in the midst of which strolled unimaginable animals, birds with multicoloured plumage, pink and blue squirrels with the heads of bear cubs climbing in the branches of trees bearing enormous fruits at the same time as gigantic flowers.",
            'de': "Ich konnte eine wunderbare, paradiesische Landschaft entdecken, und ich finde in Wirklichkeit kein Beiwort, um die Verzauberung zu beschreiben, die der Anblick riesiger Blumen verschaffte, eine schöner als die andere, in deren Mitte unvorstellbare Tiere umherspazierten, Vögel mit vielfarbigem Gefieder, rosa und blaue Eichhörnchen mit dem Kopf von Bärenjungen, die in die Zweige von Bäumen kletterten, die enorme Früchte zugleich mit gigantischen Blumen trugen.",
            'es': "Pude descubrir un paisaje maravilloso, paradisíaco, y no encuentro en realidad ningún calificativo para describir el encantamiento procurado por la visión de flores inmensas, cada una más bella que la otra, en medio de las cuales se paseaban animales inimaginables, pájaros de plumajes multicolores, ardillas rosas y azules con cabeza de oseznos trepando por las ramas de árboles que llevaban frutos enormes al mismo tiempo que flores gigantescas.",
            'ru': "Я смог обнаружить чудесный, райский пейзаж, и я не нахожу на деле никакого определения, чтобы описать очарование, доставленное видением огромных цветов, один прекраснее другого, среди которых разгуливали невообразимые животные, птицы с многоцветным оперением, розовые и синие белки с головой медвежат, карабкающиеся по ветвям деревьев, несущих огромные плоды одновременно с гигантскими цветами.",
            'ja': "その花々の真ん中を、想像もつかない動物たち、多色の羽の鳥たち、巨大な花々と同時に巨大な果実を実らせる木々の枝をよじ登る、子熊の頭をしたピンクと青のリスたちが歩き回っていた。",
            'ko': "그 꽃들의 한가운데를, 상상도 못할 동물들, 다채로운 깃털의 새들, 거대한 꽃들과 동시에 거대한 열매를 맺는 나무들의 가지를 기어오르는, 새끼 곰의 머리를 한 분홍색과 파란색 다람쥐들이 거닐고 있었다.",
            'zh': "我能发现一片奇妙的、乐园般的景色，实际上我找不到任何形容词来描述巨大的花朵——一朵比一朵更美——之景所带来的迷醉，在花朵中间漫步着无法想象的动物、羽毛多彩的鸟、有小熊头的粉色和蓝色松鼠，攀爬在同时结着巨大果实和巨大花朵的树木的枝条上。",
            'zh-Hant': "我能發現一片奇妙的、樂園般的景色，實際上我找不到任何形容詞來描述巨大的花朵——一朵比一朵更美——之景所帶來的迷醉，在花朵中間漫步着無法想象的動物、羽毛多彩的鳥、有小熊頭的粉色和藍色松鼠，攀爬在同時結着巨大果實和巨大花朵的樹木的枝條上。",
        },
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 38): [
        # opens with « (Yahweh running speech) — first piece keeps the «, continuation has no «
        {
            'fr': "Sur la planète où nous sommes actuellement vivent en ce moment huit mille quatre cents Terriens, ayant atteint durant leur vie un niveau d'ouverture d'esprit sur l'infini suffisant ou ayant permis à l'humanité terrestre de s'éloigner de son niveau primitif par ses découvertes, ses écrits, sa façon d'organiser la société, ses actes exemplaires par leur fraternité, leur amour ou leur désintéressement, et d'autre part les sept cents Elohim membres du conseil des éternels.",
            'en': "On the planet where we are currently live at this moment eight thousand four hundred Terrans, having attained during their life a level of opening of mind on the infinite sufficient or having permitted terrestrial humanity to move away from its primitive level by its discoveries, its writings, its way of organizing society, its acts exemplary by their fraternity, their love or their disinterestedness, and on the other hand the seven hundred Elohim members of the council of the eternals.",
            'de': "Auf dem Planeten, wo wir uns gegenwärtig befinden, leben in diesem Augenblick achttausendvierhundert Erdbewohner, die während ihres Lebens ein hinreichendes Niveau der Geistesöffnung für das Unendliche erreicht haben oder die der irdischen Menschheit erlaubt haben, sich durch ihre Entdeckungen, ihre Schriften, ihre Art, die Gesellschaft zu organisieren, ihre durch Brüderlichkeit, Liebe oder Uneigennützigkeit beispielhaften Taten von ihrem primitiven Niveau zu entfernen, und andererseits die siebenhundert Elohim, Mitglieder des Rates der Ewigen.",
            'es': "En el planeta donde nos encontramos actualmente viven en este momento ocho mil cuatrocientos Terrícolas, que han alcanzado durante su vida un nivel de apertura de mente a lo infinito suficiente o que han permitido a la humanidad terrestre alejarse de su nivel primitivo por sus descubrimientos, sus escritos, su manera de organizar la sociedad, sus actos ejemplares por su fraternidad, su amor o su desinterés, y por otra parte los setecientos Elohim miembros del consejo de los eternos.",
            'ru': "На планете, где мы находимся в настоящее время, живёт в этот момент восемь тысяч четыреста землян, достигших в течение своей жизни достаточного уровня открытости разума бесконечному или позволивших земному человечеству удалиться от своего первобытного уровня своими открытиями, своими писаниями, своей манерой организовывать общество, своими поступками, образцовыми по их братству, их любви или их бескорыстию, а с другой стороны семьсот Элохим, членов совета вечных.",
            'ja': "そして他方には永遠者の評議会の構成員である七百人のエロヒムがいます。",
            'ko': "그리고 다른 한편에는 영원자 평의회의 구성원인 칠백 명의 엘로힘이 있습니다.",
            'zh': "在我们目前所在的行星上，此刻生活着八千四百名地球人，他们在其一生中到达了对无限的精神敞开的足够水平，或者通过其发现、其著作、其组织社会的方式、其因友爱、爱或无私而堪为典范的行为，使地球人类得以远离其原始水平；另一方面有七百名作为永恒者评议会成员的埃洛希姆。",
            'zh-Hant': "在我們目前所在的行星上，此刻生活着八千四百名地球人，他們在其一生中到達了對無限的精神敞開的足夠水平，或者通過其發現、其著作、其組織社會的方式、其因友愛、愛或無私而堪爲典範的行爲，使地球人類得以遠離其原始水平；另一方面有七百名作爲永恆者評議會成員的埃洛希姆。",
        },
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 40): [
        {
            'fr': "Leur durée de vie est similaire à la nôtre, c'est-à-dire, grâce à une petite intervention chirurgicale, de sept-cents ans environ.",
            'en': "Their duration of life is similar to ours, that is to say, thanks to a small surgical intervention, about seven hundred years.",
            'de': "Ihre Lebensdauer ist der unseren ähnlich, das heißt, dank einer kleinen chirurgischen Intervention, etwa siebenhundert Jahre.",
            'es': "Su duración de vida es similar a la nuestra, es decir, gracias a una pequeña intervención quirúrgica, de unos setecientos años.",
            'ru': "Их продолжительность жизни подобна нашей, то есть, благодаря маленькому хирургическому вмешательству, около семисот лет.",
            'ja': "彼らの寿命は私たちのと同様、すなわち小さな外科的介入のおかげで約七百年です。",
            'ko': "그들의 수명은 우리의 것과 비슷하며, 즉 작은 외과적 개입 덕분에 약 칠백 년입니다.",
            'zh': "他们的寿命与我们的相似，也就是说，借助一次小小的外科干预，约七百年。",
            'zh-Hant': "他們的壽命與我們的相似，也就是說，藉助一次小小的外科干預，約七百年。",
        },
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 73): [
        {
            'fr': "Il me répondit qu'il s'agissait de la femme idéale esthétiquement parlant ou plutôt d'un des trois types de femme idéale défini par l'ordinateur en fonction des goûts de la majorité des résidents de la planète, mais que je pouvais demander toutes modifications qui me feraient plaisir.",
            'en': "He answered me that it was a question of the ideal woman aesthetically speaking or rather of one of the three types of ideal woman defined by the computer in function of the tastes of the majority of the residents of the planet, but that I could ask all modifications which would give me pleasure.",
            'de': "Er antwortete mir, es handle sich um die ästhetisch gesprochen ideale Frau oder vielmehr um einen der drei vom Computer nach dem Geschmack der Mehrheit der Bewohner des Planeten definierten Typen idealer Frauen, aber dass ich alle Veränderungen verlangen könne, die mir Vergnügen machen würden.",
            'es': "Me respondió que se trataba de la mujer ideal estéticamente hablando o más bien de uno de los tres tipos de mujer ideal definido por el ordenador en función de los gustos de la mayoría de los residentes del planeta, pero que yo podía pedir todas las modificaciones que me dieran placer.",
            'ru': "Он ответил мне, что речь идёт об идеальной женщине эстетически говоря, или, скорее, об одном из трёх типов идеальной женщины, определённом компьютером в зависимости от вкусов большинства жителей планеты, но что я могу попросить все изменения, которые доставили бы мне удовольствие.",
            'ja': "彼は私に、それは美的に言って理想の女、というよりむしろ、惑星の住民の大多数の好みに応じてコンピューターによって定義された三種類の理想の女の一つだが、私を喜ばせるであろうあらゆる変更を求めることができると答えた。",
            'ko': "그는 내게, 그것은 미적으로 말해 이상적인 여자, 더 정확히는 행성 거주자의 대다수의 취향에 따라 컴퓨터에 의해 정의된 세 종류의 이상적인 여자 중 하나이지만, 나를 기쁘게 할 모든 변경을 청할 수 있다고 답했다.",
            'zh': "他回答我说这是审美上说的理想女人，或更确切地说是计算机根据这个行星大多数居民的喜好所定义的三种理想女人类型之一，但我能要求一切会让我高兴的修改。",
            'zh-Hant': "他回答我說這是審美上說的理想女人，或更確切地說是計算機根據這個行星大多數居民的喜好所定義的三種理想女人類型之一，但我能要求一切會讓我高興的修改。",
        },
    ],
    ('extraterrestrials-took-me-to-their-planet', 2, 83): [
        # opens with « (Yahweh running speech)
        {
            'fr': "Une note est attribuée à chacun en fonction de ses actions durant sa vie, selon qu'il ait cheminé vers l'amour et la vérité, ou vers la haine et l'obscurantisme.",
            'en': "A mark is attributed to each one in function of his actions during his life, according to whether he has walked towards love and truth, or towards hate and obscurantism.",
            'de': "Eine Note wird jedem zugeteilt, je nach seinen Handlungen während seines Lebens, je nachdem, ob er zur Liebe und zur Wahrheit geschritten ist oder zum Hass und zum Obskurantismus.",
            'es': "Una nota se atribuye a cada uno en función de sus acciones durante su vida, según haya caminado hacia el amor y la verdad, o hacia el odio y el oscurantismo.",
            'ru': "Оценка приписывается каждому в зависимости от его действий в течение его жизни, в зависимости от того, шёл ли он к любви и истине или к ненависти и обскурантизму.",
            'ja': "各々に、その生涯における彼の行為に応じて、彼が愛と真実に向かって歩んだか、憎しみと蒙昧主義に向かって歩んだかに応じて、評点が与えられます。",
            'ko': "저마다에게, 그 생애에서의 그의 행위에 따라, 그가 사랑과 진실을 향해 걸었는지, 증오와 몽매주의를 향해 걸었는지에 따라, 평점이 부여됩니다.",
            'zh': "一个评分按照每一个在其一生中的行为被赋予给他，依他是走向爱与真理，还是走向恨与蒙昧主义。",
            'zh-Hant': "一個評分按照每一個在其一生中的行爲被賦予給他，依他是走向愛與真理，還是走向恨與矇昧主義。",
        },
    ],
    ('extraterrestrials-took-me-to-their-planet', 3, 2): [
        {
            'fr': "\"Ce n'est pas parce que nul ne voit la vérité qu'elle devient une erreur\", aussi si vous entreprenez d'ouvrir cette porte, ignorez les sarcasmes de ceux qui n'ont rien vu ou qui, ayant vu, font semblant de ne rien voir par peur de ce qu'ils ne connaissent pas.",
            'en': "\"It is not because no one sees the truth that it becomes an error\", so if you undertake to open this door, ignore the sarcasm of those who have seen nothing or who, having seen, pretend to see nothing out of fear of what they do not know.",
            'de': "„Es ist nicht deshalb, weil niemand die Wahrheit sieht, dass sie zu einem Irrtum wird“; wenn ihr es also unternehmt, diese Tür zu öffnen, ignoriert den Spott derer, die nichts gesehen haben, oder die, nachdem sie gesehen haben, vorgeben, nichts zu sehen, aus Angst vor dem, was sie nicht kennen.",
            'es': "«No es porque nadie vea la verdad que ésta se vuelve un error»; así pues, si emprendéis abrir esta puerta, ignorad los sarcasmos de quienes no han visto nada o que, habiendo visto, fingen no ver nada por miedo de lo que no conocen.",
            'ru': "«Не потому, что никто не видит истину, она становится заблуждением»; итак, если вы предпринимаете открыть эту дверь, не обращайте внимания на насмешки тех, кто ничего не видел, или кто, увидев, делает вид, что ничего не видит, из страха перед тем, чего не знает.",
            'ja': "ですからもしあなたがこの扉を開けようと企てるなら、何も見なかった者たち、あるいは見たのに自分の知らないものへの恐れから何も見ないふりをする者たちの皮肉を、無視なさい。",
            'ko': "그러므로 만일 그대가 이 문을 열려고 도모한다면, 아무것도 보지 못한 자들, 혹은 보았으면서도 자신이 알지 못하는 것에 대한 두려움 때문에 아무것도 보지 못하는 척하는 자들의 조롱을 무시하십시오.",
            'zh': "「并非因为没有人看见真理，真理就成为谬误」；因此，倘若您着手开启这道门，请无视那些什么也没看见的人，或那些看见了却因害怕自己所不知道的事物而假装什么也没看见的人的讥讽。",
            'zh-Hant': "「並非因爲沒有人看見真理，真理就成爲謬誤」；因此，倘若您着手開啓這道門，請無視那些什麼也沒看見的人，或那些看見了卻因害怕自己所不知道的事物而假裝什麼也沒看見的人的譏諷。",
        },
    ],
    # ch3 p191: split at the only period + a semicolon-equivalent (option C, 3 pieces).
    # JA/KO use period equivalents since their sentence structure differs from FR's
    # semicolon-chained meditation. Drift is acceptable for audiobook.
    ('extraterrestrials-took-me-to-their-planet', 3, 191): [
        # split 1: end of opening "city → continent" zoom-out
        {
            'fr': "puis le continent.",
            'en': "then the continent.",
            'de': "dann der Kontinent.",
            'es': "luego el continente.",
            'ru': "затем континент.",
            'ja': "次いで大陸がそうなるまでです。",
            'ko': "그다음 대륙이 그렇게 될 때까지입니다.",
            'zh': "然后是大陆。",
            'zh-Hant': "然後是大陸。",
        },
        # split 2: end of "Earth → solar system → Elohim/eternals planet" beat
        # FR/EN/DE/ES/RU split at the semicolon at "...l'éternité ;"
        # JA/KO/ZH split at the equivalent sentence-end after the Elohim/eternals reference
        {
            'fr': "où tu seras un jour admis pour l'éternité ;",
            'en': "where you will one day be admitted for eternity;",
            'de': "wo du eines Tages für die Ewigkeit aufgenommen werden wirst;",
            'es': "donde un día serás admitido para la eternidad;",
            'ru': "куда ты однажды будешь принят на вечность;",
            'ja': "あなたがいつの日か永遠に受け入れられる永遠者の惑星があります──に対して、自分を位置づけなさい。",
            'ko': "그대가 언젠가 영원히 받아들여질 영원자의 행성이 있습니다 — 에 대하여 자기를 자리매김하십시오.",
            'zh': "您有朝一日将被永恒地接纳于此——来定位自己；",
            'zh-Hant': "您有朝一日將被永恆地接納於此——來定位自己；",
        },
    ],
    # === LWTE ===
    # NOTE: LWTE has FR + partial-EN translations only; DE/ES/RU/JA/KO/ZH/ZH-Hant are empty strings.
    # We split anyway to preserve paragraph ID alignment across languages (required by the
    # interlinear feature). Empty languages stay empty; their pieces stay empty too.
    # The EN translation is not paragraph-aligned to FR for most paragraphs — splits produce
    # whatever the heuristic finds at the same relative position, which is fine since EN is
    # already non-aligned.
    ('lets-welcome-the-extraterrestrials', 1, 28): [
        {
            'fr': "En résumé, l'erreur de ces méthodes de datation est de partir du principe que le comportement atomique actuel a toujours été le même et partant de là de faire un calcul dont les bases sont fausses, car rien n'est constant dans l'univers ni dans l'espace ni dans le temps.",
            'en': "FAQ - NOTHING IS CONSTANT IN SPACE AND TIME",
            'de': "",
            'es': "",
            'ru': "",
            'ja': "",
            'ko': "",
            'zh': "",
            'zh-Hant': "",
        },
    ],
    ('lets-welcome-the-extraterrestrials', 1, 85): [
        {
            'fr': "Il faut donc faire un choix, et un parti politique ne pèse pas lourd face aux messages des Elohim.",
            'en': "They will have to be stronger than the beliefs that they have engendered.",
            'de': "",
            'es': "",
            'ru': "",
            'ja': "",
            'ko': "",
            'zh': "",
            'zh-Hant': "",
        },
    ],
    ('lets-welcome-the-extraterrestrials', 1, 176): [
        {
            'fr': "L'homme total détruit cette maison, trace des plans adaptés à ses goûts et à sa fantaisie, récupère dans les ruines de l'ancienne construction les matériaux qui lui semblent réutilisables et, en les combinant à de nouveaux composants, fabrique une nouvelle habitation parfaitement adaptée à sa véritable personnalité.",
            'en': "The mere fact that Man is a self-programming computer does not make him different from the machine.",
            'de': "",
            'es': "",
            'ru': "",
            'ja': "",
            'ko': "",
            'zh': "",
            'zh-Hant': "",
        },
        {
            'fr': "Ces maisons alignées et toutes semblables, vendues maintenant en série et formant d'abominables villages uniformes sont le reflet exact du niveau de conscience de ceux qui les habitent.",
            'en': "It could be also possible to program a computer so that it could be self-programming.",
            'de': "",
            'es': "",
            'ru': "",
            'ja': "",
            'ko': "",
            'zh': "",
            'zh-Hant': "",
        },
    ],
    ('lets-welcome-the-extraterrestrials', 2, 59): [
        {
            'fr': "Nous vous proposons de nous aider à accélérer cette catastrophe finale qui ne fera que purifier l'univers en détruisant des êtres qui sont le fruit d'une expérience ratée.",
            'en': "For this, you will also have to tell them that you have met with an extra-terrestrial, and he has warned you of an invasion of the Earth by them.",
            'de': "",
            'es': "",
            'ru': "",
            'ja': "",
            'ko': "",
            'zh': "",
            'zh-Hant': "",
        },
        {
            'fr': "Si vous acceptez de m'aider en appliquant mon plan qui repose sur une activation des différents racismes existant en l'homme afin d'obtenir l'éclatement d'une guerre mondiale raciale, vous serez rapidement puissant et riche.",
            'en': "In this way, Humanity will increase its armaments to prepare itself against possible attack from the sky.",
            'de': "",
            'es': "",
            'ru': "",
            'ja': "",
            'ko': "",
            'zh': "",
            'zh-Hant': "",
        },
    ],
    ('lets-welcome-the-extraterrestrials', 3, 41): [
        {
            'fr': "Il était indiqué également si le choc engendré était léger, moyen, fort ou très fort.",
            'en': "20.",
            'de': "",
            'es': "",
            'ru': "",
            'ja': "",
            'ko': "",
            'zh': "",
            'zh-Hant': "",
        },
    ],
    ('lets-welcome-the-extraterrestrials', 3, 74): [
        {
            'fr': "Il y a toujours une justice pour justifier les pires injustices.",
            'en': "Unfortunately, they have woken up too late.",
            'de': "",
            'es': "",
            'ru': "",
            'ja': "",
            'ko': "",
            'zh': "",
            'zh-Hant': "",
        },
    ],
    ('lets-welcome-the-extraterrestrials', 4, 88): [
        {
            'fr': "là réside la vérité; – L'évolution par hasard, selon une succession de hasards, c'est un mythe ; au contraire, l'évolution réside d'abord dans l'esprit des créateurs ; – Personne ne peut appartenir à un autre; nous ne sommes pas la propriété de personne ; d'où incidences dans les relations de travail, le mariage, les relations humaines, etc.",
            'en': "",
            'de': "",
            'es': "",
            'ru': "",
            'ja': "",
            'ko': "",
            'zh': "",
            'zh-Hant': "",
        },
        {
            'fr': "penser, créer, s'épanouir; – Comment s'aimer soi-même pour aimer vraiment les autres; – Les solutions proposées aux grands problèmes qui assaillent l'humanité :",
            'en': "",
            'de': "",
            'es': "",
            'ru': "",
            'ja': "",
            'ko': "",
            'zh': "",
            'zh-Hant': "",
        },
    ],
    ('the-book-which-tells-the-truth', 3, 163): [
        # split 1: end of cloud/suits/four-creators commentary
        {
            'fr': 'vos cosmonautes sont très brillantes.',
            'en': 'the suits of your cosmonauts are very shiny.',
            'de': 'die Anzüge Ihrer Kosmonauten sehr glänzend sind.',
            'es': 'los trajes de sus cosmonautas son muy brillantes.',
            'ru': 'костюмы ваших космонавтов очень блестящи.',
            'ja': 'あなたがたの宇宙飛行士の服がきわめて輝いていることに気づくことができました。',
            'ko': '여러분의 우주 비행사들의 복장이 매우 빛난다는 것을 알아챌 수 있었습니다.',
            'zh': '您们能注意到您们宇航员的服装十分光亮。',
            'zh-Hant': '您們能注意到您們宇航員的服裝十分光亮。',
        },
        # split 2: end of wheel/rim/portholes explanation
        {
            'fr': 'en modifiant leurs structures atomiques à volonté.',
            'en': 'by modifying their atomic structures at will.',
            'de': 'ihre atomaren Strukturen nach Belieben veränderten.',
            'es': 'modificando sus estructuras atómicas a voluntad.',
            'ru': 'изменяя их атомные структуры по желанию.',
            'ja': 'その原子構造を意のままに変えることによって透かし見る手段を見いだしていなかったからです。',
            'ko': '그 원자 구조를 마음대로 바꾸어 꿰뚫어 보는 수단을 찾지 못했기 때문입니다.',
            'zh': '因为我们还没有找到借随意改变金属壁原子结构而透视它们的手段。',
            'zh-Hant': '因爲我們還沒有找到借隨意改變金屬壁原子結構而透視它們的手段。',
        },
    ],
}


def split_text(text: str, marker: str) -> tuple[str, str]:
    """Return (piece_through_marker, remainder). Marker must occur exactly once."""
    if marker not in text:
        raise ValueError(f'marker not found: {marker!r} in text {text[:80]!r}…')
    if text.count(marker) != 1:
        raise ValueError(f'marker appears {text.count(marker)}× (need exactly 1): {marker!r}')
    i = text.find(marker)
    end = i + len(marker)
    return text[:end].strip(), text[end:].strip()


def split_paragraph(p: dict, markers_list: list[dict]) -> list[dict]:
    """Split one paragraph dict into N+1 paragraph dicts."""
    pieces_fr = [p['text']]
    pieces_i18n = {lang: [p['i18n'][lang]] for lang in p['i18n']}

    for markers in markers_list:
        # split FR
        before, after = split_text(pieces_fr[-1], markers['fr'])
        pieces_fr[-1] = before
        pieces_fr.append(after)
        # split each language
        for lang in pieces_i18n:
            marker = markers.get(lang)
            if marker is None:
                raise ValueError(f'no marker for lang {lang!r}')
            before, after = split_text(pieces_i18n[lang][-1], marker)
            pieces_i18n[lang][-1] = before
            pieces_i18n[lang].append(after)

    out = []
    for i, text in enumerate(pieces_fr):
        new_p = {
            'n': p['n'],  # placeholder, renumbered later
            'speaker': p['speaker'],
            'text': text,
            'i18n': {lang: pieces_i18n[lang][i] for lang in pieces_i18n},
            'refId': p['refId'],  # placeholder
        }
        out.append(new_p)
    return out


def renumber(ch: dict, book_code: str, chapter_n: int) -> None:
    for i, p in enumerate(ch['paragraphs'], start=1):
        p['n'] = i
        p['refId'] = f'{book_code}-{chapter_n}:{i}'


def main():
    by_chapter: dict[tuple[str, int], list[tuple[int, list[dict]]]] = {}
    for (book, chap, pn), markers in SPLITS.items():
        by_chapter.setdefault((book, chap), []).append((pn, markers))

    for (book, chap), splits in by_chapter.items():
        path = LIB / book / f'chapter-{chap}.json'
        ch = json.loads(path.read_text())
        book_code = ch['bookCode']

        # Process splits from highest paragraph number down so insertion indices stay valid
        splits.sort(key=lambda x: -x[0])
        any_applied = False
        for pn, markers_list in splits:
            idx = next(i for i, p in enumerate(ch['paragraphs']) if p['n'] == pn)
            original = ch['paragraphs'][idx]
            # Idempotency check: if the first marker's FR text isn't followed by more content
            # in the current paragraph, the split was already applied — skip.
            first_marker_fr = markers_list[0]['fr']
            if first_marker_fr not in original['text']:
                print(f'  {book} ch{chap} p{pn}: SKIP (already applied — first marker not present)')
                continue
            trailing = original['text'].split(first_marker_fr, 1)[1].strip()
            if not trailing:
                print(f'  {book} ch{chap} p{pn}: SKIP (already applied — first marker is at end)')
                continue
            new_pieces = split_paragraph(original, markers_list)
            print(f'  {book} ch{chap} p{pn}: 1 paragraph → {len(new_pieces)} pieces')
            for j, piece in enumerate(new_pieces):
                print(f'    piece {j+1}: {len(piece["text"])}c FR / {len(piece["i18n"]["en"])}c EN')
            ch['paragraphs'][idx:idx+1] = new_pieces
            any_applied = True

        if any_applied:
            renumber(ch, book_code, chap)
            path.write_text(json.dumps(ch, ensure_ascii=False, indent=2) + '\n')
            print(f'wrote {path} ({len(ch["paragraphs"])} paragraphs total)')
        else:
            print(f'  no changes for ch{chap}')


if __name__ == '__main__':
    main()
