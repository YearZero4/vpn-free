############### - DEPENDENCY - #############
from mistralOCR import extract
from bs4 import BeautifulSoup as b
from datetime import datetime
import requests, os, zipfile, sys, time, shutil
from pyfiglet import Figlet
from pathlib import Path
from colorama import init, Fore, Style

############################################

############### COLORS ################
GREEN=f"{Fore.GREEN}{Style.BRIGHT}"
WHITE=f"{Fore.WHITE}{Style.BRIGHT}"
RESET=f"{Style.RESET_ALL}"
#######################################

def estandarizar_ovpns():
 base_dir = Path("src")
 if os.name == "nt":
 	credenciales_path = ".credentials.txt"
 else:
 	credenciales_path = "../../.credentials.txt"
 for ovpn_file in base_dir.rglob("*.ovpn"):
  try:
   with open(ovpn_file, 'r+') as f:
    contenido = f.readlines()
    contenido = [line for line in contenido 
     if not line.strip().startswith("auth-user-pass")]
    for i, line in enumerate(contenido):
     if line.strip().startswith("<ca>"):
      contenido.insert(i, f"auth-user-pass {credenciales_path}\n")
      break
    f.seek(0)
    f.writelines(contenido)
    f.truncate()
    print(f" {GREEN}[+]{RESET} Actualizado: {ovpn_file}")
  except Exception as e:
   print(f"Error en {ovpn_file}: {str(e)}")

def genFolder():
	if not os.path.exists('src'):
		os.makedirs('src')

def linkPass():
	now = datetime.now()
	date = now.strftime("%Y%m%d%H%M")
	lPass=f'https://www.vpnbook.com/password.php?t={date}'
	return lPass

def verifiedIMG(Rimg):
	if os.path.exists(Rimg):
			return True
	else:
		return False

def saveImg(Rimg, content):
	with open(Rimg, 'wb') as f:
		if verifiedIMG == True:
			os.remove(Rimg)
		f.write(content)
		f.close()

def downloadIMG(Rimg, url):
	req=requests.get(url)
	res=req.content
	saveImg(Rimg, res)

def dPass(Rimg, link):
	dIMG=downloadIMG(Rimg, link)

def ovpn(link):
	n=1
	country=[]
	zipLink=[]
	vpnb='https://www.vpnbook.com'
	req=requests.get(link)
	soup=b(req.content, 'html.parser')
	find=soup.find_all('ul', class_='disc')
	tx=find[0].text.splitlines()
	for x in tx:
		search=x.find('VPN)')
		if search != -1:
			countryVPN=' '.join(x.split()[1:])
			country.append(countryVPN)
	etText=str(find[1])
	soup000 = b(etText, 'html.parser')
	links = soup000.find_all('li')
	for li in links:
		a_tag = li.find('a')
		if a_tag and a_tag.has_attr('href'):
			zip0=f'{vpnb}{a_tag["href"]}'
			zipLink.append(zip0)
			pass
	return country, zipLink

def zipDownload(name, zipUrl):
 try:
  filename = name.replace(')', '').replace('(', '').replace(' ', '_') + '.zip'
  rtZip = os.path.join('src', filename)
  newName = os.path.join('src', filename.replace('.zip', ''))
  with open(rtZip, 'wb') as f:
   f.write(requests.get(zipUrl).content)
  print(f"{GREEN} [+]{RESET} ZIP {filename} [DESCARGADO]")
  with zipfile.ZipFile(rtZip, 'r') as zip_ref:
   if os.path.exists(newName):
    shutil.rmtree(newName)
   os.makedirs(newName)
   for file in zip_ref.namelist():
    if file.endswith('.ovpn'):
     zip_ref.extract(file, newName)
     extracted_path = os.path.join(newName, file)
     if os.path.dirname(file): 
      shutil.move(extracted_path, newName)
      subfolder = os.path.join(newName, os.path.dirname(file))
      if os.path.exists(subfolder):
       shutil.rmtree(subfolder, ignore_errors=True)
  for _ in range(5):
   try:
    os.remove(rtZip)
    break
   except PermissionError:
    time.sleep(0.5)
  else:
   print(f" {GREEN}[!]{RESET} No se pudo eliminar {rtZip}")
  print(f" {GREEN}[+]{RESET} Extracción completada: {newName}")
 except Exception as e:
  print(f" {GREEN}[!]{RESET} Error procesando {filename}: {str(e)}")
  if 'rtZip' in locals() and os.path.exists(rtZip):
   try: os.remove(rtZip)
   except: pass
  if 'newName' in locals() and os.path.exists(newName):
   try: shutil.rmtree(newName, ignore_errors=True)
   except: pass

def execSys(one_instruction, two_instruction):
	so=os.name
	try:
		if so == "nt":
			os.system(one_instruction)
		else:
			os.system(two_instruction)
	except Exception as e:
		print(f"Error ejecutando comando: {str(e)}")

def password0(rpass):
	genFolder()
	dPass(rpass, linkPass())
	if verifiedIMG(rpass) == True:
		password=extract('src/password.png')
		print(f"\n{GREEN} [+]{WHITE} Usuario : {GREEN}vpnbook\n [+]{WHITE} Password:{GREEN} {password}{RESET}\n")
		with open('.credentials.txt', 'w') as f:
			f.write(f'vpnbook\n{password}')

