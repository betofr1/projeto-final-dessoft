import pygame
import tabuleiro
import random 
import ala_norte
import ala_sul
import tab_tutorial
import ala_leste_1
import ala_leste_final

# definindo parametros usados nas classes e funcoes: 
#pygame.init()    
#fonte = pygame.font.SysFont("Arial", 100)
#fonte_2 = pygame.font.SysFont('Arial', 25)
#VERMELHO = (255,0,0)
#tab = tab_tutorial.TAB_6
#TILESIZE = 20
#MAPWIDTH = len(tab[0])
#MAPHEIGHT = len(tab)
#tela = pygame.display.set_mode([MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE])


#funcao botao

def botao(texto,x,y,l,a,cor1,tela,font,action):
    mouse = pygame.mouse.get_pos()
    TILESIZE = 20
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(tela, cor1, (x*TILESIZE,y*TILESIZE, l*TILESIZE, a*TILESIZE))
    tela.blit(font.render(texto, True, (0,0,0)), (x*TILESIZE, y*TILESIZE))
    if (x*TILESIZE+l*TILESIZE) > mouse[0] > (x*TILESIZE) and (y*TILESIZE+a*TILESIZE) > mouse[1] > (y*TILESIZE):
        if click[0] == 1:
            if action == 1:
                return 3
            if action == 0:
                return 2
            
#classe monstro

class Monstro:
    def __init__(self,x,y,cor,tamanho,tela,tab,vida_m):
        self.tab = tab
        self.tela = tela
        self.tamanho = tamanho
        self.x = x
        self.y = y
        self.cor = cor
        self.ret = pygame.Rect(self.x*self.tamanho,self.y*self.tamanho,self.tamanho,self.tamanho)
        self.MAPWIDTH = len(tab[0])
        self.MAPHEIGHT = len(tab)
        self.vida_m = vida_m
       
    def anda(self,l1,l2,l3,count,lanterna):
        self.count = count
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        if lanterna == True:
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
                    
    def vida(self,arma_dic,MONSTRO,arma,QUIT,nome_arma):
        self.arma_dic = arma_dic
        self.MONSTRO = MONSTRO
        self.arma = arma
        self.QUIT = QUIT
        self.nome_arma = nome_arma
        
        if self.arma == True: 
            if self.vida_m > 0 and self.arma_dic[self.nome_arma] > 0:
                self.vida_m = self.vida_m - self.arma_dic[self.nome_arma]
                

            if self.vida_m <= 0: 
                self.MONSTRO = False
            
            if self.arma_dic[self.nome_arma] <= 0 and self.vida_m > 0:
                self.MONSTRO = True 
                self.QUIT = True
            
            if self.arma_dic[self.nome_arma] <= 0: 
                self.arma = False
                
            if self.arma_dic[self.nome_arma] > 0: 
                self.arma_dic[self.nome_arma] -= 1 
                
            if self.arma_dic[self.nome_arma] <= 0:
                self.arma_dic = {}
                self.arma = False
                #label6 = fonte_2.render("Sua arma quebrou...fuja", True, VERMELHO)
                #tela.blit(label6, (19*TILESIZE, 27*TILESIZE))
            
                
                
        if self.arma == False: 
            self.QUIT = True
            
