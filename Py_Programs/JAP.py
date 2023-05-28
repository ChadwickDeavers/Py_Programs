# Japanese Learning Program, I made it as a way to help me with learning japanese
# pretty simple program, want to put all phrases in a csv so the main file is less bloaty and applies to ZEN more
# contains Hiragana and Katakana
""" Created by: AK1R4S4T0H
"""
import sys
from PySide6 import QtCore, QtGui, QtWidgets
import random
import os

os.environ['QT_QPA_PLATFORM'] = 'xcb'

japanese_phrases = {
    'こんにちは': 'Konnichiwa - Hello',
    'ありがとう': 'Arigatou - Thank you',
    'おはよう': 'Ohayou - Good morning',
    'さようなら': 'Sayounara - Goodbye',
    'はい': 'Hai - Yes',
    'いいえ': 'Iie - No',
    'おいしい': 'Oishii - Delicious',
    'すごい': 'Sugoi - Amazing',
    'かわいい': 'Kawaii - Cute',
    'あさごはん': 'Asagohan - Breakfast',
    'ひるごはん': 'Hirugohan - Lunch',
    'ばんごはん': 'Bangohan - Dinner',
    'おやすみなさい': 'Oyasuminasai - Good night',
    'わかりません': 'Wakarimasen - I don\'t understand',
    'お願いします': 'Onegaishimasu - Please',
    'ごめんなさい': 'Gomen nasai - Sorry',
    'はじめまして': 'Hajimemashite - Nice to meet you',
    'お疲れ様です': 'Otsukaresama desu - Good job/Well done',
    'お邪魔します': 'Ojama shimasu - Excuse me (when entering someone\'s home or office)',
    'よろしくお願いします': 'Yoroshiku onegaishimasu - Nice to meet you/Please treat me well',
    'お早うございます': 'Ohayou gozaimasu - Good morning (formal)',
    'こんばんは': 'Konbanwa - Good evening',
    'おやすみなさい': 'Oyasuminasai - Good night (formal)',
    'お元気ですか': 'Ogenki desu ka? - How are you?',
    'はい、元気です': 'Hai, genki desu - Yes, I\'m fine',
    'ありがとうございます': 'Arigatou gozaimasu - Thank you (formal)',
    'どういたしまして': 'Dou itashimashite - You\'re welcome',
    'すみません': 'Sumimasen - Excuse me/Sorry',
    'ごめんください': 'Gomen kudasai - May I come in?',
    'お邪魔しています': 'Ojama shiteimasu - Sorry for disturbing you',
    'いただきます': 'Itadakimasu - Let\'s eat (before a meal)',
    'ごちそうさまでした': 'Gochisousama deshita - Thank you for the meal (after a meal)',
    'いい天気ですね': 'Ii tenki desu ne - Nice weather, isn\'t it?',
    'お疲れさまでした': 'Otsukaresama deshita - Good work (after work)',
    'がんばってください': 'Ganbatte kudasai - Good luck/Do your best',
    'お元気で': 'Ogenki de - Take care/Stay well',
    'お楽しみください': 'Otanoshimi kudasai - Enjoy yourself',
    'おめでとうございます': 'Omedetou gozaimasu - Congratulations (formal)',
    'お誕生日おめでとうございます': 'Otanjoubi omedetou gozaimasu - Happy birthday (formal)',
    'どうぞよろしくお願いします': 'Douzo yoroshiku onegaishimasu - Please take care of me/Nice to meet you',
    'お先に失礼します': 'Osaki ni shitsurei shimasu - Excuse me for leaving before you (when leaving work or a social gathering)',
    'もう一度言ってください': 'Mou ichido itte kudasai - Could you please repeat that?',
    'どこですか': 'Doko desu ka? - Where is it?',
    'どうやって行けばいいですか': 'Dou yatte ikeba ii desu ka? - How do I get there?',
    'いつ行きますか': 'Itsu ikimasu ka? - When are you going?',
    '何時ですか': 'Nanji desu ka? - What time is it?',
    'ちょっと待ってください': 'Chotto matte kudasai - Please wait a moment',
    'どうもありがとう': 'Doumo arigatou - Thank you very much',
    'お気をつけて': 'Oki wo tsukete - Take care (when someone is leaving)',
    'どうしたんですか': 'Doushitan desu ka? - What\'s wrong?',
    'すみません、道に迷ってしまいました': 'Sumimasen, michi ni mayotte shimaimashita - Sorry, I got lost',
    'いらっしゃいませ': 'Irasshaimase - Welcome',
    'お大事に': 'Odaijini - Get well soon',
    'お会いできて嬉しいです': 'Oai dekite ureshii desu - Im glad to meet you',
    'お土産': 'Omiyage - Souvenir',
    'お祝い': 'Oiwai - Celebration',
    'お金持ち': 'Okane mochi - Rich person',
    'お金がない': 'Okane ga nai - I have no money',
    'お先にどうぞ': 'Osaki ni douzo - Please go ahead',
    'がっかり': 'Gakkari - Disappointed',
    'きのう': 'Kinou - Yesterday',
    'きょう': 'Kyou - Today',
    'あした': 'Ashita - Tomorrow',
    'あつい': 'Atsui - Hot',
    'さむい': 'Samui - Cold',
    'わたしのなまえは...です': 'Watashi no namae wa...desu - My name is...',
    'だいじょうぶ': 'Daijoubu - Its alright',
    'はし': 'Hashi - Chopsticks',
    'たんじょうび': 'Tanjoubi - Birthday',
    'じかん': 'Jikan - Time',
    'しょくどう': 'Shokudou - Dining hall/cafeteria',
    'とうきょう': 'Toukyou - Tokyo',
    'にほんご': 'Nihongo - Japanese (language)',
    'おおきい': 'Ookii - Big',
    'ちいさい': 'Chiisai - Small',
    'わかい': 'Wakai - Young',
    'ふるい': 'Furui - Old',
    'ゆうめいな': 'Yuumeina - Famous',
    'ほしい': 'Hoshii - I want',
    'とても': 'Totemo - Very',
    'すごく': 'Sugoku - Extremely',
    'やさしい': 'Yasashii - Kind',
    'はやい': 'Hayai - Early/Fast',
    'おそい': 'Osoi - Late/Slow',
    'いいえ、大丈夫です': 'Iie, daijoubu desu - No, Im fine',
    'これは何ですか': 'Kore wa nan desu ka? - What is this?',
    'あの人はだれですか': 'Ano hito wa dare desu ka? - Who is that person?',
    'ほん': 'Hon - Book',
    'くつ': 'Kutsu - Shoes',
    'ねこ': 'Neko - Cat',
    'いぬ': 'Inu - Dog',
    'うさぎ': 'Usagi - Rabbit',
    'さかな': 'Sakana - Fish',
    'あ': 'A',
    'い': 'I',
    'う': 'U',
    'え': 'E',
    'お': 'O',
    'か': 'KA',
    'き': 'KI',
    'く': 'KU',
    'け': 'KE',
    'こ': 'KO',
    'さ': 'SA',
    'し': 'SHI',
    'す': 'SU',
    'せ': 'SE',
    'そ': 'SO',
    'た': 'TA',
    'ち': 'CHI',
    'つ': 'TSU',
    'て': 'TE',
    'と': 'TO',
    'な': 'NA',
    'に': 'NI',
    'ぬ': 'NU',
    'ね': 'NE',
    'の': 'NO',
    'は': 'HA',
    'ひ': 'HI',
    'ふ': 'FU',
    'へ': 'HE',
    'ほ': 'HO',
    'ま': 'MA',
    'み': 'MI',
    'む': 'MU',
    'め': 'ME',
    'も': 'MO',
    'や': 'YA',
    'ゆ': 'YU',
    'よ': 'YO',
    'ら': 'RA',
    'り': 'RI',
    'る': 'RU',
    'れ': 'RE',
    'ろ': 'RO',
    'わ': 'WA',
    'を': 'WO',
    'ア': 'A',
    'イ': 'I',
    'ウ': 'U',
    'エ': 'E',
    'オ': 'O',
    'カ': 'KA',
    'キ': 'KI',
    'ク': 'KU',
    'ケ': 'KE',
    'コ': 'KO',
    'サ': 'SA',
    'シ': 'SHI',
    'ス': 'SU',
    'セ': 'SE',
    'ソ': 'SO',
    'タ': 'TA',
    'チ': 'CHI',
    'ツ': 'TSU',
    'テ': 'TE',
    'ト': 'TO',
    'ナ': 'NA',
    'ニ': 'NI',
    'ヌ': 'NU',
    'ネ': 'NE',
    'ノ': 'NO',
    'ハ': 'HA',
    'ヒ': 'HI',
    'フ': 'FU',
    'ヘ': 'HE',
    'ホ': 'HO',
    'マ': 'MA',
    'ミ': 'MI',
    'ム': 'MU',
    'メ': 'ME',
    'モ': 'MO',
    'ヤ': 'YA',
    'ユ': 'YU',
    'ヨ': 'YO',
    'ラ': 'RA',
    'リ': 'RI',
    'ル': 'RU',
    'レ': 'RE',
    'ロ': 'RO',
    'ワ': 'WA',
    'ヲ': 'WO',
    'ン': 'N',
}

class JapanesePhrasesApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Japanese Phrases")
        self.setGeometry(100, 100, 1500, 400)

        self.japanese_label = QtWidgets.QLabel(self)
        self.japanese_label.setFont(QtGui.QFont("Arial", 24))
        self.japanese_label.setStyleSheet("background-color: black; color: white")
        self.japanese_label.setAlignment(QtCore.Qt.AlignCenter)

        self.button = QtWidgets.QPushButton("Show me a phrase!")
        self.button.setStyleSheet("color: #FFFFFF;background-color: #165753;font-size: 12px;padding: 5px")

        self.button.clicked.connect(self.display_phrase)

        self.label = QtWidgets.QLabel("10 second timer on Button press")

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.japanese_label, stretch=1)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.display_phrase()

    def display_phrase(self):
        phrase, definition = random.choice(list(japanese_phrases.items()))
        self.japanese_label.setText(f"{phrase}: {definition}")

        QtCore.QTimer.singleShot(10000, self.display_phrase)  # 10 second timer

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    japanese_app = JapanesePhrasesApp()
    japanese_app.show()
    sys.exit(app.exec())