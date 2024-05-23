import turtle as T
import random
screen = T.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "yellow", "green", "blue", "purple"]
user_bet = user_bet.lower()
y_position = [-70, -40, -10, 20, 50, 80]
is_race_on = False

all_turtle = []
for turtle_ind in range(0, 5):
    # tim = T.Turtle()
    # tim.shape("turtle")
    turtle_ = T.Turtle(shape="turtle")
    turtle_.color(colors[turtle_ind])
    turtle_.penup()
    turtle_.goto(-220, y=y_position[turtle_ind])
    all_turtle.append(turtle_)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(
                    f"You've won! The {winning_turtle} turtle is the winner ")
            else:
                print(
                    f"You've lose! The {winning_turtle} turtle is the winner ")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
