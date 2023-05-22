import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian States and Union Territories")
image = "Indian map void-fx game.gif"
screen.addshape(image)

turtle.shape(image)
'''
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
'''

guessed_state = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{len(guessed_state)} States Correct", prompt="Write a state name").title()
    data = pandas.read_csv("states_and_union_territories.csv")
    all_states = data.state.to_list()
    print(answer_state)
    if answer_state == "Exit":
        print(answer_state)
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                print(answer_state)
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print(answer_state)
        break
    elif answer_state in all_states:
        print(answer_state)
        print(all_states)
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

        if len(guessed_state) < 37:
            game_is_on = True
        else:
            game_is_on = False
