''' Rainworld Sim  rainmland'''
#necessary
import time
import random
from colorama import init   #only need this to make windows and python terminal work
init()

#colours (had to use ansi, i dont think rich works in thonny)
RED = "\033[31m"                #im actually so smart holy
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
BLACK   = "\033[30m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"
RESET = "\033[0m"


#intro
print('__          __  _ ')                         
print('\ \        / / | |')                        
print(" \ \  /\  / /__| | ___ ___  _ __ ___   ___") 
print("  \ \/  \/ / _ \ |/ __/ _ \|  '_ ` _ \/ _ \ ")
print('   \  /\  /  __/ | (_| (_) | | | | | |  __/')
print('    \/  \/ \___|_|\___\___/|_| |_| |_|\___|')
time.sleep(1)
print('   _           ')
print('  | |       	  ')	
print('  | |_ ___     ')
print('  | __/ _ \    ')
print('  | || (_) |   ')
print('   \__\___/    ')
time.sleep(1)
print('  _ ')
print(' (_)')
time.sleep(1)    
print('       _ ')
print('      (_)')
time.sleep(1)    
print('             _ ')
print('            (_)') 
time.sleep(1.25)          
print('__      __         ______        _____   _____   _  ')  #Very Accurate Eco-System Simulator
print('\ \    / / /\     |  ____|      / ____| / ____| | | ')
print(' \ \  / / /  \    | |__  ______| (___  | (___   | | ')
print('  \ \/ / / /\ \   |  __||______|\___ \  \___ \  | | ')
print('   \  / / ____ \ _| |____ _   _ ____) | ____) | |_| ')
print('    \(_)_/    \_(_)______(_) (_)_____(_)_____/  (_) ')
time.sleep(0.75)
print('A.K.A Very Accurate Eco-System Simulator (BETA-1.0)')
print()
#patch notes
time.sleep(2)
print()
print('Beta 1.0 has introduced:')
print(f'-The world of {RED}c{YELLOW}o{GREEN}l{CYAN}o{BLUE}u{MAGENTA}r{RESET}!')
print('-Major menu overhaul!')
print('-Added help section')
print(f'-There are now {GREEN}2{RESET} while loops at play! (thank god)')
print('-Patch notes have now been moved out of the way.')
print('-Added achievements.')
print(f'-Diseases have been added.')
print()
time.sleep(0.5)
print(f'-P.S, It is reccommended to run this through the {BLUE}Windows {RESET}or {YELLOW}Python {RESET}terminal! Type EXACTLY what it tells you to. Besides the predators, prey, scavengers and plants! Those are all yours :)')
print()
time.sleep(3)
print()
game = input(f'{GREEN}Play {RESET}or {RED}Exit{RESET}?-')          #menu
if game == 'Exit':
    print('Bye bye!')
    time.sleep(1.5)
    print('jerk...')
    time.sleep(0.25)
    exit()




#help menu
helpmenu = input('\033[0mWould you like some help?-\033[0m \033[92mYES(EXTREMELY RECCOMMENDED)\033[92m \033[91mNO\033[91m\033[0m-\033[0m')
helpmenu2 = 0

