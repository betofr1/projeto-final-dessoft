import pygame
import tabuleiro
import random 
import ala_norte
import ala_sul

#funcao botao
def botao(texto,x,y,l,a,cor1,tela,font,action = None):
    TILESIZE = 20
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(tela, cor1, (x*TILESIZE,y*TILESIZE, l*TILESIZE, a*TILESIZE))
    tela.blit(font.render(texto, True, (0,0,0)), (x*TILESIZE, y*TILESIZE))
    if x*TILESIZE+l*TILESIZE > mouse[0] > x*TILESIZE and y*TILESIZE+a*TILESIZE > mouse[1] > y*TILESIZE:
        if click[0] == 1 and action != None:
            if action == 'play':
                return 1
            if action == 'quit':
                return 2
    


class Monstro:
    def __init__(self,x,y,cor,tamanho,tela,tab,vida_m):
        self.tab = tab
        self.tela = tela
        self.tamanho = tamanho
        self.x = x
        self.y = y
        self.cor = cor
        self.ret =pygame.Rect(self.x*self.tamanho,self.y*self.tamanho,self.tamanho,self.tamanho)
        self.MAPWIDTH = len(tab[0])
        self.MAPHEIGHT = len(tab)
        self.vida_m = vida_m
       



    def anda(self,l1,l2,l3,count):
        self.count = count
        
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
       
        
        if self.ret.colliderect(self.l1) == True or self.ret.colliderect(self.l2) == True or self.ret.colliderect(self.l3) == True:    
            pygame.draw.rect(self.tela, self.cor, self.ret)
        
        if self.count == 0:
            
            num = random.randint(0,4)    
            if self.x < (self.MAPWIDTH - 1) and self.tab[self.y][self.x+1] != 1 and self.tab[self.y][self.x+1] != 5:
                if num == 0:
                    self.ret.move_ip(1*self.tamanho,0)
                    self.x += 1
            if self.y < (self.MAPHEIGHT -1) and self.tab[self.y+1][self.x] != 1 and self.tab[self.y+1][self.x] != 5:
                if num == 1:
                    self.ret.move_ip(0,1*self.tamanho)
                    self.y += 1
            if self.y >0 and self.tab[self.y-1][self.x] != 1 and self.tab[self.y-1][self.x] != 5:
                if num == 2:
                    self.ret.move_ip(0,-1*self.tamanho)
                    self.y -= 1
            if self.x > 0 and self.tab[self.y][self.x-1] != 1 and self.tab[self.y][self.x-1] != 5:
                if num == 3:
                    self.ret.move_ip(-1*self.tamanho,0)
                    self.x -= 1
                    
    
        
    def vida(self,vida_a,MONSTRO,arma,QUIT):
        
        self.vida_a = vida_a
        self.MONSTRO = MONSTRO
        self.arma = arma
        self.QUIT = QUIT
        
        if self.arma == True:
            
            if self.vida_m > 0 and self.vida_a > 0:
                self.vida_m = self.vida_m - self.vida_a
                
                print("vida monstro: ", self.vida_m)
                print("vida arma", self.vida_a)
                
            if self.vida_m <= 0: 
                self.MONSTRO = False
                print("morreu")
            
            if self.vida_a <= 0 and self.vida_m > 0:
                self.MONSTRO = True 
                self.QUIT = True
            
            if self.vida_a <= 0: 
                self.arma = False
                
                
        if self.arma == False: 
            self.QUIT = True
            
            
            
        
            
        
        
        
            
        