def main():
    #definindo dimensoes
    pygame.init()
    tab = tab_tutorial.TAB_6
    TILESIZE = 20
    MAPWIDTH = len(tab[0])
    MAPHEIGHT = len(tab)
    
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

    # definindo telas: 
    tela = pygame.display.set_mode([MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE])
    tela2 = pygame.Surface((TILESIZE*5,TILESIZE*30))
    telag_2= pygame.Surface((TILESIZE*14,TILESIZE*9))
    telag_3 = pygame.Surface((TILESIZE*9,TILESIZE*12))
    telag_4 = pygame.Surface((TILESIZE*14,TILESIZE*5))
    telag_5 = pygame.Surface((TILESIZE*26,TILESIZE*30))
    telag_6 = pygame.Surface((TILESIZE*5,TILESIZE*12))
    telag_7 = pygame.Surface((TILESIZE*11,TILESIZE*4))
    telag_8 = pygame.Surface((TILESIZE*40,TILESIZE*30))
    #telag_9 = pygame.Surface((TILESIZE*2,TILESIZE*5))
    #telag_10= pygame.Surface((TILESIZE*3,TILESIZE*5))
    #telag_11 = pygame.Surface((TILESIZE*4,TILESIZE*3))
    #telag_12 = pygame.Surface((TILESIZE*3,TILESIZE*4))
    #telag_13 = pygame.Surface((TILESIZE*3,TILESIZE*4))
    #telag_14 = pygame.Surface((TILESIZE*2,TILESIZE*1))
    #telag_15 = pygame.Surface((TILESIZE*2,TILESIZE*5))
    #telag_16 = pygame.Surface((TILESIZE*2,TILESIZE*5))
    tela2.fill(PRETO)
    telag_2.set_alpha(250)
    telag_2.fill(PRETO)
    telag_3.set_alpha(200)
    telag_3.fill(PRETO)
    telag_4.set_alpha(200)
    telag_4.fill(PRETO)
    telag_5.set_alpha(200)
    telag_5.fill(PRETO)
    telag_6.set_alpha(200)
    telag_6.fill(PRETO)
    telag_7.set_alpha(200)
    telag_7.fill(PRETO)
    telag_8.set_alpha(200)
    telag_8.fill(PRETO)
    #telag_9.fill(PRETO)
    #telag_10.fill(PRETO)
    #telag_11.fill(PRETO)
    #telag_12.fill(PRETO)
    #telag_13.fill(PRETO)
    #telag_13.fill(PRETO)
    #telag_14.fill(PRETO)
    #telag_15.fill(PRETO)
    #telag_16.fill(PRETO)

    # texto 
    fonte = pygame.font.SysFont("Arial", 100)
    fonte_2 = pygame.font.SysFont('Arial', 25)

    #pygame functions
    key_pressed = pygame.key.get_pressed()
    pygame.display.set_caption("LABIRINTO DOS INFERNO")
    relogio = pygame.time.Clock()
    nome_tela = 'jogo'
    

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
    

    mi_sul = 2
    mj_sul = 2
    m2i_sul = 27
    m2j_sul = 13
    m3i_sul = 27
    m3j_sul = 24
    m4i_sul = 8
    m4j_sul = 23
    
    mi_leste1 = 27
    mj_leste1 = 2
    m2i_leste1 = 2
    m2j_leste1 = 14
    m3i_leste1 = 21
    m3j_leste1 = 23
    m4i_leste1 = 10
    m4j_leste1 = 25
    
    mi_leste2 = 27
    mj_leste2 = 2
    m2i_leste2 = 27
    m2j_leste2 = 29
    m3i_leste2 = 23
    m3j_leste2 = 33
    m4i_leste2 = 22
    m4j_leste2 = 16
    m5i_leste2 = 15
    m5j_leste2 = 37
    m6i_leste2 = 15
    m6j_leste2 = 33
    
    vida_monstro_hall = 10
    vida_monstro_norte = 15
    vida_monstro_sul = 20
    vida_monstro_leste1 = 25
    vida_monstro_leste2 = 30
    
    armas = {"catana": 10, "soco_ingles": 5}         # dicionario 
    
    
    monstro_hall = Monstro(mj_hall,mi_hall,VERMELHO,TILESIZE,tela,tabuleiro.TAB,vida_monstro_hall)
    monstro2_hall = Monstro(m2j_hall,m2i_hall,VERMELHO,TILESIZE,tela,tabuleiro.TAB,vida_monstro_hall)
    monstro3_hall = Monstro(m3j_hall,m3i_hall,VERMELHO,TILESIZE,tela,tabuleiro.TAB,vida_monstro_hall)
    monstro_norte = Monstro(mj_norte,mi_norte,VERMELHO,TILESIZE,tela,ala_norte.TAB_2,vida_monstro_norte)
    monstro2_norte = Monstro(m2j_norte,m2i_norte,VERMELHO,TILESIZE,tela,ala_norte.TAB_2,vida_monstro_norte)
    monstro3_norte = Monstro(m3j_norte,m3i_norte,VERMELHO,TILESIZE,tela,ala_norte.TAB_2,vida_monstro_norte)
    monstro4_norte = Monstro(m4j_norte,m4i_norte,VERMELHO,TILESIZE,tela,ala_norte.TAB_2,vida_monstro_norte)
    monstro_sul = Monstro(mj_sul,mi_sul,VERMELHO,TILESIZE,tela,ala_sul.TAB_3,vida_monstro_sul)
    monstro2_sul = Monstro(m2j_sul,m2i_sul,VERMELHO,TILESIZE,tela,ala_sul.TAB_3,vida_monstro_sul)
    monstro3_sul= Monstro(m3j_sul,m3i_sul,VERMELHO,TILESIZE,tela,ala_sul.TAB_3,vida_monstro_sul)
    monstro4_sul = Monstro(m4j_sul,m4i_sul,VERMELHO,TILESIZE,tela,ala_sul.TAB_3,vida_monstro_sul)
    monstro_leste1 = Monstro(mj_leste1,mi_leste1,VERMELHO,TILESIZE,tela,ala_leste_1.TAB_5,vida_monstro_leste1)
    monstro2_leste1 = Monstro(m2j_leste1,m2i_leste1,VERMELHO,TILESIZE,tela,ala_leste_1.TAB_5,vida_monstro_leste1)
    monstro3_leste1 = Monstro(m3j_leste1,m3i_leste1,VERMELHO,TILESIZE,tela,ala_leste_1.TAB_5,vida_monstro_leste1)
    monstro4_leste1 = Monstro(m4j_leste1,m4i_leste1,VERMELHO,TILESIZE,tela,ala_leste_1.TAB_5,vida_monstro_leste1)
    monstro_leste2 = Monstro(mj_leste2,mi_leste2,VERMELHO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2)
    monstro2_leste2 = Monstro(m2j_leste2,m2i_leste2,VERMELHO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2)
    monstro3_leste2 = Monstro(m3j_leste2,m3i_leste2,VERMELHO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2)
    monstro4_leste2 = Monstro(m4j_leste2,m4i_leste2,VERMELHO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2)
    monstro5_leste2 = Monstro(m5j_leste2,m5i_leste2,VERMELHO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2)
    monstro6_leste2 = Monstro(m6j_leste2,m6i_leste2,VERMELHO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2)


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
    arma2_leste2_pos = pygame.Rect(24*TILESIZE,6*TILESIZE,TILESIZE,TILESIZE)
    arma3_leste2_pos = pygame.Rect(32*TILESIZE,7*TILESIZE,TILESIZE,TILESIZE)
    
    arma_soco_hall = False
    arma1_soco_norte = False
    arma2_catana_norte = False
    arma3_catana_norte = False
    arma1_soco_sul = False
    arma2_catana_sul = False
    arma3_soco_sul = False
    arma1_catana_leste1 = False
    arma2_soco_leste1 = False
    arma1_catana_leste2 = False
    arma2_soco_leste2 = False
    arma3_catana_leste2 = False
    
    arma_dic = {}
    
    #definindo lanterna
    lanterna_pos = pygame.Rect(6*TILESIZE,2*TILESIZE,TILESIZE,TILESIZE)
    A_LUZ1 = pygame.Rect((pj-1)*TILESIZE,(pi-3)*TILESIZE,TILESIZE*3,TILESIZE*7)
    A_LUZ2 = pygame.Rect((pj-3)*TILESIZE,(pi-1)*TILESIZE,TILESIZE*7,TILESIZE*3)
    A_LUZ3 = pygame.Rect((pj-2)*TILESIZE,(pi-2)*TILESIZE,TILESIZE*5,TILESIZE*5)

    #BOOL
    chave1 = False
    Fullscreen = False
    sair = False
    lanterna = False

    
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
    
    MONSTRO1_SUL = True
    MONSTRO2_SUL = True
    MONSTRO3_SUL = True
    MONSTRO4_SUL = True
    
    MONSTRO1_LESTE1 = True
    MONSTRO2_LESTE1 = True
    MONSTRO3_LESTE1 = True
    MONSTRO4_LESTE1 = True
    
    MONSTRO1_LESTE2 = True
    MONSTRO2_LESTE2 = True
    MONSTRO3_LESTE2 = True
    MONSTRO4_LESTE2 = True
    MONSTRO5_LESTE2 = True
    MONSTRO6_LESTE2 = True
    
    count = 0  
    count_m = 0  
    #imagens
    background_hall= pygame.image.load("entrada.png")
    background_alanorte = pygame.image.load("ala-norte.png")
    background_alasul = pygame.image.load("ala-sul.png")
    background_alaleste1 = pygame.image.load("ala-leste-1.png")
    background_alaleste2 = pygame.image.load("ala-leste-final.png")
    background_tutorial = pygame.image.load("tutorial.png")
    katana = pygame.image.load("katana.png")
    martelo = pygame.image.load("smallhammer.png")
    adaga = pygame.image.load("adaga.png")


   

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
#========================================================================================
             # CENARIOS:

            if tab == tab_tutorial.TAB_6:
                tela.blit(background_tutorial, [0,0])

            if tab == tabuleiro.TAB:
                tela.blit(background_hall,[0,0])
                tela.blit(telag_5,[14*TILESIZE,0*TILESIZE])
                tela.blit(telag_6,[9*TILESIZE,9*TILESIZE])
                tela.blit(telag_7,[3*TILESIZE,26*TILESIZE])
   
                if lanterna == False:  
                    pygame.draw.rect(tela,AZUL,lanterna_pos)

                count += 1
                if count == 5:
                    count = 0
                    luz = not luz
        
                if luz == True:

                    tela.blit(telag_2,[0*TILESIZE,0*TILESIZE])
                    tela.blit(telag_3,[0*TILESIZE,9*TILESIZE])
                    tela.blit(telag_4,[0*TILESIZE,21*TILESIZE])
                    
                if pi == 2 and pj == 6:

                    lanterna = True

                if pi == 11 and pj == 11:
                    
                    if len(arma_dic) == 0:

                        arma_dic = {'soco_ingles':armas['soco_ingles']}
                        arma_soco_hall = True
                        arma_atual = arma_soco_hall
                        nome_arma = "soco_ingles"
                        
                
                if pi == monstro_hall.y and pj == monstro_hall.x:

                    monstro_hall.vida(arma_dic,MONSTRO1_HALL,arma_atual,QUIT,nome_arma)
                    QUIT = monstro_hall.QUIT
                    MONSTRO1_HALL= monstro_hall.MONSTRO
                    arma_dic = monstro_hall.arma_dic
                        
                if pi == monstro2_hall.y and pj ==monstro2_hall.x: 
                    
                    monstro2_hall.vida(arma_dic,MONSTRO2_HALL,arma_atual,QUIT,nome_arma)
                    QUIT = monstro2_hall.QUIT
                    MONSTRO2_HALL= monstro2_hall.MONSTRO
                    arma_dic = monstro2_hall.arma_dic
                
                if pi == monstro3_hall.y and pj == monstro3_hall.x:
                    
                    monstro3_hall.vida(arma_dic,MONSTRO3_HALL,arma_atual,QUIT,nome_arma)
                    QUIT = monstro3_hall.QUIT
                    MONSTRO3_HALL= monstro3_hall.MONSTRO
                    arma_dic = monstro3_hall.arma_dic
                    
                if MONSTRO1_HALL == True: 
                    monstro_hall.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m,lanterna)
                    
                if MONSTRO2_HALL == True: 
                    monstro2_hall.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m,lanterna)
                    
                if MONSTRO3_HALL== True: 
                    monstro3_hall.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m,lanterna)
                
                    
                if arma_soco_hall == False:
                    if arma_hall_pos.colliderect(A_LUZ1) == True or arma_hall_pos.colliderect(A_LUZ2) == True or arma_hall_pos.colliderect(A_LUZ3) == True:
                        pygame.draw.rect(tela,VERDE,arma_hall_pos)       
  #---------------------------------------------------------------------------      
            if tab == ala_norte.TAB_2: 
                tela.blit(background_alanorte, [0,0])
                tela.blit(telag_8,[0*TILESIZE,0*TILESIZE])
               
                if MONSTRO1_NORTE == True: 
                    monstro_norte.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m,lanterna)
                    
                if MONSTRO2_NORTE == True: 
                    monstro2_norte.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m,lanterna)
                    
                if MONSTRO3_NORTE == True: 
                    monstro3_norte.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m,lanterna)
            
                if MONSTRO4_NORTE == True:
                    monstro4_norte.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m,lanterna)
                    


                if pi == monstro_norte.y and pj == monstro_norte.x: 
                    
                    monstro_norte.vida(arma_dic,MONSTRO1_NORTE,arma_atual,QUIT,nome_arma)
                    QUIT = monstro_norte.QUIT
                    MONSTRO1_NORTE= monstro_norte.MONSTRO
                    arma_dic = monstro_norte.arma_dic
                    
                if pi == monstro2_norte.y and pj == monstro2_norte.x: 
                    
                    monstro2_norte.vida(arma_dic,MONSTRO2_NORTE,arma_atual,QUIT,nome_arma)
                    QUIT = monstro2_norte.QUIT
                    MONSTRO2_NORTE= monstro2_norte.MONSTRO
                    arma_dic = monstro2_norte.arma_dic

                if pi == monstro3_norte.y and pj == monstro3_norte.x: 
                    
                    monstro3_norte.vida(arma_dic,MONSTRO3_NORTE,arma_atual,QUIT,nome_arma)
                    QUIT = monstro3_norte.QUIT
                    MONSTRO3_NORTE= monstro3_norte.MONSTRO
                    arma_dic = monstro3_norte.arma_dic
                    
                if pi == monstro4_norte.y and pj == monstro4_norte.x: 
                    
                    monstro4_norte.vida(arma_dic,MONSTRO4_NORTE,arma_atual,QUIT,nome_arma)
                    QUIT = monstro4_norte.QUIT
                    MONSTRO4_NORTE= monstro4_norte.MONSTRO
                    arma_dic = monstro4_norte.arma_dic

                if pi == 2 and pj == 2: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'catana':armas['catana']}
                        
                        arma2_catana_norte = True
                        arma_atual = arma2_catana_norte
                        nome_arma = "catana"
                    
                if arma2_catana_norte == False:
               
                    if arma1_norte_pos.colliderect(A_LUZ1) == True or arma1_norte_pos.colliderect(A_LUZ2) == True or arma1_norte_pos.colliderect(A_LUZ3) == True:
                        pygame.draw.rect(tela,VERDE,arma1_norte_pos)
                  
                if pi == 27 and pj == 2: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'soco_ingles':armas['soco_ingles']}
                        arma1_soco_norte = True
                        arma_atual = arma1_soco_norte
                        nome_arma = "soco_ingles"
                    
                    
                if arma1_soco_norte == False:
                    if arma2_norte_pos.colliderect(A_LUZ1) == True or arma2_norte_pos.colliderect(A_LUZ2) == True or arma2_norte_pos.colliderect(A_LUZ3) == True:
                     pygame.draw.rect(tela,VERDE,arma2_norte_pos)
                  
                if pi == 24 and pj == 37: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'catana':armas['catana']}
                        arma3_catana_norte = True
                        arma_atual = arma3_catana_norte
                        nome_arma = "catana"
                    
                if arma3_catana_norte == False:
                    if arma3_norte_pos.colliderect(A_LUZ1) == True or arma3_norte_pos.colliderect(A_LUZ2) == True or arma3_norte_pos.colliderect(A_LUZ3) == True:
                        pygame.draw.rect(tela,VERDE,arma3_norte_pos)
