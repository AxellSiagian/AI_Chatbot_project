import random
import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz
from tabulate import tabulate
import re
from nltk.tokenize import word_tokenize
import sys
import tkinter
from tkinter import *
import time
# from google_drive_downloader import GoogleDriveDownloader as gdd

# Message
M_GREETING = ["Halo", "Hi", "Hai", "Hello", "wassup", "Hey", "woi", "apa kabar", "kabar"]

M_DETAILS_BASIST = [
    "basist", "info", "apa itu basist", "info tentang basist", "basist bisa apa",
    "AI", "detail dari chatbot", "Teknologi apa yang digunakan untuk mengembangkan chatbot ini?",
    "cara kerja", "mekanisme", "chatbot",
]

M_CREATORS = [
    "pembuat", "membuat", "siapa", "basist", "pencipta", "pembuat basist", "siapa yang membuat basist",
    "mengembangkan chatbot", "merancang chatbot"
]

M_JOKI_QUESTION = [
    "joki", "Bisa joki apa", "Joki apa", "Ada joki apa", "Paket joki", "tahu", "apa",
    "Paket joki apa aja", "tanya", "bertanya", "detail", "jasa", "cari", "nanya",
    "paket", "jasa", "jasa apa aja", "jenis joki", "macam joki"
]

M_DETAILS_MAKALAH = [
    "makalah", "Joki makalah", "Joki makalah", "Mau joki makalah", "Tolong jokiin makalahku",
    "Bikinin makalah", "jelaskan", "detail", "proses makalah", "apa", "jasa"
]
M_DETAILS_CODING = [
    "coding", "koding",  "joki coding", "joki coding",  "Ngoding", "Mau joki ngoding",  "pemrograman", "joki coding harganya berapa",
    "Tolong jokiin tugas coding", "Bikinin code", "Buat code", "jelaskan", "detail", "jasa"
    "proses coding", "apa"
]
M_DETAILS_SKRIPSI = [
    "skripsi", "joki skripsi", "Mau joki skripsi", "Tolong jokiin skripsiku", "joki skripsi harganya berapa",
    "Bikinin skripsi", "jelaskan", "detail", "proses skripsi", "apa", "jasa",
]

M_PRICE_MAKALAH = [
    "harga", "joki makalah berapa", "harga joki makalah", "joki makalah harganya berapa", "jokiin makalah",
    "Harga makalah", "harga berapa", "berapa", 'paket joki makalah', 'paket', "biaya"
]
M_PRICE_CODING = [
    "coding", "koding", "harga", "Joki coding berapa", "Harga coding makalah",
    "Harga ngoding", "harga berapa", "berapa", 'paket', 'paket joki coding ', "biaya", "harga joki skripsi"
]
M_PRICE_SKRIPSI = [
    "skripsi", "harga", "Joki berapa", "Harga skripsi makalah",
    "harga berapa", "berapa", 'paket joki skripsi', 'paket', "biaya"
]

M_CONTACT = [
    "kontak", "kontak", "cara kontak", "hubungi", "hubungi", "menghubungi", "bertanya langsung", "pakai jasa joki",
    "customer service", "telpon", "nomor telpon", "alamat email", "bertanya"
]

M_FINISH = [
    "selesai", "keluar", "quit", "saya puas", "baik, terima kasih", "terima kasih", "terimakasih"
]

M_SWEAR = [
    "bangsat", "asu", "goblok", "kontol", "bajingan", "anjir", "kampret",
    "jancuk", "jancok", "kampret", "fuck", "shit", "bitch", "retard", "cunt",
    "asshole", "bastard"
]
M_EKSIT = [
    "y", "ya", "iya", "yaa", "Y", "YA", "Ya"
]

# Response
R_FIRST_GREETING = [
    "Hallo, selamat datang! Saya Basist, chatbot untuk jasa joki." +
    "\n        Ada yang bisa saya bantu?"
]