if helpmenu == 'YES':
    helpmenu2 = 1
    while helpmenu2 == 1:
        print()
        print(f'What would you like {GREEN}help{RESET} with?-')
        print(f"Predators, Prey, Plants, Scavengers, Climate Change, Events, Weather, Seasons, Ticks, Diseases, Patch Notes. Type '{RED}Exit{RESET}' to leave.")
        helprequest = input('Enter-')
        if helprequest == 'Exit':
            print()
            break
        elif helprequest == 'Diseases':
            print()
            print(f"Diseases are sudden and can last 1-3 months. They lower the species' population.")
        elif helprequest == 'Predators':
            print()
            print('At the top of the food chain, Predators are the killers in the ecosystem, they keep the population of the prey and scavengers in check. Their population growth is slow to compensate for that. The Predators represent animals such as wolves, tigers, etc.')
            print()
            time.sleep(1.5)
            print('----------------------------------------------')
        elif helprequest == 'Prey':
            print()
            print('Prey represent your typical herbivore, they feed on plants and breed quickly. They are near the bottom of the food-chain and are eaten by everyone besides the plants. The Prey represent animals such as sheep, rabbits, deer, etc.')
            print()
            time.sleep(1.5)
            print('----------------------------------------------')
        elif helprequest == 'Plants':
            print()
            print('At the bottom of the food chain, they grow rapidly and are fed on by the Prey and Scavengers. They are VITAL. The plants represent... well... Plants.')
            print()
            time.sleep(1.5)
            print('----------------------------------------------')
        elif helprequest == 'Scavengers':
            print()
            print('The scavengers are the most unique, they are just below the predators in the food chain. They feed on plants and also prey in smaller amounts. They, as their name suggests they prefer to scavenge rather than hunt. The Scavengers represent animals such as foxes, raccoons, etc.')
            print()
            time.sleep(1.5)
            print('----------------------------------------------')
        elif helprequest == 'Climate Change':
            print()
            print(f'Climate Change is an option that you may change during the setup phase. It can drastically affect plants and adds many events related to it. You should keep this turned {RED}off{RESET} for your first run!')
            print()
            time.sleep(1.5)
            print('----------------------------------------------')
        elif helprequest == 'Events':
            print()
            print(f'Events are random things that have a chance to occur each {YELLOW}Tick{RESET}. They will always display a message explaining what happens.')
            print()
            time.sleep(1.5)
            print('----------------------------------------------')
        elif helprequest == 'Weather':
            print()
            print(f'Weather is randomised on each {YELLOW}Tick{RESET}. Each weather has an impact on the population growth and decline of species.')
            print()
            time.sleep(1.5)
            print('----------------------------------------------')
        elif helprequest == 'Seasons':
            print()
            print(f'Seasons, much like {YELLOW}Weather{RESET} impact species populations but on a grander scale. They last 3 {YELLOW}Ticks{RESET} each. (Weather will soon be impacted by seasons).')
            print()
            time.sleep(1.5)
            print('----------------------------------------------')
        elif helprequest == 'Ticks':
            print()
            print(f"Ticks are the game's way of counting time. Each tick will print out the population of the populations, seasons, weather, events, etc. Each tick is 3 seconds at the moment.")
            print()
            time.sleep(1.5)
            print('----------------------------------------------')
        elif helprequest == 'Patch Notes':
            print()
            print('Choose: Alpha-1.0, Alpha-1.5, Alpha-2.0, Alpha-3.0 or Beta-1.0')
            patchnote = input('Which patchnotes would you like to read?-')
            if patchnote == 'Alpha-1.0':
                print()
                print('Alpha 1.0 has introduced:')
                print('-Simulation is much more accurate and random now, due to being rewritten to be percentage based along with many other balancing changes.')
                print('-Added fully functional seasons with side-effects')
                print('-Added year counter')
                print('-Added nuke and actual functioning radiation (lol)')
                print("-Added alot more events, making it more interesting compared to the Pre-Alpha's singular event...")
                print('-Polished intro and edited alot of text.')
                print('-Prey population growth now scales based on the number of plants (Used to be completely flat growth number)')
                print('-Added congratulatory message each time your ecosystem survives a year (You should probably follow the default numbers the first go around...)')
                print("-Made the ending message less useless with actual stats (It's only a single stat)")
                print('-Overhauled climate change completely, percentage based, extra mode, more polished.')
                print('-Added snarky code comments and under the hood changes you will never see')
                print('-Made everything easier to understand for the player.')
                print('-Made exit less sudden (and now with added coolness)')
                print('-Added event based on the options you selected at the start! (More soon to come!)')
                print('-General polish everywhere.')
                print('-Added patch notes (bruh)')
                print()
                time.sleep(1.5)
                print('----------------------------------------------')
                
            elif patchnote == 'Alpha-1.5':
                print()
                print('Alpha 1.5 has introduced:')
                print('-Everything (Besides events) is now percentage based!')
                print('-Major balancing changes. (simulation can last more than 6 years!)')
                print('-New predator control event.')
                print('-Removed cuss words')
                print('-Changed file name to the actual name (bruh)')
                time.sleep(1.5)
                print('----------------------------------------------')
                
            elif patchnote == 'Alpha-2.0':
                print()
                print('-Alpha 2.0 has introduced:')
                print('-Weather system has been implemented')
                print('-More events have been added')
                print('-Overhauled radiation completely.')
                print('-Alot of improvements to print and output code along with general polish')
                time.sleep(1.5)
                print('----------------------------------------------')
                
            elif patchnote == 'Alpha-3.0':
                print()
                print('Alpha 3.0 has introduced:')
                print('-New species!!! The scavengers, which feast upon prey and plants now help balance out the simulation.')
                print('-More events!')
                print('-Alot of balancing changes.')
                print('-Small predator hunting overhaul.')
                print('-Climate change improved.')
                time.sleep(1.5)
                print('----------------------------------------------')
                
            elif patchnote == 'Beta-1.0':
                print()
                print('Beta 1.0 has introduced:')
                print(f'-The world of {RED}c{YELLOW}o{GREEN}l{CYAN}o{BLUE}u{MAGENTA}r{RESET}!')
                print('-Major menu overhaul!')
                print('-Added help section')
                print(f'-There are now {GREEN}2{RESET} while loops at play! (thank god)')
                print('-Patch notes have now been moved out of the way.')
                print('-Added achievements.')
                print(f'-Diseases have been added.')
                time.sleep(1.5)
                print('----------------------------------------------')
                
            else:
                print()
                print('Invalid! Check your spelling and capitals!')
                print()
                time.sleep(1.5)
                print('----------------------------------------------')
                
                
                
                
                
                
            
            
            
        else:
            print()
            print('Invalid! Check your spelling and capitals!')
            print()
            time.sleep(1.5)
            print('----------------------------------------------')
                
            


