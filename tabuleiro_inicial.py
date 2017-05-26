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

def botao(texto,x,y,l,a,cor1,cor2,tela,font,action):
    mouse = pygame.mouse.get_pos()
    TILESIZE = 20
    click = pygame.mouse.get_pressed()
    tela.blit(font.render(texto, False, (cor1)), ((x+1)*TILESIZE, (y+1)*TILESIZE))
    if (x*TILESIZE+l*TILESIZE) > mouse[0] > (x*TILESIZE) and (y*TILESIZE+a*TILESIZE) > mouse[1] > (y*TILESIZE):
        tela.blit(font.render(texto, False, (cor2)), ((x+1)*TILESIZE, (y+1)*TILESIZE))
        if click[0] == 1:
            if action == 1:
                return 3
            if action == 0:
                return 2
            
#classe monstro
     
class Monstro:
    def __init__(self,x,y,cor,tamanho,tela,tab,vida_m,tela_monstro,fonte):
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
        self.tela_monstro = tela_monstro
        self.fonte = fonte
        self.a  = self.vida_m
       
    def anda(self,l,count,lanterna,zombie):
        self.count = count
        self.l = l
        self.lanterna = lanterna
        
        if self.lanterna == True:
            if self.ret.colliderect(self.l) == True:
                #pygame.draw.rect(self.tela, self.cor, self.ret)
                self.tela.blit(zombie,[self.x*self.tamanho,self.y*self.tamanho])
        
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

                    
    def vida(self,arma_dic,MONSTRO,arma,QUIT,nome_arma,quebrou):
        
        self.arma_dic = arma_dic
        self.MONSTRO = MONSTRO
        self.arma = arma
        self.QUIT = QUIT
        self.nome_arma = nome_arma
        self.quebrou = quebrou 
        #a  = self.vida_m
        
        #self.tela.blit(self.tela_monstro,[self.MAPWIDTH*self.tamanho,20*self.tamanho])
        
        #label_inventario8 = self.fonte.render("MONSTRO:", True, self.cor)
        #self.tela.blit(label_inventario8, ([self.MAPWIDTH*self.tamanho + 10 ,21*self.tamanho]))
        
        #label_inventario9 = self.fonte.render(("vida = {0}".format(str(self.vida_m))), True, self.cor)
        #self.tela.blit(label_inventario9, ([self.MAPWIDTH*self.tamanho + 10 ,25*self.tamanho]))
        
        #label_inventario10 = self.fonte.render(("vida máxima = {0}".format(str(self.a))), True, self.cor)
        #self.tela.blit(label_inventario10, ([self.MAPWIDTH*self.tamanho + 10 ,23*self.tamanho]))
        
        if self.arma == False and self.vida_m > 0: 
            self.QUIT = True
        #self.arma_dic[self.nome_arma][1] = int(self.arma_dic[self.nome_arma][1])
        if self.arma == True: 
            
            #print("vida arma",self.arma_dic[self.nome_arma][1])
            
            if self.vida_m > 0 and self.arma_dic[self.nome_arma][1] > 0:
                self.vida_m -= self.arma_dic[self.nome_arma][0]
                self.arma_dic[self.nome_arma][1] -= 1
                print(self.vida_m)
                

            if self.vida_m <= 0: 
                self.MONSTRO = False
            
            if self.arma_dic[self.nome_arma][1] <= 0 and self.vida_m > 0:
                self.MONSTRO = True 
                self.QUIT = True
                
            print("vida arma",self.arma_dic[self.nome_arma][1])
            
            if self.arma_dic[self.nome_arma][1] <= 0: 
                self.arma = False
                self.arma_dic = {}
                self.quebrou = 1
        
        if self.vida_m >= 0 : 
            
            self.tela.blit(self.tela_monstro,[self.MAPWIDTH*self.tamanho,20*self.tamanho])
            
            label_inventario8 = self.fonte.render("MONSTRO :", True, self.cor)
            self.tela.blit(label_inventario8, ([self.MAPWIDTH*self.tamanho + 10 ,23*self.tamanho]))
            
            label_inventario9 = self.fonte.render((" - vida atual = {0}".format(str(self.vida_m))), True, self.cor)
            self.tela.blit(label_inventario9, ([self.MAPWIDTH*self.tamanho + 10 ,27*self.tamanho]))
            
            label_inventario10 = self.fonte.render((" - vida máxima = {0}".format(str(self.a))), True, self.cor)
            self.tela.blit(label_inventario10, ([self.MAPWIDTH*self.tamanho + 10 ,25*self.tamanho]))
            