R_OTHER_GREETING = [
    "Ada hal lain yang bisa saya bantu?"
]

R_CREATORS = [
    "Huuheheheh, Basist adalah program ChatBot dari kelompok TR 'Ho'oh':" +
    "\n        > (672021002) - Nicholas Irvan Winata" +
    "\n        > (672021037) - Anthony Febrian Aria Sena" +
    "\n        > (672021213) - Axell Amadeus Siagian"
]

R_DETAILS_BASIST = [
    "Perkenalkan nama saya Basist (BAmbang aSISTant)" +
    "\n        Saya  chatbot yang didesain untuk menjawab pertanyaan mengenai" +
    "\n        jasa  joki :D. Saya dibuat  dengan bahasa  pemrograman  Python" +
    "\n        dengan bantuan library khusus. Semoga apa yang disediakan oleh" +
    "\n        chatbot ini dapat bermanfaat bagi semua user!"
]

R_GREETING = [
    "Hallo, saya Basist!! Ada yang bisa saya bantu?",
    "Selamat datang! Saya Basist, ada yang bisa saya bantu?",
    "Haii, saya Basist! Apa dapat saya bantu hari ini?"
]

R_JOKI_QUESTION = [
    "Kami Ho'oh Inc menyediakan 3 jenis jasa joki tugas yaitu:" +
    "\n        > Makalah" +
    "\n        > Coding" +
    "\n        > Skripsi" +
    "\n        Silakan bertanya lanjut..."
]

R_DETAILS_MAKALAH = [
    "Kami menyediakan jasa joki untuk membuat makalah. Informasi yang" +
    "\n        harus diberikan  yaitu detail  tugas seperti judul, jema, jumlah" +
    "\n        halaman,  dan  deadline yang  disesuaikan dengan paket yang kami" +
    "\n        sediakan. Ingin bertanya lanjut tentang harga? Silakan bertanya!",

    "Kami menyediakan jasa joki untuk membuat makalah. Informasi yang" +
    "\n        harus diberikan  yaitu detail  tugas seperti judul, jema, jumlah" +
    "\n        halaman,  dan  deadline yang  disesuaikan dengan paket yang kami" +
    "\n        sediakan. Ingin pakai jasa kami? Minta kontak kami aja!",
]

R_DETAILS_CODING = [
    "Tentu saja kami  menyediakan jasa  coding! Informasi yang harus" +
    "\n        disediakan yaitu jenis  program yang diinginkan, bahasa program" +
    "\n        yang sesuai, tema program, dan deadline yang disesuaikan dengan" +
    "\n        paket yang kami sediakan. Ingin bertanya  lanjut tentang harga?" +
    "\n        Silakan bertanya!",

    "Tentu saja kami  menyediakan jasa  coding! Informasi yang harus" +
    "\n        disediakan yaitu jenis  program yang diinginkan, bahasa program" +
    "\n        yang sesuai, tema program, dan deadline yang disesuaikan dengan" +
    "\n        paket yang kami sediakan.  Ingin pakai jasa kami? Minta  kontak" +
    "\n        kami aja!"
]
R_DETAILS_SKRIPSI = [
    "Jasa joki untuk skripsi adalah salah satu jasa yang kami sediakan!" +
    "\n        Detail yang kami  perlukan untuk jasa skripsi yaitu topik skripsi," +
    "\n        jurusan, bab yang ingin ditulis, format dari skripsi, dan deadline" +
    "\n        yang sesuai dengan paket yang kami sediakan. Ingin bertanya lanjut" +
    "\n        tentang harga? Silakan bertanya",

    "Jasa joki untuk skripsi adalah salah  satu jasa yang kami sediakan!" +
    "\n        Detail yang kami  perlukan untuk  jasa skripsi yaitu topik skripsi," +
    "\n        jurusan, bab yang ingin ditulis, format  dari skripsi, dan deadline" +
    "\n        yang sesuai dengan paket yang kami sediakan. Ingin pakai jasa kami?" +
    "\n        Minta kontak kami aja!"
]