def main():
    
    tab = tabuleiro.TAB
    #definindo dimensoes
    TILESIZE = 20
    MAPWIDTH = len(tab[0])
    MAPHEIGHT = len(tab)
    pygame.init()
    
    # definindo telas: 
    tela = pygame.display.set_mode([MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE])
    tela2 = pygame.Surface((TILESIZE*5,TILESIZE*30))
    telag_2= pygame.Surface((TILESIZE*4,TILESIZE*9))
    telag_3 = pygame.Surface((TILESIZE*4,TILESIZE*2))
    telag_4 = pygame.Surface((TILESIZE*3,TILESIZE*3))
    telag_5 = pygame.Surface((TILESIZE*1,TILESIZE*3))
    telag_6 = pygame.Surface((TILESIZE*3,TILESIZE*4))
    telag_7 = pygame.Surface((TILESIZE*1,TILESIZE*4))
    telag_8 = pygame.Surface((TILESIZE*4,TILESIZE*5))
    telag_9 = pygame.Surface((TILESIZE*2,TILESIZE*5))
    telag_10= pygame.Surface((TILESIZE*3,TILESIZE*5))
    telag_11 = pygame.Surface((TILESIZE*4,TILESIZE*3))
    telag_12 = pygame.Surface((TILESIZE*3,TILESIZE*4))
    telag_13 = pygame.Surface((TILESIZE*3,TILESIZE*4))
    telag_14 = pygame.Surface((TILESIZE*2,TILESIZE*1))
    telag_15 = pygame.Surface((TILESIZE*2,TILESIZE*5))
    telag_16 = pygame.Surface((TILESIZE*2,TILESIZE*5))
    
    # texto 
    fonte = pygame.font.SysFont("Arial", 100)
    fonte_2 = pygame.font.SysFont('Arial', 25)


    pygame.display.set_caption("LABIRINTO DOS INFERNO")
    relogio = pygame.time.Clock()
    
    #definindo cores: 
    BRANCO = (255,255,255)
    AZUL = (0,0,255)
    PRETO = (0,0,0)
    VERMELHO = (255,0,0)
    VERDE = (0,255,0)
    ROSA = (214,34,191)
    CINZA_SUPER_CLARO = (164,163,173)
    CINZA_CLARO = (139, 138, 153)
    CINZA_MEDIO = (129, 126, 143)
    CINZA_MEIO_ESCURO = (105, 104, 119)
    CINZA_ESCURO = (79, 78, 88)
    chave1 = False
    #definindo jogador
    pi = 14
    pj = 0
    jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)
    #definindo monstros
    mi_hall = 15
    mj_hall= 16
    m2i_hall = 3
    m2j_hall = 25
    m3i_hall = 27
    m3j_hall = 35
    mi_norte = 19
    mj_norte = 6
    m2i_norte = 17
    m2j_norte = 2
    m3i_norte = 22
    m3j_norte = 17
    m4i_norte = 3
    m4j_norte = 21
    
    
    catana = 10
    soco_ingles = 2.5
    
    monstro_hall = Monstro(mj_hall,mi_hall,VERMELHO,TILESIZE,tela,tab,10)
    monstro2_hall = Monstro(m2j_hall,m2i_hall,VERMELHO,TILESIZE,tela,tab,10)
    monstro3_hall = Monstro(m3j_hall,m3i_hall,VERMELHO,TILESIZE,tela,tab,10)
    monstro_norte = Monstro(mj_norte,mi_norte,VERMELHO,TILESIZE,tela,ala_norte.TAB_2,15)
    monstro2_norte = Monstro(m2j_norte,m2i_norte,VERMELHO,TILESIZE,tela,ala_norte.TAB_2,15)
    monstro3_norte = Monstro(m3j_norte,m3i_norte,VERMELHO,TILESIZE,tela,ala_norte.TAB_2,15)
    monstro4_norte = Monstro(m4j_norte,m4i_norte,VERMELHO,TILESIZE,tela,ala_norte.TAB_2,15)


    arma_hall_pos = pygame.Rect(11*TILESIZE,11*TILESIZE,TILESIZE,TILESIZE)
    arma1_norte_pos = pygame.Rect(2*TILESIZE,2*TILESIZE,TILESIZE,TILESIZE)
    arma2_norte_pos = pygame.Rect(2*TILESIZE,27*TILESIZE,TILESIZE,TILESIZE)
    arma3_norte_pos = pygame.Rect(37*TILESIZE,24*TILESIZE,TILESIZE,TILESIZE)
    arma1_sul_pos = pygame.Rect(2*TILESIZE,19*TILESIZE,TILESIZE,TILESIZE)
    arma2_sul_pos = pygame.Rect(33*TILESIZE,4*TILESIZE,TILESIZE,TILESIZE)
    arma3_sul_pos = pygame.Rect(30*TILESIZE,27*TILESIZE,TILESIZE,TILESIZE)
    arma1_leste1_pos = pygame.Rect(6*TILESIZE,27*TILESIZE,TILESIZE,TILESIZE)
    arma2_leste1_pos = pygame.Rect(25*TILESIZE,6*TILESIZE,TILESIZE,TILESIZE)
    arma1_leste2_pos = pygame.Rect(12*TILESIZE,23*TILESIZE,TILESIZE,TILESIZE)
    arma2_leste2_pos = pygame.Rect(32*TILESIZE,6*TILESIZE,TILESIZE,TILESIZE)
    arma3_leste2_pos = pygame.Rect(32*TILESIZE,7*TILESIZE,TILESIZE,TILESIZE)
    
    
    #definindo lanterna
    lanterna_pos = pygame.Rect(6*TILESIZE,2*TILESIZE,TILESIZE,TILESIZE)
    A_LUZ1 = pygame.Rect((pj-1)*TILESIZE,(pi-3)*TILESIZE,TILESIZE*3,TILESIZE*7)
    A_LUZ2 = pygame.Rect((pj-3)*TILESIZE,(pi-1)*TILESIZE,TILESIZE*7,TILESIZE*3)
    A_LUZ3 = pygame.Rect((pj-2)*TILESIZE,(pi-2)*TILESIZE,TILESIZE*5,TILESIZE*5)

    
    Fullscreen = False
    sair = False
    lanterna = False
    arma_soco_hall = False
    arma_soco_norte = False
    arma1_catana_norte = False
    arma2_catana_norte = False
    
    
    
    arma_catana = False
    key_pressed = pygame.key.get_pressed()
    luz = True
    QUIT = False
    MONSTRO1_HALL = True
    MONSTRO2_HALL = True
    MONSTRO3_HALL = True
    MONSTRO1_NORTE = True
    MONSTRO2_NORTE = True
    MONSTRO3_NORTE = True
    MONSTRO4_NORTE = True
    vida_a = 5
    
    count = 0  
    count_m = 0  
    nome_tela = 'jogo'
    background_hall= pygame.image.load("entrada.png")
    background_alanorte = pygame.image.load("ala-norte.png")
    background_alasul = pygame.image.load("ala sul.png")
    background_alaleste1 = pygame.image.load("ala-leste-1.png")
    background_alaleste2 = pygame.image.load("ala-leste-final.png")
   

