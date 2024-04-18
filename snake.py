import pygame

class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[100, 50]]
        self.radius = 10
        self.dx = 10
        self.dy = 0
        self.score = 0
        self.screen_width = 0
        self.screen_height = 0
        self.screen = None
        self.purple = (128, 0, 128)


    def set_hight_and_width(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def set_screen(self, screen):
        self.screen = screen

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(self.screen, self.purple, element, self.radius)

    def move(self):
        if self.size > 1:
            for i in range(self.size - 1, 0, -1):
                self.elements[i] = list(self.elements[i - 1])

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

    def add_element(self):
        self.size += 1
        self.elements.append([0, 0])

    def collision_with_food(self, food_pos):
        return self.elements[0] == food_pos

    def collision_with_boundaries(self):
        return (
            self.elements[0][0] >= self.screen_width
            or self.elements[0][0] < 0
            or self.elements[0][1] >= self.screen_height
            or self.elements[0][1] < 0
        )

    def collision_with_self(self):
        return any(
            self.elements[0] == element and index != 0
            for index, element in enumerate(self.elements)
        )
    
    def get_score(self):
        return self.size - 1