R_PRICE_MAKALAH = [
    "Price list Joki Makalah :" +
    "\n        > Paket Kebut Sehari (1 Hari)  200.000" +
    "\n        > Paket Ekspress (3 Hari)      100.000" +
    "\n        > Paket Wajar (7 hari)         50.000"
]
R_PRICE_CODING = [
    "Price list Joki Coding :" +
    "\n        - Paket Kebut Semalam (12 Jam) 340.000" +
    "\n        - Paket Kepepet (3 Hari)       100.000 - 200.000" +
    "\n        - Paket Mager (6 Hari)         50.000 - 100.000"
]
R_PRICE_SKRIPSI = [
    "Price List Joki Skripsi :" +
    "\n        - Paket Lengkap Skripsi (7 Hari)   500.000" +
    "\n        - Paket Kepepet (3 Hari)           100.000 - 200.000" +
    "\n        - Paket Kepepet + lengkap (3 Hari) 727.000"
]

R_CONTACT = [
    "Silakan menghubungi kami melalui berikut:" +
    "\n        > Instagram    : @Hooh_OFFICIAL" +
    "\n        > Whatsapp    : +62 727-3172-3842" +
    "\n        > Telpon         : 0213-69420" +
    "\n        > Email          : jasa.joki@hooh.com" +
    "\n        > Website      : jasakoding.ril.edu"
]

R_MORE_DETAILS = [
    "Tolong berikan pertanyaan yang lebih spesifik. Kami menyediakan" +
    "\n        jasa untuk coding, makalah, dan skripsi."
]
R_UNKNOWN = [
    "Saya kurang mengerti maksud anda. Tolong berikan pertanyaan yang lebih sesuai!",
    "Saya tidak paham apa maksud anda, silakan coba menanyakan hal lainnya...",
    "Saya tidak memahami chat anda... Silakan bertanya lagi!"
]

R_FINISH = "BOT : Apakah anda ingin mengakhirkan chat kita? Input 'Y' untuk mengakhiri\n>> You: "


def def_greeting():
    response = R_FIRST_GREETING[random.randrange(len(R_GREETING))]
    return response


def creators():
    response = R_CREATORS[random.randrange(len(R_CREATORS))]
    return response


def greeting():
    response = R_GREETING[random.randrange(len(R_GREETING))]
    return response


def detailsBasist():
    response = R_DETAILS_BASIST[random.randrange(len(R_DETAILS_BASIST))]
    return response


def pertanyaanJoki():
    response = R_JOKI_QUESTION[random.randrange(len(R_JOKI_QUESTION))]
    return response


def detailsMakalah():
    response = R_DETAILS_MAKALAH[random.randrange(len(R_DETAILS_MAKALAH))]
    return response


def detailsCoding():
    response = R_DETAILS_CODING[random.randrange(len(R_DETAILS_CODING))]
    return response


def detailsSkripsi():
    response = R_DETAILS_SKRIPSI[random.randrange(len(R_DETAILS_SKRIPSI))]
    return response


def hargaMakalah():
    response = R_PRICE_MAKALAH[random.randrange(len(R_PRICE_MAKALAH))]
    return response


def hargaCoding():
    response = R_PRICE_CODING[random.randrange(len(R_PRICE_CODING))]
    return response


def hargaSkripsi():
    response = R_PRICE_SKRIPSI[random.randrange(len(R_PRICE_SKRIPSI))]
    return response


def moredetail():
    response = R_MORE_DETAILS[random.randrange(len(R_MORE_DETAILS))]
    return response


def contact():
    response = R_CONTACT[random.randrange(len(R_CONTACT))]
    return response


def unknown():
    response = R_UNKNOWN[random.randrange(len(R_UNKNOWN))]
    return response


