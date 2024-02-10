import pygame 
from components import Image, TextParagraph, Button


pygame.init()


from values import RESOLUTION, TITLE, BACKGROUND_COLOR, FONT_PATH, LOGO_PATH


class Game:

    def __init__(self,resolution : tuple, title : str, logo_path : str) -> None:
        self.screen = pygame.display.set_mode(resolution)
        self.logo = pygame.image.load(logo_path)

        pygame.display.set_caption(title)
        pygame.display.set_icon(self.logo)

        self.running = True

        self.lungime_patrat = 200

        self.player_assets = {
            '0' : './assets/0_label.png',
            'x' : './assets/x_label.png'
        }

    def home_screen(self) -> None:

        self.logo = Image(LOGO_PATH,"center-150",self.screen, (400,300))
        self.playText = TextParagraph("Play",FONT_PATH,40,(0,0,0),'center-550',255,self.screen)
        self.playButton = Button((250,60),self.playText,(255,255,255),'center-550',20,self.screen,10)

        self.quit_text = TextParagraph("quit",FONT_PATH,30,(0,0,0),'center-625',255,self.screen)
        self.quit_Button = Button((150,45),self.quit_text,(255,255,255),'center-625',15,self.screen,10)


        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.playButton.mouse_over():
                        self.gameplay_screen()
                    if self.quit_Button.mouse_over():
                        pygame.quit()
                        self.running = False 

            self.screen.fill(BACKGROUND_COLOR)
            self.screen.blit(self.logo.image,self.logo.rect)
            self.playButton.display_button()
            self.quit_Button.display_button()
            

            pygame.display.update()

    def draw_table(self) -> None:
        pygame.draw.line(self.screen,(255,255,255),(1200,200),(1200,800),10)
        pygame.draw.line(self.screen,(255,255,255),(1400,200),(1400,800),10)

        pygame.draw.line(self.screen,(255,255,255),(1000,400),(1600,400),10)
        pygame.draw.line(self.screen,(255,255,255),(1000,600),(1600,600),10)

    def define_table(self,start_x : int, start_y : int) -> None:
            self.table = [
                [(start_x,start_y),(start_x+self.lungime_patrat,start_y),(start_x+self.lungime_patrat*2,start_y)],
                [(start_x,start_y+self.lungime_patrat),(start_x+self.lungime_patrat,start_y+self.lungime_patrat),(start_x+self.lungime_patrat*2,start_y+self.lungime_patrat)],
                [(start_x,start_y+self.lungime_patrat*2),(start_x+self.lungime_patrat,start_y+self.lungime_patrat*2),(start_x+self.lungime_patrat*2,start_y+self.lungime_patrat*2)]
            ]
            self.assets = [
                [None,None,None],
                [None,None,None],
                [None,None,None]
            ]
            self.assets_path = [
                [None,None,None],
                [None,None,None],
                [None,None,None]
            ]

    def check_table(self, player : str) -> None:
        mouse_pos = pygame.mouse.get_pos()
        for line in self.table:
            for element in line:
                if mouse_pos[0] >= element[0] and mouse_pos[0] <= element[0] + self.lungime_patrat:
                    if mouse_pos[1] >= element[1] and mouse_pos[1] <= element[1] + self.lungime_patrat:
                        index_line = self.table.index(line)
                        index_col = line.index(element)
                        if self.assets[index_line][index_col] != None:
                            return False
                        new_image = Image(self.player_assets[player],(element[0],element[1]),self.screen)
                        self.assets[index_line][index_col] = new_image
                        self.assets_path[index_line][index_col] = player
                        return True
        return False
    
    def game_over_check(self) -> None:

        # Liniar cases
        for i in range(len(self.table)):
            if self.assets_path[i][0] == self.assets_path[i][1] == self.assets_path[i][2]:
                return self.assets_path[i][0]
            if self.assets_path[0][i] == self.assets_path[1][i] == self.assets_path[2][i]:
                return self.assets_path[0][i]
        
        # Diagonal cases
        if self.assets_path[0][0] == self.assets_path[1][1] == self.assets_path[2][2]:
            return self.assets_path[0][0]
        if self.assets_path[2][0] == self.assets_path[1][1] == self.assets_path[0][2]:
            return self.assets_path[1][1]


    def draw_table_assets(self) -> None:
        for line in self.assets:
            for image in line:
                if image != None:
                    image.display_image()


    def gameplay_screen(self) -> None:
        
        label_x = self.playText = TextParagraph("x turn",FONT_PATH,100,(0,0,0),'400x300',255,self.screen)
        label_0 = self.playText = TextParagraph("0 turn",FONT_PATH,100,(0,0,0),'400x500',55,self.screen)
        winner = None
        turn_player = 'x'
        self.define_table(1000,200)


        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.check_table(turn_player):
                        winner = self.game_over_check()
                        if turn_player == '0':
                            turn_player = 'x'
                        else:
                            turn_player = '0'


            self.screen.fill(BACKGROUND_COLOR)
            if turn_player == '0':
                label_x.change_opacity(50)
                label_0.change_opacity(255)
            else:
                label_x.change_opacity(255)
                label_0.change_opacity(50)
            label_x.display_text()
            label_0.display_text()
            self.draw_table()
            self.draw_table_assets()
            pygame.display.update()
            if winner != None:
                self.winner_screen(winner)


    def winner_screen(self,winner):

        winner_text = TextParagraph(f"{winner} won the game!", FONT_PATH,80, (255,255,255), 'center-50',255,self.screen)
        playText = TextParagraph("play again",FONT_PATH,20,(0,0,0),'1270x80',255,self.screen)
        playAgainButton = Button((100,30),playText,(255,255,255),'1260x80',20,self.screen,3)

        quitText = TextParagraph("quit",FONT_PATH,15,(0,0,0),'1295x120',255,self.screen)
        quitButton = Button((80,20),quitText,(255,255,255),'1270x120',20,self.screen,3)
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if playAgainButton.mouse_over():
                        self.gameplay_screen()
                    if quitButton.mouse_over():
                        pygame.quit()
                        self.running = False

            winner_text.display_text()
            playAgainButton.display_button()
            quitButton.display_button()
            pygame.display.update()
            

Game(RESOLUTION,TITLE,LOGO_PATH).home_screen()