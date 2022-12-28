from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter import messagebox as mbox
from algo import main

root = Tk()
root.title("RRT")
root.geometry("1100x800")
width = 700
height = 700

#Задание окна
canvas = Canvas(bg="white", width=width, height=height)  # график
canvas.pack(side=LEFT, anchor=CENTER, expand=1)


#Поле кнопок
frame_buttons = Frame(root, relief=RAISED, borderwidth=1, background="#FFF")
frame_buttons.pack(side=RIGHT, fill=BOTH, expand=True)

# saveButton = Button(frame_buttons, text="Сохранить")
# saveButton.pack(side=TOP, padx=5, pady=5)


#Поставить точку старта
def getStart():
    try:
        float(startX.get())
        float(startY.get())
    except ValueError:
        print(1)
        mbox.showwarning("Ошибка!", "Координаты введенный не верно.")
    if float(startX.get()) > 10 or float(startX.get()) < -10 or float(startY.get()) > 10 or float(startY.get()) < -10:
        print(1)
        mbox.showwarning("Ошибка!оординаты введенный не верно.")
    else:
        start.append(float(startX.get())*35)
        start.append(float(startY.get())*35)
        x1, y1 = (start[0] - 2), (start[1] - 2)
        x2, y2 = (start[0] + 2), (start[1] + 2)
        canvas.create_oval(x1+width/2, height/2-y1, x2+width/2, height/2-y2, fill="#ff0000")
        btnStart["state"] = "disabled"
frame_start = Frame(frame_buttons, relief=RAISED,borderwidth=1, background="#FFF")
frame_start.pack(side=TOP, fill=BOTH, ipadx=5, ipady=5, padx=5, pady=5)
labelStartX = ttk.Label(frame_start, text="X:", font=("Arial", 10), width=3)
labelStartX.pack(side=LEFT, padx=5, pady=5)
startX = ttk.Entry(frame_start, width=10)
startX.pack(side=LEFT, padx=5, pady=5)

labelStartY = ttk.Label(frame_start, text="Y:", font=("Arial", 10), width=3)
labelStartY.pack(side=LEFT, padx=5, pady=5)
startY = ttk.Entry(frame_start, width=10)
startY.pack(side=LEFT, padx=5, pady=5)

btnStart = ttk.Button(frame_start, text="Add Start", command=getStart)
btnStart.pack(side=LEFT, padx=5, pady=5)
start = []

#Поставить точку конца
def getEnd():
    try:
        float(endX.get())
        float(endY.get())
    except ValueError:
        print(1)
        mbox.showwarning("Ошибка!", "Координаты введенный не верно.")
    if float(endX.get()) > 10 or float(endX.get()) < -10 or float(endY.get()) > 10 or float(endY.get()) < -10:
        print(1)
        mbox.showwarning("Ошибка!", "Координаты введенный не верно.")
    else:
        end.append(float(endX.get())*35)
        end.append(float(endY.get())*35)
        x1, y1 = (end[0] - 2), (end[1] - 2)
        x2, y2 = (end[0] + 2), (end[1] + 2)
        canvas.create_oval(x1+width/2, height/2-y1, x2+width/2, height/2-y2, fill="#0000ff")
        btnEnd["state"] = "disabled"

frame_end = Frame(frame_buttons, relief=RAISED,borderwidth=1, background="#FFF")
frame_end.pack(side=TOP, fill=BOTH, ipadx=5, ipady=5, padx=5, pady=5)
labelEndX = ttk.Label(frame_end, text="X:", font=("Arial", 10), width=3)
labelEndX.pack(side=LEFT, padx=5, pady=5)
endX = ttk.Entry(frame_end, width=10)
endX.pack(side=LEFT, padx=5, pady=5)

labelEndY = ttk.Label(frame_end, text="Y:", font=("Arial", 10), width=3)
labelEndY.pack(side=LEFT, padx=5, pady=5)
endY = ttk.Entry(frame_end, width=10)
endY.pack(side=LEFT, padx=5, pady=5)

btnEnd = ttk.Button(frame_end, text="Add End", command=getEnd)
btnEnd.pack(side=LEFT, padx=5, pady=5)
end = []