# tes probabilitas/closeness input user dengan salah satu dari jenis response
def test_probability(input_user, message_reference, required_words=[], blocked_words=[]):
    # input_user adalah pesan yang masuk dari user setelah dibersih
    # message_reference adalah list yang kita deklarasi di atas untuk cek mana response yang nantinya tepat
    # required_words adalah keyword yang perlu dalam pesan untuk trigger response, nanti bantu buat pertanyaan specific u/ paket jasa joki
    # blocked_words adalah keyword yang tidak boleh ada dalam pesan, nanti bantu buat pertanyaan detail tentang jasa lainnya

    # keyword_test dipake buat deteksi bila kata kunci yang HARUS ada di message user, ada atau ga
    keyword_test = "False"
    blocked_word_test = "Not Blocked"

    # keyword_empty ini biar klo required_words kosong, dia ttp bisa return probabilitas-nya
    # (not requred_words) -> return value True kalo kosong
    keyword_empty = (not required_words)

    blocked_word_empty = (not blocked_words)

    # percentage_list buat nampung semua probabilitas sesuai dengan hasil fuzzy
    percentage_list = []

    # mencari tingkatan closeness dgn fuzzy antara input user dan masing" reference message
    for sentence in message_reference:
        percentage_list.append(fuzz.token_set_ratio(input_user, sentence))

    sorted_percentage_list = sorted(percentage_list, reverse=True)
    # print(sorted_percentage_list)

    testmultiply = 2
    testSum = 0
    testweightsum = 0
    for index, probability in enumerate(sorted_percentage_list):
        weight = (len(sorted_percentage_list) - (0.5*index)) * testmultiply
        if (weight > 0):
            testweightsum = testweightsum + weight
        testSum = (probability * weight) + testSum

    testpercentage = testSum / testweightsum
    percentage = testpercentage

    # cek apakah required_words ada di input user atau ngga
    words_input = input_user.lower().split()
    for kata1 in words_input:
        for kata2 in blocked_words:
            if kata1 == kata2:
                blocked_word_test = "Blocked"
        for kata2 in required_words:
            if kata1 == kata2:
                keyword_test = "True"

    if blocked_word_empty:
        blocked_word_test = "Not Required"
    if keyword_empty:
        keyword_test = "Not Required"

    result = [percentage, keyword_test, blocked_word_test]

    return result


