"""
This script is a Pygame-based game where the player controls a dinosaur character
navigating through a series of obstacles. Pygame is a set of Python modules
designed for writing video games, providing functionalities for creating graphics,
sound, and handling user input.

Key Components:
1. Initialization: Pygame is initialized using `pygame.init()`, preparing the
   framework for use.

2. Game Settings: Global variables like `game_speed`, `x_pos_bg`, `y_pos_bg`,
   and `points` are defined for tracking game dynamics and scoring.

3. Main Game Loop: The `main` function contains the core game loop. This loop
   continuously checks for events (like key presses or the window closing),
   updates game state, and redraws the screen.

    a. Event Handling: Pygame's event system is used to respond to key presses
       and window closing events.
    b. Graphics Rendering: Game entities like the dinosaur, clouds, and obstacles
       are drawn onto the game window (`SCREEN`). Pygame functions like `blit`
       are used for drawing.
    c. Collision Detection: Pygame's rectangle collision feature is used to
       detect collisions between the dinosaur and obstacles.
    d. Scoring: Points are incremented based on game progress.

4. Game Pause and Unpause: Functions `paused` and `unpause` manage the game's
   pause state. During a pause, the game loop halts its usual update and draw
   cycle.

5. Background Management: The `background` function handles the scrolling
   background effect, giving a sense of movement.

6. Obstacle Management: Obstacles are dynamically generated and managed,
   offering variety and challenge in the gameplay.

7. Menu System: The `menu` function provides a start/restart interface and
   displays the player's score. It's also responsible for initiating the main
   game loop.

Pygame Functions:
- `pygame.init()`: Initializes all imported Pygame modules.
- `pygame.time.Clock()`: Creates an object to help track time.
- `clock.tick(fps)`: Limits the game loop to a maximum framerate.
- `pygame.display.update()`: Updates the contents of the entire display.
- `pygame.key.get_pressed()`: Gets the state of all keyboard buttons.
- `pygame.event.get()`: Retrieves all events from the event queue.
- `pygame.quit()`: Uninitializes all Pygame modules.
- `SCREEN.blit()`: Draws one image onto another.

This game is a simple yet engaging implementation demonstrating various aspects
of game development using Pygame, including graphics rendering, event handling,
collision detection, and game state management.
"""


from resources import RUNNING
import datetime
import pygame
import pygame_textinput
import random
import threading
from settings import SCREEN_WIDTH, SCREEN, SCREEN_HEIGHT, GAME_SPEED
from dinosaur import Dinosaur
from cloud import Cloud
from obstacles import SmallCactus, LargeCactus, Bird, Meteor, Powerup_red, Powerup_yellow, Powerup_purple, Powerup_turquoise, Powerup_green
from resources import BG, SMALL_CACTUS, LARGE_CACTUS, BIRD, METEOR, POWERUPS, TROPHY

# Initialize Pygame
pygame.init()

# List to store obstacles
obstacles = []

#game modes
multiplayer_mode = False
coop_mode = False
#mission mode
first_mission = False
second_mission = False
third_mission = False
fourth_mission = False
fifth_mission = False
#missionentitel bei congrats feld
m_one = False
m_two = False
m_three = False
m_four = False
m_five = False
#powerups
double_points_p_one = False
double_points_p_two = False
double_coins = False
unbreakable = False
double_speed = False
slower_speed = False
POWER_UP_TIME = 5000 #5 seconds
power_up_timer = 0
#coop mode revive option
REVIVE_TIME = 10000 #10 seconds
revive_timer = 0
revive_one = False
revive_two = False


#---normaler highscore---
def load_highscore():
    with open('highscore.txt', 'r') as f:
        content = f.read()
        return int(content)

def save_highscore(points):
    with open("highscore.txt", "w") as f:
        f.write(str(points))

#---name speichern---
def load_highscore_name():
    with open('highscore_name.txt', 'r') as f:
        loadname = f.read()
        return str(loadname)

def save_highscore_name(name):
    with open("highscore_name.txt", "w") as f:
        f.write(str(name))

#---Missionen speichern wegen Achievements---
def first_mission_done(mission_one):
    with open("first_mission.txt", "w") as f:
        f.write(str(mission_one))

def load_first_mission():
    with open('first_mission.txt', 'r') as f:
        content = f.read()
        return str(content)

def second_mission_done(mission_two):
    with open("second_mission.txt", "w") as f:
        f.write(mission_two)

def load_second_mission():
    with open('second_mission.txt', 'r') as f:
        content = f.read()
        return str(content)

def third_mission_done(mission_three):
    with open("third_mission.txt", "w") as f:
        f.write(mission_three)

def load_third_mission():
    with open('third_mission.txt', 'r') as f:
        content = f.read()
        return str(content)

def fourth_mission_done(mission_four):
    with open("fourth_mission.txt", "w") as f:
        f.write(mission_four)

def load_fourth_mission():
    with open('fourth_mission.txt', 'r') as f:
        content = f.read()
        return str(content)

def fifth_mission_done(mission_five):
    with open("fifth_mission.txt", "w") as f:
        f.write(mission_five)

def load_fifth_mission():
    with open('fifth_mission.txt', 'r') as f:
        content = f.read()
        return str(content)