# definindo loop

    while sair != True:
        
        if nome_tela == 'jogo':
          
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        Fullscreen = not Fullscreen
                        if Fullscreen:
                            tela = pygame.display.set_mode([MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE], pygame.FULLSCREEN, 32)
                        else:
                            screen = pygame.display.set_mode([MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE])
                        
                        
                          
            #movimento jogador
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_RIGHT]:
                if pj < (MAPWIDTH - 1) and (tab[pi][pj+1] != 1):
                    jogador.move_ip(TILESIZE,0)
                    pj += 1
            if key_pressed[pygame.K_UP]:
                if pi > 0 and (tab[pi-1][pj] != 1):
                    jogador.move_ip(0,-TILESIZE)
                    pi -= 1
            if key_pressed[pygame.K_LEFT]:
                if pj > 0 and (tab[pi][pj-1] != 1):
                    jogador.move_ip(-TILESIZE,0)
                    pj -= 1
            if key_pressed[pygame.K_DOWN]:
                if (pi < (MAPHEIGHT - 1)) and (tab[pi+1][pj] != 1):
                    jogador.move_ip(0,TILESIZE)
                    pi += 1

            
    # se tocar no monstro: 
            
            if tab == tabuleiro.TAB:
                
                if pi == monstro_hall.y and pj == monstro_hall.x: 
                    
                    monstro_hall.vida(arma,MONSTRO1_HALL,arma_soco,QUIT)
                    QUIT = monstro_hall.QUIT
                    MONSTRO1_HALL= monstro_hall.MONSTRO
                        
                if pi == monstro2_hall.y and pj ==monstro2_hall.x: 
                    
                    monstro2_hall.vida(vida_a,MONSTRO2_HALL,arma,QUIT)
                    QUIT = monstro2_hall.QUIT
                    MONSTRO2_HALL= monstro2_hall.MONSTRO
                
                if pi == monstro3_hall.y and pj == monstro3_hall.x:
                    
                    monstro3_hall.vida(vida_a,MONSTRO3_HALL,arma,QUIT)
                    QUIT = monstro3_hall.QUIT
                    MONSTRO3_HALL= monstro3_hall.MONSTRO
                        
            if tab == ala_norte.TAB_2: 
               
                if pi == monstro_norte.y and pj == monstro_norte.x: 
                    monstro_norte.vida(vida_a,MONSTRO1_NORTE,arma,QUIT)
                    QUIT = monstro_norte.QUIT
                    MONSTRO1_NORTE= monstro_norte.MONSTRO
                        
                if pi == monstro2_norte.y and pj == monstro2_norte.x: 
                    monstro2_norte.vida(vida_a,MONSTRO2_NORTE,arma,QUIT)
                    QUIT = monstro2_norte.QUIT
                    MONSTRO2_NORTE= monstro2_norte.MONSTRO
                        
                if pi == monstro3_norte.y and pj == monstro3_norte.x: 
                    
                    monstro3_norte.vida(vida_a,MONSTRO3_NORTE,arma,QUIT)
                    QUIT = monstro3_norte.QUIT
                    MONSTRO3_NORTE= monstro3_norte.MONSTRO
                    
                if pi == monstro4_norte.y and pj == monstro4_norte.x: 
                    monstro4_norte.vida(vida_a,MONSTRO4_NORTE,arma,QUIT)
                    QUIT = monstro4_norte.QUIT
                    MONSTRO4_NORTE= monstro4_norte.MONSTRO
               
            
               
            
            
        
        
            relogio.tick(12)

            
            
            
            
            #tela.fill(PRETO)
            
            if tab == ala_norte.TAB_2:
                tela.blit(background_alanorte, [0,0])

            if tab == tabuleiro.TAB: 
                tela.blit(background_hall,[0,0])
            
        
                tela2.fill(PRETO)
                telag_2.fill(PRETO)
                telag_3.fill(PRETO)
                telag_4.fill(PRETO)
                telag_5.fill(PRETO)
                telag_6.fill(PRETO)
                telag_7.fill(PRETO)
                telag_8.fill(PRETO)
                telag_9.fill(PRETO)
                telag_10.fill(PRETO)
                telag_11.fill(PRETO)
                telag_12.fill(PRETO)
                telag_13.fill(PRETO)
                telag_13.fill(PRETO)
                telag_14.fill(PRETO)
                telag_15.fill(PRETO)
                telag_16.fill(PRETO)
            
            count += 1

            if tab == tabuleiro.TAB:
                
                if count == 5:
                    count = 0
                    luz = not luz
        
                if luz == True:     
                    
                    tela.blit(telag_2,[5*TILESIZE,10*TILESIZE])
                    tela.blit(telag_3,[5*TILESIZE,8*TILESIZE])
                    tela.blit(telag_4,[5*TILESIZE,5*TILESIZE])
                    tela.blit(telag_5,[8*TILESIZE,5*TILESIZE])
                    tela.blit(telag_6,[9*TILESIZE,5*TILESIZE])
                    tela.blit(telag_7,[12*TILESIZE,5*TILESIZE])
                    tela.blit(telag_8,[10*TILESIZE,0*TILESIZE])
                    tela.blit(telag_9,[8*TILESIZE,0*TILESIZE])
                    tela.blit(telag_10,[5*TILESIZE,0*TILESIZE])
                    tela.blit(telag_11,[5*TILESIZE,19*TILESIZE])
                    tela.blit(telag_12,[5*TILESIZE,22*TILESIZE])
                    tela.blit(telag_13,[8*TILESIZE,22*TILESIZE])
                    tela.blit(telag_14,[9*TILESIZE,21*TILESIZE])
                    tela.blit(telag_15,[11*TILESIZE,21*TILESIZE])
                    tela.blit(telag_16,[13*TILESIZE,21*TILESIZE])
        
            if pi == 2 and pj == 6:
                
                lanterna = True
                
            if lanterna == True: 
                A_LUZ1 = pygame.Rect((pj-1)*TILESIZE,(pi-3)*TILESIZE,TILESIZE*3,TILESIZE*7)
                A_LUZ2 = pygame.Rect((pj-3)*TILESIZE,(pi-1)*TILESIZE,TILESIZE*7,TILESIZE*3)
                A_LUZ3 = pygame.Rect((pj-2)*TILESIZE,(pi-2)*TILESIZE,TILESIZE*5,TILESIZE*5)
                #pygame.draw.rect(tela,BRANCO,A_LUZ1)
                #pygame.draw.rect(tela,BRANCO,A_LUZ2)
                #pygame.draw.rect(tela,BRANCO,A_LUZ3)
                s2 = pygame.Surface((TILESIZE*7,TILESIZE*3))  
                s2.set_alpha(50)                
                s2.fill((255,255,255))           
                tela.blit(s2, ((pj-3)*TILESIZE,(pi-1)*TILESIZE))
                s3 = pygame.Surface((TILESIZE*5,TILESIZE*5))  
                s3.set_alpha(50)                
                s3.fill((255,255,255))           
                tela.blit(s3, ((pj-2)*TILESIZE,(pi-2)*TILESIZE))
                s1 = pygame.Surface((TILESIZE*3,TILESIZE*7))  
                s1.set_alpha(50)                
                s1.fill((255,255,255))           
                tela.blit(s1, ((pj-1)*TILESIZE,(pi-3)*TILESIZE))
                
            
            if lanterna == False: 
                
                pygame.draw.rect(tela,AZUL,lanterna_pos)
                
            pygame.draw.rect(tela,ROSA,jogador)
            
            
            
            # monstro: 
            
            if tab == tabuleiro.TAB: 
                
                if MONSTRO1_HALL == True: 
                    monstro_hall.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m)
                    
                if MONSTRO2_HALL == True: 
                    monstro2_hall.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m)
                    
                if MONSTRO3_HALL== True: 
                    monstro3_hall.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m)
                
                if pi == 11 and pj == 11: 
                    
                    arma_soco_hall = True
                    
            if arma_soco-hall == False:
                if arma_hall_pos.colliderect(A_LUZ1) == True or arma_hall_pos.colliderect(A_LUZ2) == True or arma_hall_pos.colliderect(A_LUZ3) == True:
                    pygame.draw.rect(tela,VERDE,arma_hall_pos)
                    
            
            if tab == ala_norte.TAB_2: 
                
                if MONSTRO1_NORTE == True: 
                    monstro_norte.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m)
                    
                if MONSTRO2_NORTE == True: 
                    monstro2_norte.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m)
                    
                if MONSTRO3_NORTE == True: 
                    monstro3_norte.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m)
            
                if MONSTRO4_NORTE == True:
                    monstro4_norte.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m)
                    
                if pi == 2 and pj == 2: 
                    
                   arma1_catana_norte = True
                    
                if arma1_catana_norte == False:
               
                    if arma1_norte_pos.colliderect(A_LUZ1) == True or arma1_norte_pos.colliderect(A_LUZ2) == True or arma1_norte_pos.colliderect(A_LUZ3) == True:
                        pygame.draw.rect(tela,VERDE,arma1_norte_pos)
                  
                if pi == 27 and pj == 2: 
                    
                   arma_soco_norte = True
                    
                if arma_soco_norte == False:
                    if arma2_norte_pos.colliderect(A_LUZ1) == True or arma2_norte_pos.colliderect(A_LUZ2) == True or arma2_norte_pos.colliderect(A_LUZ3) == True:
                     pygame.draw.rect(tela,VERDE,arma2_norte_pos)
                  
                if pi == 24 and pj == 37: 
                    
                   arma2_catana_norte = True
                    
                if arma2_catana_norte == False:
                    if arma3_norte_pos.colliderect(A_LUZ1) == True or arma3_norte_pos.colliderect(A_LUZ2) == True or arma3_norte_pos.colliderect(A_LUZ3) == True:
                        pygame.draw.rect(tela,VERDE,arma3_norte_pos)
        
            
            count_m += 1
            if count_m == 2:
                count_m = 0

                
                
     # ir para a ala norte: 
        
           
            if tab[pi][pj] == 11: 
                
                tab = ala_norte.TAB_2
                pj = 20
                pi = 28 
                jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)
            
            if tab == ala_norte.TAB_2 and pj == 20 and pi == 28: 
                
                label2 = fonte_2.render("Ala norte", True, VERMELHO)
                tela.blit(label2, (19*TILESIZE, 26*TILESIZE))
                
            
    # ir para o hall: 
        
            if tab[pi][pj] == 2:
                
                
                
                tab = tabuleiro.TAB
                pj = 20
                pi = 1
                jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)
            
            if tab == tabuleiro.TAB and pj == 20 and pi == 1: 
                
                label3 = fonte_2.render("Hall", True, VERMELHO)
                tela.blit(label3, (19*TILESIZE, 2*TILESIZE))
                
            if tab == tabuleiro.TAB and pj == 20 and pi == 28: 
                
                label5 = fonte_2.render("Hall", True, VERMELHO)
                tela.blit(label5, (19*TILESIZE, 27*TILESIZE))
            
            
    # ala sul:
        
            if tab == ala_norte.TAB_2: 
                
                if pi == 3 and pj == 37: 
                    
                    chave1 = True
                
                
            if tab[pi][pj] == 6 and chave1 == True: 
                
                tab = ala_sul.TAB_3
                pj = 20
                pi = 1
                jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)
                
            if tab[pi][pj] == 6 and chave1 == False: 
                
                label1 = fonte_2.render("A porta esta trancada, vá para a ala norte", True, VERMELHO)
                tela.blit(label1, (19*TILESIZE, 27*TILESIZE))
            
            if tab[pi][pj] == 4:
                
                tab = tabuleiro.TAB
                pj = 20
                pi = 29
                jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)
            
            if tab == ala_sul.TAB_3 and pj == 20 and pi == 1: 
                
                label4 = fonte_2.render("Ala Sul", True, VERMELHO)
                tela.blit(label4, (19*TILESIZE, 2*TILESIZE))
                
            
            
        if QUIT == True: 
                
            nome_tela = 'quit'
            

            if nome_tela == 'quit':
        
                tela.fill(PRETO)
                        
                label2 = fonte.render("VOCÊ PERDEU...", True, VERMELHO)
                
                tela.blit(label2, (5*TILESIZE, 3*TILESIZE))
            
                b1 = botao("play again",7,22,5,3,VERMELHO,tela,fonte_2,'play')
                        
                if b1 == 1:
                    nome_tela = 'jogo'
                    #pygame.init()
                else: 
                    pass
                        
                b2 = botao("sair",25,22,5,3,VERMELHO,tela,fonte_2,'quit')
                        
                if b2 == 2:
                    pygame.quit()
                else:
                    pass

        pygame.display.update()
    pygame.quit()
main()

