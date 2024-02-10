import pygame

class Image:
    def __init__(self, image_path : str, position : str, surface : tuple, size = None) -> None:
        
        self.path = image_path
        self.image = pygame.image.load(image_path)
        self.rect = (0,0)
        self.surface = surface
        self.change_size(size)
        self.get_position(position)

    def get_position(self,position) -> None:

        width, height = self.image.get_size()
        surface = self.surface.get_size()

        if position == "center":
            self.rect = (surface[0] // 2 - width // 2, surface[1] // 2 - height // 2)
        elif position == "right-up-corner":
            self.rect = (0,0)
        elif position == "right-bottom-corner":
            self.rect = (0, surface[1] - height)
        elif position == "left-up-corner":
            self.rect = (surface[0] - width, 0)
        elif position == "left-bottom-corner":
            self.rect = (surface[0] - width, surface[1] - height)
        elif type(position) == tuple:
            self.rect = (position[0],position[1])
        else:
            position = position.split('-')
            if position[0] == "center":
                self.rect = (surface[0] // 2 - width // 2, int(position[1]))
            if position[1] == "center":
                self.rect = (int(position[0]), surface[1] // 2 - height // 2)


    def change_size(self,size):
        if size != None:
            self.image = pygame.transform.scale(self.image, size)

    def display_image(self):
        self.surface.blit(self.image,self.rect)


class TextParagraph:
    def __init__(self, text : str, font_family : str, size : tuple, color : tuple, position : tuple, opacity : int, surface : object) -> None:
        
        self.surface = surface
        
        self.font = pygame.font.Font(font_family,size)
        self.text_label = self.font.render(text,True,color)
        self.text_label.set_alpha(opacity)
        self.rect = (0,0)
        
        self.get_position(position,surface)

    def change_opacity(self,opacity):
        self.text_label.set_alpha(opacity)

    def get_position(self,position,surface) -> None:

        width, height = self.text_label.get_size()
        surface = surface.get_size()

        if position == "center":
            self.rect = (surface[0] // 2 - width // 2, surface[1] // 2 - height // 2)
        elif position == "right-up-corner":
            self.rect = (0,0)
        elif position == "right-bottom-corner":
            self.rect = (0, surface[1] - height)
        elif position == "left-up-corner":
            self.rect = (surface[0] - width, 0)
        elif position == "left-bottom-corner":
            self.rect = (surface[0] - width, surface[1] - height)
        elif len(position.split('x')) == 2:
            self.rect = (int(position.split('x')[0]), int(position.split('x')[1]))
        else:
            position = position.split('-')
            if position[0] == "center":
                self.rect = (surface[0] // 2 - width // 2, int(position[1]))
            if position[1] == "center":
                self.rect = (int(position[0]), surface[1] // 2 - height // 2)



    def display_text(self):
        self.surface.blit(self.text_label,self.rect)
"""
center
right-up-corner
right-bottom-corner
left-up-corner
left-bottom-corner

custom ("x,y")

center-height
width-center
"""

class Button:
    def __init__(self, 
                 size : tuple, text : object, color : tuple, position : str, 
                 border_radius : int, surface : object, 
                 width = 0, color_width = (0,0,0)):
        
        self.text = text
        self.surface = surface
        self.color = color
        self.border_radius = border_radius
        self.width = width
        self.color_width = color_width

        self.get_position(position,surface,size)
        self.display_button()

    def get_position(self,position,surface,size) -> None:

        width, height = size
        surface = surface.get_size()

        if position == "center":
            self.rect = (surface[0] // 2 - width // 2, surface[1] // 2 - height // 2)
        elif position == "right-up-corner":
            self.rect = (0,0)
        elif position == "right-bottom-corner":
            self.rect = (0, surface[1] - height)
        elif position == "left-up-corner":
            self.rect = (surface[0] - width, 0)
        elif position == "left-bottom-corner":
            self.rect = (surface[0] - width, surface[1] - height)
        elif 'x' in position:
            position = position.split('x')
            self.rect = (int(position[0]), int(position[1]))
        else:
            position = position.split('-')
            if position[0] == "center":
                self.rect = (surface[0] // 2 - width // 2, int(position[1]))
            if position[1] == "center":
                self.rect = (int(position[0]), surface[1] // 2 - height // 2)
        self.rect = self.rect + size
        print(self.rect)
        if self.width:
            self.width_border_rect = (self.rect[0] - (self.width//2), self.rect[1] - (self.width//2), size[0] + self.width, size[1] + self.width) 
            print(self.width_border_rect)

    
    def display_button(self):
        if self.width:
            pygame.draw.rect(self.surface,self.color_width,self.width_border_rect,0,self.border_radius+5)
        pygame.draw.rect(self.surface,self.color,self.rect,0,self.border_radius)
        self.text.display_text()

    def mouse_over(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] >= self.rect[0] and mouse_pos[0] <= self.rect[0] + self.rect[2]:
            if mouse_pos[1] >= self.rect[1] and  mouse_pos[1] <= self.rect[1] + self.rect[3]:
                return True 
        return False