#setup
print()
print(f'The numbers in {GREEN}green{RESET} are reccommended for a first playthrough!')
predator = int(input(f'Enter the amount of {YELLOW}Predators{RESET} (Should not be very high) ({GREEN}25{RESET})-'))
prey = int(input(f'Enter the amount of {YELLOW}Prey{RESET} (Should be many times higher than Predators) ({GREEN}1000{RESET})-'))
plants = int(input(f'Enter the amount of {YELLOW}Plants{RESET} (Should be alot more than Prey) ({GREEN}10000{RESET})-'))
scavenger = int(input(f'Enter the amount of {YELLOW}Scavengers{RESET} (Should be inbetween Prey and Predators) ({GREEN}300{RESET})-'))

climatechange = input(f'Is there {YELLOW}climate change{RESET}? {GREEN}YES{RESET}/{RED}NO{RESET} (Answer in all caps. {RED}NO{RESET} is {GREEN} reccommended{RESET} for a first playthrough.')


ccmild = 0      #climate modifiers
ccmoderate = 0
cchigh = 0
cckillme = 0
                 


if climatechange == 'YES':																	#climate change modifier
    climatemode = input(f'What mode of {YELLOW}Climate Change{RESET}? {WHITE}Mild{RESET}, Moderate, High or are you a Bad Person?-')
    if climatemode == 'Mild':
         ccmild = 1
         print('Climate change is mild')
    elif climatemode == 'Moderate':
        ccmoderate = 1
        print('Climate change is moderate')
    elif climatemode == 'High':
        cchigh = 1
        print('Climate change is high')
    elif climatemode == 'Bad Person':
        cckillme = 1
        print('Bad boy ;3')

predatortype = input(f'What type of {YELLOW}Predators{RESET} are we dealing with? (Regular, Fast Breeder, Fast Hunter.)-')

ptregular = 0
ptfb = 0
ptfh = 0

if predatortype == 'Regular':              #predator modifiers
    ptregular = 1
elif predatortype == 'Fast Breeder':
    ptfb = 1