#---Hauptmenü---
def main_menu():
    run = True
    selected = 0
    while run:
        SCREEN.fill((130, 128, 200))
        font = pygame.font.Font("freesansbold.ttf", 30)
        title = font.render("Dinosaur Game", True, FONT_COLOR)
        # Options text
        if selected == 0:
            start_game = font.render("Start Game <-", True, FONT_COLOR)
            trophies = font.render("Trophies", True, FONT_COLOR)
            shop_b = font.render("Shop", True, FONT_COLOR)
            ranking = font.render("Ranking", True, FONT_COLOR)
            m_settings = font.render("Settings", True, FONT_COLOR)
            quit_game = font.render("Quit", True, FONT_COLOR)
        elif selected == 1:
            start_game = font.render("Start Game ", True, FONT_COLOR)
            trophies = font.render("Trophies <- ", True, FONT_COLOR)
            shop_b = font.render("Shop", True, FONT_COLOR)
            ranking = font.render("Ranking", True, FONT_COLOR)
            m_settings = font.render("Settings", True, FONT_COLOR)
            quit_game = font.render("Quit", True, FONT_COLOR)
        elif selected == 2:
            start_game = font.render("Start Game", True, FONT_COLOR)
            trophies = font.render("Trophies", True, FONT_COLOR)
            shop_b = font.render("Shop <-", True, FONT_COLOR)
            ranking = font.render("Ranking", True, FONT_COLOR)
            m_settings = font.render("Settings", True, FONT_COLOR)
            quit_game = font.render("Quit", True, FONT_COLOR)
        elif selected == 3:
            start_game = font.render("Start Game", True, FONT_COLOR)
            trophies = font.render("Trophies", True, FONT_COLOR)
            shop_b = font.render("Shop", True, FONT_COLOR)
            ranking = font.render("Ranking <-", True, FONT_COLOR)
            m_settings = font.render("Settings", True, FONT_COLOR)
            quit_game = font.render("Quit", True, FONT_COLOR)
        elif selected == 4:
            start_game = font.render("Start Game ", True, FONT_COLOR)
            trophies = font.render("Trophies", True, FONT_COLOR)
            shop_b = font.render("Shop", True, FONT_COLOR)
            ranking = font.render("Ranking", True, FONT_COLOR)
            m_settings = font.render("Settings <-", True, FONT_COLOR)
            quit_game = font.render("Quit", True, FONT_COLOR)
        elif selected == 5:
            start_game = font.render("Start Game", True, FONT_COLOR)
            trophies = font.render("Trophies", True, FONT_COLOR)
            shop_b = font.render("Shop", True, FONT_COLOR)
            ranking = font.render("Ranking", True, FONT_COLOR)
            m_settings = font.render("Settings", True, FONT_COLOR)
            quit_game = font.render("Quit <-", True, FONT_COLOR)

        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 10))
        start_game_rect = start_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        trophies_rect = trophies.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        shop_button_rect = shop_b.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.4))
        ranking_rect = ranking.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        m_settings_rect = m_settings.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.7))
        quit_game_rect = quit_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))

        SCREEN.blit(title, title_rect)
        SCREEN.blit(start_game, start_game_rect)
        SCREEN.blit(trophies, trophies_rect)
        SCREEN.blit(shop_b, shop_button_rect)
        SCREEN.blit(ranking, ranking_rect)
        SCREEN.blit(m_settings, m_settings_rect)
        SCREEN.blit(quit_game, quit_game_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 6
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % 6
                elif event.key == pygame.K_RETURN:
                    if selected == 0:  # start game
                        run = False
                        choose_game_mode()
                    elif selected == 1:  # missionen
                        run = False
                        trophy()
                    elif selected == 2:  # shop
                        run = False
                        shop()
                    elif selected == 3:  # ranking
                        run = False
                        trophy()
                    elif selected == 4:  # settings
                        run = False
                        menu_settings()
                    elif selected == 5:  # quit game
                        pygame.quit()
                        quit()

#---Game Mode Auswahl---
def choose_game_mode():
    run = True
    selected = 0
    global multiplayer_mode, coop_mode
    while run:
        SCREEN.fill((130, 128, 200))
        font = pygame.font.Font("freesansbold.ttf", 30)
        title = font.render("Choose Game Mode", True, FONT_COLOR)
        if selected == 0:
            start_game = font.render("Normal Game Mode <-", True, FONT_COLOR)
            mission_start = font.render("Mission Mode", True, FONT_COLOR)
            multiplayer = font.render("Multiplayer Mode: Competition", True, FONT_COLOR)
            coop = font.render("Multiplayer Mode: Coop", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
            quit_game = font.render("Quit", True, FONT_COLOR)
            multiplayer_mode = False
            coop_mode = False
        elif selected == 1:
            start_game = font.render("Normal Game Mode", True, FONT_COLOR)
            mission_start = font.render("Mission Mode <-", True, FONT_COLOR)
            multiplayer = font.render("Multiplayer Mode: Competition", True, FONT_COLOR)
            coop = font.render("Multiplayer Mode: Coop", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
            quit_game = font.render("Quit", True, FONT_COLOR)
            multiplayer_mode = False
            coop_mode = False
        elif selected == 2:
            start_game = font.render("Normal Game Mode", True, FONT_COLOR)
            mission_start = font.render("Mission Mode", True, FONT_COLOR)
            multiplayer = font.render("Multiplayer Mode: Competition <-", True, FONT_COLOR)
            coop = font.render("Multiplayer Mode: Coop", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
            quit_game = font.render("Quit", True, FONT_COLOR)
            multiplayer_mode = True
            coop_mode = False
        elif selected == 3:
            start_game = font.render("Normal Game Mode", True, FONT_COLOR)
            mission_start = font.render("Mission Mode", True, FONT_COLOR)
            multiplayer = font.render("Multiplayer Mode: Competition", True, FONT_COLOR)
            coop = font.render("Multiplayer Mode: Coop <-", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
            quit_game = font.render("Quit", True, FONT_COLOR)
            multiplayer_mode = False
            coop_mode = True
        elif selected == 4:
            start_game = font.render("Normal Game Mode", True, FONT_COLOR)
            mission_start = font.render("Mission Mode", True, FONT_COLOR)
            multiplayer = font.render("Multiplayer Mode: Competition", True, FONT_COLOR)
            coop = font.render("Multiplayer Mode: Coop", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu <-", True, FONT_COLOR)
            quit_game = font.render("Quit", True, FONT_COLOR)
            multiplayer_mode = False
            coop_mode = False
        elif selected == 5:
            start_game = font.render("Normal Game Mode", True, FONT_COLOR)
            mission_start = font.render("Mission Mode", True, FONT_COLOR)
            multiplayer = font.render("Multiplayer Mode: Competition", True, FONT_COLOR)
            coop = font.render("Multiplayer Mode: Coop", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
            quit_game = font.render("Quit <-", True, FONT_COLOR)
            multiplayer_mode = False
            coop_mode = False

        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 10))
        start_game_rect = start_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        mission_start_rect = mission_start.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        multiplayer_rect = multiplayer.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.4))
        coop_rect = coop.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        back_to_menu_rect = back_to_menu.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.7))
        quit_game_rect = quit_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))

        SCREEN.blit(title, title_rect)
        SCREEN.blit(start_game, start_game_rect)
        SCREEN.blit(mission_start, mission_start_rect)
        SCREEN.blit(multiplayer, multiplayer_rect)
        SCREEN.blit(coop, coop_rect)
        SCREEN.blit(back_to_menu, back_to_menu_rect)
        SCREEN.blit(quit_game, quit_game_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 6
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % 6
                elif event.key == pygame.K_RETURN:
                    if selected == 0:  # start normal game
                        run = False
                        main()
                    elif selected == 1:  # missionen
                        run = False
                        mission()
                    elif selected == 2:  # multiplayer competition mode
                        run = False
                        main()
                    elif selected == 3:  # multiplayer coop mode
                        run = False
                        coop_mode = True
                        main()
                    elif selected == 4:  # back to menu
                        run = False
                        main_menu()
                    elif selected == 5:  # quit game
                        pygame.quit()
                        quit()

def mission():
    global first_mission, second_mission, third_mission, fourth_mission, fifth_mission
    run = True
    selected = 0
    while run:
        SCREEN.fill((130, 128, 200))
        font = pygame.font.Font("freesansbold.ttf", 30)
        mission_title = font.render("Missions", True, FONT_COLOR)

        if selected == 0:  #mission 1
            mission1 = font.render("Mission 1: Jump over 10 Cactuses <-", True, FONT_COLOR)
            mission2 = font.render("Mission 2: Survive 15 Obstacles", True, FONT_COLOR)
            mission3 = font.render("Mission 3: Reach 500 Points", True, FONT_COLOR)
            mission4 = font.render("Mission 4: Reach 1000 Points", True, FONT_COLOR)
            mission5 = font.render("Mission 5: Master The Troll Mode", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
            first_mission = True
            second_mission = False
            third_mission = False
            fourth_mission = False
            fifth_mission = False
        elif selected == 1:  #mission 2
            mission1 = font.render("Mission 1: Jump over 10 Cactuses", True, FONT_COLOR)
            mission2 = font.render("Mission 2: Survive 15 Obstacles <-", True, FONT_COLOR)
            mission3 = font.render("Mission 3: Reach 500 Points", True, FONT_COLOR)
            mission4 = font.render("Mission 4: Reach 1000 Points", True, FONT_COLOR)
            mission5 = font.render("Mission 5: Master The Troll Mode", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
            first_mission = False
            second_mission = True
            third_mission = False
            fourth_mission = False
            fifth_mission = False
        elif selected == 2:  #mission 3
            mission1 = font.render("Mission 1: Jump over 10 Cactuses", True, FONT_COLOR)
            mission2 = font.render("Mission 2: Survive 15 Obstacles", True, FONT_COLOR)
            mission3 = font.render("Mission 3: Reach 500 Points <-", True, FONT_COLOR)
            mission4 = font.render("Mission 4: Reach 1000 Points", True, FONT_COLOR)
            mission5 = font.render("Mission 5: Master The Troll Mode", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
            first_mission = False
            second_mission = False
            third_mission = True
            fourth_mission = False
            fifth_mission = False
        elif selected == 3:  #mission 4
            mission1 = font.render("Mission 1: Jump over 10 Cactuses", True, FONT_COLOR)
            mission2 = font.render("Mission 2: Survive 15 Obstacles", True, FONT_COLOR)
            mission3 = font.render("Mission 3: Reach 500 Points ", True, FONT_COLOR)
            mission4 = font.render("Mission 4: Reach 1000 Points <-", True, FONT_COLOR)
            mission5 = font.render("Mission 5: Master The Troll Mode", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
            first_mission = False
            second_mission = False
            third_mission = False
            fourth_mission = True
            fifth_mission = False
        elif selected == 4:  #mission 5 troll mode?
            mission1 = font.render("Mission 1: Jump over 10 Cactuses", True, FONT_COLOR)
            mission2 = font.render("Mission 2: Survive 15 Obstacles", True, FONT_COLOR)
            mission3 = font.render("Mission 3: Reach 500 Points ", True, FONT_COLOR)
            mission4 = font.render("Mission 4: Reach 1000 Points", True, FONT_COLOR)
            mission5 = font.render("Mission 5: Master The Troll Mode <-", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
            first_mission = False
            second_mission = False
            third_mission = False
            fourth_mission = False
            fifth_mission = True
        elif selected == 5:  #back to menu
            mission1 = font.render("Mission 1: Jump over 10 Cactuses", True, FONT_COLOR)
            mission2 = font.render("Mission 2: Survive 15 Obstacles", True, FONT_COLOR)
            mission3 = font.render("Mission 3: Reach 500 Points ", True, FONT_COLOR)
            mission4 = font.render("Mission 4: Reach 1000 Points", True, FONT_COLOR)
            mission5 = font.render("Mission 5: Master The Troll Mode", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu <-", True, FONT_COLOR)

        mission_title_rect = mission_title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6))
        mission1_rect = mission1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3.5))
        mission2_rect = mission2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.6))
        mission3_rect = mission3.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.1))
        mission4_rect = mission4.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.75))
        mission5_rect = mission5.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))
        back_to_menu_rect = back_to_menu.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.3))
        SCREEN.blit(mission_title, mission_title_rect)
        SCREEN.blit(mission1, mission1_rect)
        SCREEN.blit(mission2, mission2_rect)
        SCREEN.blit(mission3, mission3_rect)
        SCREEN.blit(mission4, mission4_rect)
        SCREEN.blit(mission5, mission5_rect)
        SCREEN.blit(back_to_menu, back_to_menu_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 6
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % 6
                elif event.key == pygame.K_RETURN:
                    if selected == 0:  # mission 1
                        run = False
                        main()
                    elif selected == 1:  # mission 2
                        run = False
                        main()
                    elif selected == 2:  # mission 3
                        run = False
                        main()
                    elif selected == 3:  # mission 4
                        run = False
                        main()
                    elif selected == 4:  # mission 5
                        run = False
                        main()
                    elif selected == 5:  # back to menu
                        run = False
                        main_menu()

def main():
    # Global variables for game settings
    global game_speed, x_pos_bg, y_pos_bg, points, points_player2, obstacles, multiplayer_mode, coop_mode, coins, REVIVE_TIME, revive_timer, revive_one, revive_two
    global first_mission, second_mission, third_mission, fourth_mission, fifth_mission, mission_one, mission_two, player_1, player_2
    global m_one, m_two, m_three, m_four, m_five, double_speed, double_points_p_one, double_points_p_two, double_coins, slower_speed, unbreakable, POWER_UP_TIME, power_up_timer

    # Set initial game state
    run = True
    clock = pygame.time.Clock()
    cloud = Cloud()
    obstacles = []
    player = Dinosaur()
    if multiplayer_mode:
        player2 = Dinosaur(True)
    if coop_mode:
        player2 = Dinosaur(True)
    game_speed = GAME_SPEED
    x_pos_bg = 0
    y_pos_bg = 380
    if multiplayer_mode:
        points = -3
    else:
        points = 0
    points_player2 = 0
    mission_one = 0
    mission_two = 0
    coins = 0
    player_1 = 0
    player_2 = 0

    font = pygame.font.Font("freesansbold.ttf", 20)
    death_count = 0
    pause = False


    def score():
        global points, game_speed, coins
        if multiplayer_mode:
            if not player_1 >= 1:
                points += 1
                coins = coins + 0.5
        elif coop_mode:
            if not player_1 >= 1:
                points += 1
                coins = coins + 0.5
        else:
            points += 1
            coins = coins + 0.5
            old_score = load_highscore()
            if old_score > points:
                save_highscore(old_score)
            else:
                save_highscore(points)

    def score_player2():
        global points_player2, game_speed
        if not player_2 >= 1:
            points_player2 += 1

    def enter_name():
        run = True
        font = pygame.font.Font("freesansbold.ttf", 30)
        name = ""
        screen = pygame.display.set_mode((1100, 600))
        pygame.display.update()
        while run:
            screen.fill((130, 128, 200))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_menu()
                if event.type == pygame.K_RETURN:
                    main()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        name += event.unicode
                    if event.key == pygame.K_b:
                        name += event.unicode
                    if event.key == pygame.K_c:
                        name += event.unicode
                    if event.key == pygame.K_d:
                        name += event.unicode
                    if event.key == pygame.K_e:
                        name += event.unicode
                    if event.key == pygame.K_f:
                        name += event.unicode
                    if event.key == pygame.K_g:
                        name += event.unicode
                    if event.key == pygame.K_h:
                        name += event.unicode
                    if event.key == pygame.K_i:
                        name += event.unicode
                    if event.key == pygame.K_j:
                        name += event.unicode
                    if event.key == pygame.K_k:
                        name += event.unicode
                    if event.key == pygame.K_l:
                        name += event.unicode
                    if event.key == pygame.K_m:
                        name += event.unicode
                    if event.key == pygame.K_n:
                        name += event.unicode
                    if event.key == pygame.K_o:
                        name += event.unicode
                    if event.key == pygame.K_p:
                        name += event.unicode
                    if event.key == pygame.K_q:
                        name += event.unicode
                    if event.key == pygame.K_r:
                        name += event.unicode
                    if event.key == pygame.K_s:
                        name += event.unicode
                    if event.key == pygame.K_t:
                        name += event.unicode
                    if event.key == pygame.K_u:
                        name += event.unicode
                    if event.key == pygame.K_v:
                        name += event.unicode
                    if event.key == pygame.K_w:
                        name += event.unicode
                    if event.key == pygame.K_x:
                        name += event.unicode
                    if event.key == pygame.K_y:
                        name += event.unicode
                    if event.key == pygame.K_z:
                        name += event.unicode
                    if event.key == pygame.K_SPACE:
                        name += event.unicode
                    if event.key == pygame.K_BACKSPACE:
                        name = name[0:-1]
                    if event.key == pygame.K_RETURN:
                        run = False

            dino_down = font.render("Dino Down", True, FONT_COLOR)
            get_name = font.render("Please enter your Name:", True, FONT_COLOR)
            got_name = font.render("Press Return when you're done", True, FONT_COLOR)
            dino_down_rect = dino_down.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6))
            get_name_rect = get_name.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            got_name_rect = got_name.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))
            SCREEN.blit(dino_down, dino_down_rect)
            SCREEN.blit(get_name, get_name_rect)
            SCREEN.blit(got_name, got_name_rect)
            name_surface = font.render(name, True, FONT_COLOR)
            SCREEN.blit(name_surface, name_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))

            save_highscore_name(name)  # name speichern für ranking!

            pygame.display.update()

    # Function to handle background movement
    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= game_speed

        font = pygame.font.Font("freesansbold.ttf", 20) #Score Anzeige während des Spiels
        print_score_one = font.render(f"Player 1: {str(points)}", True, FONT_COLOR)
        print_score_one_rect = print_score_one.get_rect(center=(SCREEN_WIDTH // 9, SCREEN_HEIGHT // 3 - 150))
        SCREEN.blit(print_score_one, print_score_one_rect)
        if multiplayer_mode or coop_mode:
            print_score_two = font.render(f"Player 2: {str(points_player2)}", True, FONT_COLOR)
            print_score_two_rect = print_score_two.get_rect(center=(SCREEN_WIDTH // 9, SCREEN_HEIGHT // 3 - 125))
            SCREEN.blit(print_score_two, print_score_two_rect)
        '''print_coins = font.render(str(coins), True, FONT_COLOR)
        print_coins_rect = print_coins.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 170))
        SCREEN.blit(print_coins, print_coins_rect)''' #Testlauf zwecks Doublecoins

    # Function to unpause the game
    def unpause():
        nonlocal pause, run
        pause = False
        run = True

    # Function to pause the game
    def paused():
        nonlocal pause
        pause = True
        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render("Game Paused, Press 'u' to Unpause", True, FONT_COLOR)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
        SCREEN.blit(text, textRect)
        pygame.display.update()

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                    unpause()

    # Main game loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                main_menu()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused()

        #Darkmode
        now = datetime.datetime.now()
        current_time = datetime.time(now.hour, now.minute, now.second)
        day_start = datetime.time(6, 00, 00)
        day_end = datetime.time(22, 00, 00)
        hour_of_time = current_time.hour
        if hour_of_time > day_start.hour and hour_of_time < day_end.hour:
            SCREEN.fill((160, 175, 255))
        else:
            SCREEN.fill((0, 0, 80))

        # Get user input
        userInput = pygame.key.get_pressed()

        # Update and draw cloud, player and both players in multiplayer
        cloud.draw(SCREEN)
        cloud.update()

        if multiplayer_mode or coop_mode:
            if not player_1 >= 1 or not revive_one: #player1 wird nur angezeigt, wenn er noch lebt
                player.draw(SCREEN)
                player.update(userInput)
            if not player_2 >= 1 or not revive_two: #player2 wird nur angezeigt, wenn er noch lebt
                player2.draw(SCREEN)
                player2.update(userInput)
        else: #player1 wird beim normalen game mode immer angezeigt
            player.draw(SCREEN)
            player.update(userInput)

        # Handle obstacles
        if len(obstacles) == 0:
            if random.randint(0, 8) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
                if first_mission:
                    mission_one += 1
                if second_mission:
                    mission_two += 1
            elif random.randint(0, 8) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
                if first_mission:
                    mission_one += 1
                if second_mission:
                    mission_two += 1
            elif random.randint(0, 8) == 2:
                obstacles.append(Bird(BIRD))
                if second_mission:
                    mission_two += 1
            elif random.randint(0, 8) == 3:
                obstacles.append(Meteor(METEOR))
                if second_mission:
                    mission_two += 1
            elif random.randint(0, 8) == 4:
                obstacles.append(Powerup_red(POWERUPS))
            elif random.randint(0, 8) == 5:
                obstacles.append(Powerup_yellow(POWERUPS))
            elif random.randint(0, 8) == 6:
                obstacles.append(Powerup_purple(POWERUPS))
            elif random.randint(0, 8) == 7:
                obstacles.append(Powerup_turquoise(POWERUPS))
            elif random.randint(0, 8) == 8:
                obstacles.append(Powerup_green(POWERUPS))

        #powerups
        if double_speed:
            elapsed_time = pygame.time.get_ticks() - power_up_timer
            if elapsed_time >= POWER_UP_TIME:
                double_speed = False
        if double_speed:
            game_speed = 200
        else:
            game_speed = 30

        if double_points_p_one: #double points für spieler 1
            elapsed_time = pygame.time.get_ticks() - power_up_timer
            if elapsed_time >= POWER_UP_TIME:
                double_points_p_one = False
        if double_points_p_one:
            points = points + 2
        else:
            points = points
        if double_points_p_two: #double points für spieler 2
            elapsed_time = pygame.time.get_ticks() - power_up_timer
            if elapsed_time >= POWER_UP_TIME:
                double_points_p_two = False
        if double_points_p_two:
            points_player2 = points_player2 + 2
        else:
            points_player2 = points_player2
        if unbreakable:
            elapsed_time = pygame.time.get_ticks() - power_up_timer
            if elapsed_time >= POWER_UP_TIME:
                unbreakable = False
        if double_coins:
            elapsed_time = pygame.time.get_ticks() - power_up_timer
            if elapsed_time >= POWER_UP_TIME:
                double_coins = False
        if double_coins:
            coins = coins + 2
        else:
            coins = coins
        if slower_speed:
            elapsed_time = pygame.time.get_ticks() - power_up_timer
            if elapsed_time >= POWER_UP_TIME:
                slower_speed = False
        if slower_speed:
            game_speed = 10
        else:
            game_speed = 30

        if revive_one:
            elapsed_time = pygame.time.get_ticks() - revive_timer
            if elapsed_time >= REVIVE_TIME:
                revive_one = False
        if revive_one:
            player_1 += 1
        else:
            player_1 = 0
        if revive_two:
            elapsed_time = pygame.time.get_ticks() - revive_timer
            if elapsed_time >= REVIVE_TIME:
                revive_two = False
        if revive_two:
            player_2 += 1
        else:
            player_2 = 0

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(obstacles)
            if multiplayer_mode or coop_mode:
                if player.dino_rect.colliderect(obstacle.rect) and obstacle.__class__.__name__ == "Powerup_red":
                    obstacles.remove(obstacle)  # powerup verschwindet
                    double_points_p_one = True
                    power_up_timer = pygame.time.get_ticks()
                elif player.dino_rect.colliderect(obstacle.rect) and obstacle.__class__.__name__ == "Powerup_yellow":
                    obstacles.remove(obstacle)
                    double_speed = True
                    power_up_timer = pygame.time.get_ticks()
                elif player.dino_rect.colliderect(obstacle.rect) and obstacle.__class__.__name__ == "Powerup_purple":
                    obstacles.remove(obstacle)
                    double_coins = True
                    power_up_timer = pygame.time.get_ticks()
                elif player.dino_rect.colliderect(obstacle.rect) and obstacle.__class__.__name__ == "Powerup_turquoise":
                    obstacles.remove(obstacle)
                    unbreakable = True
                    power_up_timer = pygame.time.get_ticks()
                elif player.dino_rect.colliderect(obstacle.rect) and obstacle.__class__.__name__ == "Powerup_green":
                    obstacles.remove(obstacle)
                    slower_speed = True
                    power_up_timer = pygame.time.get_ticks()
                elif player2.dino_rect.colliderect(obstacle.rect) and obstacle.__class__.__name__ == "Powerup_red":
                    obstacles.remove(obstacle)
                    double_speed = True
                    power_up_timer = pygame.time.get_ticks()
                elif player2.dino_rect.colliderect(obstacle.rect) and obstacle.__class__.__name__ == "Powerup_yellow":
                    obstacles.remove(obstacle)
                    double_points_p_two = True
                    power_up_timer = pygame.time.get_ticks()
                elif player2.dino_rect.colliderect(obstacle.rect) and obstacle.__class__.__name__ == "Powerup_purple":
                    obstacles.remove(obstacle)
                    double_coins = True
                    power_up_timer = pygame.time.get_ticks()
                elif player2.dino_rect.colliderect(obstacle.rect) and obstacle.__class__.__name__ == "Powerup_turquoise":
                    obstacles.remove(obstacle)
                    unbreakable = True
                    power_up_timer = pygame.time.get_ticks()
                elif player2.dino_rect.colliderect(obstacle.rect) and obstacle.__class__.__name__ == "Powerup_green":
                    obstacles.remove(obstacle)
                    slower_speed = True
                    power_up_timer = pygame.time.get_ticks()
                elif player.dino_rect.colliderect(obstacle.rect) and not unbreakable:  #wenn unbreakable = True kann der Dino nicht sterben
                    if coop_mode:
                        revive_timer = pygame.time.get_ticks()
                        revive_one = True
                    else:
                        player_1 += 1  # erhöht den counter, wenn die Variable gleich 1 ist, wird der dino nicht mehr angezeigt

                elif player2.dino_rect.colliderect(obstacle.rect) and not unbreakable: #wenn unbreakable = True kann der Dino nicht sterben
                    if coop_mode:
                        revive_timer = pygame.time.get_ticks()
                        revive_two = True
                    else:
                        player_2 += 1

                elif player_1 >= 1 and player_2 >= 1:
                    revive_one = False
                    revive_two = False
                    death_count += 1 #ende wenn beide gestorben sind
                    menu(death_count)

            else:  # normaler game mode
                if player.dino_rect.colliderect(obstacle.rect) and obstacle.__class__.__name__ == "Powerup_red":
                    obstacles.remove(obstacle)  # powerup verschwindet
                    double_speed = True
                    power_up_timer = pygame.time.get_ticks()
                elif player.dino_rect.colliderect(obstacle.rect) and obstacle.__class__.__name__ == "Powerup_yellow":
                    obstacles.remove(obstacle)
                    double_points_p_one = True
                    power_up_timer = pygame.time.get_ticks()
                elif player.dino_rect.colliderect(obstacle.rect) and obstacle.__class__.__name__ == "Powerup_purple":
                    obstacles.remove(obstacle)
                    double_coins = True
                    power_up_timer = pygame.time.get_ticks()
                elif player.dino_rect.colliderect(obstacle.rect) and obstacle.__class__.__name__ == "Powerup_turquoise":
                    obstacles.remove(obstacle)
                    unbreakable = True
                    power_up_timer = pygame.time.get_ticks()
                elif player.dino_rect.colliderect(obstacle.rect) and obstacle.__class__.__name__ == "Powerup_green":
                    obstacles.remove(obstacle)
                    slower_speed = True
                    power_up_timer = pygame.time.get_ticks()
                elif player.dino_rect.colliderect(obstacle.rect) and not unbreakable:  # normales Obstacle
                    pygame.time.delay(2000)
                    enter_name()  # name eingeben bei singleplayer
                    death_count += 1
                    menu(death_count)

#Missionen erfolgreich beendet:
            if first_mission:
                if mission_one == 11:  # mission beenden
                    first_mission_done("First Mission Done")
                    m_one = True
                    congrats1()
            if second_mission:
                if mission_two == 16:
                    second_mission_done("Second Mission Done")
                    m_two = True
                    congrats1()
            if third_mission:
                if points == 500:
                    third_mission_done("Third Mission Done")
                    m_three = True
                    congrats1()
            if fourth_mission:
                if points == 1000:
                    fourth_mission_done("Fourth Mission Done")
                    m_four = True
                    congrats1()
            if fifth_mission:
                if points == 30000:
                    fifth_mission_done("Fifth Mission Done")
                    m_five = True
                    congrats1()

        # Update background and score
        background()
        score()
        score_player2()

        # Update display and tick clock
        clock.tick(30)
        pygame.display.update()

def menu(death_count):
    global points  # Access the global points variable to display the score.
    global FONT_COLOR  # Access the global font color variable for consistent text color.
    global name
    run = True  # Flag to keep the menu loop running.

    while run:
        FONT_COLOR = (255, 255, 255)  # Set the font color to white for visibility.
        SCREEN.fill((130, 128, 200))  # Fill the screen
        pygame.font.init()  # Initialize Pygame font module.
        font = pygame.font.Font("freesansbold.ttf", 30)  # Set the font and size for the text.

        # Check if it's the start of the game or a restart after death.
        if death_count == 0:
            main_menu()
            run = True
            while run:
                pygame.display.update()

        elif death_count > 0:
            # Display a message to restart the game and the last score.
            if multiplayer_mode: #death menu competition
                score = font.render(f"Score by Player 1: {str(points)} ", True, FONT_COLOR)
                score2 = font.render(f"Score by Player 2: {str(points_player2)} ", True, FONT_COLOR)
                if points > points_player2:
                    higherscore = font.render(f"Player 1 is the Winner", True, FONT_COLOR)
                elif points_player2 > points:
                    higherscore = font.render(f"Player 2 is the Winner", True, FONT_COLOR)
                else:
                    higherscore = font.render(f"Both Players have won", True, FONT_COLOR)

                score_rect = score.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
                score2_rect = score2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
                higherscore_rect = higherscore.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
                SCREEN.blit(score, score_rect)
                SCREEN.blit(score2, score2_rect)
                SCREEN.blit(higherscore, higherscore_rect)
            elif coop_mode: #death menu coop
                score = font.render(f"Game Over", True, FONT_COLOR)
                scoreRect = score.get_rect()
                scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
                SCREEN.blit(score, scoreRect)
            elif first_mission or second_mission or third_mission or fourth_mission or fifth_mission: #death menu missionen
                failed_mission = font.render("You have Failed this Mission, but you can Try Again", True, FONT_COLOR)
                try_again = font.render("By Pressing any Key to Restart", True, FONT_COLOR)
                failed_mission_rect = failed_mission.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
                try_again_rect = try_again.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
                SCREEN.blit(failed_mission, failed_mission_rect)
                SCREEN.blit(try_again, try_again_rect)
            else: #normales deathmenu
                score = font.render(f"Score by {str(load_highscore_name())}: {str(points)} ", True, FONT_COLOR)
                scoreRect = score.get_rect()
                scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
                SCREEN.blit(score, scoreRect)  # Draw the score on the screen.

                higherscore = font.render(f"Highscore: {str(load_highscore())}", True, FONT_COLOR)
                scoreRect = higherscore.get_rect()
                scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
                SCREEN.blit(higherscore, scoreRect)  # Draw the highscore on the screen.

        # Render the text and position it on the screen.
        if not first_mission or second_mission or third_mission or fourth_mission or fifth_mission:
            text = font.render("Press any Key to Restart", True, FONT_COLOR)
            text_rect = text.get_rect()
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            SCREEN.blit(text, text_rect)  # Draw the text on the screen.

        # Display an image representing the game character.
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()  # Update the entire screen with everything drawn.

        # Event loop to handle window closing and key presses.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game if the window close button is clicked.
                run = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                # Start the main game loop if any key is pressed.
                main()

def congrats1():
    run = True
    while run:
        SCREEN.fill((130, 128, 200))
        font = pygame.font.Font("freesansbold.ttf", 30)

        if m_one:
            m_title = "'Mission 1: Jump over 10 Catuses'"
        elif m_two:
            m_title = "'Mission 2: Survive 15 Obstacles'"
        elif m_three:
            m_title = "'Mission 3: Reach 500 Points'"
        elif m_four:
            m_title = "'Mission 4: Reach 1000 Points'"
        elif m_five:
            m_title = "'Mission 5: Master the Troll Mode'"

        con = font.render("Congrats!", True, FONT_COLOR)
        missiondone = font.render(f"You have completed {m_title} succesfully!", True, FONT_COLOR)
        view_mission = font.render(f"You can view your Achievements under 'Trophies'", True, FONT_COLOR)
        pressreturn = font.render("Press any Key to Continue", True, FONT_COLOR)
        con_rect = con.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3.25))
        missiondone_rect = missiondone.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.5))
        view_mission_rect = view_mission.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        pressreturn_rect = pressreturn.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))
        SCREEN.blit(con, con_rect)
        SCREEN.blit(missiondone, missiondone_rect)
        SCREEN.blit(view_mission, view_mission_rect)
        SCREEN.blit(pressreturn, pressreturn_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                main_menu()
            if event.type == pygame.KEYDOWN:
                mission()

def trophy():
    run = True
    selected = 0

    while run:
        SCREEN.fill((130, 128, 200))
        font = pygame.font.Font("freesansbold.ttf", 30)
        trophy_title = font.render("Trophies", True, FONT_COLOR)
        m_one = font.render(str(load_first_mission()), True, FONT_COLOR)
        m_two = font.render(str(load_second_mission()), True, FONT_COLOR)
        m_third = font.render(str(load_third_mission()), True, FONT_COLOR)
        m_four = font.render(str(load_fourth_mission()), True, FONT_COLOR)
        if selected == 0:  # trophy
            back_to_menu = font.render("Back To Menu <-", True, FONT_COLOR)
            back_to_mission = font.render("Back To Mission", True, FONT_COLOR)
        elif selected == 1:  # back
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
            back_to_mission = font.render("Back To Mission <-", True, FONT_COLOR)

        trophy_title_rect = trophy_title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8))
        m_one_rect = m_one.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4.5))
        m_two_rect = m_two.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        m_third_rect = m_third.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.2))
        m_four_rect = m_four.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.7))
        back_to_menu_rect = back_to_menu.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.3))
        back_to_mission_rect = back_to_mission.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.2))

        SCREEN.blit(m_one, m_one_rect)
        SCREEN.blit(m_two, m_two_rect)
        SCREEN.blit(m_third, m_third_rect)
        SCREEN.blit(m_four, m_four_rect)
        SCREEN.blit(trophy_title, trophy_title_rect)
        SCREEN.blit(back_to_menu, back_to_menu_rect)
        SCREEN.blit(back_to_mission, back_to_mission_rect)
        SCREEN.blit(TROPHY[0], (SCREEN_WIDTH // 8, SCREEN_HEIGHT // 2 - 140))
        SCREEN.blit(TROPHY[0], (SCREEN_WIDTH // 1.35, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 2
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % 2
                elif event.key == pygame.K_RETURN:
                    if selected == 0:  # back to menu
                        run = False
                        main_menu()
                    if selected == 1:  # back to mission
                        run = False
                        mission()


#---not finished yet---
def menu_settings():
    run = True
    selected = 0
    while run:
        SCREEN.fill((130, 128, 200))
        font = pygame.font.Font("freesansbold.ttf", 30)
        settings_title = font.render("Settings", True, FONT_COLOR)
        if selected == 0:  # music
            s_music = font.render("Music <-", True, FONT_COLOR)
            s_2 = font.render("Skins", True, FONT_COLOR)
            s_3 = font.render("Difficulty", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
        elif selected == 1:  # skins
            s_music = font.render("Music", True, FONT_COLOR)
            s_2 = font.render("Skins <-", True, FONT_COLOR)
            s_3 = font.render("Difficulty", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
        elif selected == 2:  # difficulty
            s_music = font.render("Music", True, FONT_COLOR)
            s_2 = font.render("Skins", True, FONT_COLOR)
            s_3 = font.render("Difficulty <-", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
        elif selected == 3:  # back to menu
            s_music = font.render("Music", True, FONT_COLOR)
            s_2 = font.render("Skins", True, FONT_COLOR)
            s_3 = font.render("Difficulty", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu <-", True, FONT_COLOR)

        settings_title_rect = settings_title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6))
        s_music_rect = s_music.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3.5))
        s_2_rect = s_2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.6))
        s_3_rect = s_3.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.1))
        back_to_menu_rect = back_to_menu.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.7))
        SCREEN.blit(settings_title, settings_title_rect)
        SCREEN.blit(s_music, s_music_rect)
        SCREEN.blit(s_2, s_2_rect)
        SCREEN.blit(s_3, s_3_rect)
        SCREEN.blit(back_to_menu, back_to_menu_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 4
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % 4
                elif event.key == pygame.K_RETURN:
                    if selected == 0:  # setting 1: music
                        run = False
                        main()
                    elif selected == 1:  # setting 2: skins
                        run = False
                        main()
                    elif selected == 2:  # setting 3: difficulty
                        run = False
                        main()
                    elif selected == 3:  # back to menu
                        run = False
                        main_menu()
def shop():
    run = True
    selected = 0
    while run:
        SCREEN.fill((130, 128, 200))
        font = pygame.font.Font("freesansbold.ttf", 30)
        shop_title = font.render("Welcome to the Shop", True, FONT_COLOR)
        if selected == 0:
            item1 = font.render("Item 1: Skin 'Mr. Dino' <-", True, FONT_COLOR)
            item2 = font.render("Item 2: Skin 'Mr. Dino'", True, FONT_COLOR)
            item3 = font.render("Item 3: Skin 'Mr. Dino'", True, FONT_COLOR)
            item4 = font.render("Item 4: Skin 'Mr. Dino'", True, FONT_COLOR)
            item5 = font.render("Item 5: Skin 'Mr. Dino'", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
        elif selected == 1:
            item1 = font.render("Item 1: Skin 'Mr. Dino'", True, FONT_COLOR)
            item2 = font.render("Item 2: Skin 'Mr. Dino' <-", True, FONT_COLOR)
            item3 = font.render("Item 3: Skin 'Mr. Dino'", True, FONT_COLOR)
            item4 = font.render("Item 4: Skin 'Mr. Dino'", True, FONT_COLOR)
            item5 = font.render("Item 5: Skin 'Mr. Dino'", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
        elif selected == 2:
            item1 = font.render("Item 1: Skin 'Mr. Dino'", True, FONT_COLOR)
            item2 = font.render("Item 2: Skin 'Mr. Dino'", True, FONT_COLOR)
            item3 = font.render("Item 3: Skin 'Mr. Dino' <-", True, FONT_COLOR)
            item4 = font.render("Item 4: Skin 'Mr. Dino'", True, FONT_COLOR)
            item5 = font.render("Item 5: Skin 'Mr. Dino'", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
        elif selected == 3:
            item1 = font.render("Item 1: Skin 'Mr. Dino'", True, FONT_COLOR)
            item2 = font.render("Item 2: Skin 'Mr. Dino'", True, FONT_COLOR)
            item3 = font.render("Item 3: Skin 'Mr. Dino'", True, FONT_COLOR)
            item4 = font.render("Item 4: Skin 'Mr. Dino' <-", True, FONT_COLOR)
            item5 = font.render("Item 5: Skin 'Mr. Dino'", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
        elif selected == 4:
            item1 = font.render("Item 1: Skin 'Mr. Dino'", True, FONT_COLOR)
            item2 = font.render("Item 2: Skin 'Mr. Dino'", True, FONT_COLOR)
            item3 = font.render("Item 3: Skin 'Mr. Dino'", True, FONT_COLOR)
            item4 = font.render("Item 4: Skin 'Mr. Dino'", True, FONT_COLOR)
            item5 = font.render("Item 5: Skin 'Mr. Dino' <-", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu", True, FONT_COLOR)
        elif selected == 5:
            item1 = font.render("Item 1: Skin 'Mr. Dino'", True, FONT_COLOR)
            item2 = font.render("Item 2: Skin 'Mr. Dino'", True, FONT_COLOR)
            item3 = font.render("Item 3: Skin 'Mr. Dino'", True, FONT_COLOR)
            item4 = font.render("Item 4: Skin 'Mr. Dino'", True, FONT_COLOR)
            item5 = font.render("Item 5: Skin 'Mr. Dino'", True, FONT_COLOR)
            back_to_menu = font.render("Back To Menu <-", True, FONT_COLOR)

        shop_title_rect = shop_title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6))
        item1_rect = item1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3.5))
        item2_rect = item2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.6))
        item3_rect = item3.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.1))
        item4_rect = item4.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.75))
        item5_rect = item5.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))
        back_to_menu_rect = back_to_menu.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.3))
        SCREEN.blit(shop_title, shop_title_rect)
        SCREEN.blit(item1, item1_rect)
        SCREEN.blit(item2, item2_rect)
        SCREEN.blit(item3, item3_rect)
        SCREEN.blit(item4, item4_rect)
        SCREEN.blit(item5, item5_rect)
        SCREEN.blit(back_to_menu, back_to_menu_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 6
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % 6
                elif event.key == pygame.K_RETURN:
                    if selected == 0:  # item 1
                        run = False
                        main()
                    elif selected == 1:  # item 2
                        run = False
                        main()
                    elif selected == 2:  # item 3
                        run = False
                        main()
                    elif selected == 3:  # item 4
                        run = False
                        main()
                    elif selected == 4:  # item 5
                        run = False
                        main()
                    elif selected == 5:  # back to menu
                        run = False
                        main_menu()

def rankings():
    run = True
    while run:
        SCREEN.fill((130, 128, 200))
        font = pygame.font.Font("freesansbold.ttf", 30)

        title = font.render("Ranking", True, FONT_COLOR)
        t1 = font.render("1. Highscore:", True, FONT_COLOR)
        highscore_one = font.render("abc", True, FONT_COLOR)
        t2 = font.render("2. Highscore:", True, FONT_COLOR)
        highscore_two = font.render("abc", True, FONT_COLOR)
        t3 = font.render("3. Highscore:", True, FONT_COLOR)
        highscore_three = font.render("abc", True, FONT_COLOR)

        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 11))
        t1_rect = t1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6))
        highscore_one_rect = highscore_one.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        t2_rect = t2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        highscore_two_rect = highscore_two.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.3))
        t3_rect = t3.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.9))
        highscore_three_rect = highscore_three.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.6))

        SCREEN.blit(title, title_rect)
        SCREEN.blit(t1, t1_rect)
        SCREEN.blit(highscore_one, highscore_one_rect)
        SCREEN.blit(t2, t2_rect)
        SCREEN.blit(highscore_two, highscore_two_rect)
        SCREEN.blit(t3, t3_rect)
        SCREEN.blit(highscore_three, highscore_three_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                run = False
                main_menu()

t1 = threading.Thread(target=menu(death_count=0), daemon=True)
pygame.init()
t1.start()