class music: 
    def __init__(self,musica,musica1,nome_tela):
        self.musica = musica
        self.musica_rodando = musica1
        self.nome_tela = nome_tela
        
    def toca_musica1(self):
        if not self.nome_tela == 'jogo':
        
            if self.musica == True: 
                if self.musica_rodando == False: 
                    musica_intro = pygame.mixer.music.load("Jesus Lastra - Abandoned - intro.mp3")
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(1.0)

    def toca_musica2(self):
        if self.nome_tela == 'jogo':
        
            if self.musica == True: 
                if self.musica_rodando == False: 
                    musica_tutorial = pygame.mixer.music.load("Abuse In The Orphanage - tutorial (online-audio-converter.com).mp3")
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.5)
                    
    def toca_musica3(self):
        if self.nome_tela == 'jogo':
        
            if self.musica == True: 
                if self.musica_rodando == False: 
                    musica_tabs = pygame.mixer.music.load("Desolate Part II.mp3")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.5)
                    
        
    
                
            
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
    VERMELHO_DARK = (150,0,0)
    VERDE = (0,255,0)
    ROSA = (214,34,191)
    white = (255,255,255,255)
    blue = (0,39,225,255)
    CINZA = (114,114,144)

    # definindo telas: 
    tela = pygame.display.set_mode([MAPWIDTH*TILESIZE + 200,MAPHEIGHT*TILESIZE])
    tela2 = pygame.Surface((TILESIZE*5,TILESIZE*30))
    telag_2= pygame.Surface((TILESIZE*14,TILESIZE*9))
    telag_3 = pygame.Surface((TILESIZE*9,TILESIZE*12))
    telag_4 = pygame.Surface((TILESIZE*14,TILESIZE*5))
    telag_5 = pygame.Surface((TILESIZE*26,TILESIZE*30))
    telag_6 = pygame.Surface((TILESIZE*5,TILESIZE*12))
    telag_7 = pygame.Surface((TILESIZE*11,TILESIZE*4))
    telag_8 = pygame.Surface((TILESIZE*40,TILESIZE*30))
    tela_inventario = pygame.Surface(([200,22*TILESIZE]))
    tela_monstro = pygame.Surface(([200,18*TILESIZE]))
    

    tela2.fill(PRETO)
    telag_2.set_alpha(200)
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
    #tela_inventario.set_alpha(200)
    tela_inventario.fill(PRETO)
    tela_monstro.fill(VERMELHO)

    # texto 
    #fonte = pygame.font.SysFont("Arial", 100)
    fonte_2 = pygame.font.Font('naughty_scratch_free.ttf', 25)
    fonte_botao = pygame.font.Font('naughty_scratch_free.ttf', 50)
    fonte_titulo = pygame.font.Font('True Lies.ttf', 120)
    label10 = fonte_2.render("A arma quebrou...corra", True, VERMELHO)
    fonte_inventario = pygame.font.Font('TravelingTypewriter.otf', 15)
    fonte_inventario1 = pygame.font.Font('TravelingTypewriter.otf', 20)

    #pygame functions
    key_pressed = pygame.key.get_pressed()
    pygame.display.set_caption("M4D BETO")
    relogio = pygame.time.Clock()
    nome_tela = ''
    tela_inicial = "inicio"
    

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
    

    armas = {'catana': [10,3], 'martelo': [5,4]}         # dicionario 
    
    
    monstro_hall = Monstro(mj_hall,mi_hall,BRANCO,TILESIZE,tela,tabuleiro.TAB,vida_monstro_hall,tela_monstro,fonte_inventario)
    monstro2_hall = Monstro(m2j_hall,m2i_hall,BRANCO,TILESIZE,tela,tabuleiro.TAB,vida_monstro_hall,tela_monstro,fonte_inventario)
    monstro3_hall = Monstro(m3j_hall,m3i_hall,BRANCO,TILESIZE,tela,tabuleiro.TAB,vida_monstro_hall,tela_monstro,fonte_inventario)
    monstro_norte = Monstro(mj_norte,mi_norte,BRANCO,TILESIZE,tela,ala_norte.TAB_2,vida_monstro_norte,tela_monstro,fonte_inventario)
    monstro2_norte = Monstro(m2j_norte,m2i_norte,BRANCO,TILESIZE,tela,ala_norte.TAB_2,vida_monstro_norte,tela_monstro,fonte_inventario)
    monstro3_norte = Monstro(m3j_norte,m3i_norte,BRANCO,TILESIZE,tela,ala_norte.TAB_2,vida_monstro_norte,tela_monstro,fonte_inventario)
    monstro4_norte = Monstro(m4j_norte,m4i_norte,BRANCO,TILESIZE,tela,ala_norte.TAB_2,vida_monstro_norte,tela_monstro,fonte_inventario)
    monstro_sul = Monstro(mj_sul,mi_sul,BRANCO,TILESIZE,tela,ala_sul.TAB_3,vida_monstro_sul,tela_monstro,fonte_inventario)
    monstro2_sul = Monstro(m2j_sul,m2i_sul,BRANCO,TILESIZE,tela,ala_sul.TAB_3,vida_monstro_sul,tela_monstro,fonte_inventario)
    monstro3_sul= Monstro(m3j_sul,m3i_sul,BRANCO,TILESIZE,tela,ala_sul.TAB_3,vida_monstro_sul,tela_monstro,fonte_inventario)
    monstro4_sul = Monstro(m4j_sul,m4i_sul,BRANCO,TILESIZE,tela,ala_sul.TAB_3,vida_monstro_sul,tela_monstro,fonte_inventario)
    monstro_leste1 = Monstro(mj_leste1,mi_leste1,BRANCO,TILESIZE,tela,ala_leste_1.TAB_5,vida_monstro_leste1,tela_monstro,fonte_inventario)
    monstro2_leste1 = Monstro(m2j_leste1,m2i_leste1,BRANCO,TILESIZE,tela,ala_leste_1.TAB_5,vida_monstro_leste1,tela_monstro,fonte_inventario)
    monstro3_leste1 = Monstro(m3j_leste1,m3i_leste1,BRANCO,TILESIZE,tela,ala_leste_1.TAB_5,vida_monstro_leste1,tela_monstro,fonte_inventario)
    monstro4_leste1 = Monstro(m4j_leste1,m4i_leste1,BRANCO,TILESIZE,tela,ala_leste_1.TAB_5,vida_monstro_leste1,tela_monstro,fonte_inventario)
    monstro_leste2 = Monstro(mj_leste2,mi_leste2,BRANCO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2,tela_monstro,fonte_inventario)
    monstro2_leste2 = Monstro(m2j_leste2,m2i_leste2,BRANCO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2,tela_monstro,fonte_inventario)
    monstro3_leste2 = Monstro(m3j_leste2,m3i_leste2,BRANCO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2,tela_monstro,fonte_inventario)
    monstro4_leste2 = Monstro(m4j_leste2,m4i_leste2,BRANCO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2,tela_monstro,fonte_inventario)
    monstro5_leste2 = Monstro(m5j_leste2,m5i_leste2,BRANCO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2,tela_monstro,fonte_inventario)
    monstro6_leste2 = Monstro(m6j_leste2,m6i_leste2,BRANCO,TILESIZE,tela,ala_leste_final.TAB_4,vida_monstro_leste2,tela_monstro,fonte_inventario)

    chave_norte_pos = pygame.Rect(37*TILESIZE,3*TILESIZE,TILESIZE,TILESIZE)
    chave_sul_pos = pygame.Rect(17*TILESIZE,15*TILESIZE,TILESIZE,TILESIZE)
    chave_final_pos = pygame.Rect(34*TILESIZE,22*TILESIZE,TILESIZE,TILESIZE)

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
    arma_atual = False
    nome_arma = ''
    quebrou = 0 
    
    #definindo lanterna
    A_LUZ =  pygame.Rect((pj-3)*TILESIZE,(pi-3)*TILESIZE,TILESIZE*7,TILESIZE*7)

    #BOOL
    chave_norte = False
    chave_sul = False
    chave_final = False
    Fullscreen = False
    sair = False
    lanterna = False
    musica1 = False # se a musica esta rodando
    musica = True
    musica2 = False # se a musica esta rodando
    musica3 = False
    
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
    count_a = 0 
    #backgorunds
    intro = pygame.image.load("intro.png").convert_alpha()
    background_hall= pygame.image.load("entrada.png").convert_alpha()
    background_alanorte = pygame.image.load("ala-norte.png").convert_alpha()
    background_alasul = pygame.image.load("ala-sul.png").convert_alpha()
    background_alaleste1 = pygame.image.load("ala-leste-1.png").convert_alpha()
    background_alaleste2 = pygame.image.load("ala-leste-final.png").convert_alpha()
    background_tutorial = pygame.image.load("tutorial.png").convert_alpha()
    
    #imagens personagens
    personagem_up = pygame.image.load("personagem_costas.png").convert_alpha()
    personagem_down = pygame.image.load("personagem_frente.png").convert_alpha()
    personagem_right = pygame.image.load("personagem_direita.png").convert_alpha()
    personagem_left = pygame.image.load("personagem_esquerda.png").convert_alpha()
    zombie = pygame.image.load("zombie_frente.png").convert_alpha()
    mask_BG = pygame.image.load("mask-BG.png").convert_alpha()
    aurea_objeto = pygame.image.load("aurea-objeto.png").convert_alpha()
    #imagens itens
    katana = pygame.image.load("Itens/katana.png").convert_alpha()
    martelo = pygame.image.load("Itens/smallhammer.png").convert_alpha()
    adaga = pygame.image.load("Itens/adaga.png").convert_alpha()
    img_lanterna = pygame.image.load("Itens/lanterna.png").convert_alpha()
    img_chave = pygame.image.load("Itens/chave.png").convert_alpha()
    img_inventario = pygame.image.load("inventario.png").convert_alpha()
    personagem = "right"
    
    #Definindo musicas
    
    