#Построить треугольник
def getTriangle():
    try:
        float(triangle1X.get())
        float(triangle1Y.get())
        float(triangle2X.get())
        float(triangle2Y.get())
        float(triangle3X.get())
        float(triangle3Y.get())
    except ValueError:
        print(1)
        mbox.showwarning("Ошибка!", "Координаты введенный не верно.")
    if float(triangle1X.get()) > 10 or float(triangle1X.get()) < -10 or float(triangle3X.get()) > 10 or float(triangle3X.get()) < -10 or float(triangle2X.get()) > 10 or float(triangle2X.get()) < -10 or float(triangle1Y.get()) > 10 or float(triangle1Y.get()) < -10 or float(triangle3Y.get()) > 10 or float(triangle3Y.get()) < -10 or float(triangle2Y.get()) > 10 or float(triangle2Y.get()) < -10:
        print(1)
        mbox.showwarning("Ошибка!", "Координаты введенный не верно.")
    else:
        x1 = float(triangle1X.get())*35
        y1 = float(triangle1Y.get())*35
        x2 = float(triangle2X.get())*35
        y2 = float(triangle2Y.get())*35
        x3 = float(triangle3X.get())*35
        y3 = float(triangle3Y.get())*35
        triangles.append(([x1, y1], [x2, y2], [x3, y3]))
        canvas.create_polygon(x1+width/2, height/2-y1, x2+width/2, height/2-y2, x3+width/2, height/2-y3, fill="#80CBC4", outline="#004D40")
        print(triangles)
frame_triangles = Frame(frame_buttons, relief=RAISED,borderwidth=1, background="#FFF")
frame_triangles.pack(side=TOP, fill=BOTH, ipadx=5, ipady=5, padx=5, pady=5)
labelTriangle1X = ttk.Label(frame_triangles, text="X1:", font=("Arial", 10), width=3)
labelTriangle1X.pack(side=TOP, padx=5, pady=5)
triangle1X = ttk.Entry(frame_triangles, width=10)
triangle1X.pack(side=TOP, padx=5, pady=5)
labelTriangle1Y = ttk.Label(frame_triangles, text="Y1:",font=("Arial", 10), width=3)
labelTriangle1Y.pack(side=TOP, padx=5, pady=5)
triangle1Y = ttk.Entry(frame_triangles, width=10)
triangle1Y.pack(side=TOP, padx=5, pady=5)

labelTriangle2X = ttk.Label(frame_triangles, text="X2:", font=("Arial", 10), width=3)
labelTriangle2X.pack(side=TOP, padx=5, pady=5)
triangle2X = ttk.Entry(frame_triangles, width=10)
triangle2X.pack(side=TOP, padx=5, pady=5)
labelTriangle1Y = ttk.Label(frame_triangles, text="Y2:",font=("Arial", 10), width=3)
labelTriangle1Y.pack(side=TOP, padx=5, pady=5)
triangle2Y = ttk.Entry(frame_triangles, width=10)
triangle2Y.pack(side=TOP, padx=5, pady=5)

labelTriangle1Y = ttk.Label(frame_triangles, text="X3:",font=("Arial", 10), width=3)
labelTriangle1Y.pack(side=TOP, padx=5, pady=5)
triangle3X = ttk.Entry(frame_triangles, width=10)
triangle3X.pack(side=TOP, padx=5, pady=5)
labelTriangle1Y = ttk.Label(frame_triangles, text="Y3:",font=("Arial", 10), width=3)
labelTriangle1Y.pack(side=TOP, padx=5, pady=5)
triangle3Y = ttk.Entry(frame_triangles, width=10)
triangle3Y.pack(side=TOP, padx=5, pady=5)

btnTriangle = ttk.Button(
    frame_triangles, text="Add Triangle", command=getTriangle)
btnTriangle.pack(side=TOP, padx=5, pady=5)
triangles = []



#Построить путь
def build():
    if start == [] or end == []:
        print(1)
        mbox.showwarning("Ошибка", "Точки не заданны")
    rrt = main(start, end, [-height/2, height/2], triangles)
    for node in rrt.nodeList:
        if node.parent is not None:
            canvas.create_line(node.x+width/2, height/2-node.y, rrt.nodeList[node.parent].x+width/2, height/2-rrt.nodeList[node.parent].y, fill="#000")
            btnBuild["state"] = "disabled"
    if rrt.path != 'Error':
        points = [(rrt.nodeList[data].x+width/2, height/2-rrt.nodeList[data].y)for data in rrt.path]
        canvas.create_line(points, fill="#ff0000", width=2)
    else:
        print(1)
        mbox.showwarning("Ошибка", "Не удалось найти путь")
btnBuild = ttk.Button(frame_buttons, text="Build path", command=build)
btnBuild.pack(side=TOP, padx=5, pady=5)


#Очистить поле
def clear():
    canvas.delete("all")
    start.clear()
    end.clear()
    triangles.clear()
    btnStart["state"] = "normal"
    btnEnd["state"] = "normal"
    btnBuild["state"] = "normal"
btnClear = ttk.Button(frame_buttons, text="Clear all", command=clear)
btnClear.pack(side=TOP, padx=5, pady=5)


root.mainloop()
