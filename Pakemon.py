import colorama as cl
try:
 import pyfiglet
except ModuleNotFoundError:
    pass 
#important <>
#pokemon way declaration
pokemon={
    "pikachu":{
        "nom":"pikachu",
        "pv":350,
        "attaque":["tonerre: -50pv","queue acier: -25pv"],
        "damage":[50,25],
        "type":"electric",
    },
    "dracaufeu":{
        "nom":"dracaufeu",
        "pv":500,
        "attaque": ["boule de feu: -100pv","draco griffe: -75 pv"],
        "damage":[100,75],
        "type":"feu",
    },
    "Arcanin":{
     "nom":"arcanin",
     "pv":650,
     "attaque":["felin feu:-110pv","griffe de feu: -80pv"],
     "damage":[110,80],
     "type":"feu"   
    },
    "Vampisic":{
      "nom":"Vampisic",
      "pv":400,
      "attaque":["torche spirituelle: -110pv","Spirito bombe: -80pv"],
      "damage":[110,80],
      "type":"fantome",
      "type_2":"normale",  
    }
}
#end of pokemon way declaration
#logo creation
try:
 pokemon_bienvenue="Pokemon v1.0.0"
 fig=pyfiglet.Figlet(font="slant")
 pokemon_bienvenue=fig.renderText(pokemon_bienvenue)
except AttributeError:
    pass
#end logo creation
#important verification way
verify=True
#end
#colorama initialisation
cl.init(autoreset=True)
#end colorama initialisation
#class creation
class Player():
    def __init__(self,pokexp,name):
        self.pokexp=pokexp
        self.name=name
class Pokexp:
    def __init__(self,couleur,file):
        self.couleur=couleur
        self.file=file