# para musica: 
    
        



# definindo loop

    while sair != True:
        
        
        
        if tela_inicial == "inicio": 
            
            musica_atual = music(musica,musica1,nome_tela)
            musica_atual.toca_musica1()
            musica1 = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
            
            tela.blit(intro, [0,0])
            #tela.blit(tela_inventario,[MAPWIDTH*TILESIZE,0])
            
            label2 = fonte_titulo.render("Lights Out", True, BRANCO)
            tela.blit(label2, (12*TILESIZE, 3*TILESIZE))
            
            play1 = 1
            exit1 = 0
            b3 = botao("Play ",10,22,8,5,VERMELHO,VERMELHO_DARK,tela,fonte_botao,play1)                        
            b4 = botao("Sair",35,22,8,5,VERMELHO,VERMELHO_DARK,tela,fonte_botao,exit1)
         
            if b3 == 3:
                nome_tela = 'jogo'
                
            elif b4 == 2:
                sair = True
            
        
        
        if nome_tela == 'jogo':
            
            #musica_atual.toca_musica1()
            

            #tela = pygame.display.set_mode([MAPWIDTH*TILESIZE + 200,MAPHEIGHT*TILESIZE])
            #tela.blit(tela_inventario,[MAPWIDTH*TILESIZE,0])
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        Fullscreen = not Fullscreen
                        if Fullscreen:
                            tela = pygame.display.set_mode([MAPWIDTH*TILESIZE + 200,MAPHEIGHT*TILESIZE], pygame.FULLSCREEN, 32)

                        else:
                            screen = pygame.display.set_mode([MAPWIDTH*TILESIZE + 200,MAPHEIGHT*TILESIZE])
                        
                        
            #print("mask",mask_BG.get_at((799,599)))
            #print("jogador",aurea_objeto.get_at(((pj+59),(pi + 59))))
            
            #if mask_BG.get_at((799,599)) == white:
                
#========================================================================================
             # CENARIOS:

            if tab == tab_tutorial.TAB_6:
                tela.blit(background_tutorial, [0,0])
                
                
                musica_atual = music(musica,musica2,nome_tela)
                musica_atual.toca_musica2()
                musica2 = True

