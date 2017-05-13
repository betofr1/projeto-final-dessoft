import pygame
import tabuleiro
import time
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
    def __init__(self,x,y,cor,tamanho,tela,tab):
        self.tab = tab
        self.tela = tela
        self.tamanho = tamanho
        self.x = x
        self.y = y
        self.cor = cor
        self.ret =pygame.Rect(self.x*self.tamanho,self.y*self.tamanho,self.tamanho,self.tamanho)



    def anda(self,l1,l2,l3,count):
        self.count = count
        
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        
        if self.ret.colliderect(self.l1) == True or self.ret.colliderect(self.l2) == True or self.ret.colliderect(self.l3) == True:    
            pygame.draw.rect(self.tela, self.cor, self.ret)
        
        if self.count == 0:
            
            num = random.randint(0,4)    
            if self.tab[self.y][self.x+1] != 1 and self.tab[self.y][self.x+1] != 5:
                if num == 0:
                    self.ret.move_ip(1*self.tamanho,0)
                    self.x += 1
            if self.tab[self.y+1][self.x] != 1 and self.tab[self.y+1][self.x] != 5:
                if num == 1:
                    self.ret.move_ip(0,1*self.tamanho)
                    self.y += 1
            if self.tab[self.y-1][self.x] != 1 and self.tab[self.y-1][self.x] != 5:
                if num == 2:
                    self.ret.move_ip(0,-1*self.tamanho)
                    self.y -= 1
            if self.tab[self.y][self.x-1] != 1 and self.tab[self.y][self.x-1] != 5:
                if num == 3:
                    self.ret.move_ip(-1*self.tamanho,0)
                    self.x -= 1
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
    font = pygame.font.SysFont('Arial', 25)


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
    pi = 0
    pj = 0
    jogador = pygame.Rect(pj*TILESIZE,pi*TILESIZE,TILESIZE,TILESIZE)
    #definindo monstros
    mi = 15
    mj = 16
    m2i = 3
    m2j = 25
    m3i = 27
    m3j = 35
    monstro = Monstro(mj,mi,VERMELHO,TILESIZE,tela,tab)
    monstro2 = Monstro(m2j,m2i,VERMELHO,TILESIZE,tela,tab)
    monstro3 = Monstro(m3j,m3i,VERMELHO,TILESIZE,tela,tab)

    arma_pos = pygame.Rect(11*TILESIZE,11*TILESIZE,TILESIZE,TILESIZE)
    #definindo lanterna
    lanterna_pos = pygame.Rect(6*TILESIZE,2*TILESIZE,TILESIZE,TILESIZE)
    A_LUZ1 = pygame.Rect((pj-1)*TILESIZE,(pi-3)*TILESIZE,TILESIZE*3,TILESIZE*7)
    A_LUZ2 = pygame.Rect((pj-3)*TILESIZE,(pi-1)*TILESIZE,TILESIZE*7,TILESIZE*3)
    A_LUZ3 = pygame.Rect((pj-2)*TILESIZE,(pi-2)*TILESIZE,TILESIZE*5,TILESIZE*5)

    
    Fullscreen = False
    sair = False
    lanterna = False
    arma = False
    key_pressed = pygame.key.get_pressed()
    luz = True
    QUIT = False
    MONSTRO = False
    count = 0  
    count_m = 0  
    nome_tela = 'jogo'

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
            
            if pi == monstro.y and pj == monstro.x or pi == monstro2.y and pj ==monstro2.x or pi == monstro3.y and pj == monstro3.x:
                MONSTRO = True
                if arma == False: 
                    QUIT = True
                if arma == True:
                    QUIT = False
                    
                    
                
            
        
        
            relogio.tick(12)

            
            
            
            
            tela.fill(PRETO)
            
            if tab == tabuleiro.TAB: 
                tela2.fill(BRANCO)
                tela.blit(tela2,[0,0])
            
        
            telag_2.fill(CINZA_SUPER_CLARO)
            telag_3.fill(CINZA_CLARO)
            telag_4.fill(CINZA_MEDIO)
            telag_5.fill(CINZA_MEDIO)
            telag_6.fill(CINZA_MEIO_ESCURO)
            telag_7.fill(CINZA_ESCURO)
            telag_8.fill(CINZA_MEDIO)
            telag_9.fill(CINZA_MEIO_ESCURO)
            telag_10.fill(CINZA_ESCURO)
            telag_11.fill(CINZA_SUPER_CLARO)
            telag_12.fill(CINZA_CLARO)
            telag_13.fill(CINZA_MEDIO)
            telag_14.fill(CINZA_MEDIO)
            telag_15.fill(CINZA_MEIO_ESCURO)
            telag_16.fill(CINZA_ESCURO)
            
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
                pygame.draw.rect(tela,BRANCO,A_LUZ1)
                pygame.draw.rect(tela,BRANCO,A_LUZ2)
                pygame.draw.rect(tela,BRANCO,A_LUZ3)
                
            
            if lanterna == False: 
                
                pygame.draw.rect(tela,AZUL,lanterna_pos)
                
                
            for coluna in range(MAPWIDTH):
                for linha in range(MAPHEIGHT):
                    if tab[linha][coluna] == 1:
                        PAREDE = pygame.Rect(coluna*TILESIZE,linha*TILESIZE,TILESIZE,TILESIZE)
                        pygame.draw.rect(tela,PRETO,PAREDE)
            pygame.draw.rect(tela,ROSA,jogador)
            
            # arma: 
            
            if tab == tabuleiro.TAB: 
                
                
                if pi == 11 and pj == 11: 
                    
                    arma = True
                    
            if arma == False:
                if arma_pos.colliderect(A_LUZ1) == True or arma_pos.colliderect(A_LUZ2) == True or arma_pos.colliderect(A_LUZ3) == True:
                    pygame.draw.rect(tela,VERDE,arma_pos)
                    
            monstro.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m)
            monstro2.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m)
            monstro3.anda(A_LUZ1,A_LUZ2,A_LUZ3,count_m)
            
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

        elif nome_tela == 'quit':

            tela.fill(PRETO)
            
            label2 = fonte.render("VOCÊ PERDEU...", True, VERMELHO)
    
            tela.blit(label2, (5*TILESIZE, 3*TILESIZE))

            b1 = botao("play again",7,22,5,3,VERMELHO,tela,font,'play')
            if b1 == 1:
                nome_tela = 'jogo'
            else: 
                pass
            b2 = botao("sair",25,22,5,3,VERMELHO,tela,font,'quit')
            if b2 == 2:
                pygame.quit()
            else:
                pass

        pygame.display.update()
    pygame.quit()
main()