# test_allMessage dipakai untuk membandingkan input user dengan masing-masing jenis response
def test_allMessage(user_input, dev_mode=True):
    # bersihin input :)
    user_input = cleanUserInput(user_input)

    # arrayOutput untuk simpan output yang mungkin dijalankan oleh chat + probabilitas masing" jenis response
    arrayOutput = []

    # fungsi respons untuk aktivasi pemilihan output yang mungkin + mencari probabilitas masing"
    def response(message_output, message_reference, required_words, blocked_words, response_category):
        output = message_output
        test_result = test_probability(user_input, message_reference,
                                       required_words, blocked_words)
        probability = test_result[0]
        keyword = test_result[1]
        blocked_word = test_result[2]
        nonlocal arrayOutput
        arrayOutput.append([output, probability, keyword,
                           blocked_word, response_category])

    # response ini untuk berbagai jenis response yang mungkin
    response(greeting(), M_GREETING, required_words=[],
             blocked_words=[], response_category='greeting')
    response(pertanyaanJoki(), M_JOKI_QUESTION, required_words=[
             'apa', 'joki', 'jasa'], blocked_words=[], response_category='question')

    response(detailsMakalah(), M_DETAILS_MAKALAH, required_words=['makalah', 'makalahnya'], blocked_words=[
             'paket', 'coding', 'code', 'program', 'skripsi', 'harga', 'biaya', 'berapa',], response_category='details')
    response(detailsCoding(), M_DETAILS_CODING, required_words=['coding', 'ngoding', 'code', 'program'], blocked_words=[
             'paket', 'makalah', 'skripsi', 'harga', 'biaya', 'berapa',], response_category='details')
    response(detailsSkripsi(), M_DETAILS_SKRIPSI, required_words=['skripsi'], blocked_words=[
             'paket', 'coding', 'code', 'program', 'makalah', 'harga', 'biaya', 'berapa',], response_category='details')

    response(hargaMakalah(), M_PRICE_MAKALAH, required_words=['harga', 'paket', 'biaya', 'berapa', 'makalah', 'makalahnya'], blocked_words=[
             'coding', 'ngoding', 'code', 'program', 'skripsi'], response_category='price')
    response(hargaCoding(), M_PRICE_CODING, required_words=[
             'harga', 'paket', 'biaya', 'berapa', 'coding', 'ngoding', 'code', 'program'], blocked_words=['makalah', 'skripsi'], response_category='price')
    response(hargaSkripsi(), M_PRICE_SKRIPSI, required_words=['harga', 'paket', 'biaya', 'berapa', 'skripsi'], blocked_words=[
             'coding', 'code', 'program', 'makalah'], response_category='price')

    response(creators(), M_CREATORS, required_words=[], blocked_words=[
             'harga', 'biaya'], response_category='credit')
    # 'pembuat', 'creator', 'merancang', 'mengembangkan', 'dibuat', 'siapa'

    response(detailsBasist(), M_DETAILS_BASIST, required_words=[],
             blocked_words=[], response_category='basist')

    response(contact(), M_CONTACT, required_words=[],
             blocked_words=[], response_category='contact')

    response(R_FINISH, M_FINISH, required_words=[],
             blocked_words=[], response_category='finish')

    # ubah arrayOutput biasa jadi array numpy biar gampang ganti ke dataframe
    arrayOutput2 = np.asarray(arrayOutput, dtype=object)

    # ubah arrayOutput2 jadi dataframe + masukin columns & index biar gampang keliatan isi dataframenya
    df = pd.DataFrame(arrayOutput2,
                      index=['Welcome', 'Joki', 'Makalah', 'Coding', 'Skripsi', 'Harga Makalah',
                             'Harga Coding', 'Harga Skripsi', 'Creators', 'Detail Basist', 'Kontak', 'Finish'],
                      columns=['Response from bot', 'Probability', 'Required Words', 'Blocked Words', 'Response Category'])

    # ubah column 'Probability' jadi numeric biar cari idmax() nanti jalan lancar
    df['Probability'] = pd.to_numeric(df['Probability'])

    # mencari nilai maximal dari probabilitas, trus pake index itu buat dapetin output yang tepat
    finalProbability = df.loc[df['Probability'].idxmax(), 'Probability']

    # current output filter: 30% minimum
    required_words_result = df.loc[df['Probability'].idxmax(
    ), 'Required Words']
    blocked_words_result = df.loc[df['Probability'].idxmax(), 'Blocked Words']
    response_category = df.loc[df['Probability'].idxmax(), 'Response Category']

    keyword_harga = [
        'skripsi', 'koding', 'coding', 'ngoding', 'makalah'
    ]

    response_category_result = False

    if (response_category == 'price'):
        for keyword in keyword_harga:
            for words in user_input.split():
                # print(keyword,words)
                if words == keyword:
                    response_category_result = True

    if (response_category == 'finish'):
        check = input(R_FINISH)
        if (check == 'y' or check == 'Y'):
            finalOutput = ""
            print("\nSemoga chatbot Basist bermanfaat! Terima kasih...")
            sys.exit()
        else:
            finalOutput = R_FIRST_GREETING[0]
    elif ((blocked_words_result == "Blocked") or (response_category == "price" and response_category_result == False)):
        finalOutput = moredetail()
    elif (finalProbability > 40) and ((required_words_result == "True") or (required_words_result == "Not Required")):
        finalOutput = df.loc[df['Probability'].idxmax(), 'Response from bot']
    else:
        finalOutput = unknown()

    if dev_mode == TRUE:
        # DEV MODE -> PROBABILITAS TABLE
        print(tabulate(df, headers='keys', tablefmt='grid'))

    return finalOutput


