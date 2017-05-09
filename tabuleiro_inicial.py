import pygame
import tabuleiro
import time

def main():
    
    
    TILESIZE = 20
    MAPWIDTH = len(tabuleiro.TAB[0])
    MAPHEIGHT = len(tabuleiro.TAB)
    pygame.init()
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
    telag_10 = pygame.Surface((TILESIZE*3,TILESIZE*5))
    telag_11 = pygame.Surface((TILESIZE*4,TILESIZE*3))
    telag_12 = pygame.Surface((TILESIZE*3,TILESIZE*4))
    telag_13 = pygame.Surface((TILESIZE*3,TILESIZE*4))
    telag_14 = pygame.Surface((TILESIZE*2,TILESIZE*1))
    telag_15 = pygame.Surface((TILESIZE*2,TILESIZE*5))
    telag_16 = pygame.Surface((TILESIZE*2,TILESIZE*5))
    
    # texto 
    
    fonte = pygame.font.SysFont("Arial", 100)


    pygame.display.set_caption("LABIRINTO DOS INFERNO")
    relogio = pygame.time.Clock()
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
    jogador = pygame.Rect(0,0,TILESIZE,TILESIZE)
    monstro = pygame.Rect(16*TILESIZE,15*TILESIZE,TILESIZE,TILESIZE)
    lanterna_pos = pygame.Rect(6*TILESIZE,2*TILESIZE,TILESIZE,TILESIZE)
    arma_pos = pygame.Rect(11*TILESIZE,11*TILESIZE,TILESIZE,TILESIZE)
    mi = 15
    mj = 16
    pi = 0
    pj = 0
    A_LUZ1 = pygame.Rect((pj-1)*TILESIZE,(pi-3)*TILESIZE,TILESIZE*3,TILESIZE*7)
    A_LUZ2 = pygame.Rect((pj-3)*TILESIZE,(pi-1)*TILESIZE,TILESIZE*7,TILESIZE*3)
    A_LUZ3 = pygame.Rect((pj-2)*TILESIZE,(pi-2)*TILESIZE,TILESIZE*5,TILESIZE*5)
    #BOTAO_QUIT = pygame.Rect(6*TILESIZE,6*TILESIZE,TILESIZE*5,TILESIZE*5)
    
    #LUZ1.fill(BRANCO)
    #LUZ2.fill(BRANCO)
    #LUZ3.fill(BRANCO)
    
    Fullscreen = False
    sair = False
    lanterna = False
    arma = False
    key_pressed = pygame.key.get_pressed()
    luz = True
    QUIT = False

    count = 0    

    while sair != True:
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

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            if pj < (MAPWIDTH - 1) and (tabuleiro.TAB[pi][pj+1] != 1):
                jogador.move_ip(TILESIZE,0)
                pj += 1
        if key_pressed[pygame.K_UP]:
            if pi > 0 and (tabuleiro.TAB[pi-1][pj] != 1):
                jogador.move_ip(0,-TILESIZE)
                pi -= 1
        if key_pressed[pygame.K_LEFT]:
            if pj > 0 and (tabuleiro.TAB[pi][pj-1] != 1):
                jogador.move_ip(-TILESIZE,0)
                pj -= 1
        if key_pressed[pygame.K_DOWN]:
            if (pi < (MAPHEIGHT - 1)) and (tabuleiro.TAB[pi+1][pj] != 1):
                jogador.move_ip(0,TILESIZE)
                pi += 1


        if pi == mi and pj == mj:
            
            QUIT = True

        
        relogio.tick(15)
        
        
        
        
        tela.fill(PRETO)
        
        
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
            
            #tela.blit(LUZ1,[(pj-1)*TILESIZE,(pi-3)*TILESIZE])
            #tela.blit(LUZ2,[(pj-3)*TILESIZE,(pi-1)*TILESIZE])
            #tela.blit(LUZ3,[(pj-2)*TILESIZE,(pi-2)*TILESIZE])
        
        if lanterna == False: 
            
            pygame.draw.rect(tela,AZUL,lanterna_pos)
            
            
        for coluna in range(MAPWIDTH):
            for linha in range(MAPHEIGHT):
                if tabuleiro.TAB[linha][coluna] == 1:
                    PAREDE = pygame.Rect(coluna*TILESIZE,linha*TILESIZE,TILESIZE,TILESIZE)
                    pygame.draw.rect(tela,PRETO,PAREDE)
        pygame.draw.rect(tela,ROSA,jogador)
        
        # arma: 
        
        if pi == 11 and pj == 11: 
            
            arma = True
                
        if arma == False:
            if arma_pos.colliderect(A_LUZ1) == True or arma_pos.colliderect(A_LUZ2) == True or arma_pos.colliderect(A_LUZ3) == True:
                pygame.draw.rect(tela,VERDE,arma_pos)
         
        if monstro.colliderect(A_LUZ1) == True or monstro.colliderect(A_LUZ2) == True or monstro.colliderect(A_LUZ3) == True:    
            pygame.draw.rect(tela,VERMELHO,monstro)
            
        
        
        
        if QUIT == True: 
            
            tela.fill(PRETO)
            
            time.sleep(0.5)
            
            label1 = fonte.render("VOCÊ PERDEU...", True, VERMELHO)
    
            tela.blit(label1, (5*TILESIZE, 3*TILESIZE))
            
            #label2 = fonte.render("QUIT", True, VERMELHO)
            
            #BOTAO_QUIT.blit(label2, (0,0))
            
            #if key_pressed[pygame.K_RIGHT]:
            
            
            
            
        
            
            
            
            
        pygame.display.update()
    pygame.quit()
main()

