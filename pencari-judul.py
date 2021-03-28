from termcolor import colored
from pyfiglet import Figlet
import requests
from resultlist import *
import re
import numpy as np

fig = Figlet(font='slant')
figfont = fig.renderText('BercocokJudul')
print(colored(figfont + "By FathurWalkers", 'blue'))

request_input = input("Masukkan judul mu sodara : ")

split_request = request_input.split(" ")
judul_split = juduljudul.split(",")

for jumlah in split_request: 
    print("Mencocok'an judul dari ", request_input)
    ite = 1

    for judul in judul_split:
        # match = re.findall(judul, jumlah)
        if judul in jumlah:
            ite += 1
            judulsama = "kata yang sama ditemukan sebanyak "
            print(judulsama + str(ite))

    # for judulini in judul_split:
    #     if jumlah in judulini:
    #         ite += 1
    #         judulsama = "kata yang sama ditemuka sebanyak "
    #         print(judulsama + ite)


    # target1 = "https://www.google.com/search?q="
    # target2 = "&safe=strict&hl=en&sxsrf=ALeKk03YYAoNgkW96vfpU463i4jweoT0vA%3A1616939279224&ei=D4lgYMyUDY26rQGbyLPgBQ&oq="
    # target3 = "&gs_lcp=Cgdnd3Mtd2l6EAM6BAgjECc6BggjECcQEzoFCAAQkQI6BQgAELEDOggILhCxAxCDAToICAAQsQMQgwE6BwgAELEDEEM6BAguEEM6CggAEIcCELEDEBQ6AggAOgQIABBDOgUILhCxAzoHCAAQhwIQFDoFCAAQyQM6BAgAEAo6BQgAEMsBOgQIABANOgYIABANEAo6CAgAEBYQChAeOgUIIRCgAToHCCEQChCgAVCw8gpYtYILYNWDC2gAcAJ4AIAB1AGIAZQYkgEGMC4yMS4xmAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=gws-wiz&ved=0ahUKEwiM2PGakNPvAhUNXSsKHRvkDFwQ4dUDCA0&uact=5"
    # total_target = target1 + jumlah + target2 + target3
    # requests.get(total_target)