# gdd.download_file_from_google_drive(file_id='1vWZxABVd1-uqtvktbyek8dj9LvhRQblP',
#                                     dest_path='./tala-stopwords-indonesia.txt',
#                                     unzip=True)

datafile = open('./tala-stopwords-indonesia.txt', "r")

stopword_list = []
for line in datafile:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    stopword_list.append(line_list[0])
datafile.close()

# bersihkan input user


def cleanUserInput(inputuser):
    empt_lst = []
    inputuser = inputuser.lower()
    inputuser = re.sub(r'[^a-zA-Z\s]', '', inputuser)
    inputuser = word_tokenize(inputuser)
    for element in inputuser:
        if len(element) > 2 and len(element) < 15:
            empt_lst.append(element)
    empt_lst = [word for word in empt_lst if not word in stopword_list]
    inputuser = " ".join(empt_lst)

    # print("\n\n\tCleaned input:", inputuser)
    return inputuser


# gui

eksit = False


def send(event=None):
    global eksit, first
    ChatBox.config(state=NORMAL)
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)
    ChatBox.config(foreground="#446665", font=("Verdana", 12))
    ChatBox.config(state=DISABLED)
    ChatBox.tag_configure('bot_text', foreground='#0b569e')
    ChatBox.yview(END)
    ChatBox.tag_configure('userr', foreground='#000000')
    if msg in M_EKSIT and eksit == True:
        ChatBox.config(state=NORMAL)
        ChatBox.insert(END, "USER : " + msg + '\n\n', 'userr')
        ChatBox.insert(
            END, "BOT  : Semoga chatbot Basist bermanfaat! Terima kasih...", 'bot_text')
        ChatBox.after(2000, sys.exit)
    elif eksit == True:
        ChatBox.config(state=NORMAL)
        ChatBox.insert(END, "USER : " + msg + '\n\n', 'userr')
        ChatBox.insert(END, "BOT  : " +
                       R_OTHER_GREETING[0] + '\n\n', 'bot_text')
        ChatBox.config(state=DISABLED)
        eksit = False
    elif msg in M_FINISH:
        eksit = True
        ChatBox.config(state=NORMAL)
        ChatBox.insert(END, "USER : " + msg + '\n\n', 'userr')
        ChatBox.insert(
            END, "BOT  : Apakah anda ingin mengakhirkan chat kita? Input 'Y' untuk mengakhiri " + '\n\n', 'bot_text')
        ChatBox.config(state=DISABLED)

    elif msg != '':
        ChatBox.config(state=NORMAL)
        ChatBox.insert(END, "USER : " + msg + '\n\n', 'userr')

        ChatBox.insert(END, "BOT  : " + test_allMessage(msg,
                       False) + '\n\n', 'bot_text')
        ChatBox.config(state=DISABLED)
        print('Bot >> ' + test_allMessage(msg, True))


root = Tk()
root.title("Basist")
root.geometry("720x500")
root.resizable(width=FALSE, height=FALSE)

# sdeclare tipe sama spe
ChatBox = Text(root, bd=0, bg="white", font="Arial")
ChatBox.config(state=DISABLED)

scrollbar = Scrollbar(root, command=ChatBox.yview, cursor="heart")
ChatBox['yscrollcommand'] = scrollbar.set

SendButton = Button(root, font=("Verdana", 12, 'bold'), text="Send",
                    bd=0, bg="#0b569e", activebackground="#3c9d9b", fg='#ffffff',
                    command=send)

EntryBox = Text(root, bd=0, bg="white", font="Arial")
EntryBox.bind("<Return>", send)

# position and size
scrollbar.place(x=700, y=6, height=406)
ChatBox.place(x=6, y=6, height=406, width=695)
EntryBox.place(x=6, y=421, height=70, width=585)
SendButton.place(x=600, y=421, height=70, width=100)


# ChatBox.insert(END, "User : hello" + '\n\n')

root.mainloop()
