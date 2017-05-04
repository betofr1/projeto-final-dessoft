import pygame
import tabuleiro
def main():
    
    
    TILESIZE = 20
    MAPWIDTH = len(tabuleiro.TAB[0])
    MAPHEIGHT = len(tabuleiro.TAB)
    pygame.init()
    tela = pygame.display.set_mode([MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE])
    tela2 = pygame.Surface((TILESIZE*5,TILESIZE*30))
    tela3 = pygame.Surface((TILESIZE*4,TILESIZE*24))
    tela4 = pygame.Surface((TILESIZE*5,TILESIZE*8))
    pygame.display.set_caption("LABIRINTO DOS INFERNO")
    relogio = pygame.time.Clock()
    BRANCO = (255,255,255)
    AZUL = (0,0,255)
    PRETO = (0,0,0)
    VERMELHO = (255,0,0)
    VERDE = (0,255,0)
    ROSA = (214,34,191)
    jogador = pygame.Rect(0,0,TILESIZE,TILESIZE)
    monstro = pygame.Rect(16*TILESIZE,15*TILESIZE,TILESIZE,TILESIZE)
    lanterna_pos = pygame.Rect(7*TILESIZE,3*TILESIZE,TILESIZE,TILESIZE)
    arma_pos = pygame.Rect(11*TILESIZE,11*TILESIZE,TILESIZE,TILESIZE)
    mi = 15
    mj = 16
    pi = 0
    pj = 0
    LUZ1 = pygame.Surface((TILESIZE*3,TILESIZE*7))
    LUZ2 = pygame.Surface((TILESIZE*7,TILESIZE*3))
    LUZ3 = pygame.Surface((TILESIZE*5,TILESIZE*5))
    LUZ1.fill(BRANCO)
    LUZ2.fill(BRANCO)
    LUZ3.fill(BRANCO)
    
    Fullscreen = False
    sair = False
    lanterna = False
    arma = False
    
    

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
                if event.key == pygame.K_DOWN:
                    if (pi < (MAPHEIGHT - 1)) and (tabuleiro.TAB[pi+1][pj] != 1):
                        jogador.move_ip(0,TILESIZE)
                        pi += 1
                if event.key == pygame.K_RIGHT:
                    if pj < (MAPWIDTH - 1) and (tabuleiro.TAB[pi][pj+1] != 1):
                        jogador.move_ip(TILESIZE,0)
                        pj += 1
                if event.key == pygame.K_UP:
                    if pi > 0 and (tabuleiro.TAB[pi-1][pj] != 1):
                        jogador.move_ip(0,-TILESIZE)
                        pi -= 1
                if event.key == pygame.K_LEFT:
                    if pj > 0 and (tabuleiro.TAB[pi][pj-1] != 1):
                        jogador.move_ip(-TILESIZE,0)
                        pj -= 1

        if pi == mi and pj == mj:
            break
        
        relogio.tick(30)
        
        tela.fill(PRETO)
        tela2.fill(BRANCO)
        tela3.fill(BRANCO)
        tela4.fill(BRANCO)
        tela.blit(tela2,[0,0])
        tela.blit(tela3,[5*TILESIZE,0])
        tela.blit(tela4,[9*TILESIZE,0])
        
        
        if pi == 3 and pj == 7:
            
            lanterna = True
            
        if lanterna == True: 
            
            tela.blit(LUZ1,[(pj-1)*TILESIZE,(pi-3)*TILESIZE])
            tela.blit(LUZ2,[(pj-3)*TILESIZE,(pi-1)*TILESIZE])
            tela.blit(LUZ3,[(pj-2)*TILESIZE,(pi-2)*TILESIZE])
        
        if lanterna == False: 
            
            pygame.draw.rect(tela,AZUL,lanterna_pos)
            
            
        for coluna in range(MAPWIDTH):
            for linha in range(MAPHEIGHT):
                if tabuleiro.TAB[linha][coluna] == 1:
                    PAREDE = pygame.Rect(coluna*TILESIZE,linha*TILESIZE,TILESIZE,TILESIZE)
                    pygame.draw.rect(tela,PRETO,PAREDE)
        pygame.draw.rect(tela,ROSA,jogador)
        
        
        if pi == 11 and pj == 11: 
            
            arma = True
                
        if arma == False: 
             pygame.draw.rect(tela,VERDE,arma_pos)
            
        pygame.draw.rect(tela,VERMELHO,monstro)
        
        
        
        pygame.display.update()
    pygame.quit()
main()