#end class creation
#main      
def Game():
    try:
     print(pokemon_bienvenue)
    except NameError:
        pass
    global name_1 
    name_1=input("Bonjour joueur 1: Veuiller entrer votre nom ")
    global pok_1
    print("Quel pokemon choisissez vous?: ")
    print(">1)",cl.Fore.YELLOW+pokemon["pikachu"]["nom"]+cl.Style.RESET_ALL)
    print(">2)",cl.Fore.LIGHTRED_EX+cl.Fore.RED+pokemon["dracaufeu"]["nom"]+cl.Style.RESET_ALL)
    print(">3)",cl.Fore.MAGENTA+pokemon["Arcanin"]["nom"]+cl.Style.RESET_ALL)
    print(">4)",cl.Fore.LIGHTBLACK_EX+pokemon["Vampisic"]["nom"]+cl.Style.RESET_ALL)
    pok_1=input("Veuillez specifier le chiffre: ")
    global player_1
    #Verification of the entry of player
    while verify:
        try:
            #integrer traduction
            pok_1=int(pok_1)
            if 0<pok_1<5:
                
                if pok_1==1:
                    #class attribution
                    player_1=Player(pokemon["pikachu"],cl.Fore.BLUE+name_1+cl.Style.RESET_ALL)
                    pok_1=Pokexp(cl.Fore.YELLOW+pokemon["pikachu"]["nom"]+cl.Style.RESET_ALL,pokemon["pikachu"])
                    print(player_1.name,pok_1.couleur,"Apparait sur le terrain")
                    break
                if pok_1==2:
                    player_1=Player(pokemon["dracaufeu"],cl.Fore.BLUE+name_1+cl.Style.RESET_ALL)
                    pok_1=Pokexp(cl.Fore.LIGHTRED_EX+cl.Fore.RED+pokemon["dracaufeu"]["nom"]+cl.Style.RESET_ALL,pokemon["dracaufeu"])
                    print(player_1.name,pok_1.couleur," apparait sur le terrain!")
                    break
                if pok_1==3:
                    player_1=Player(pokemon["Arcanin"],cl.Fore.BLUE+name_1+cl.Style.RESET_ALL)
                    pok_1=Pokexp(cl.Fore.MAGENTA+pokemon["Arcanin"]["nom"]+cl.Style.RESET_ALL,pokemon["Arcanin"])
                    print(player_1.name,pok_1.couleur," apparait sur le terrain")
                    break
                if pok_1==4:
                    player_1=Player(pokemon["Vampisic"],cl.Fore.BLUE+name_1+cl.Style.RESET_ALL)
                    pok_1=Pokexp(cl.Fore.LIGHTBLACK_EX+pokemon["Vampisic"]["nom"]+cl.Style.RESET_ALL,pokemon["Vampisic"])
                    print(player_1.name,pok_1.couleur," apparait sur le terrain!")
                    break
                   #end class attribution
            #checking the interval 1-4
            if pok_1>=5:
             print(cl.Back.RED+"Entrer un compris entre 1 et 4"+cl.Back.RESET)
             pok_1=input("Ecriver ici:  ")
            if pok_1<=0:
                print(cl.Back.RED+"Entrer un compris entre 1 et 4"+cl.Back.RESET)
                pok_1=input("Ecriver ici:  ")
            #end checking the interval 1-4
        except ValueError:
            print(cl.Back.RED+"Entrer un nombre pas une lettre"+cl.Back.RESET)
            pok_1=input("Ecriver ici:  ")
        #end integrer traduction
        #I don't know why but a TypeError is created so i fix it because it's break the programm
        except TypeError:
            pass
    global player_2
    global pok_2
    global name_2
    #same way for but is for the player two
    name_2=input("Joueur 2 veuillez ecrire votre nom:  ")
    print("Quel pokemon choisissez vous?: ")
    print(">1)",cl.Fore.YELLOW+pokemon["pikachu"]["nom"]+cl.Style.RESET_ALL)
    print(">2)",cl.Fore.LIGHTRED_EX+cl.Fore.RED+pokemon["dracaufeu"]["nom"]+cl.Style.RESET_ALL)
    print(">3)",cl.Fore.MAGENTA+pokemon["Arcanin"]["nom"]+cl.Style.RESET_ALL)
    print(">4)",cl.Fore.LIGHTBLACK_EX+pokemon["Vampisic"]["nom"]+cl.Style.RESET_ALL)
    pok_2=input(" Ecriver ici: ")
    while verify:
        try:
         pok_2=int(pok_2)
         if 0<pok_2<5:
             if pok_2==1:
                  player_2=Player(pokemon["pikachu"],cl.Fore.GREEN+name_2+cl.Style.RESET_ALL)
                  pok_2=Pokexp(cl.Fore.YELLOW+pokemon["pikachu"]["nom"]+cl.Style.RESET_ALL,pokemon["pikachu"])
                  print(player_2.name,pok_2.couleur," apparait sur le terrain")
                  break
             if pok_2==2:
                 player_2=Player(pokemon["dracaufeu"],cl.Fore.GREEN+name_2+cl.Style.RESET_ALL)
                 pok_2=Pokexp(cl.Fore.YELLOW+pokemon["dracaufeu"]["nom"]+cl.Style.RESET_ALL,pokemon["dracaufeu"])
                 print(player_2.name,pok_2.couleur," apparait sur le terrain!")
                 break
             if pok_2==3:
                 player_2=Player(pokemon["Arcanin"],cl.Fore.GREEN+name_2+cl.Style.RESET_ALL)
                 pok_2=Pokexp(cl.Fore.YELLOW+pokemon["Arcanin"]["nom"]+cl.Style.RESET_ALL,pokemon["Arcanin"])
                 print(player_2.name,pok_2.couleur," appaait sur le terrain")
                 break
             if pok_2==4:
                 player_2=Player(pokemon["Vampisic"],cl.Fore.GREEN+name_2+cl.Style.RESET_ALL)
                 pok_2=Pokexp(cl.Fore.YELLOW+pokemon["Vampisic"]["nom"]+cl.Style.RESET_ALL,pokemon["Vampisic"])
                 print(player_2.name,pok_2.couleur," apparait sur le terrain")
                 break
         else:
             print(cl.Back.RED+"Entrer un compris entre 1 et 4"+cl.Back.RESET)
             pok_2=input("Ecriver ici: ")
        except ValueError:
            print(cl.Back.RED+"Entrer un nombre pas une lettre"+cl.Back.RESET)
            pok_2=input("Ecriver ici:  ")
        #end
    def Fight(pok_1,pok_2,player_1,player_2):
        print(cl.Back.LIGHTWHITE_EX+"QUE LE COMBAT COMMENCE"+cl.Back.RESET)
        #principal clause of the fonction
        global damage_1
        global damage_2
        #Beginning of the fight
        while player_1.pokexp["pv"]>0 or player_2.pokexp["pv"]>0:
            print(f"{player_1.name} votre pokemon est\n {pok_1.couleur} \n et son nombre de pv est: ")
            #changement of the color of the pv about the quantity 
            #for player_1
            if 200<player_1.pokexp["pv"]:
                pv_1_str=cl.Back.GREEN+str(player_1.pokexp["pv"])+cl.Back.RESET
            elif 200>player_1.pokexp["pv"]:
                pv_1_str=cl.Back.YELLOW+str(player_1.pokexp["pv"])+cl.Back.RESET
            elif 100>player_1.pokexp["pv"]:
                pv_1_str=cl.Back.RED+str(player_1.pokexp["pv"])+cl.Back.RESET
            elif 0>=player_1.pokexp["pv"]:
                player_1.pokexp["pv"]=0
                pv_1_str=cl.Back.RED+str(player_1.pokexp["pv"])+cl.Back.RESET
                break
            #for player_2
            if 200<player_2.pokexp["pv"]:
                pv_2_str=cl.Back.GREEN+str(player_2.pokexp["pv"])+cl.Back.RESET
            elif 200>player_2.pokexp["pv"]:
                pv_2_str=cl.Back.YELLOW+str(player_2.pokexp["pv"])+cl.Back.RESET
            elif 100>player_2.pokexp["pv"]:
                pv_2_str=cl.Back.RED+str(player_2.pokexp["pv"])+cl.Back.RESET
            elif 0>=player_2.pokexp["pv"]:
                player_2.pokexp["pv"]=0
                pv_2_str=cl.Back.RED+str(player_2.pokexp["pv"])+cl.Back.RESET
            
            letter_error=cl.Back.RED+"Entrer un nombre pas une lettre"+cl.Back.RESET
            range_error=cl.Back.RED+"Entrer un compris entre 1 et 2"+cl.Back.RESET
            print(pv_1_str)
            print("Quel attaque choisissez vous ")
            print("1) ",player_1.pokexp["attaque"][0])
            print("2)",player_1.pokexp["attaque"][1])
            damage_1=input("Specifier le chiffre: ")
            while verify:
                try:
                    damage_1=int(damage_1)
                    if 0<damage_1<3:
                      break
                    else:
                     print(range_error)
                     damage_1=input("Ecriver ici: ")
                except ValueError:
                    print(letter_error)
                    damage_1=input("Ecriver ici: ")
            if damage_1==1:
                player_2.pokexp["pv"]=player_2.pokexp["pv"]-player_1.pokexp["damage"][0]
                print(player_2.name," il reste a ",pok_2.couleur,pv_2_str)
            elif damage_1==2:
                player_2.pokexp["pv"]=player_2.pokexp["pv"]-player_1.pokexp["damage"][1]
                print(player_2.name," il reste a ",pok_2.couleur,pv_2_str)
            else:
                pass
            print(player_2.name," a votre tour d'attaquer")
            print("Quelle attaque choisisser vous")
            print("1)",player_2.pokexp["attaque"][0])
            print("2)",player_2.pokexp["attaque"][1])
            damage_2=input("Ecriver ici: ")
            while verify:
                try:
                    damage_2=int(damage_2)
                    if 0<damage_2<3:
                        break
                    else:
                        print(range_error)
                        damage_2=input("Ecriver ici: ")
                except ValueError:
                    print(letter_error)
                    damage_2=input("Ecriver ici: ")
            if damage_2==1:
                 player_1.pokexp["pv"]=player_1.pokexp["pv"]-player_2.pokexp["damage"][0]
                 print(player_1.name," il reste a ",pok_1.couleur,pv_1_str)
            elif damage_2==2:
                 player_1.pokexp["pv"]=player_1.pokexp["pv"]-player_2.pokexp["damage"][0]
                 print(player_1.name," il reste a ",pok_1.couleur,pv_1_str)
            else:
                 pass
            if player_2.pokexp["pv"]<=0:
                player_2.pokexp["pv"]=0
                pl_2_str=str(player_2.pokexp["pv"])
                print(player_2.name," il reste a ",pok_2.couleur,cl.Back.RED+pl_2_str+cl.Back.RESET,"   Vous avez perdu ")
                break
            elif player_1.pokexp["pv"]<=0:
                player_1.pokexp["pv"]=0
                pl_1_str=str(player_1.pokexp["pv"])
                print(player_1.name," il reste a ",pok_1.couleur,cl.Back.RED+pl_1_str+cl.Back.RESET," Vous avez perdu")
                break
            else:
                pass
    Fight(pok_1,pok_2,player_1,player_2)
    input("Appuyer sur n'importe quel touche pour sortir ")
Game()