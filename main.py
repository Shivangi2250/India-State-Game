import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S STATE GAME")
image= "india_blank_state.gif"
screen.addshape(image)
turtle.shape(image)    # image is available on the screen now it can be used by turtle

# def get_mouse_click_coor(x,y):
#    print (x,y)
# turtle.onscreenclick(get_mouse_click_coor)       #now you can get the coordinates of the area where you will
# # click on the screen BUT we wont use it as angela has already provided us with the data stored in 29_states.csv

import pandas as pd

# # create new pandas DataFrame
# df = pd.DataFrame(list())
#
# # write empty DataFrame to new csv file
# df.to_csv('my_empty.csv')

data=pandas.read_csv("29_states")


all_states=data["state"].to_list()
# print(state_list)

guessed_state=[]

while len(guessed_state) <29:
    ans_state = screen.textinput(title=f"{len(guessed_state)}/29 correct states", prompt="What is the next state?")
    Ans_state = ans_state.title()
    if ans_state == "exit":
        missing_states=[state for state in all_states if state not in guessed_state]  #using list comprehension
        # missing_list=[]              #without using list comprehension
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        # print(missing_states)
        missed_states_dataframe=pandas.DataFrame(missing_states)
        csv_missed_states=missed_states_dataframe.to_csv("missed_states")
        break
    if Ans_state in all_states:
        guessed_state.append(Ans_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data["state"]==Ans_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(Ans_state)




# screen.mainloop()

