#----------------------------------------------------------------------------------------
            if tab == ala_sul.TAB_3: 
                tela.blit(background_alasul, [0,0])
                tela.blit(telag_8,[0*TILESIZE,0*TILESIZE])
                
                if pi == monstro_sul.y and pj == monstro_sul.x: 
                    
                    monstro_sul.vida(arma_dic,MONSTRO1_SUL,arma_atual,QUIT,nome_arma)
                    QUIT = monstro_sul.QUIT
                    MONSTRO1_SUL= monstro_sul.MONSTRO
                    arma_dic = monstro_sul.arma_dic
                    
                if pi == monstro2_sul.y and pj == monstro2_sul.x: 
                    
                    monstro2_sul.vida(arma_dic,MONSTRO2_SUL,arma_atual,QUIT,nome_arma)
                    QUIT = monstro2_sul.QUIT
                    MONSTRO2_SUL= monstro2_sul.MONSTRO
                    arma_dic = monstro2_sul.arma_dic
                    
                if pi == monstro3_sul.y and pj == monstro3_sul.x: 
                    
                    monstro3_sul.vida(arma_dic,MONSTRO3_SUL,arma_atual,QUIT,nome_arma)
                    QUIT = monstro3_sul.QUIT
                    MONSTRO3_SUL= monstro3_sul.MONSTRO
                    arma_dic = monstro3_sul.arma_dic
                    
                if pi == monstro4_sul.y and pj == monstro4_sul.x: 
                    
                    monstro4_sul.vida(arma_dic,MONSTRO4_SUL,arma_atual,QUIT,nome_arma)
                    QUIT = monstro4_sul.QUIT
                    MONSTRO4_SUL= monstro4_sul.MONSTRO
                    arma_dic = monstro4_sul.arma_dic
                    
                if MONSTRO1_SUL == True: 
                    monstro_sul.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m)
                    
                if MONSTRO2_SUL == True: 
                    monstro2_sul.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m)
                    
                if MONSTRO3_SUL == True: 
                    monstro3_sul.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m)
            
                if MONSTRO4_SUL == True:
                    monstro4_sul.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m)
                
                if pi == 19 and pj == 2: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'soco_ingles':armas['soco_ingles']}
                        arma1_soco_sul = True
                        arma_atual = arma1_soco_sul
                        nome_arma = "soco_ingles"
                    
                if arma1_soco_sul == False:
               
                    if arma1_sul_pos.colliderect(A_LUZ1) == True or arma1_sul_pos.colliderect(A_LUZ2) == True or arma1_sul_pos.colliderect(A_LUZ3) == True:
                        pygame.draw.rect(tela,VERDE,arma1_sul_pos)
                        
                if pi == 4 and pj == 33: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'catana':armas['catana']}
                        arma2_catana_sul = True
                        arma_atual = arma2_catana_sul
                        nome_arma = "catana"
                    
                if arma2_catana_sul == False:
               
                    if arma2_sul_pos.colliderect(A_LUZ1) == True or arma2_sul_pos.colliderect(A_LUZ2) == True or arma2_sul_pos.colliderect(A_LUZ3) == True:
                        pygame.draw.rect(tela,VERDE,arma1_sul_pos)
                
                if pi == 27 and pj == 30: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'soco_ingles':armas['soco_ingles']}
                        arma3_soco_sul = True
                        arma_atual = arma3_soco_sul
                        nome_arma = "soco_ingles"
                    
                if arma3_soco_sul == False:
               
                    if arma3_sul_pos.colliderect(A_LUZ1) == True or arma3_sul_pos.colliderect(A_LUZ2) == True or arma3_sul_pos.colliderect(A_LUZ3) == True:
                        pygame.draw.rect(tela,VERDE,arma3_norte_pos)
