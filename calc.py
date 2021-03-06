import math
import random

#test

#main menu function
def mainMenu():

    #vars
    #general
    result = "error: input out of range"
    option = 0

    #main Menu
    option = float(input("[0:exit] [1:einfach] [2:komplex] [3:trigonometrie] [4:umrechnung] [5:grafiktaschenrechner] [6:algorithmen] [7:freie berechnung] [8:konstanten]"))

    
     
    

    #easter egg: 1 Rock Paper Scissors game!
    if(option == float(42)):
        def rock_paper_scissors():
            print("Welcome to Rock Paper Scissors")
            print("Please choose:")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            print("4. Quit")
            user_choice = int(input("Enter your choice: "))
            while user_choice != 4:
                computer_choice = random.randint(1, 3)
                if user_choice == computer_choice and user_choice == 1:
                    print("\nTie! We both chose rock!\n")
                if user_choice == computer_choice and user_choice == 2:
                    print("\nTie! We both chose paper!\n")
                if user_choice == computer_choice and user_choice == 3:
                    print("\nTie! We both chose scissors!\n")
                elif user_choice == 1 and computer_choice == 2:
                    print("\nYou lose! I chose paper and you rock!\n")
                elif user_choice == 1 and computer_choice == 3:
                    print("\nYou win! You chose rock and i scissors!\n")
                elif user_choice == 2 and computer_choice == 1:
                    print("\nYou win! You chose paper and i rock!\n")
                elif user_choice == 2 and computer_choice == 3:
                    print("\nYou lose! I chose scissors and you paper!\n")
                elif user_choice == 3 and computer_choice == 1:
                    print("\nYou lose! I chose rock and you scissors!\n")
                elif user_choice == 3 and computer_choice == 2:
                    print("\nYou win! You chose scissors and i paper!\n")
                elif(user_choice == float(69)):
                    print("\nNice!\n")
                else:
                    print("\nYou loose because you didnt choose anything\n")
                print("Please choose:")
                print("1. Rock")
                print("2. Paper")
                print("3. Scissors")
                print("4. Quit")
                user_choice = int(input("Enter your choice: "))
            print("Thanks for playing")
            mainMenu()

        rock_paper_scissors()

    #function to return the result
    def resultFunction(result):
        print(str(result) + "\n")
        mainMenu()

    #function for the simple math
    if(option == float(1)):
        def simpleMenu(option):
            option = float(input("[0:go back] [1:addieren] [2:subtrahieren] [3:multiplizieren] [4:dividieren]"))
            
            #go back
            if(option == float(0)):
                mainMenu()

            input1 = float(input("input1: "))
            input2 = float(input("input2: "))

            #add
            if(option == float(1)):
                print("\n" + str(input1) + " + " + str(input2) + " = ")
                result = input1 + input2
                if(input1 + input2 == 0.1 + 0.2):
                    result = 0.3
                resultFunction(result)
            
            #substract
            elif(option == float(2)):
                print("\n" + str(input1) + " - " + str(input2) + " = ")
                result = input1 - input2
                resultFunction(result)
            
            #multiplicate
            elif(option == float(3)):
                print("\n" + str(input1) + " * " + str(input2) + " = ")
                result = input1 * input2
                resultFunction(result)
            
            #divide
            elif(option == float(4)):
                print("\n" + str(input1) + " / " + str(input2) + " = ")
                result = input1 / input2
                resultFunction(result)

        simpleMenu(option)
    
    #function for complicated math
    elif(option == float(2)):
        def complicatedMenu(option):
            option = float(input("[0:go back] [1:wurzel] [2:x^y]"))

            #go back
            if(option == float(0)):
                mainMenu()

            input1 = float(input("input1: "))
            
            #squareroot
            if(option == float(1)):
                print("\nWurzel aus " + str(input1) + " = ")
                result = math.sqrt(input1)
                resultFunction(result)

            #exponential
            elif(option == float(2)):
                input2 = float(input("input2: "))
                print("\n" + str(input1) + " ^ " + str(input2) + " = ")
                result = input1 ** input2
                resultFunction(result)

        complicatedMenu(option)
    
    #trigonometric functions
    elif(option == float(3)):
        def trigonometricMenu(option):
            option = float(input("[0:go back] [1:sin] [2:cos] [3:tan] [4:Dreieck]"))

            #go back
            if(option == float(0)):
                mainMenu()
            
            #triangular
            elif(option == float(4)):
                def triangularMenu(option):
                    option = float(input("[1:SSS] [2:SWS] [3:WSW] [4:WWS]")) #[5:SSW]

                    #go back
                    if(option == float(0)):
                        trigonometricMenu(option)

                    #SSS(Nur Seiten)
                    elif(option == float(1)):
                        input1 = float(input("a: "))
                        input2 = float(input("b: "))
                        input3 = float(input("c: "))
                        
                        alpha = float(math.degrees(math.acos(((input1 ** 2) - (input2 ** 2) - (input3 ** 2)) / ( -2 * input2 * input3))))
                        beta = float(math.degrees(math.acos(((input2 ** 2) - (input1 ** 2) - (input3 ** 2)) / ( -2 * input1 * input3))))
                        gamma = float(math.degrees(math.acos(((input3 ** 2) - (input2 ** 2) - (input1 ** 2)) / ( -2 * input2 * input1))))
                        
                        result = ("\na= " + str(input1) + "\nb= " + str(input2) + "\nc= " + str(input3) + "\nalpha= " + str(alpha) + "\nbeta=  " + str(beta) + "\ngamma= " + str(gamma))
                        resultFunction(result)
                    
                    #SWS(2 Seite ohne gegen??berliegenden Winkel(1))
                    elif(option == float(2)):
                        input1 = float(input("a: "))
                        input2 = float(input("beta: "))
                        input3 = float(input("c: "))
                        
                        b = float(math.sqrt((input1 ** 2 + input3 ** 2) - 2 * input1 * input3 * (math.cos((input2 * math.pi / 180)))))
                        alpha = float(math.degrees(math.asin(math.sin((input2 * math.pi / 180)) / b * input1))) 
                        gamma = float(180 - input2 - alpha)
                        
                        result = ("\na= " + str(input1) + "\nb= " + str(b) + "\nc= " + str(input3) + "\nalpha= " + str(alpha) + "\nbeta=  " + str(input2) + "\ngamma= " + str(gamma))
                        resultFunction(result)
                    
                    #WSW(2 Winkel ohne gegen??berliegender Seite(1))
                    elif(option == float(3)):
                        input1 = float(input("alpha: "))
                        input2 = float(input("b: "))
                        input3 = float(input("gamma: "))
                        
                        beta = float(180 - (float(input1) + float(input3)))
                        a = float(input2 / math.sin(beta * math.pi / 180) * math.sin(input1 * math.pi / 180))
                        c = float(input2 / math.sin(beta * math.pi / 180) * math.sin(input3 * math.pi / 180))

                        result = ("\na= " + str(a) + "\nb= " + str(input2) + "\nc= " + str(c) + "\nalpha= " + str(input1) + "\nbeta=  " + str(beta) + "\ngamma= " + str(input3))
                        resultFunction(result)
                    
                    #WWS(2 Winkel mit gegen??berliegender Seite(1))
                    elif(option == float(4)):
                        input1 = float(input("alpha: "))
                        input2 = float(input("beta: "))
                        input3 = float(input("a: "))
                        
                        gamma = float(180 - input1 - input2)
                        b = float(input3 / math.sin(input1 * math.pi / 180) * math.sin(input2 * math.pi / 180))
                        c = float(input3 / math.sin(input1 * math.pi / 180) * math.sin(gamma * math.pi / 180))
                        
                        result = ("\na= " + str(input3) + "\nb= " + str(b) + "\nc= " + str(c) + "\nalpha= " + str(input1) + "\nbeta=  " + str(input2) + "\ngamma= " + str(gamma))
                        resultFunction(result)

                    #SSW(2 Seiten mit gegen??berliegenden Winkel(1))
                    #elif(option == float(5)):
                    #    input1 = float(input("a: "))
                    #    input2 = float(input("b: "))
                    #    input3 = float(input("alpha: "))
                    #    beta = float(math.asin(math.sin(alpha * math.pi / 180) * input2))
                    #    gamma = float(180 - input3 - beta)
                    #    c = (input1 / math.sin(input3 * math.pi / 180) * math.sin(gamma * math.pi / 180)) 
                    #    result = ("\na= " + str(input1) + "\nb= " + str(input2) + "\nc= " + str(c) + "\nalpha= " + str(input3) + "\nbeta=  " + str(beta) + "\ngamma= " + str(gamma)) """
                
                triangularMenu(option)

            input1 = float(input("input1: "))
            
            #sin
            if(option == float(1)):
                print("\nSinus von " + str(input1) + " =")
                result = math.sin(input1)
                print("Grad:")
                print(result / math.pi / 180)
                print("Bogenma??:")
                resultFunction(result)
            
            #cos
            elif(option == float(2)):
                print("\nCosinus von " + str(input1) + " =")
                result = math.cos(input1)
                print("Grad:")
                print(result / math.pi / 180)
                print("Bogenma??:")
                resultFunction(result)
            
            #tan
            elif(option == float(3)):
                print("\nTangens von " + str(input1) + " =")
                result = math.tan(input1)
                resultFunction(result)


        trigonometricMenu(option)

    #conversion
    elif(option == float(4)):
        def conversionMenu(option):
            option = float(input("[0:go back] [1:L??nge] [2:Volumen]"))
        
            #goback
            if(option == float(0)):
                mainMenu()
        
            #distances
            elif(option == float(1)):
                option = float(input("[1:km->mil] [2:mil->km] [3:meter->feet] [4:feet->meter] [5:cm->zoll] [6:zoll->cm] [7:km->sm] [8:sm->km]"))
                input1 = float(input("input1: "))

                def distancesMenu(option):
                    #km->mil
                    if(option == float(1)):
                        result = input1 / 1.609
                        resultFunction(result)
                    
                    #mil->km
                    elif(option == float(2)):
                        result = input1 * 1.609
                        resultFunction(result)

                    #meter->feet
                    elif(option == float(3)):
                        result = input1 * 3.281
                        resultFunction(result)

                    #feet->meter
                    elif(option == float(4)):
                        result = input1 / 3.281
                        resultFunction(result)

                    #cm->zoll
                    elif(option == float(5)):
                        result = input1 / 2.54
                        resultFunction(result)
                    
                    #zoll->cm
                    elif(option == float(6)):
                        result = input1 * 2.54
                        resultFunction(result)
                    
                    #km->sm
                    elif(option == float(7)):
                        result = input1 / 1.852
                        resultFunction(result)
                    
                    #sm->km
                    elif(option == float(8)):
                        result = input1 * 1.852
                        resultFunction(result)
                    
                distancesMenu(option)
            
            #volume
            elif(option == float (2)):
                result = "error: function not availible yet"
                resultFunction(result)

        conversionMenu(option)
    
    #space for graphical calculator
    
    elif(option == float(5)):
        def graphicalMenu(option):



            option = float(input("[1:linear] [2:exponential] [3:sinusfuktion] [4:cosinusfunktion]"))
            import pygame

            if(option == 1):
                print("formel: f(x)=ax+b")
                a = float(input("a: "))
                b = float(input("b: ")) * 50 - float(250)

                screenx = 500
                screeny = 500
                pygame.init()
                screen = pygame.display.set_mode((screenx, screeny))
                screen.fill((255, 255, 255))

                for i in range(10):
                        i = (i - 5) * 50

                        altx = float(i + 250)
                        alty = float((a * i + b) * -1)
                        
                        x = float(i + 300)
                        y = float((a * (i + 50) + b) * -1)
                        
                        print("x= " + str(x) + "y= " + str(y) + "altx= " + str(altx) + "alty= " + str(alty))
                        #pygame.draw.line(screen, (255, 255, 255), (altx, alty), (x, y), 2)
                        #pygame.display.update()

                while True:
                    for event in pygame.event.get():
        
                        if event.type == pygame.QUIT:
                            quit()
    
                    
                    for i in range(10):
                        i = (i - 5) * 50
                        
                        pygame.draw.line(screen, (20, 40, 60), (250, 0), (250, 500))
                        pygame.draw.line(screen, (20, 40, 60), (0, 250), (500, 250))

                        pygame.draw.line(screen, (20, 40, 60), (245, 225), (255, 225))
                        pygame.draw.line(screen, (20, 40, 60), (240, 200), (260, 200))
                        pygame.draw.line(screen, (20, 40, 60), (245, 175), (255, 175))
                        pygame.draw.line(screen, (20, 40, 60), (240, 150), (260, 150))
                        pygame.draw.line(screen, (20, 40, 60), (245, 125), (255, 125))
                        pygame.draw.line(screen, (20, 40, 60), (240, 100), (260, 100))
                        pygame.draw.line(screen, (20, 40, 60), (245, 75), (255, 75))
                        pygame.draw.line(screen, (20, 40, 60), (240, 50), (260, 50))
                        pygame.draw.line(screen, (20, 40, 60), (245, 25), (255, 25))
                        pygame.draw.line(screen, (20, 40, 60), (240, 0), (260, 0))
                        pygame.draw.line(screen, (20, 40, 60), (245, 275), (255, 275))
                        pygame.draw.line(screen, (20, 40, 60), (240, 300), (260, 300))
                        pygame.draw.line(screen, (20, 40, 60), (245, 325), (255, 325))
                        pygame.draw.line(screen, (20, 40, 60), (240, 350), (260, 350))
                        pygame.draw.line(screen, (20, 40, 60), (245, 375), (255, 375))
                        pygame.draw.line(screen, (20, 40, 60), (240, 400), (260, 400))
                        pygame.draw.line(screen, (20, 40, 60), (245, 425), (255, 425))
                        pygame.draw.line(screen, (20, 40, 60), (240, 450), (260, 450))
                        pygame.draw.line(screen, (20, 40, 60), (245, 475), (255, 475))
                        pygame.draw.line(screen, (20, 40, 60), (240, 500), (260, 500))

                        pygame.draw.line(screen, (20, 40, 60), (225, 245), (225, 255))
                        pygame.draw.line(screen, (20, 40, 60), (200, 240), (200, 260))
                        pygame.draw.line(screen, (20, 40, 60), (175, 245), (175, 255))
                        pygame.draw.line(screen, (20, 40, 60), (150, 240), (150, 260))
                        pygame.draw.line(screen, (20, 40, 60), (125, 245), (125, 255))
                        pygame.draw.line(screen, (20, 40, 60), (100, 240), (100, 260))
                        pygame.draw.line(screen, (20, 40, 60), (75, 245), (75, 255))
                        pygame.draw.line(screen, (20, 40, 60), (50, 240), (50, 260))
                        pygame.draw.line(screen, (20, 40, 60), (25, 245), (25, 255))
                        pygame.draw.line(screen, (20, 40, 60), (275, 245), (275, 255))
                        pygame.draw.line(screen, (20, 40, 60), (300, 240), (300, 260))
                        pygame.draw.line(screen, (20, 40, 60), (325, 245), (325, 255))
                        pygame.draw.line(screen, (20, 40, 60), (350, 240), (350, 260))
                        pygame.draw.line(screen, (20, 40, 60), (375, 245), (375, 255))
                        pygame.draw.line(screen, (20, 40, 60), (400, 240), (400, 260))
                        pygame.draw.line(screen, (20, 40, 60), (425, 245), (425, 255))
                        pygame.draw.line(screen, (20, 40, 60), (450, 240), (450, 260))
                        pygame.draw.line(screen, (20, 40, 60), (475, 245), (475, 255))
                        pygame.draw.line(screen, (20, 40, 60), (500, 240), (500, 260))

                        pygame.display.update()
                        
                        altx = float(i + 250)
                        alty = float((a * i + b) * -1)
                        
                        x = float(i + 300)
                        y = float((a * (i + 50) + b) * -1)
                        
                        #print("x= " + str(x) + "y= " + str(y) + "altx= " + str(altx) + "alty= " + str(alty))
                        pygame.draw.line(screen, (0, 0, 255), (altx, alty), (x, y))
                        pygame.display.update()
                        
                        
            elif(option == float(2)):
                print("formel: f(x)=ax^2+b")
                
            elif(option == float(3)):


                print("formel: s(x)=a*sin(c(x-b))")
                a = float(input("a: "))
                b = float(input("b: "))
                c = float(input("c: "))

                screenx = 500
                screeny = 500

                pygame.init()
                screen = pygame.display.set_mode((screenx, screeny))
                screen.fill((255, 255, 255))

                for x in range(screenx):

                    x = x
                    altx = x - 1
                    y = a * math.sin(c * (x -b))
                    alty = a * math.sin(c * (altx -b))

                    

                    y = y * 250
                    alty = alty * 250
                    y = y + 250
                    alty = alty + 250
                    
                    print("x= " + str(x) + "y= " + str(y) + "altx= " + str(altx) + "alty= " + str(alty))
                
                while True:
                    for event in pygame.event.get():
    
    
                        if event.type == pygame.QUIT:
                            quit()
                    for x in range(screenx):
                        
                        altx = x - 1
                        altx = altx * 0.01
                        x = x * 0.01
                        alty = a * math.sin((c * ( altx - b)))
                        y = a * math.sin((c * ( x - b)))
                        y = y * 100
                        alty = alty * 100
                        x = x * 100
                        altx = altx * 100

                        
                        pygame.draw.line(screen, (255, 0, 0), (altx, alty + int(screenx / 2)), (x, y + int(screenx / 2)))
                        pygame.display.update()
                    

                    
                        
                    pygame.draw.line(screen, (20, 40, 60), (250, 0), (250, 500))
                    pygame.draw.line(screen, (20, 40, 60), (0, 250), (500, 250))
                    pygame.display.update()
                

        graphicalMenu(option)


    #crypto functions
    elif(option == float(6)):
        def cryptoMenu(option):
            option = float(input("[0:go back] [1:sha] [2:md] [3:shake] [4:blake2]"))
            import hashlib

            if(option == float(1)):
                option = float(input("[1:sha256] [2:sha512] [3:sha224] [4:sha384] [5:sha1]"))
            elif(option == float(2)):
                option = float(input("[1:md5]")) + float(10)
            elif(option == float(3)):
                option = float(input("[1:shake_128] [2:shake_256]")) + float(20)
            elif(option == float(4)):
                option = float(input("[1:blake2b] [2:blake2s]")) + float(30)

            input1 = str(input("input1: "))
            
            if(option == float(0)):
                mainMenu()
            elif(option == float(1)):
                result = hashlib.sha256(input1.encode("ascii")).hexdigest()
                resultFunction(result)
            elif(option == float(2)):
                result = hashlib.sha512(input1.encode("ascii")).hexdigest()
                resultFunction(result)
            elif(option == float(3)):
                result = hashlib.sha224(input1.encode("ascii")).hexdigest()
                resultFunction(result)
            elif(option == float(4)):
                result = hashlib.sha384(input1.encode("ascii")).hexdigest()
                resultFunction(result)
            elif(option == float(5)):
                result = hashlib.sha1(input1.encode("ascii")).hexdigest()
                resultFunction(result)
            
            elif(option == float(11)):
                result = hashlib.md5(input1.encode("ascii")).hexdigest()
                resultFunction(result)

            elif(option == float(21)):
                result = hashlib.shake_128(input1.encode("ascii")).hexdigest()
                resultFunction(result)
            elif(option == float(22)):
                result = hashlib.shake_256(input1.encode("ascii")).hexdigest()
                resultFunction(result)
        
            elif(option == float(31)):
                result = hashlib.blake2b(input1.encode("ascii")).hexdigest()
                resultFunction(result)
            elif(option == float(32)):
                result = hashlib.blake2s(input1.encode("ascii")).hexdigest()
                resultFunction(result)

        cryptoMenu(option)

    #Freie berechnung (funktioniert nicht!!!)
    elif(option == float(7)):
        def freeMenu(option):
            
            print("\naktuell k??nnen nur + - * / benutzt werden k??nnen und nur ein Operator gleichzeitig!!!\n")
            input1 = input("Input1: ")
            if(input1.find('+')!=-1):
                result = sum(map(float,(input1.split('+'))))
            if(input1.find('-')!=-1):
                result = sum(map(float,(input1.split('-'))))
            if(input1.find('*')!=-1):
                result = sum(map(float,(input1.split('*'))))
            if(input1.find('/')!=-1):
                result = sum(map(float,(input1.split('/'))))

            print(float(str(input1)))
            

            print(result)
            
            




        freeMenu(option)

    elif(option == float(8)):
        def konsMenu(option):
            option = float(input("[0:go back] [1:Mathe] [2:Physik] [3:Chemie]"))

            if(option == float(1)):
                option = float(input("[0:go back] [1:pi]"))

                if(option == float(1)):
                    result = math.pi
                    resultFunction(result)
            elif(option == float(2)):
                result = 0

            elif(option == float(3)):
                input1 = str(input("input1: "))

                f = open("Periodensystem.txt", "r")
                result = f.readline(input1)
                resultFunction(result)
                


            
                    



        konsMenu(option)

        
    
                
    
    
    
    
    elif(option == 69):
        print("\nNice!\n")
    elif(option == 0): 
        exit()

mainMenu()