elif predatortype == 'Fast Hunter':
    ptfh = 1

season = 0     #summer = 1-3 , autumn = 4-6, winter = 7-9, spring = 10-12
years_survived = 0          #stat to display at ecosystem collapse

radiation = 0           #random buffs and debuffs
    
#simulation start, rewrite nearly done 
print()
print("Every 1 equals 10, so 100 is actually equal to 1000, that's why there are decimals. TLDR SCALE 1/10")
print('Each tick is 1 month')
print()
if ccmild == 1 or ccmoderate ==1 or cchigh == 1:
    print('Climate change will heavily affect the already fragile and damaged ecosystem...')
if cckillme == 1:
    print("This simulation won't last very long will it...")
print()

while True:     #somehow works idk, dont touch too much
    #plant code
    if plants >= 1:
        plants += plants * 0.07    #plant growth
          
        if season>=1 and season <=3:     #summer
            plants += plants * 0.075
        elif season>=4 and season <=6:   #autumn
            plants -= plants * 0.04
        elif season>=7 and season <=9:   #winter
            plants -= plants * 0.1
        elif season>=10 and season <=12: #spring
            plants += plants * 0.25
            
        if ccmild == 1:     #climate change debuffs
            plants -= plants * 0.005
        elif ccmoderate == 1:
            plants -= plants * 0.01
        elif cchigh == 1:
            plants -= plants * 0.05
        elif cckillme == 1:
            plants -= plants * 0.1
            
    #prey code
    if plants > 0 and prey >= 2:
        plants -= prey // 1.45   #prey plant eating
        if plants > 6000:        #prey reproduction
           prey += prey * 0.025        #scales based on plant population
        if plants <= 3500:           #wtf why is it based on an arbitrary number :skull_emoji:
           prey -= prey * 0.02
        if plants<=999:
           prey -= prey * 0.08
           
           
           
        if season>=1 and season <=3:   #summmer    #prey percentage reproduction
            prey+= prey * 0.02
        if season>=4 and season <=6:   #autumn
            prey-=prey * 0.001
        if season>=7 and season <=9:   #winter 
            prey-=prey * 0.02
        if season>= 10 and season <=12:#spring
            prey+=prey * 0.035
           
    
    
    #scav code
    scavenger_rate = 1                   #change if balancing eating
    if scavenger >= 1:                  
        prey -= prey * 0.001 * scavenger_rate         #scav eating
        plants -= plants * 0.0025 * scavenger_rate

                     #scav reproduction
        if season>=1 and season <=3:   #summmer    #scav percentage reproduction
            scavenger+= scavenger * 0.04
        if season>=4 and season <=6:   #autumn
            scavenger-=scavenger * 0.01
        if season>=7 and season <=9:   #winter 
            scavenger-=scavenger * 0.025
        if season>= 10 and season <=12:#spring
            scavenger+=scavenger * 0.055
    
    
    
    
    
    
    
    #pred code
    predator_rate = 1
    if prey > 0 and predator >= 2:
        prey -= predator // 2  #predator hunting
        scavenger -= scavenger * 0.0015 * predator_rate
        if ptfh == 1:
            prey-= predator //5
            scavenger -= predator//1.75
            
        predator += predator * 0.0001            #predator reproduction
        if ptfb == 1:
            predator += predator * 0.00025
        
   
    #starvation code
    if prey<1 and predator>1:  #no food :(   (predator)
        predator *= 0.8
        
    if prey>1 and plants<1:   #no food 2 (prey)
        prey *= 0.8
        
    if scavenger>1 and plants<1 and prey<1:  #no food 3 (scav)
        scavenger *= 0.8
        
    if predator>prey:   #not enough food (predator)
        predator-=1
        
    if prey>plants:   #not enough  food2 (prey)
        prey-=5
        
        
        
    if predator>1:   #natural predator death idk
        predator-=0.2
        
    #numbers wont go into negatives
    plants = max(plants, 0)
    prey = max(prey, 0)
    predator = max(predator, 0)
    
    #diseases
   # disease duration counters
    if 'blight_active' not in locals():     #only way this works without creating disease ultra overload
        blight_active = 0
        flu_active = 0
        rabies_active = 0
        parasite_active = 0