#---------------------------------------------------------------------------------------
            if tab == ala_leste_1.TAB_5:
                
                if pi == monstro_leste1.y and pj == monstro_leste1.x: 
                    
                    monstro_leste1.vida(arma_dic,MONSTRO1_LESTE1,arma_atual,QUIT,nome_arma)
                    QUIT = monstro_leste1.QUIT
                    MONSTRO1_LESTE1= monstro_leste1.MONSTRO
                    arma_dic = monstro_leste1.arma_dic
                    
                if pi == monstro2_leste1.y and pj == monstro2_leste1.x: 
                    
                    monstro2_leste1.vida(arma_dic,MONSTRO2_LESTE1,arma_atual,QUIT,nome_arma)
                    QUIT = monstro2_leste1.QUIT
                    MONSTRO2_LESTE1= monstro2_leste1.MONSTRO 
                    arma_dic = monstro2_leste1.arma_dic
                    
                if pi == monstro3_leste1.y and pj == monstro3_leste1.x: 
                    
                    monstro3_leste1.vida(arma_dic,MONSTRO3_LESTE1,arma_atual,QUIT,nome_arma)
                    QUIT = monstro3_leste1.QUIT
                    MONSTRO3_LESTE1= monstro3_leste1.MONSTRO
                    arma_dic = monstro3_leste1.arma_dic
                    
                if pi == monstro4_leste1.y and pj == monstro4_leste1.x: 
                    
                    monstro4_leste1.vida(arma_dic,MONSTRO4_LESTE1,arma_atual,QUIT,nome_arma)
                    QUIT = monstro4_leste1.QUIT
                    MONSTRO4_LESTE1= monstro4_leste1.MONSTRO
                    arma_dic = monstro4_leste1.arma_dic
                    
                if pi == 27 and pj == 6: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'catana':armas['catana']}
                        arma1_catana_leste1 = True
                        arma_atual = arma1_catana_leste1
                        nome_arma = "catana"
                    
                if arma1_catana_leste1 == False:
               
                    if arma1_leste1_pos.colliderect(A_LUZ1) == True or arma1_leste1_pos.colliderect(A_LUZ2) == True or arma1_leste1_pos.colliderect(A_LUZ3) == True:
                        pygame.draw.rect(tela,VERDE,arma1_leste1_pos)
                        
                if pi == 6 and pj == 25: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'soco_ingles':armas['soco_ingles']}
                        arma2_soco_leste1 = True
                        arma_atual = arma2_soco_leste1
                        nome_arma = "soco_ingles"
                    
                if arma2_soco_leste1 == False:
               
                    if arma2_leste1_pos.colliderect(A_LUZ1) == True or arma2_leste1_pos.colliderect(A_LUZ2) == True or arma2_leste1_pos.colliderect(A_LUZ3) == True:
                        pygame.draw.rect(tela,VERDE,arma2_leste1_pos)