#-------------------------------------------------------------------------------------
            if tab != tab_tutorial.TAB_6:
                
                musica_atual = music(musica,musica3,nome_tela)
                musica_atual.toca_musica3()
                musica3 = True
                
            if tab == tabuleiro.TAB:
                
            
                #print("mask",mask_BG.get_at((799,599)))
                #tela.blit(telag_8,[0*TILESIZE,0*TILESIZE])
                #print("jogador",aurea_objeto.get_at(((pj+59),(pi + 59))))
                tela.blit(background_hall,[0,0])
                tela.blit(telag_5,[14*TILESIZE,0*TILESIZE])
                tela.blit(telag_6,[9*TILESIZE,9*TILESIZE])
                tela.blit(telag_7,[3*TILESIZE,26*TILESIZE])
   
                if lanterna == False:  

                    tela.blit(img_lanterna, [6*TILESIZE,2*TILESIZE])


                count += 1
                
                if count == 5:
                    count = 0
                    luz = not luz
        
                if luz == True:

                    tela.blit(telag_2,[0*TILESIZE,0*TILESIZE])
                    tela.blit(telag_3,[0*TILESIZE,9*TILESIZE])
                    tela.blit(telag_4,[0*TILESIZE,21*TILESIZE])
                    
                if lanterna == True: 
                    tela.blit(aurea_objeto,[((pj*TILESIZE)-3*TILESIZE),((pi*TILESIZE)-3*TILESIZE)])
                
                    if aurea_objeto.get_at(((pj+59),(pi + 59))) == blue:
                        
                        background_hall_mask = background_hall.convert()
                        background_hall_mask.fill(PRETO)
                        
                    
                        background_hall_mask.blit(aurea_objeto,[((pj*TILESIZE)-3*TILESIZE),((pi*TILESIZE)-3*TILESIZE)])
                        background_hall_mask.set_colorkey(blue)
                        
                        tela.blit(background_hall,[0,0])
                        tela.blit(background_hall_mask,[0,0])
                        A_LUZ =  pygame.Rect((pj-3)*TILESIZE,(pi-3)*TILESIZE,TILESIZE*7,TILESIZE*7)
                    
                if pi == 2 and pj == 6:

                    lanterna = True

                if pi == 11 and pj == 11:
                    
                    if len(arma_dic) == 0:

                        arma_dic = {'martelo':armas['martelo']}
                        arma_soco_hall = True
                        arma_atual = arma_soco_hall
                        nome_arma = 'martelo'
                        
                
                if pi == monstro_hall.y and pj == monstro_hall.x and MONSTRO1_HALL == True:

                    monstro_hall.vida(arma_dic,MONSTRO1_HALL,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro_hall.QUIT
                    MONSTRO1_HALL= monstro_hall.MONSTRO
                    arma_dic = monstro_hall.arma_dic
                    arma_atual = monstro_hall.arma
                    quebrou = monstro_hall.quebrou
                    
                        
                if pi == monstro2_hall.y and pj ==monstro2_hall.x and MONSTRO2_HALL == True: 
                    
                    monstro2_hall.vida(arma_dic,MONSTRO2_HALL,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro2_hall.QUIT
                    MONSTRO2_HALL= monstro2_hall.MONSTRO
                    arma_dic = monstro2_hall.arma_dic
                    arma_atual = monstro2_hall.arma
                    quebrou = monstro2_hall.quebrou
                    
                
                if pi == monstro3_hall.y and pj == monstro3_hall.x and MONSTRO3_HALL == True:
                    
                    monstro3_hall.vida(arma_dic,MONSTRO3_HALL,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro3_hall.QUIT
                    MONSTRO3_HALL= monstro3_hall.MONSTRO
                    arma_dic = monstro3_hall.arma_dic
                    arma_atual = monstro3_hall.arma
                    quebrou = monstro3_hall.quebrou
                    
                        
                if MONSTRO1_HALL == True: 
                    monstro_hall.anda(A_LUZ,count_m,lanterna,zombie)
                    
                if MONSTRO2_HALL == True: 
                    monstro2_hall.anda(A_LUZ,count_m,lanterna,zombie)
                    
                if MONSTRO3_HALL== True: 
                    monstro3_hall.anda(A_LUZ,count_m,lanterna,zombie)
                
                    
                if arma_soco_hall == False:
                    if arma_hall_pos.colliderect(A_LUZ) == True: 
                        tela.blit(martelo,[11*TILESIZE,11*TILESIZE])     
  #---------------------------------------------------------------------------      
            if tab == ala_norte.TAB_2: 
                #print("mask",mask_BG.get_at((799,599)))
                #print("jogador",aurea_objeto.get_at(((pj+59),(pi + 59))))
                tela.blit(background_alanorte, [0,0])
                tela.blit(telag_8,[0*TILESIZE,0*TILESIZE])
                
                if lanterna == True: 
                    tela.blit(aurea_objeto,[((pj*TILESIZE)-3*TILESIZE),((pi*TILESIZE)-3*TILESIZE)])
                
                    if aurea_objeto.get_at(((pj+59),(pi + 59))) == blue:
                        
                        background_alanorte_mask = background_alanorte.convert()
                        background_alanorte_mask.fill(PRETO)
                        
                    
                        background_alanorte_mask.blit(aurea_objeto,[((pj*TILESIZE)-3*TILESIZE),((pi*TILESIZE)-3*TILESIZE)])
                        background_alanorte_mask.set_colorkey(blue)
                        
                        tela.blit(background_alanorte,[0,0])
                        tela.blit(background_alanorte_mask,[0,0])
                        A_LUZ =  pygame.Rect((pj-3)*TILESIZE,(pi-3)*TILESIZE,TILESIZE*7,TILESIZE*7)
               
                if MONSTRO1_NORTE == True: 
                    monstro_norte.anda(A_LUZ,count_m,lanterna,zombie)
                    
                if MONSTRO2_NORTE == True: 
                    monstro2_norte.anda(A_LUZ,count_m,lanterna,zombie)
                    
                if MONSTRO3_NORTE == True: 
                    monstro3_norte.anda(A_LUZ,count_m,lanterna,zombie)
            
                if MONSTRO4_NORTE == True:
                    monstro4_norte.anda(A_LUZ,count_m,lanterna,zombie)
                    


                if pi == monstro_norte.y and pj == monstro_norte.x and MONSTRO1_NORTE == True: 
                    
                    monstro_norte.vida(arma_dic,MONSTRO1_NORTE,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro_norte.QUIT
                    MONSTRO1_NORTE= monstro_norte.MONSTRO
                    arma_dic = monstro_norte.arma_dic
                    arma_atual = monstro_norte.arma
                    quebrou = monstro_norte.quebrou
                    
                if pi == monstro2_norte.y and pj == monstro2_norte.x and MONSTRO2_NORTE == True: 
                    
                    monstro2_norte.vida(arma_dic,MONSTRO2_NORTE,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro2_norte.QUIT
                    MONSTRO2_NORTE= monstro2_norte.MONSTRO
                    arma_dic = monstro2_norte.arma_dic
                    arma_atual = monstro2_norte.arma
                    quebrou = monstro2_norte.quebrou 
                    
                if pi == monstro3_norte.y and pj == monstro3_norte.x and MONSTRO3_NORTE == True: 
                    
                    monstro3_norte.vida(arma_dic,MONSTRO3_NORTE,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro3_norte.QUIT
                    MONSTRO3_NORTE= monstro3_norte.MONSTRO
                    arma_dic = monstro3_norte.arma_dic
                    arma_atual = monstro3_norte.arma
                    quebrou = monstro3_norte.quebrou
                    
                if pi == monstro4_norte.y and pj == monstro4_norte.x and MONSTRO4_NORTE == True: 
                    
                    monstro4_norte.vida(arma_dic,MONSTRO4_NORTE,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro4_norte.QUIT
                    MONSTRO4_NORTE= monstro4_norte.MONSTRO
                    arma_dic = monstro4_norte.arma_dic
                    arma_atual = monstro4_norte.arma
                    quebrou = monstro4_norte.quebrou
                    
                if pi == 2 and pj == 2: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'catana':armas['catana']}
                        
                        arma2_catana_norte = True
                        arma_atual = arma2_catana_norte
                        nome_arma = 'catana'
                    
                if arma2_catana_norte == False:
               
                    if arma1_norte_pos.colliderect(A_LUZ) == True:
                        tela.blit(martelo,[2*TILESIZE,2*TILESIZE])
                  
                if pi == 27 and pj == 2: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'martelo':armas['martelo']}
                        arma1_soco_norte = True
                        arma_atual = arma1_soco_norte
                        nome_arma = 'martelo'
                    
                    
                if arma1_soco_norte == False:
                    if arma2_norte_pos.colliderect(A_LUZ) == True: 
                        tela.blit(martelo,[2*TILESIZE,27*TILESIZE])
                  
                if pi == 24 and pj == 37: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'catana':armas['catana']}
                        arma3_catana_norte = True
                        arma_atual = arma3_catana_norte
                        nome_arma = 'catana'
                    
                if arma3_catana_norte == False:
                    if arma3_norte_pos.colliderect(A_LUZ) == True:
                        tela.blit(katana,[37*TILESIZE,24*TILESIZE])

                if chave_norte == False:
                    if chave_norte_pos.colliderect(A_LUZ) == True:
                        tela.blit(img_chave,[37*TILESIZE,3*TILESIZE])  
                if pi == 3 and pj == 37:    
                    chave_norte = True
#----------------------------------------------------------------------------------------
            if tab == ala_sul.TAB_3: 
                tela.blit(background_alasul, [0,0])
                tela.blit(telag_8,[0*TILESIZE,0*TILESIZE])
                
                if lanterna == True: 
                    tela.blit(aurea_objeto,[((pj*TILESIZE)-3*TILESIZE),((pi*TILESIZE)-3*TILESIZE)])
                
                    if aurea_objeto.get_at(((pj+59),(pi + 59))) == blue:
                        
                        background_alasul_mask = background_alasul.convert()
                        background_alasul_mask.fill(PRETO)
                        
                    
                        background_alasul_mask.blit(aurea_objeto,[((pj*TILESIZE)-3*TILESIZE),((pi*TILESIZE)-3*TILESIZE)])
                        background_alasul_mask.set_colorkey(blue)
                        
                        tela.blit(background_alasul,[0,0])
                        tela.blit(background_alasul_mask,[0,0])
                        A_LUZ =  pygame.Rect((pj-3)*TILESIZE,(pi-3)*TILESIZE,TILESIZE*7,TILESIZE*7)
                
                if pi == monstro_sul.y and pj == monstro_sul.x and MONSTRO1_SUL == True: 
                    
                    monstro_sul.vida(arma_dic,MONSTRO1_SUL,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro_sul.QUIT
                    MONSTRO1_SUL= monstro_sul.MONSTRO
                    arma_dic = monstro_sul.arma_dic
                    arma_atual = monstro_sul.arma
                    quebrou = monstro_sul.quebrou
                    
                if pi == monstro2_sul.y and pj == monstro2_sul.x and MONSTRO2_SUL == True: 
                    
                    monstro2_sul.vida(arma_dic,MONSTRO2_SUL,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro2_sul.QUIT
                    MONSTRO2_SUL= monstro2_sul.MONSTRO
                    arma_dic = monstro2_sul.arma_dic
                    arma_atual = monstro2_sul.arma
                    quebrou = monstro2_sul.quebrou
                   
                if pi == monstro3_sul.y and pj == monstro3_sul.x and MONSTRO3_SUL == True: 
                    
                    monstro3_sul.vida(arma_dic,MONSTRO3_SUL,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro3_sul.QUIT
                    MONSTRO3_SUL= monstro3_sul.MONSTRO
                    arma_dic = monstro3_sul.arma_dic
                    arma_atual = monstro3_sul.arma
                    quebrou = monstro3_sul.quebrou
                    
                if pi == monstro4_sul.y and pj == monstro4_sul.x and MONSTRO4_SUL == True: 
                    
                    monstro4_sul.vida(arma_dic,MONSTRO4_SUL,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro4_sul.QUIT
                    MONSTRO4_SUL= monstro4_sul.MONSTRO
                    arma_dic = monstro4_sul.arma_dic
                    arma_atual = monstro4_sul.arma
                    quebrou = monstro4_sul.quebrou
                    
                if MONSTRO1_SUL == True: 
                    monstro_sul.anda(A_LUZ,count_m,lanterna,zombie)
                    
                if MONSTRO2_SUL == True: 
                    monstro2_sul.anda(A_LUZ,count_m,lanterna,zombie)
                    
                if MONSTRO3_SUL == True: 
                    monstro3_sul.anda(A_LUZ,count_m,lanterna,zombie)
            
                if MONSTRO4_SUL == True:
                    monstro4_sul.anda(A_LUZ,count_m,lanterna,zombie)
                
                if pi == 19 and pj == 2: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'martelo':armas['martelo']}
                        arma1_soco_sul = True
                        arma_atual = arma1_soco_sul
                        nome_arma = 'martelo'
                    
                if arma1_soco_sul == False:
               
                    if arma1_sul_pos.colliderect(A_LUZ) == True:
                        tela.blit(martelo,[2*TILESIZE,19*TILESIZE])
                        
                if pi == 4 and pj == 33: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'catana':armas['catana']}
                        arma2_catana_sul = True
                        arma_atual = arma2_catana_sul
                        nome_arma = 'catana'
                    
                if arma2_catana_sul == False:
               
                    if arma2_sul_pos.colliderect(A_LUZ) == True:
                        tela.blit(katana,[33*TILESIZE,4*TILESIZE])
                
                if pi == 27 and pj == 30: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'martelo':armas['martelo']}
                        arma3_soco_sul = True
                        arma_atual = arma3_soco_sul
                        nome_arma = 'martelo'
                    
                if arma3_soco_sul == False:
               
                    if arma3_sul_pos.colliderect(A_LUZ) == True:
                        tela.blit(martelo,[30*TILESIZE,27*TILESIZE])

                if chave_sul == False:
                    if chave_sul_pos.colliderect(A_LUZ) == True:
                        tela.blit(img_chave,[17*TILESIZE,15*TILESIZE])    
                if pi == 15 and pj == 17:    
                    chave_sul = True
#---------------------------------------------------------------------------------------
            if tab == ala_leste_1.TAB_5:
                
                tela.blit(background_alaleste1, [0,0])
                tela.blit(telag_8,[0*TILESIZE,0*TILESIZE])
                
                if lanterna == True: 
                    tela.blit(aurea_objeto,[((pj*TILESIZE)-3*TILESIZE),((pi*TILESIZE)-3*TILESIZE)])
                
                    if aurea_objeto.get_at(((pj+59),(pi + 59))) == blue:
                        
                        background_alaleste1_mask = background_alaleste1.convert()
                        background_alaleste1_mask.fill(PRETO)
                        
                    
                        background_alaleste1_mask.blit(aurea_objeto,[((pj*TILESIZE)-3*TILESIZE),((pi*TILESIZE)-3*TILESIZE)])
                        background_alaleste1_mask.set_colorkey(blue)
                        
                        tela.blit(background_alaleste1,[0,0])
                        tela.blit(background_alaleste1_mask,[0,0])
                        A_LUZ =  pygame.Rect((pj-3)*TILESIZE,(pi-3)*TILESIZE,TILESIZE*7,TILESIZE*7)
                
                if MONSTRO1_LESTE1 == True: 
                    monstro_leste1.anda(A_LUZ,count_m,lanterna,zombie)
                
                if MONSTRO2_LESTE1 == True: 
                    monstro2_leste1.anda(A_LUZ,count_m,lanterna,zombie)
                    
                if MONSTRO3_LESTE1 == True: 
                    monstro3_leste1.anda(A_LUZ,count_m,lanterna,zombie)
                
                if MONSTRO4_LESTE1 == True: 
                    monstro4_leste1.anda(A_LUZ,count_m,lanterna,zombie)
                
                if pi == monstro_leste1.y and pj == monstro_leste1.x and MONSTRO1_LESTE1 == True: 
                    
                    monstro_leste1.vida(arma_dic,MONSTRO1_LESTE1,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro_leste1.QUIT
                    MONSTRO1_LESTE1= monstro_leste1.MONSTRO
                    arma_dic = monstro_leste1.arma_dic
                    arma_atual = monstro_leste1.arma
                    quebrou = monstro_leste1.quebrou
                   
                if pi == monstro2_leste1.y and pj == monstro2_leste1.x and MONSTRO2_LESTE1 == True: 
                    
                    monstro2_leste1.vida(arma_dic,MONSTRO2_LESTE1,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro2_leste1.QUIT
                    MONSTRO2_LESTE1= monstro2_leste1.MONSTRO 
                    arma_dic = monstro2_leste1.arma_dic
                    arma_atual = monstro2_leste1.arma
                    quebrou = monstro2_leste1.quebrou
                    
                if pi == monstro3_leste1.y and pj == monstro3_leste1.x and MONSTRO3_LESTE1 == True: 
                    
                    monstro3_leste1.vida(arma_dic,MONSTRO3_LESTE1,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro3_leste1.QUIT
                    MONSTRO3_LESTE1= monstro3_leste1.MONSTRO
                    arma_dic = monstro3_leste1.arma_dic
                    arma_atual = monstro3_leste1.arma
                    quebrou = monstro3_leste1.quebrou
                       
                if pi == monstro4_leste1.y and pj == monstro4_leste1.x and MONSTRO4_LESTE1 == True: 
                    
                    monstro4_leste1.vida(arma_dic,MONSTRO4_LESTE1,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro4_leste1.QUIT
                    MONSTRO4_LESTE1= monstro4_leste1.MONSTRO
                    arma_dic = monstro4_leste1.arma_dic
                    arma_atual = monstro4_leste1.arma
                    quebrou = monstro4_leste1.quebrou
                    
                if pi == 27 and pj == 6: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'catana':armas['catana']}
                        arma1_catana_leste1 = True
                        arma_atual = arma1_catana_leste1
                        nome_arma = 'catana'
                    
                if arma1_catana_leste1 == False:
               
                    if arma1_leste1_pos.colliderect(A_LUZ) == True:
                        tela.blit(katana,[6*TILESIZE,27*TILESIZE])
                        
                if pi == 6 and pj == 25: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'martelo':armas['martelo']}
                        arma2_soco_leste1 = True
                        arma_atual = arma2_soco_leste1
                        nome_arma = 'martelo'
                    
                if arma2_soco_leste1 == False:
               
                    if arma2_leste1_pos.colliderect(A_LUZ) == True: 
                        tela.blit(martelo,[25*TILESIZE,6*TILESIZE])

                if chave_final == False:
                    if chave_final_pos.colliderect(A_LUZ) == True:
                        tela.blit(img_chave,[34*TILESIZE,22*TILESIZE])
                if pi == 22 and pj == 34:    
                    chave_final = True
#------------------------------------------------------------------------------------                        
            if tab == ala_leste_final.TAB_4:
                
                tela.blit(background_alaleste2, [0,0])
                tela.blit(telag_8,[0*TILESIZE,0*TILESIZE])
                
                if lanterna == True: 
                    tela.blit(aurea_objeto,[((pj*TILESIZE)-3*TILESIZE),((pi*TILESIZE)-3*TILESIZE)])
                
                    if aurea_objeto.get_at(((pj+59),(pi + 59))) == blue:
                        
                        background_alaleste2_mask = background_alaleste2.convert()
                        background_alaleste2_mask.fill(PRETO)
                        
                    
                        background_alaleste2_mask.blit(aurea_objeto,[((pj*TILESIZE)-3*TILESIZE),((pi*TILESIZE)-3*TILESIZE)])
                        background_alaleste2_mask.set_colorkey(blue)
                        
                        tela.blit(background_alaleste2,[0,0])
                        tela.blit(background_hall_alaleste2,[0,0])
                        A_LUZ =  pygame.Rect((pj-3)*TILESIZE,(pi-3)*TILESIZE,TILESIZE*7,TILESIZE*7)
                
                if MONSTRO1_LESTE2 == True: 
                    monstro_leste2.anda(A_LUZ,count_m,lanterna,zombie)
                    
                if MONSTRO2_LESTE2 == True: 
                    monstro2_leste2.anda(A_LUZ,count_m,lanterna,zombie)
                    
                if MONSTRO3_LESTE2 == True: 
                    monstro3_leste2.anda(A_LUZ,count_m,lanterna,zombie)
                    
                if MONSTRO4_LESTE2 == True: 
                    monstro4_leste2.anda(A_LUZ,count_m,lanterna,zombie)
                
                if MONSTRO5_LESTE2 == True: 
                    monstro5_leste2.anda(A_LUZ,count_m,lanterna,zombie)
                    
                if MONSTRO6_LESTE2 == True: 
                    monstro6_leste2.anda(A_LUZ,count_m,lanterna,zombie)
                    
                if pi == monstro_leste2.y and pj == monstro_leste2.x and MONSTRO1_LESTE2 == True: 
                    
                    monstro_leste2.vida(arma_dic,MONSTRO1_LESTE2,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro_leste2.QUIT
                    MONSTRO1_LESTE2= monstro_leste2.MONSTRO
                    arma_dic = monstro_leste2.arma_dic
                    arma_atual = monstro_leste2.arma
                    quebrou = monstro_leste2.quebrou
                    
                    if quebrou == 1: 
                        tela.blit(label10, (monstro_leste2.x, (monstro_leste2.y - 1)))
                        quebrou = 0 
                        
                if pi == monstro2_leste2.y and pj == monstro2_leste2.x and MONSTRO2_LESTE2 == True: 
                    
                    monstro2_leste2.vida(arma_dic,MONSTRO2_LESTE2,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro2_leste2.QUIT
                    MONSTRO2_LESTE2= monstro2_leste2.MONSTRO
                    arma_dic = monstro2_leste2.arma_dic
                    arma_atual = monstro2_leste2.arma
                    quebrou = monstro2_leste2.quebrou
                       
                if pi == monstro3_leste2.y and pj == monstro3_leste2.x and MONSTRO3_LESTE2 == True: 
                    
                    monstro3_leste2.vida(arma_dic,MONSTRO3_LESTE2,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro3_leste2.QUIT
                    MONSTRO3_LESTE2= monstro3_leste2.MONSTRO
                    arma_dic = monstro3_leste2.arma_dic
                    arma_atual = monstro3_leste2.arma
                    quebrou = monstro3_leste2.quebrou
                      
                if pi == monstro4_leste2.y and pj == monstro4_leste2.x and MONSTRO4_LESTE2 == True: 
                    
                    monstro4_leste2.vida(arma_dic,MONSTRO4_LESTE2,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro4_leste2.QUIT
                    MONSTRO4_LESTE2= monstro4_leste2.MONSTRO
                    arma_dic = monstro4_leste2.arma_dic
                    arma_atual = monstro4_leste2.arma
                    quebrou = monstro4_leste2.quebrou
                    
                if pi == monstro5_leste2.y and pj == monstro5_leste2.x and MONSTRO5_LESTE2 == True: 
                    
                    monstro5_leste2.vida(arma_dic,MONSTRO5_LESTE2,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro5_leste2.QUIT
                    MONSTRO5_LESTE2= monstro5_leste2.MONSTRO
                    arma_dic = monstro5_leste2.arma_dic
                    arma_atual = monstro5_leste2.arma
                    quebrou = monstro5_leste2.quebrou
                      
                if pi == monstro6_leste2.y and pj == monstro6_leste2.x and MONSTRO6_LESTE2 == True: 
                    
                    monstro6_leste2.vida(arma_dic,MONSTRO6_LESTE2,arma_atual,QUIT,nome_arma,quebrou)
                    QUIT = monstro6_leste2.QUIT
                    MONSTRO6_LESTE2= monstro6_leste2.MONSTRO
                    arma_dic = monstro6_leste2.arma_dic
                    arma_atual = monstro6_leste2.arma
                    quebrou = monstro6_leste2.quebrou
                       
                if pi == 23 and pj == 12: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'catana':armas['catana']}
                        arma1_catana_leste2 = True
                        arma_atual = arma1_catana_leste2
                        nome_arma = 'catana'
                    
                if arma1_catana_leste2 == False:
               
                    if arma1_leste2_pos.colliderect(A_LUZ) == True:
                        tela.blit(martelo,[12*TILESIZE,23*TILESIZE])
                        
                if pi == 6 and pj == 24: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'martelo':armas['martelo']}
                        arma2_soco_leste2 = True
                        arma_atual = arma2_soco_leste2
                        nome_arma = 'martelo'
                    
                if arma2_soco_leste2 == False:
               
                    if arma2_leste2_pos.colliderect(A_LUZ) == True:
                        tela.blit(martelo,[24*TILESIZE,6*TILESIZE])
                    
                if pi == 7 and pj == 32: 
                    
                    if len(arma_dic) == 0:
                        
                        arma_dic = {'catana':armas['catana']}
                        arma3_catana_leste2 = True
                        arma_atual = arma3_catana_leste2
                        nome_arma = 'catana'
                    
                if arma3_catana_leste2 == False:
               
                    if arma3_leste2_pos.colliderect(A_LUZ) == True:
                        tela.blit(martelo,[32*TILESIZE,7*TILESIZE])
                        
            if quebrou == 1: 
                count_a +=1
                tela.blit(label10, (15*TILESIZE,10*TILESIZE))
                if count_a == 30:
                    quebrou = 0
                    count_a = 0
#======================================================================================
            
            if lanterna == True: 
                
            
                    
                A_LUZ =  pygame.Rect((pj-3)*TILESIZE,(pi-3)*TILESIZE,TILESIZE*7,TILESIZE*7)
            
            
            count_m += 1
            if count_m == 3:
                count_m = 0
                
 # ------------------------ir pro hall------------------------------
            if tab[pi][pj] == 14:
                tab = tabuleiro.TAB
                pi = 14
                pj = 0
                jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)
                
 #-------------------ir para a ala norte------------------------------------
            if tab[pi][pj] == 11: 
                tab = ala_norte.TAB_2
                pj = 20
                pi = 28 
                jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)
            
# ---------------------voltando para o hall----------------------------------------------
            if tab[pi][pj] == 2: 
                tab = tabuleiro.TAB
                pj = 20
                pi = 1
                jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)

#--------------------------------abrindo ala sul---------------------------------------               
            if tab[pi][pj] == 6 and chave_norte == True: 
                tab = ala_sul.TAB_3
                pj = 20
                pi = 1
                jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)
                
            if tab[pi][pj] == 6 and chave_norte == False: 
                label1 = fonte_2.render("A porta esta trancada, va para a ala norte", True, BRANCO)
                tela.blit(label1, (2*TILESIZE, 27*TILESIZE))
 
#----------------------------voltando para o hall----------------------------------------
           
            if tab[pi][pj] == 4:
                tab = tabuleiro.TAB
                pj = 20
                pi = 28
                jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)
                
#------------------------------abrindo ala_leste1---------------------------------------------
            if tab[pi][pj] == 12 and chave_sul == True: 
                tab = ala_leste_1.TAB_5
                pj = 1
                pi = 13
                jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)
                
            if tab[pi][pj] == 12 and chave_sul == False: 
                label7 = fonte_2.render("A porta esta trancada, va para a ala sul", True, BRANCO)
                tela.blit(label7, (2*TILESIZE, 13*TILESIZE))

#----------------------------abrindo ala final -------------------------------------------
            if tab[pi][pj] == 15 and chave_final == True: 
                tab = ala_leste_final.TAB_4
                pj = 1
                pi = 13
                jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)

            if tab[pi][pj] == 15 and chave_final == False: 
                label8 = fonte_2.render("A porta esta trancada, va para a ala leste 1", True, BRANCO)
                tela.blit(label8, (2*TILESIZE, 12*TILESIZE))
                
#------------------------------------voltando para leste1------------------------------------------------                
            if tab[pi][pj] == 20: 
                tab = tabuleiro.TAB
                pj = 38
                pi = 14
                jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)     

 
#-------------------------------------voltando para o hall-----------------------------
            if tab[pi][pj] == 8: 
                tab = ala_leste_1.TAB_5
                pj = 38
                pi = 14
                jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)    
    

                
#--------------------------------------escritas---------------------------------------------------

# falta os nomes dos outos tabuleiros, igual codigo abaixo: 
    
            if tab == ala_norte.TAB_2 and pj == 20 and pi == 28: 
                label2 = fonte_2.render("Ala norte", True, BRANCO)
                tela.blit(label2, (15*TILESIZE, 26*TILESIZE))

            if tab == ala_sul.TAB_3 and pj == 20 and pi == 1: 
                label4 = fonte_2.render("Ala Sul", True, BRANCO)
                tela.blit(label4, (15*TILESIZE, 2*TILESIZE))
                
            if tab == tabuleiro.TAB and pj == 20 and pi == 1: 
                label3 = fonte_2.render("Hall", True, BRANCO)
                tela.blit(label3, (15*TILESIZE, 2*TILESIZE))
                
            if tab == tabuleiro.TAB and pj == 20 and pi == 28:                
                label5 = fonte_2.render("Hall", True, BRANCO)
                tela.blit(label5, (15*TILESIZE, 27*TILESIZE))
                
            if tab == tabuleiro.TAB and pj == 38 and pi == 13:                
                label9 = fonte_2.render("Hall", True, BRANCO)
                tela.blit(label9, (36*TILESIZE, 12*TILESIZE))
            
            if tab == ala_leste_1 and pj == 1 and pi == 13:                
                label9 = fonte_2.render("ala leste", True, BRANCO)
                tela.blit(label9, (15*TILESIZE, 27*TILESIZE))
                
#-------------------------------------------------------------------------------------

            if len(arma_dic) == 0:
                
                tela.blit(tela_inventario,[MAPWIDTH*TILESIZE,0])
                tela.blit(img_inventario,[MAPWIDTH*TILESIZE,0])
                
                label_inventario1 = fonte_inventario1.render("Inventário:", True, PRETO)
                tela.blit(label_inventario1, ([MAPWIDTH*TILESIZE + 40 ,0.3*TILESIZE]))
                
                if lanterna == False: 
                
                    label_inventario6 = fonte_inventario.render("- Vazio", True, PRETO)
                    tela.blit(label_inventario6, ([MAPWIDTH*TILESIZE + 30 ,3*TILESIZE]))
                    
                if lanterna == True: 
                
                    label_inventario11 = fonte_inventario.render("- Lanterna", True, PRETO)
                    tela.blit(label_inventario11, ([MAPWIDTH*TILESIZE + 30 ,3*TILESIZE]))
               
                if chave_norte == True:
                        
                    label_inventario7 = fonte_inventario.render("__________________", True, PRETO)
                    tela.blit(label_inventario7, ([MAPWIDTH*TILESIZE + 15 ,12*TILESIZE]))
                        
                    label_inventario12 = fonte_inventario.render("- Chaves :", True, PRETO)
                    tela.blit(label_inventario12, ([MAPWIDTH*TILESIZE + 30 ,13*TILESIZE]))
                
                        
                    label_inventario12 = fonte_inventario.render("     Ala sul", True, PRETO)
                    tela.blit(label_inventario12, ([MAPWIDTH*TILESIZE + 5 ,15*TILESIZE]))
                    
                if chave_sul == True:
                    
                    label_inventario13 = fonte_inventario.render("   Ala leste", True, PRETO)
                    tela.blit(label_inventario13, ([MAPWIDTH*TILESIZE + 5 ,17*TILESIZE]))
                        
                if chave_final == True:
                        
                    label_inventario14 = fonte_inventario.render("    Chave da saída", True, PRETO)
                    tela.blit(label_inventario14, ([MAPWIDTH*TILESIZE + 5 ,19*TILESIZE]))
                        
                
                    
            if len(arma_dic) == 1:
                
                    tela.blit(tela_inventario,[MAPWIDTH*TILESIZE,0])
                    tela.blit(img_inventario,[MAPWIDTH*TILESIZE,0])
                    
                    label_inventario1 = fonte_inventario1.render("Inventário", True, PRETO)
                    tela.blit(label_inventario1, ([MAPWIDTH*TILESIZE + 40 ,0.3*TILESIZE]))
                
                    label_inventario2 = fonte_inventario.render("- Arma atual :", True, PRETO)
                    tela.blit(label_inventario2, ([MAPWIDTH*TILESIZE + 10 ,5*TILESIZE]))
                    
                    label_inventario3 = fonte_inventario.render(("    nome : {0}".format(nome_arma)), True, PRETO)
                    tela.blit(label_inventario3, ([MAPWIDTH*TILESIZE + 1 ,7*TILESIZE]))
                    
                    label_inventario4 = fonte_inventario.render(("    poder da arma : {0}".format(arma_dic[nome_arma][0])), True, PRETO)
                    tela.blit(label_inventario4, ([MAPWIDTH*TILESIZE + 1 ,9*TILESIZE]))
                        
                    label_inventario5 = fonte_inventario.render(("    vida da arma : {0}".format(arma_dic[nome_arma][1])), True, PRETO)
                    tela.blit(label_inventario5, ([MAPWIDTH*TILESIZE + 1 ,11*TILESIZE]))
                        
                        
                    if lanterna == True: 
                
                        label_inventario11 = fonte_inventario.render("- Lanterna", True, PRETO)
                        tela.blit(label_inventario11, ([MAPWIDTH*TILESIZE + 30 ,3*TILESIZE]))
                        
                        label_inventario7 = fonte_inventario.render("__________________", True, PRETO)
                        tela.blit(label_inventario7, ([MAPWIDTH*TILESIZE + 15 ,4*TILESIZE]))
                
                        
                    if chave_norte == True:
                        
                        label_inventario7 = fonte_inventario.render("__________________", True, PRETO)
                        tela.blit(label_inventario7, ([MAPWIDTH*TILESIZE + 15 ,12*TILESIZE]))
                        
                        label_inventario12 = fonte_inventario.render("- Chaves :", True, PRETO)
                        tela.blit(label_inventario12, ([MAPWIDTH*TILESIZE + 30 ,13*TILESIZE]))
                
                        
                        label_inventario12 = fonte_inventario.render("    Ala sul", True, PRETO)
                        tela.blit(label_inventario12, ([MAPWIDTH*TILESIZE + 5 ,15*TILESIZE]))
                    
                    if chave_sul == True:
                        
                        label_inventario13 = fonte_inventario.render("    Ala leste", True, PRETO)
                        tela.blit(label_inventario13, ([MAPWIDTH*TILESIZE + 5 ,17*TILESIZE]))
                        
                    if chave_final == True:
                        
                        label_inventario14 = fonte_inventario.render("    Chave da saída", True, PRETO)
                        tela.blit(label_inventario14, ([MAPWIDTH*TILESIZE + 5 ,19*TILESIZE]))
                        
            
            #movimento jogador
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_RIGHT]:
                if pj < (MAPWIDTH - 1) and (tab[pi][pj+1] != 1):
                    jogador.move_ip(TILESIZE,0)
                    pj += 1
                    personagem = "right"
            if key_pressed[pygame.K_UP]:
                if pi > 0 and (tab[pi-1][pj] != 1):
                    jogador.move_ip(0,-TILESIZE)
                    pi -= 1
                    personagem = "up"
            if key_pressed[pygame.K_LEFT]:
                if pj > 0 and (tab[pi][pj-1] != 1):
                    jogador.move_ip(-TILESIZE,0)
                    pj -= 1
                    personagem = "left"
            if key_pressed[pygame.K_DOWN]:
                if (pi < (MAPHEIGHT - 1)) and (tab[pi+1][pj] != 1):
                    jogador.move_ip(0,TILESIZE)
                    pi += 1
                    personagem = "down"
                    
            if personagem == "right":
                
                tela.blit(personagem_right,[pj*TILESIZE,pi*TILESIZE])
                
            if personagem == "up":
                
                tela.blit(personagem_up,[pj*TILESIZE,pi*TILESIZE])
                
            if personagem == "left":
            
                tela.blit(personagem_left,[pj*TILESIZE,pi*TILESIZE])
                
            if personagem == "down": 
                
                tela.blit(personagem_down,[pj*TILESIZE,pi*TILESIZE])
#================================================================================
                    
#------------------------------------------------------------------------------------------
            
            if QUIT == True: 
                nome_tela = 'quit'
            

        if nome_tela == 'quit':
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
            
            tela.fill(PRETO)
            
            label2 = fonte_titulo.render("Voce Perdeu...", True, BRANCO)
            tela.blit(label2, (6*TILESIZE, 3*TILESIZE))
            
            play = 1
            exit = 0
    
            b1 = botao("play again",10,22,18,4,VERMELHO,VERMELHO_DARK,tela,fonte_botao,play)                        
            b2 = botao("sair",35,22,8,4,VERMELHO,VERMELHO_DARK,tela,fonte_botao,exit)
         
            if b1 == 3:
                nome_tela = 'jogo'

                tab = tab_tutorial.TAB_6
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
                
                armas = {'catana': [10,3], 'martelo': [5,4]}         # dicionario 
                
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
                arma_atual = False
                nome_arma = ''
                quebrou = 0 
                

                #BOOL
                chave_norte = False
                chave_sul = False
                chave_final = False
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

            elif b2 == 2:
                sair = True

        relogio.tick(12)
        pygame.display.update()
    pygame.quit()
main()