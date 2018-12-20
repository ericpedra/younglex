from datetime import *
import os
from platform import system
from colorama import Fore								
from colorama import Style
from colorama import init
init(autoreset=True)
init(autoreset=True)
fr  =   Fore.RED
fc  =   Fore.CYAN											
fw  =   Fore.WHITE
fy  =   Fore.YELLOW
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT
os.system('title Filter Domain\Country by Eric Pedra')
def clear():
    if system()=='Linux':
        os.system('clear')
    elif system()=='Windows':
        os.system('cls')
today = datetime.today()
month = today.strftime('%B' + ' /')
day = today.strftime('%d' + ' /')
year = today.strftime('%Y')
print("{}{}\n\t\tTanggal Waktu Hari Ini : "+"[ " + (day) + " " + (month) + " " + (year)+" ]").format(fc,sb)
banner='''{}{}\t

++++++++++++++++++++++++++++++++++

                        Filter Domain / Negara
1.Permintaan/Request Negara Kalian
2.Permintaan/Request Domain Kalian
[-]--------------------------------------------------------------------------------------------------[-]
1.Negara :COM,NET,US,CA,FR,UK,AF,AX,AL,DZ,AS,AD,AO,AI,QA,AG|
2.Domain :Hotmail,Yahoo,Yandex,Aol,Outlook,Live,Msn,Ymail.    |
                             Source Code:Google
                                 
++++++++++++++++++++++++++++++++++

'''.format(fy,sb)
print(banner)
siyass='''\n\n{}{}


                 1.Ngopi
                 2.Coding
                 3.Tulisan Harus Benar Dan Jangan Kapital
                 4.Pikiran Unik
                 5.Gunakan Otak
                          EVOLUTION | FB.COM/Ahmad.AI.Ghazali



'''.format(fc,sb)
print('{}{}\n\t\t[1] Negara Filtre (Contoh : CA NET COM US)').format(fg,sb)
print('{}{}\n\t\t[2] Domain Filtre (Contoh : Hotmail Gmail Aol Yahoo)').format(fg,sb)
filt = raw_input(("{}{}\n\n\tApa yang Anda Ingin Pilih ? --> ").format(fr,sb))
def filters():
    list = raw_input(('{}{}\n\tMasukkan Nama Mailist Untuk Filter Ini --> ').format(fy,sb))
    type = raw_input(('{}{}\n\t\tMasukkan Tipe Negara yang Anda Inginkan Filter (contoh : CA COM NET) --> ').format(fc,sb))
    clear()
    print(siyass)
    file = open(list).readlines()
    if (len(file) > 0):
      for ip in file:
        sites = ip.rstrip()
        type2 = '.' + (type)
        if type2 in sites:
            print ('{}{}Hasil Akan Disimpan Ke Result.txt :D\t\t ==> '+(sites)).format(fg,sb)
            f = open('Result.txt', 'a')
            f.write(sites) 
            f.write('\n')
        else:
            pass
	
def filters2():
    list = raw_input(('{}{}\n\tMasukkan Nama Mailist Untuk Filter Ini --> ').format(fy,sb))
    type = raw_input(('{}{}\n\t\tMasukkan Tipe Negara yang Anda Inginkan Filter (Contoh : Gmail Aol Yahoo) --> ').format(fc,sb))
    clear()
    print(siyass)
    file = open(list).readlines()
    if (len(file) > 0):
      for ip in file:
        sites = ip.rstrip()
        type2 = (type)
        if type2 in sites:
            print ('{}{}Hasil Akan Disimpan Ke Result2.txt :D\t\t ==> '+ (sites)).format(fg,sb)
            f = open('Result2.txt', 'a')
            f.write(sites) 
            f.write('\n')
if filt =='1':
    filters()
elif filt == '2':
    filters2()
else:
    pass
    
