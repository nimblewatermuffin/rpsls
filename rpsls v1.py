import pygame, sys, random

state = 0

# handles creating/starting the screen & quitting 
class UI:
    
    def __init__(self, target, width, height, title1, title2):
        pygame.init()
        
        # keep track of game state
        self.target = target
        
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = fpsClock = pygame.time.Clock()
        self.title1 = title1
        self.title2 = title2
        self.title = pygame.display.set_caption(title1 + title2)

    def start(self):
        self.screen.fill((0, 0, 0))

    def quit(self):
        pygame.quit()
        sys.exit()

# a class to handle game states
class State:
    
    def __init__(self, state):
        self.state = 0
        self.comp_choice = None
        self.result_color = (255,255,255)
        
        self.sm = 100
        self.lg = 130

        self.rock = "Rock"
        self.paper = "Paper"
        self.scissors = "Scissors"
        self.lizard = "Lizard"
        self.spock = "Spock"

        self.rock_img = pygame.image.load('rock.png')
        self.paper_img = pygame.image.load('paper.png')
        self.scissors_img = pygame.image.load('scissors.png')
        self.lizard_img = pygame.image.load('lizard.png')
        self.spock_img = pygame.image.load('vulcan symbol.png')

        self.small_rock = pygame.transform.scale(self.rock_img, (self.sm, self.sm))
        self.small_paper = pygame.transform.scale(self.paper_img, (self.lg, self.lg))
        self.small_scissors = pygame.transform.scale(self.scissors_img, (self.lg, self.lg))
        self.small_lizard = pygame.transform.scale(self.lizard_img, (self.lg, self.sm))
        self.small_spock = pygame.transform.scale(self.spock_img, (self.sm, self.sm))

        self.rock_pos = [screen.width // 2 - 50, 10]
        self.paper_pos = [100, 150]
        self.scissors_pos = [screen.width - 230, 150]
        self.lizard_pos = [screen.width // 2 - 160, screen.height - 150]
        self.spock_pos = [screen.width // 2 + 80, screen.height - 150]

    # transition to the next game state
    def transition(self, UI):
        if self.state == 0:
            self.comp_result = evaluate.computer_choice()
            screen.target = Playing
        elif self.state == 1:
            screen.target = Evaluating
        else:
            self.comp_result = evaluate.computer_choice()
            screen.target = Start

    def str_to_img(self, string):
        if string == self.rock:
            return self.small_rock
        elif string == self.paper:
            return self.small_paper
        elif string == self.scissors:
            return self.small_scissors
        elif string == self.lizard:
            return self.small_lizard
        elif string == self.spock:
            return self.small_spock

    def num_to_str(self, num):
        if num == 0:
            return self.rock
        elif num == 1:
            return self.spock
        elif num == 2:
            return self.paper
        elif num == 3:
            return self.lizard
        else:
            return self.scissors

    def str_to_num(self, string):
        if string == self.rock:
            return 0
        elif string == self.spock:
            return 1
        elif string == self.paper:
            return 2
        elif string == self.lizard:
            return 3
        else:
            return 4

# the first game state
class Start(State):
    
    def __init__(self, state):
        super().__init__(state)
        self.state = 0
        
    def create_menu(self, window):
        draw_text(window.screen, window.title1, 50, (255, 255, 255),
                  (window.width // 2, window.height // 2 - 50))
        draw_text(window.screen, window.title2, 50, (255, 255, 255),
                  (window.width // 2, window.height // 2))
        draw_text(window.screen, "Click to play", 30, (0,0,255),
                  (window.width // 2, window.height // 2 + 50))

# the second game state
class Playing(State):
    
    def __init__(self, state):
        super().__init__(state)
        self.state = 1
        screen.screen.fill((0,0,0))

    def draw_text(self, screen):
        draw_text(screen.screen, self.rock, 30, (255,255,255),
                  (screen.width // 2, 130))
        draw_text(screen.screen, self.paper, 30, (255,255,255), (155, 300))
        draw_text(screen.screen, self.scissors, 30, (255,255,255),
                  (screen.width - 160, 300))
        draw_text(screen.screen, self.lizard, 30, (255,255,255),
                  (screen.width // 2 - 100, screen.height - 30))
        draw_text(screen.screen, self.spock, 30, (255,255,255),
                  (screen.width // 2 + 130, screen.height - 30))
        draw_text(screen.screen, 'Click an image', 36, (255,255,255),
                  (screen.width // 2, screen.height // 2))

    def draw_image(self, screen):
        screen.screen.blit(self.small_rock, self.rock_pos)
        screen.screen.blit(self.small_paper, self.paper_pos)
        screen.screen.blit(self.small_scissors, self.scissors_pos)
        screen.screen.blit(self.small_lizard, self.lizard_pos)
        screen.screen.blit(self.small_spock, self.spock_pos)

# the final game state
class Evaluating(State):
    
    def __init__(self, state):
        super().__init__(state)
        self.state = 2
        screen.screen.fill((0,0,0))
        self.player_pos = [100, screen.height // 2]
        self.comp_pos = [screen.width - 250, screen.height // 2]
        self.result_pos = [screen.width // 2, 70]
        self.comp_result = self.computer_choice()
        
    def get_result(self, player_choice, comp_choice):
        result = (self.str_to_num(comp_choice) - self.str_to_num(player_choice)) % 5
        if result == 1 or result == 2:
            self.result_color = (255,0,0)
            self.result = "Computer wins"
        elif result == 3 or result == 4:
            self.result_color = (0, 255, 0)
            self.result = "You win"
        elif result == 0:
            self.result_color = (255,255,255)
            self.result = "You tied"

    def computer_choice(self):
        comp_choice = self.num_to_str(random.randrange(5))
        return comp_choice

    def draw_text(self, screen):
        evaluate.computer_choice()
        draw_text(screen.screen, "Player choice:", 30, (255,255,255),
                  (self.player_pos[0] + 70, self.player_pos[1] - 100))
        draw_text(screen.screen, evaluate.clicked_txt, 30, (255,255,255),
                  (self.player_pos[0] + 70, self.player_pos[1] - 50))
        draw_text(screen.screen, "Computer choice:", 30, (255,255,255),
                  (self.comp_pos[0] + 50, self.comp_pos[1] - 100))
        draw_text(screen.screen, self.comp_result, 30, (255,255,255),
                  (self.comp_pos[0] + 50, self.comp_pos[1] - 50))
        draw_text(screen.screen, evaluate.result, 50,
                  evaluate.result_color, self.result_pos)
        draw_text(screen.screen, "Click to play again", 30, (0,0,255),
                  (screen.width // 2, screen.height - 70))

    def draw_image(self, screen):
        screen.screen.blit(evaluate.clicked_img, self.player_pos)
        screen.screen.blit(evaluate.str_to_img(self.comp_result),
                           self.comp_pos)

"""def make_blinking_text(screen, text, size, color, location):
    if pygame.font:
        font = pygame.font.Font(None, size)
        text = font.render(text, 1, color)
        blink_rect = text.get_rect()
        if milliseconds % 2000 == 0:
            text = font.render(text, 1, (0,0,0))
        else:
            text = font.render(text, 1, color)"""

def draw_text(screen, text, size, color, location):
    if pygame.font:
        font = pygame.font.Font(None, size)
        text = font.render(text, 1, color)
        textpos = text.get_rect()
        textpos.centerx = location[0]
        textpos.centery = location[1]
        screen.blit(text, textpos)

def main_loop(screen):
    run = True
    while run:
        screen.start()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if screen.target == Start:
                menu.create_menu(screen)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu.transition(screen)
                    
            elif screen.target == Playing:
                in_play.draw_image(screen)
                in_play.draw_text(screen)
                pygame.display.update()

                # calculate which image the player clicked on & keep track of it
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if in_play.rock_pos[0] <= pos[0] <= in_play.rock_pos[0] + in_play.sm and in_play.rock_pos[1] <= pos[1] <= in_play.rock_pos[1] + in_play.sm:
                        evaluate.clicked_img = evaluate.small_rock
                        evaluate.clicked_txt = evaluate.rock
                    elif in_play.paper_pos[0] <= pos[0] <= in_play.paper_pos[0] + in_play.lg and in_play.paper_pos[1] <= pos[1] <= in_play.paper_pos[1] + in_play.lg:
                        evaluate.clicked_img = evaluate.small_paper
                        evaluate.clicked_txt = evaluate.paper
                    elif in_play.scissors_pos[0] <= pos[0] <= in_play.scissors_pos[0] + in_play.lg and in_play.scissors_pos[1] <= pos[1] <= in_play.scissors_pos[1] + in_play.lg:
                        evaluate.clicked_img = evaluate.small_scissors
                        evaluate.clicked_txt = evaluate.scissors
                    elif in_play.lizard_pos[0] <= pos[0] <= in_play.lizard_pos[0] + in_play.lg and in_play.lizard_pos[1] <= pos[1] <= in_play.lizard_pos[1] + in_play.sm:
                        evaluate.clicked_img = evaluate.small_lizard
                        evaluate.clicked_txt = evaluate.lizard
                    elif in_play.spock_pos[0] <= pos[0] <= in_play.spock_pos[0] + in_play.sm and in_play.spock_pos[1] <= pos[1] <= in_play.spock_pos[1] + in_play.sm:
                        evaluate.clicked_img = evaluate.small_spock
                        evaluate.clicked_txt = evaluate.spock
                    in_play.transition(screen)

            elif screen.target == Evaluating:
                # calculate who won & display appropriately
                evaluate.get_result(evaluate.clicked_txt, evaluate.comp_result)
                evaluate.draw_image(screen)
                evaluate.draw_text(screen)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    evaluate.transition(screen)
    screen.quit()

screen = UI(Start, 700, 500, "Rock, Paper, Scissors, ", "Lizard, Spock")
menu = Start(state)
in_play = Playing(state)
evaluate = Evaluating(state)

main_loop(screen)
