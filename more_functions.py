try:
    import tkinter
except ImportError:
    import tkinter as tkinter
def parabola(page,size):
    for x in range(-size, size):
        y = x*x/size
        plot(page,x,y)

def draw_axis(page):
    page.update()
    x_origin = page.winfo_width()/2
    y_origin = page.winfo_height()/2
    page.configure(scrollregion = (-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin,0, x_origin,0, fill="black")
    page.create_line(0,y_origin,0, -y_origin, fill="black")

def plot(page, x,y):
    page.create_line(x,-y,x+1,-y+1, fill="red")

mainWindow = tkinter.Tk()
mainWindow.title("parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row = 0,column = 0)

draw_axis(canvas)
parabola(canvas,100)
parabola(canvas,200)


mainWindow.mainloop()

