import tkinter as tk
import tkinter.ttk as ttk
from AStarAlgorithm import find_path


class Window(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=2)
        self.create_variables()
        self.create_widgets()
        self.create_layout()
        self.binds()

    def create_variables(self):
        self.switch = tk.StringVar()
        self.switch.set('start')
        self.start_coords = ()
        self.finish_coords = ()
        self.matrix = [[True for _ in range(200)] for _ in range(200)]
        self.finished = False

    def create_widgets(self):
        self.map = tk.Canvas(self, width=800, height=800, bg='white')
        self.RadiobuttonStart = ttk.Radiobutton(self, text='Place starting point', variable=self.switch, value='start')
        self.RadiobuttonFinish = ttk.Radiobutton(self, text='Place finishing point', variable=self.switch,
                                                 value='finish')
        self.RadiobuttonWalls = ttk.Radiobutton(self, text='Place walls', variable=self.switch, value='wall')
        self.ButtonStart = ttk.Button(self, text='Find path')
        self.ButtonClear = ttk.Button(self, text='Clear')

    def create_layout(self):
        self.map.grid(row=0, column=0, rowspan=20)
        self.RadiobuttonStart.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.RadiobuttonFinish.grid(row=1, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.RadiobuttonWalls.grid(row=2, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.ButtonStart.grid(row=3, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.ButtonClear.grid(row=4, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

    def click_mouse(self, event):
        if not self.finished:
            if self.switch.get() == 'wall':
                x0, y0 = event.x // 4 * 4, event.y // 4 * 4
                self.map.create_rectangle(x0, y0, x0 + 4, y0 + 4, fill='black')
                self.matrix[x0 // 4][y0 // 4] = False

            elif self.switch.get() == 'start':
                x0, y0 = event.x // 4 * 4, event.y // 4 * 4
                self.map.create_rectangle(x0, y0, x0 + 4, y0 + 4, fill='green', outline='green')
                if len(self.start_coords) > 0:
                    x, y = self.start_coords
                    self.map.create_rectangle(x*4, y*4, x*4 + 4, y*4 + 4, fill='white', outline='white')
                self.start_coords = (x0 // 4, y0 // 4)

            else:
                x0, y0 = event.x // 4 * 4, event.y // 4 * 4
                self.map.create_rectangle(x0, y0, x0 + 4, y0 + 4, fill='red', outline='green')
                if len(self.finish_coords) > 0:
                    x, y = self.finish_coords
                    self.map.create_rectangle(x*4, y*4, x*4 + 4, y*4 + 4, fill='white', outline='white')
                self.finish_coords = (x0 // 4, y0 // 4)

    def start(self, event):
        try:
            for i in find_path(self.matrix, self.start_coords, self.finish_coords)[:-1]:
                x, y = i
                self.map.create_rectangle(x * 4, y * 4, x * 4 + 4, y * 4 + 4, fill='blue', outline='blue')
        except:
            print('No such path')
        finished = True

    def place_wall(self, event):
        if not self.finished:
            if self.switch.get() == 'wall':
                x0, y0 = event.x // 4 * 4, event.y // 4 * 4
                self.map.create_rectangle(x0, y0, x0 + 4, y0 + 4, fill='black')
                self.matrix[x0 // 4][y0 // 4] = False

    def clear(self, event):
        self.start_coords = ()
        self.finish_coords = ()
        self.matrix = [[True for _ in range(200)] for _ in range(200)]
        self.finished = False
        self.map.delete('all')

    def binds(self):
        self.map.bind('<Button-1>', self.click_mouse)
        self.map.bind('<B1-Motion>', self.place_wall)
        self.map.bind('<Button-1>', self.click_mouse)
        self.map.bind('<Button-1>', self.click_mouse)
        self.ButtonStart.bind('<Button-1>', self.start)
        self.ButtonClear.bind('<Button-1>', self.clear)