#blight (plants)
    if blight_active == 0 and random.randint(0,50) == 49:
        blight_active = random.randint(1,3)
        print('----------------------------------------------')
        print(f'A {GREEN}Blight{RESET} has affected the {YELLOW}Plant{RESET} population!.')
    if blight_active >=1:
        print('----------------------------------------------')
        print(f'The {GREEN}Blight continues...')
        

#flu (prey)
    if flu_active == 0 and random.randint(0,50) == 48:
        flu_active = random.randint(1,3)
        print('----------------------------------------------')
        print(f'A {GREEN}Flu{RESET} has affected the {YELLOW}Prey{RESET} population!.')
    if flu_active >=1:
        print('----------------------------------------------')
        print(f'The {GREEN}Flu{RESET} spreads...')
        

#rabies (scavengers)
    if rabies_active == 0 and random.randint(0,50) == 47:
        rabies_active = random.randint(1,3)
        print('----------------------------------------------')
        print(f'{GREEN}Rabies{RESET} has affected the {YELLOW}Scavenger{RESET} population!.')
    if rabies_active >=1:
        print('----------------------------------------------')
        print(f'{GREEN}Rabies{RESET} spreads...')
        
        

#parasites (predators)
    if parasite_active == 0 and random.randint(0,50) == 46:
        parasite_active = random.randint(1,3)
        print('----------------------------------------------')
        print(f'A {GREEN}Parasite{RESET} has affected the {YELLOW}Predator{RESET} population!.')
    if parasite_active >=1:
        print('----------------------------------------------')
        print(f'The {GREEN}Parasite{RESET} spreads...')
        