#------------------------------------------------------------------------------------                        
            if tab == ala_leste_final.TAB_4:
                
                if pi == monstro_leste2.y and pj == monstro_leste2.x: 
                    
                    monstro_leste2.vida(arma_dic,MONSTRO1_LESTE2,arma_atual,QUIT,nome_arma)
                    QUIT = monstro_leste2.QUIT
                    MONSTRO1_LESTE2= monstro_leste2.MONSTRO
                    arma_dic = monstro_leste2.arma_dic
                    
                if pi == monstro2_leste2.y and pj == monstro2_leste2.x: 
                    
                    monstro2_leste2.vida(arma_dic,MONSTRO2_LESTE2,arma_atual,QUIT,nome_arma)
                    QUIT = monstro2_leste2.QUIT
                    MONSTRO2_LESTE2= monstro2_leste2.MONSTRO
                    arma_dic = monstro2_leste2.arma_dic
                    
                if pi == monstro3_leste2.y and pj == monstro3_leste2.x: 
                    
                    monstro3_leste2.vida(arma_dic,MONSTRO3_LESTE2,arma_atual,QUIT,nome_arma)
                    QUIT = monstro3_leste2.QUIT
                    MONSTRO3_LESTE2= monstro3_leste2.MONSTRO
                    arma_dic = monstro3_leste2.arma_dic
                    
                if pi == monstro4_leste2.y and pj == monstro4_leste2.x: 
                    
                    monstro4_leste2.vida(arma_dic,MONSTRO4_LESTE2,arma_atual,QUIT,nome_arma)
                    QUIT = monstro4_leste2.QUIT
                    MONSTRO4_LESTE2= monstro4_leste2.MONSTRO
                    arma_dic = monstro4_leste2.arma_dic
                    
                if pi == monstro5_leste2.y and pj == monstro5_leste2.x: 
                    
                    monstro5_leste2.vida(arma_dic,MONSTRO5_LESTE2,arma_atual,QUIT,nome_arma)
                    QUIT = monstro5_leste2.QUIT
                    MONSTRO5_LESTE2= monstro5_leste2.MONSTRO
                    arma_dic = monstro5_leste2.arma_dic
                    
                if pi == monstro6_leste2.y and pj == monstro6_leste2.x: 
                    
                    monstro6_leste2.vida(arma_dic,MONSTRO6_LESTE2,arma_atual,QUIT,nome_arma)
                    QUIT = monstro6_leste2.QUIT
                    MONSTRO6_LESTE2= monstro6_leste2.MONSTRO
                    arma_dic = monstro6_leste2.arma_dic
                    
                if pi == 23 and pj == 12: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'catana':armas['catana']}
                        arma1_catana_leste2 = True
                        arma_atual = arma1_catana_leste2
                        nome_arma = "catana"
                    
                if arma1_catana_leste2 == False:
               
                    if arma1_leste2_pos.colliderect(A_LUZ1) == True or arma1_leste2_pos.colliderect(A_LUZ2) == True or arma1_leste2_pos.colliderect(A_LUZ3) == True:
                        pygame.draw.rect(tela,VERDE,arma1_leste2_pos)
                        
                if pi == 6 and pj == 24: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'soco_ingles':armas['soco_ingles']}
                        arma2_soco_leste2 = True
                        arma_atual = arma2_soco_leste2
                        nome_arma = "soco_ingles"
                    
                if arma2_soco_leste2 == False:
               
                    if arma2_leste2_pos.colliderect(A_LUZ1) == True or arma2_leste2_pos.colliderect(A_LUZ2) == True or arma2_leste2_pos.colliderect(A_LUZ3) == True:
                        pygame.draw.rect(tela,VERDE,arma2_leste2_pos)
                    
                if pi == 7 and pj == 32: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'catana':armas['catana']}
                        arma3_catana_leste2 = True
                        arma_atual = arma3_catana_leste2
                        nome_arma = "catana"
                    
                if arma3_catana_leste2 == False:
               
                    if arma3_leste2_pos.colliderect(A_LUZ1) == True or arma3_leste2_pos.colliderect(A_LUZ2) == True or arma3_leste2_pos.colliderect(A_LUZ3) == True:
                        pygame.draw.rect(tela,VERDE,arma3_leste2_pos)  
