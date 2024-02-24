import tkinter
import random
canvas_width = 400
canvas_height = 400
delay = 100
cell_size = 20

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

root = tkinter.Tk()
root.title('Snake')
canvas = tkinter.Canvas(root, width=canvas_width, height=canvas_height, bg='black')
canvas.pack()
snake = [(100, 100), (80, 100), (60, 100)]
snake_direction = right
food = None
score = 0
m = False
def create_food():
    global food
    x = random.randint(0, canvas_width / cell_size - 1) * cell_size
    y = random.randint(0, canvas_height / cell_size - 1) * cell_size
    food = (x, y)
    canvas.create_oval(food[0], food[1], food[0] + cell_size, food[1] + cell_size, fill='red')

def move_snake():
    global snake_direction, score, m

    for s in snake:
        canvas.create_rectangle(s[0], s[1], s[0] + cell_size, s[1] + cell_size, fill='green', tags='snake')

    new_head = (snake[0][0] + snake_direction[0] * cell_size, snake[0][1] + snake_direction[1] * cell_size)
    if new_head in snake or new_head[0] < 0 or new_head[0] >= canvas_width or new_head[1] < 0 or new_head[1] >= canvas_height:
        canvas.create_text(canvas_width / 2, canvas_height / 2, text=f'Игра окончена Очки {score}', fill='white', font=('Verdana', 20))
        return
    snake.insert(0, new_head)

    canvas.create_rectangle(new_head[0], new_head[1], new_head[0] + cell_size, new_head[1] + cell_size, fill='green')

    if new_head == food:
        create_food()
        score += 1
    else:
        a = snake.pop()
        canvas.delete('snake')


    canvas.after(delay, move_snake)

def move_up(event):
    global snake_direction
    if snake_direction != down:
        snake_direction = up

def move_down(event):
    global snake_direction
    if snake_direction != up:
        snake_direction = down

def move_left(event):
    global snake_direction
    if snake_direction != right:
        snake_direction = left

def move_right(event):
    global snake_direction
    if snake_direction != left:
        snake_direction = right

root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Right>", move_right)
root.bind("<Left>", move_left)
create_food()
'''
i = 0
for s in snake:
    if len(snake) - 1 == i:
        canvas.create_rectangle(s[0], s[1], s[0] + cell_size, s[1] + cell_size, fill='green', tags='last')
    else:
        canvas.create_rectangle(s[0], s[1], s[0] + cell_size, s[1] + cell_size, fill='green')
    i += 1'''
move_snake()

root.mainloop()