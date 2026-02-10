import turtle
import pandas
import time
from board_states import BoardStates

screen = turtle.Screen()
screen.title("Estados Brasil")
screen.setup(width=800, height= 800)
image = "./Python/Bootcamp/day25/BRquiz/brasil.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print("," + str(int(x)) + "," + str(int(y)))
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("./Python/Bootcamp/day25/BRquiz/brazil_states.csv")
states = data["state"].to_list()
capitals = data["capital"].to_list()
x_state = data["x"].to_list()
y_state = data["y"].to_list()
x_capital = data["w"].to_list()
y_capital = data["z"].to_list()
states_dict = {state: (x, y) for (state, x, y) in zip(states, x_state, y_state)}
capital_dict = {capital: (x, y) for (capital, x, y) in zip(capitals, x_capital, y_capital)}

board_states = BoardStates()
guessed_states = []
guessed_capitals = []

game_is_on = True

while game_is_on:
    answer = screen.textinput(title=f"{len(guessed_states)}/54 Estados e Capitais", prompt="Entre um estado ou capital?").title()
    
    if answer in states and answer not in guessed_states:
        position = states_dict[answer]
        board_states.write_state(state=answer, coordinate=position)
        guessed_states.append(answer)
    elif answer in capitals and answer not in guessed_capitals:
        position = capital_dict[answer]
        board_states.write_state(state=answer, coordinate=position)
        guessed_states.append(answer)
    elif answer == "Quit":
        game_is_on = False
        for state in guessed_states:
            states.remove(state)
        new_data = pandas.DataFrame(states)
        new_data.to_csv("./Python/Bootcamp/day25/USquiz/states_to_learn.csv")
            
    elif answer in guessed_states:
        print("You already guessed this one")
    else:
        print("Not a state")

    if len(guessed_states) == len(states):
        game_is_on = False
    time.sleep(1)

screen.exitonclick()