#======================================================================================
            
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
                
            
                
            pygame.draw.rect(tela,ROSA,jogador)
            
            
            
            count_m += 1
            if count_m == 3:
                count_m = 0
            #ir pro hall
            if tab[pi][pj] == 14:
                tab = tabuleiro.TAB
                pi = 14
                pj = 0
                jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)
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
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
            
            tela.fill(PRETO)
            
            label2 = fonte.render("VOCÊ PERDEU...", True, VERMELHO)
            tela.blit(label2, (5*TILESIZE, 3*TILESIZE))
            
            play = 1
            exit = 0
            b1 = botao("play again",7,22,5,3,VERMELHO,tela,fonte_2,play)                        
            b2 = botao("sair",25,22,5,3,VERMELHO,tela,fonte_2,exit)
         
            if b1 == 3:
                nome_tela = 'jogo'

                tab = tab_tutorial.TAB_6
                chave1 = False
                #definindo jogador
                pi = 14
                pj = 0
                jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)

                #definindo monstros
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
                mi_sul = 2
                mj_sul = 2
                m2i_sul = 27
                m2j_sul = 13
                m3i_sul = 27
                m3j_sul = 24
                m4i_sul = 8
                m4j_sul = 23
                mi_leste1 = 27
                mj_leste1 = 2
                m2i_leste1 = 2
                m2j_leste1 = 14
                m3i_leste1 = 21
                m3j_leste1 = 23
                m4i_leste1 = 10
                m4j_leste1 = 25
                mi_leste2 = 27
                mj_leste2 = 2
                m2i_leste2 = 27
                m2j_leste2 = 29
                m3i_leste2 = 23
                m3j_leste2 = 33
                m4i_leste2 = 22
                m4j_leste2 = 16
                m5i_leste2 = 15
                m5j_leste2 = 37
                m6i_leste2 = 15
                m6j_leste2 = 33
                vida_monstro_hall = 10
                vida_monstro_norte = 15
                vida_monstro_sul = 20
                vida_monstro_leste1 = 25
                vida_monstro_leste2 = 30
                
                armas = {"catana": 10, "soco_ingles": 2.5}         # dicionario 
                
                monstro_hall = Monstro(mj_hall,mi_hall,VERMELHO,TILESIZE,tela,tabuleiro.TAB,vida_monstro_hall)
                monstro2_hall = Monstro(m2j_hall,m2i_hall,VERMELHO,TILESIZE,tela,tabuleiro.TAB,vida_monstro_hall)
                monstro3_hall = Monstro(m3j_hall,m3i_hall,VERMELHO,TILESIZE,tela,tabuleiro.TAB,vida_monstro_hall)
                monstro_norte = Monstro(mj_norte,mi_norte,VERMELHO,TILESIZE,tela,ala_norte.TAB_2,vida_monstro_norte)
                monstro2_norte = Monstro(m2j_norte,m2i_norte,VERMELHO,TILESIZE,tela,ala_norte.TAB_2,vida_monstro_norte)
                monstro3_norte = Monstro(m3j_norte,m3i_norte,VERMELHO,TILESIZE,tela,ala_norte.TAB_2,vida_monstro_norte)
                monstro4_norte = Monstro(m4j_norte,m4i_norte,VERMELHO,TILESIZE,tela,ala_norte.TAB_2,vida_monstro_norte)
                monstro_sul = Monstro(mj_sul,mi_sul,VERMELHO,TILESIZE,tela,ala_sul.TAB_3,vida_monstro_sul)
                monstro2_sul = Monstro(m2j_sul,m2i_sul,VERMELHO,TILESIZE,tela,ala_sul.TAB_3,vida_monstro_sul)
                monstro3_sul= Monstro(m3j_sul,m3i_sul,VERMELHO,TILESIZE,tela,ala_sul.TAB_3,vida_monstro_sul)
                monstro4_sul = Monstro(m4j_sul,m4i_sul,VERMELHO,TILESIZE,tela,ala_sul.TAB_3,vida_monstro_sul)
                monstro_leste1 = Monstro(mj_leste1,mi_leste1,VERMELHO,TILESIZE,tela,ala_leste_1.TAB_5,vida_monstro_leste1)
                monstro2_leste1 = Monstro(m2j_leste1,m2i_leste1,VERMELHO,TILESIZE,tela,ala_leste_1.TAB_5,vida_monstro_leste1)
                monstro3_leste1 = Monstro(m3j_leste1,m3i_leste1,VERMELHO,TILESIZE,tela,ala_leste_1.TAB_5,vida_monstro_leste1)
                monstro4_leste1 = Monstro(m4j_leste1,m4i_leste1,VERMELHO,TILESIZE,tela,ala_leste_1.TAB_5,vida_monstro_leste1)
                monstro_leste2 = Monstro(mj_leste2,mi_leste2,VERMELHO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2)
                monstro2_leste2 = Monstro(m2j_leste2,m2i_leste2,VERMELHO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2)
                monstro3_leste2 = Monstro(m3j_leste2,m3i_leste2,VERMELHO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2)
                monstro4_leste2 = Monstro(m4j_leste2,m4i_leste2,VERMELHO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2)
                monstro5_leste2 = Monstro(m5j_leste2,m5i_leste2,VERMELHO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2)
                monstro6_leste2 = Monstro(m6j_leste2,m6i_leste2,VERMELHO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2)

                sair = False
                lanterna = False
                arma = False
                luz = True
                QUIT = False
                MONSTRO1_HALL = True
                MONSTRO2_HALL = True
                MONSTRO3_HALL = True
                MONSTRO1_NORTE = True
                MONSTRO2_NORTE = True
                MONSTRO3_NORTE = True
                MONSTRO4_NORTE = True
                
                count = 0  
                count_m = 0  
      
            elif b2 == 2:
                sair = True

        relogio.tick(12)
        pygame.display.update()
    pygame.quit()
main()