def start():
	init(autoreset=True)
	execSys("cls", "clear")
	print(f"""{GREEN}
  ███████▀▀▀░░░░░░░▀▀▀███████
  ████▀░░░░░░░░░░░░░░░░░▀████
  ███│░░░░░░░░░░░░░░░░░░░│███
  ██▌│░░░░░░░░░░░░░░░░░░░│▐██
  ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
  ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
  ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
  ██▌░│██████▌░░░▐██████│░▐██
  ███░│▐███▀▀░░▄░░▀▀███▌│░███
  ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
  ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
  ████▄─┘██▌░░░░░░░▐██└─▄████
  █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
  ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
  █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
  ███████▄░░░░░░░░░░░▄███████		
  """)
	
	print(GREEN + Figlet(font='digital').renderText(" vpnbook_free"))
	link='https://www.vpnbook.com/freevpn'
	rpass=os.path.join('src' ,'password.png')
	print(f""" {GREEN}======================================\n [1]{WHITE} Conectarme a un OVPN almacenado
 {GREEN}[2]{WHITE} Descargar ZIP CON OVPN \n{GREEN} [3]{WHITE} Actualizar credenciales de VPN-FREE\n{GREEN} [X]{WHITE} Finalizar SCRIPT [AHORA]\n {GREEN}======================================{WHITE}
		""")

	opc=input(f"{GREEN} [+]{WHITE} Seleccione su opcion => {GREEN}")
	print("")
	if opc == "1":
		lvpn=[]
		try:
			listOvpn=os.listdir('src')
		except:
			print(" [NO EXISTEN OVPN DESCARGADOS]")
			sys.exit()
		try:
			listOvpn.remove("password.png")
		except ValueError:
			pass
		print(" [*] LISTA DE VPN GUARDADOS: \n")
		for i in enumerate(listOvpn):
		 print(f'{GREEN} [{i[0]+1}]{WHITE} => {i[1]}')
		 lvpn.append([i[1]])
		vpnNumber=int(input("\n [*] Selecciona numero de VPN => "))
		rfolder=os.path.join('src', lvpn[vpnNumber-1][0])
		listDIR=os.listdir(rfolder)
		N00=lvpn[vpnNumber-1][0]
		listvpn=[]
		for idx, file in enumerate(listDIR):
			print(f'{GREEN} [{idx+1}]{WHITE} => {file}')
			listvpn.append([file])
		sel=int(input("\n [+] Seleccione el ovpn numero => "))
		OvpnSEL=listvpn[sel-1][0]
		print(f' [+] Seleccionastes => {OvpnSEL}')
		VPN=os.path.join('src', lvpn[vpnNumber-1][0], OvpnSEL)
		directory=os.path.join('src', lvpn[vpnNumber-1][0])
		VPN_WIN=f'.\\src\\{N00}\\{OvpnSEL}'
		print(VPN_WIN)
		execSys(f".\\win_openvpn\\openvpn.exe {VPN_WIN}", f"cd {directory} ; sudo openvpn {OvpnSEL}")
	elif opc == "3":
	 password0(rpass)
	elif opc == "X" or opc == "x":
	 print(" [+] Hasta la proxima...")
	 sys.exit()
	else:
	 country, zipLink = ovpn(link)
	 for number, y in enumerate(zip(country, zipLink)):
	  print(f' {GREEN}[{number+1}] {y[0]}{RESET} -> {y[1]}')
	 print(f" {GREEN}[ALL]{RESET} Descargar todos los zip")
	 password0(rpass)
	 selNumber=input("\n Selecciona una VPN del (1-12) o [ALL] = ")
	 if selNumber == 'ALL' or selNumber == 'all':
	  execSys("rmdir /s /q src", "rm -rf src")
	  os.makedirs('src')
	  rep = {}
	  num = 0
	  for i in zipLink:
	   zD = zipLink[num]
	   original_nm = country[num]
	   nm = original_nm
	   if original_nm in rep:
	    rep[original_nm] += 1
	    nm = f"{original_nm}{rep[original_nm] + 1}"
	   else:
	    rep[original_nm] = 0
	   try:
	    zipDownload(nm, zD)
	   except OSError:
	    rep[original_nm] += 1
	    nm = f"{original_nm}{rep[original_nm] + 1}"
	    zipDownload(nm, zD)
	   num += 1
	  estandarizar_ovpns()
	 else:
	  zD = zipLink[int(selNumber)-1]
	  nm = country[int(selNumber)-1]
	  zipDownload(nm, zD)
	  target_dir = Path(f"src/{nm.replace(')', '').replace('(', '').replace(' ', '_')}")
	  for ovpn_file in target_dir.glob("*.ovpn"):
	   with open(ovpn_file, 'r+') as f:
	    lines = f.readlines()
	    f.seek(0)
	    f.writelines([l for l in lines if not l.strip().startswith("auth-user-pass")])
	    f.write(f"auth-user-pass {'.credentials.txt' if os.name == 'nt' else '../../.credentials.txt'}\n")
	    f.truncate()


if __name__ == '__main__':
	try:
		while True:
			start()
			input("\n [+] Presione [ENTER] Para Continuar...")
	except KeyboardInterrupt:
		print(f"\n {GREEN}[+]{WHITE} Script interrumpuido...")









