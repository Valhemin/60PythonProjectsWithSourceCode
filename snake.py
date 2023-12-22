
import tkinter
import random
import sys
import math

window = tkinter.Tk()


window_dimensions = [625, 625]
window.geometry(str(window_dimensions[0]) + "x" + str(window_dimensions[1]))
window.resizable(0, 0)


window.title("Snake Game")


window.protocol("WM_DELETE_WINDOW", sys.exit)


frames_per_second = 12


game_canvas = tkinter.Canvas(
    window, width=window_dimensions[0], height=window_dimensions[1], bd=0, highlightthickness=0)
game_canvas.pack()


game_scale = 25
game_dimensions = [window_dimensions[0] /
                   game_scale, window_dimensions[1] / game_scale]


player_coords = [math.floor(game_dimensions[0] / 2.0),
                 math.floor(game_dimensions[1] / 2.0)]
player_tail = []


player_velocity = [1, 0]


def generateAppleCoords():

    global player_tail

    generated_apple_coords = [random.randint(
        0, (game_dimensions[0] - 1)), random.randint(0, (game_dimensions[1] - 1))]

    for item in player_tail:
        if (item[0] == generated_apple_coords[0] and item[1] == generated_apple_coords[1]):
            return generateAppleCoords()

    return generated_apple_coords


apple_coords = generateAppleCoords()


velocity_changed_this_frame = False


def createGridItem(coords, hexcolor):
    game_canvas.create_rectangle((coords[0]) * game_scale, (coords[1]) * game_scale, (coords[0] + 1)
                                 * game_scale, (coords[1] + 1) * game_scale, fill=hexcolor, outline="#222222", width=3)


def gameloop():
    global frames_per_second
    global velocity_changed_this_frame
    global game_canvas
    global game_dimensions
    global window_dimensions
    global player_tail
    global player_coords
    global player_velocity
    global apple_coords

    window.after(int(1000 / frames_per_second), gameloop)

    velocity_changed_this_frame = False

    game_canvas.delete("all")

    game_canvas.create_rectangle(
        0, 0, window_dimensions[0], window_dimensions[1], fill="#222222", outline="#222222")

    player_tail.append([player_coords[0], player_coords[1]])

    player_coords[0] += player_velocity[0]
    player_coords[1] += player_velocity[1]

    if (player_coords[0] == game_dimensions[0]):
        player_coords[0] = 0
    elif (player_coords[0] == -1):
        player_coords[0] = game_dimensions[0] - 1
    elif (player_coords[1] == game_dimensions[1]):
        player_coords[1] = 0
    elif (player_coords[1] == -1):
        player_coords[1] = game_dimensions[1] - 1

    for item in player_tail:

        if (item[0] == player_coords[0] and item[1] == player_coords[1]):

            player_coords = [math.floor(
                game_dimensions[0] / 2.0), math.floor(game_dimensions[1] / 2.0)]
            player_tail = []
            player_velocity = [1, 0]
            apple_coords = generateAppleCoords()

        createGridItem(item, "#00ff00")

    createGridItem(apple_coords, "#ff0000")

    if (apple_coords[0] == player_coords[0] and apple_coords[1] == player_coords[1]):
        apple_coords = generateAppleCoords()
    else:
        player_tail.pop(0)


def onKeyDown(e):
    global player_velocity
    global velocity_changed_this_frame

    if (velocity_changed_this_frame == False):

        velocity_changed_this_frame = True

        if (e.keysym == "Left" and player_velocity[0] != 1):
            player_velocity = [-1, 0]
        elif (e.keysym == "Right" and player_velocity[0] != -1):
            player_velocity = [1, 0]
        elif (e.keysym == "Up" and player_velocity[1] != 1):
            player_velocity = [0, -1]
        elif (e.keysym == "Down" and player_velocity[1] != -1):
            player_velocity = [0, 1]
        else:

            velocity_changed_this_frame = False


window.bind("<KeyPress>", onKeyDown)


gameloop()


window.mainloop()