#disease debuffs

    if blight_active > 0:
        plants -= 750
        blight_active -= 1

    if flu_active > 0:
        prey -= 50
        flu_active -= 1

    if rabies_active > 0:
        scavenger -= 30
        rabies_active -= 1

    if parasite_active > 0:
        predator -= 1
        parasite_active -= 1
        


   
        
    
    
    #events
    
    
    if random.randint(0,6) == 1:    #increases plant pop sometimes
        plants = plants+2250
        print()
        print('----------------------------------------------')
        print(f'{GREEN}Bloom{RESET}! (Plant pop increases)')
        
    if random.randint(0,10) == 5:
        prey = prey+100
        print()
        print('----------------------------------------------')
        print(f'Irruptive growth in {YELLOW}Prey{RESET} population!')   #sudden prey growth
        
    if random.randint(0,40) == 10:              #helps manage prey and plant pop
        prey = prey-80
        plants = plants-1000
        scavenger = scavenger-50
        predator = predator+5
        print()
        print('----------------------------------------------')
        print(f'A drought has massacred the {YELLOW}Prey{RESET} and {YELLOW}Scavenger{RESET} population, {YELLOW}Predators{RESET} feast on their corpses as plants wilt away!')
        
    if random.randint(0,1250) == 500:    #ecosystem killer
        plants = plants-7500
        prey = prey-750
        scavenger = scavenger-100
        predator = predator-25.5
        print()
        print('----------------------------------------------')
        print(f'Ultra Large Meteorite! {YELLOW}Plant{RESET} and animal populations are devastated!')
        
    if random.randint(0,1000) == 250:   #uh oh
        plants = plants-5000
        prey = prey-400
        scavenger = scavenger-100
        predator = predator-15.75
        radiation = 1
        print()
        print('----------------------------------------------')
        print(f'An untouched, abandoned nuclear device has suddenly detonated! {GREEN}Radiation{RESET} has contaminated the land!')
        
    if random.randint(0,35) == 8:        #plant control
        plants = plants-2000
        prey = prey-50
        scavenger = scavenger-10
        predator = predator-1
        print()
        print('----------------------------------------------')
        print(f'A forest fire has devastated {YELLOW}Plant{RESET} life in the area, and to an extent animal life aswell.')
        
    if ccmoderate == 1 or cchigh == 1 or cckillme == 1:       #climate consequence
        if random.randint(0,40) == 4:
            plants = plants-1500
            prey = prey-75
            scavenger = scavenger-25
            predator = predator-1.5
            print()
            print('----------------------------------------------')
            print('Acid rain, corrosive and hurts! (alot)')
            
            
    if predator>=100 and random.randint(0,7) == 3:                   #predator control
        predator = predator-25
        print()
        print('----------------------------------------------')
        print(f'There is too much competition for food! {YELLOW}Predator{RESET} populations drop...')
        
    if random.randint(0,55) == 20:        #natural disaster, make affected by climate change later
        print()
        print('----------------------------------------------')
        print("There's a natural disaster! All populations are affected!")       
        predator = predator - 10
        plants = plants - 2000
        scavenger = scavenger - 50
        prey = prey - 150
        
        
        
    if random.randint(0,10) == 9:                            #predator increases population
        print()
        print('----------------------------------------------')
        print(f'What a bountiful hunt for the {YELLOW}Predators{RESET}!')
        predator = predator + 2.5
        prey = prey - 100
        
        
    if random.randint(0,20) == 10:                            #invasive species
        print()
        print('----------------------------------------------')
        print('An invasive species has entered the ecosystem!')
        prey = prey-250
        scavenger = scavenger - 50
        plants = plants -7500
        
    if random.randint(0,75) == 44:                             #gotta put radiation in someway without it being ultra rare and for nothing...
        print()
        print('----------------------------------------------')
        print(f'An ancient nuclear plant has suddenly started leaking... {GREEN}Radiation{RESET} spreads!')
        radiation = 1
        
        
    if random.randint(0,15) == 12:                              #scav boost
        print()
        print('----------------------------------------------')
        print(f'{YELLOW}Scavenger{RESET} populations have been very lucky with their finds... (Scav pop increases.)')
        scavenger = scavenger + 50
        
        
        
    if ccmild == 0 and ccmoderate == 0 and cchigh == 0 and cckillme == 0 and random.randint(0,55) == 10:             #heatwave, cc affected
        print()
        print('----------------------------------------------')
        print(f'A {RED}heatwave{RESET} is approaching!')
        plants = plants - 1000
    if ccmild == 1 and ccmoderate == 0 and cchigh == 0 and cckillme == 0 and random.randint(0,25) == 10:
        print()
        print('----------------------------------------------')
        print(f'A {RED}heatwave{RESET} is approaching!')
        plants = plants - 2000
    if ccmild == 0 and ccmoderate == 1 and cchigh == 0 and cckillme == 0 and random.randint(0,20) == 10:
        print()
        print('----------------------------------------------')
        print(f'A {RED}heatwave{RESET} is approaching!')
        plants = plants - 3000   
    if ccmild == 0 and ccmoderate == 0 and cchigh == 1 and cckillme == 0 and random.randint(0,10) == 10:
        print()
        print('----------------------------------------------')
        print(f'A {RED}heatwave{RESET} is approaching!')
        plants = plants - 4000
    if ccmild == 0 and ccmoderate == 0 and cchigh == 0 and cckillme == 1 and random.randint(0,5) == 10:
        print()
        print('----------------------------------------------')
        print(f'A {RED}heatwave{RESET} is approaching!')
        plants = plants - 5000
    
        
        
        
        
        
        
        
        
    
    print()
    print('----------------------------------------------')
    print(f"Plants: {plants:.2f}, Prey: {prey:.2f}, Scavengers: {scavenger:.2f}, Predators: {predator:.2f}")  #stat display, rounds to 2 decimal points
    print()
   
    
    
    weather = random.randint(0,5)   #weather
    
    stormy = 0
    clear = 0
    sunny = 0
    cloudy = 0
    raining = 0
    windy = 0
    
    if weather == 0:                    #scuffed but works, no need for rework
        print('The weather is stormy!')
        stormy = 1
        clear = 0
        sunny = 0
        cloudy = 0
        raining = 0
        windy = 0
    if weather == 1:
        print('The weather is clear!')
        stormy = 0
        clear = 1
        sunny = 0
        cloudy = 0
        raining = 0
        windy = 0
    if weather == 2:
        print('It is sunny!')
        stormy = 0
        clear = 0
        sunny = 1
        cloudy = 0
        raining = 0
        windy = 0
    if weather == 3:
        print('It is cloudy!')
        stormy = 0
        clear = 0
        sunny = 0
        cloudy = 1
        raining = 0
        windy = 0
    if weather == 4:
        print('It is raining!')
        stormy = 0
        clear = 0
        sunny = 0
        cloudy = 0
        raining = 1
        windy = 0
    if weather == 5:
        print('It is windy!')
        stormy = 0
        clear = 0
        sunny = 0
        cloudy = 0
        raining = 0
        windy = 1
      
      
    if stormy == 1:                   #weather effects
        plants -= plants * 0.002
        prey -= prey * 0.001
        predator -= 0.1
        
    if clear == 1:
        plants += plants * 0.001
        prey += prey * 0.0025
        
    if sunny == 1:
        plants += plants * 0.002
        prey += prey * 0.004
    
    if cloudy == 1:
        plants -= plants * 0.001
        
    if raining == 1:
        plants += plants * 0.003
        
    if windy == 1:
        plants -= plants * 0.001
        
    
    #radiation system
    
    
    if radiation >= 1:
        radiation = radiation + 1
        print(f'{GREEN}Radiation{RESET} plagues the land!')
    if radiation == 36:
        print(f'Most of the {GREEN}radiation{RESET} has dissipated...')
        radiation = 0
        
    if radiation >= 1 and radiation <=12:          #rad effects
        plants -= plants * 0.075
    if radiation >=13 and radiation <=24:
        plants -= plants * 0.05
    if radiation >=25 and radiation <=30:
        plants -= plants * 0.005
    if radiation >= 31 and radiation <= 35:
        plants -= plants * 0.0025
        
        
        
        
        
        
        
        
    
    if plants<1:                               #game ending
        print('Ecosystem Collapse!')
        time.sleep(0.75)
        print(f"The ecosystem has survived: {years_survived} years!")
        time.sleep(5)
        exit()
    elif predator<1:
        print('Ecosystem Collapse!')
        time.sleep(0.75)
        print(f"The ecosystem has survived: {years_survived} years!")
        time.sleep(5)
        exit()
    elif prey<1:
        print('Ecosystem Collapse!')
        time.sleep(0.75)
        print()
        print(f"The ecosystem has survived: {years_survived} years!")
        time.sleep(5)
        exit()
    elif scavenger<1:
        print('Ecosystem Collapse!')
        time.sleep(0.75)
        print()
        print(f"The ecosystem has survived: {years_survived} years!")
        time.sleep(5)
        exit()
    
    
    #counters, dont touch

    season +=1                            
 
    
    
    
    
    #seasons
    
    if season>=1 and season<=3:             
        print(f'{RED}Summer{RESET}!')
    elif season>=4 and season <=6:
        print(f'{YELLOW}Autumn{RESET}!')
    elif season>=7 and season <=9:
        print(f'{BLUE}Winter{RESET}!')
    elif season>=10 and season <=12:
        print(f'{GREEN}Spring{RESET}!')
        
    if season == 13:                                          #year counter
        print('The ecosystem has survived a full year!')
        season = 1
        years_survived +=1
        print(f'{YELLOW}Summer{RESET}!')
        
        
    achievement_ys = 0                     #Achievements
    achievement_ccys = 0
        
    if years_survived >= 5:
        achievement_ys = 1
        print('Achievement unlocked! 5 years survived.')
        
    if cckillme == 1 and years_survived == 1:
        achievement_ccys = 1
        print("Achievement unlocked! You've done the impossible...")
        
        
    print('Month',season)
    print(f'Years survived: {years_survived}')
    print()
    print()
    print()
    time.sleep(3)
    
    
    
    