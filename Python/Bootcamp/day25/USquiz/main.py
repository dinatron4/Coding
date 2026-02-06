import turtle
import pandas
import time
from board_states import BoardStates

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height= 800)
image = "./Python/Bootcamp/day25/USquiz/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("./Python/Bootcamp/day25/USquiz/50_states.csv")
states = data["state"].to_list()
x_cord = data["x"].to_list()
y_cord = data["y"].to_list()
states_dict = {state: (x, y) for (state, x, y) in zip(states, x_cord, y_cord)}
# print(our_dict)
# print(states)

board_states = BoardStates()
guessed_states = []

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another state's name?").title()
    
    if answer_state in states and answer_state not in guessed_states:
        position = states_dict[answer_state]
        board_states.write_state(state=answer_state, coordinate=position)
        guessed_states.append(answer_state)
    elif answer_state == "Quit":
        game_is_on = False
        missing_states = [state for state in states if state not in guessed_states]
        # for state in guessed_states:
        #     states.remove(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("./Python/Bootcamp/day25/USquiz/states_to_learn.csv")
            
    elif answer_state in guessed_states:
        print("You already guessed this one")
    else:
        print("Not a state")

    if len(guessed_states) == len(states):
        game_is_on = False
    time.sleep(1)

# screen.exitonclick()