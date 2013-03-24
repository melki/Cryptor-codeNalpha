# prog d'encodage décodage...
import random
import os

def getordre(a):
	ordre,i=[0],1
	while(i<a):
		ordre=ordre+[i]
		i+=1
	random.shuffle(ordre)	
			
	return ordre


#Pb avec les '\n' et avec les clés trop grandes....

print('### codeN(0.01) ###')
print('### Melki 2013 ###')
choix=""
while (choix!='e' and choix!='E' and choix!='q' and choix!='Q' and choix!='D' and choix!='d'):
	print('Souhaitez vous encoder un fichier ou decoder un fichier ? (e/d), ou bien quitter ? (q) : ')
	choix=input()
	if(choix=='e' or choix=='E'):
		choix,a="",0
		src=input('Veuillez entrer le fichier à encoder : \n')
		src=str(src)
		try:
			file = open(src,'r') 
		except:
			print('Erreur le fichier n\'existe pas \n')
			a=1
		if(a==0):	
			degre=input('Entrez le degré de sécurité voulu \n')
			degre,i,j,k,nbtotal=int(degre),0,0,0,0
			ordre=getordre(degre)
			new=[0]	
			while (j<degre-1):
					new+=[0]
					j+=1
			while(k<degre):
				new[k]=[]
				k+=1
			while 1:
				i=0
				line=file.readline()
				if (line==""):
					break
				while (i<len(line)-1):
					new[ordre[nbtotal%(degre)]]+=[line[i]]
					
					i=i+1;
					nbtotal+=1
				new[ordre[nbtotal%(degre)]]+=['\n']	
				nbtotal+=1
			dest=input('Veuillez entrer le nom du fichier de destination : \n')
			dest=str(dest)+".txt"	
			file_dest=open(dest,'w')
			z=0
			zprime=0
			u=0
			while (z<=nbtotal+degre+1):
				try:
					text=str(new[z%degre][u])
					existence=1
				except:
					existence=0
				if(existence==1):	
					file_dest.write(text)
				z+=1
				zprime+=1
				if(zprime>(u+1)*degre):
					u+=1
					zprime=0
				
			n=1		
			key=str(ordre[0])
			while(n<degre):
				key+="."+str(ordre[n])
				n+=1
			print('Voici votre clé de décodage, notez la soigneusement : ', key)
			fkey=open(key+'.txt','a')
	if(choix=='q' or choix=='Q'):
		break

print(new)		
print('Bye \n')
file.close()
file_dest.close()
fkey.close()
os.system("pause")		
