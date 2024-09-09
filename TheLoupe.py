import os
import sys
import mss
import json
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter
from win32api import GetSystemMetrics, GetKeyState, GetAsyncKeyState
from threading import Thread
import pystray
import keys



app_name = 'The Loupe'
current_dir = os.path.dirname(os.path.realpath(__file__))

config_path = os.path.join(current_dir, 'config.json')
icon_path = os.path.join(current_dir, 'icon.png')


class TheLoupeConfig(tk.Toplevel):
    def __init__(self, tl):
        self.tl = tl

        super().__init__(self.tl)
        
        self.title(f'{app_name}: Config')
        self.iconphoto(False, tk.PhotoImage(file=icon_path))

        self.screen_size = (GetSystemMetrics(0), GetSystemMetrics(1))
    
        self.pad = 5
        self.width = 360
        self.element_width = self.width - self.pad * 2
        self.mini_display_scale = self.screen_size[0] / self.element_width
        self.mini_display_height = self.screen_size[1] / self.mini_display_scale
        self.opacity_key_pressed = None

        validate_command = self.register(self.validate_number_input)

        self.protocol("WM_DELETE_WINDOW", self.close)
        # self.attributes('-toolwindow', True)
        self.resizable(False, False)
        # self.tl.bind("<Configure>", self.on_configure)

        frame_1 = tk.Frame(self) # Zoom / Default opacity / On press opacity
        frame_1.pack(padx=self.pad, pady=(self.pad, 0), fill=tk.BOTH, expand=True)
        frame_1.grid_columnconfigure(2, weight=100)

        zoom_label = ttk.Label(frame_1, text="Zoom:")
        zoom_label.grid(row=0, column=0, padx=(0, self.pad), sticky='w')
        
        self.zoom_value = ttk.Label(frame_1, text=self.tl.zoom)
        self.zoom_value.grid(row=0, column=1, padx=self.pad)

        self.zoom = ttk.Scale(frame_1, orient=tk.HORIZONTAL, from_=1.0, to=10.0, command=self.update_zoom)
        self.zoom.set(self.tl.zoom)
        self.zoom.grid(row=0, column=2, sticky='ew', padx=(self.pad, 0))


        default_opacity_label = ttk.Label(frame_1, text="Default opacity:")
        default_opacity_label.grid(row=1, column=0, padx=(0, self.pad), sticky='w')
        
        self.default_opacity_value = ttk.Label(frame_1, text=self.tl.default_opacity)
        self.default_opacity_value.grid(row=1, column=1, padx=self.pad)
        
        self.default_opacity = ttk.Scale(frame_1, orient=tk.HORIZONTAL, from_=0.0, to=1.0, command=self.update_default_opacity)
        self.default_opacity.set(self.tl.default_opacity)
        self.default_opacity.grid(row=1, column=2, sticky='ew', padx=(self.pad, 0))


        on_press_opacity = ttk.Label(frame_1, text="On press opacity:")
        on_press_opacity.grid(row=2, column=0, padx=(0, self.pad), sticky='w')
        
        self.on_press_opacity_value = ttk.Label(frame_1, text=self.tl.on_press_opacity)
        self.on_press_opacity_value.grid(row=2, column=1, padx=self.pad)
        
        self.on_press_opacity = ttk.Scale(frame_1, orient=tk.HORIZONTAL, from_=0.0, to=1.0, command=self.update_on_press_opacity)
        self.on_press_opacity.set(self.tl.on_press_opacity)
        self.on_press_opacity.grid(row=2, column=2, sticky='ew', padx=(self.pad, 0))        


        frame_2 = tk.Frame(self) # Opacity key
        frame_2.pack(padx=self.pad, pady=(0, self.pad), fill=tk.BOTH, expand=True)
        frame_2.grid_columnconfigure(1, weight=100)

        opacity_key = ttk.Label(frame_2, text="Opacity key:")
        opacity_key.grid(row=0, column=0, padx=(0, self.pad), sticky='w')

        self.opacity_key = ttk.Button(frame_2, command=self.update_opacity_key)
        self.opacity_key.grid(row=0, column=1, sticky='ew', padx=(self.pad, 0))

        self.set_opacity_key_button_text()


        self.mini_display = tk.Canvas(self, width=self.element_width, height=self.mini_display_height, bg="lightgray") # mini display
        self.mini_display.pack()
        self.mini_display.bind("<B1-Motion>", self.update_mini_display_target)

        self.cross = self.draw_mini_display_cross()

        

        frame_3 = tk.Frame(self) # Target coordinates / Loupe position / Loupe size
        frame_3.pack(padx=self.pad, pady=self.pad, fill=tk.BOTH, expand=True)
        frame_3.grid_columnconfigure(1, weight=50)
        frame_3.grid_columnconfigure(3, weight=50)


        target_x_label = ttk.Label(frame_3, text="Target coordinates:")
        target_x_label.grid(row=0, column=0, padx=(0, self.pad), sticky='w')

        target_x = ttk.Entry(frame_3, validate="key", validatecommand=(validate_command, 'target', 0, "%P"))
        target_x.insert(0, self.tl.target[0])
        target_x.grid(row=0, column=1, sticky='ew', padx=self.pad)
        
        target_sep_label = ttk.Label(frame_3, text="⨉")
        target_sep_label.grid(row=0, column=2, sticky='e')

        target_y = ttk.Entry(frame_3, validate="key", validatecommand=(validate_command, 'target', 1, "%P"))
        target_y.insert(0, self.tl.target[1])
        target_y.grid(row=0, column=3, sticky='ew', padx=(self.pad, 0))


        pos_label = ttk.Label(frame_3, text="Loupe position:")
        pos_label.grid(row=1, column=0, padx=(0, self.pad), sticky='w')
        
        pos_x = ttk.Entry(frame_3, validate="key", validatecommand=(validate_command, 'pos', 0, "%P"))
        pos_x.insert(0, self.tl.pos[0])
        pos_x.grid(row=1, column=1, sticky='ew', padx=self.pad)

        pos_sep_label = ttk.Label(frame_3, text="⨉")
        pos_sep_label.grid(row=1, column=2, sticky='e')

        pos_y = ttk.Entry(frame_3, validate="key", validatecommand=(validate_command, 'pos', 1, "%P"))
        pos_y.insert(0, self.tl.pos[1])
        pos_y.grid(row=1, column=3, sticky='ew', padx=(self.pad, 0))


        size_label = ttk.Label(frame_3, text="Loupe size:")
        size_label.grid(row=2, column=0, padx=(0, self.pad), sticky='w')

        size_x = ttk.Entry(frame_3, validate="key", validatecommand=(validate_command, 'size', 0, "%P"))
        size_x.insert(0, self.tl.size[0])
        size_x.grid(row=2, column=1, sticky='ew', padx=self.pad)

        size_sep_label = ttk.Label(frame_3, text="⨉")
        size_sep_label.grid(row=2, column=2, sticky='e')

        size_y = ttk.Entry(frame_3, validate="key", validatecommand=(validate_command, 'size', 1, "%P"))
        size_y.insert(0, self.tl.size[1])
        size_y.grid(row=2, column=3, sticky='ew', padx=(self.pad, 0))
        
        

        self.size = (size_x, size_y)
        self.pos = (pos_x, pos_y)
        self.target = (target_x, target_y)


        self.update_idletasks()
        self.geometry(f"{self.width}x{self.winfo_height() + self.pad}")



    def close(self):
        self.mini_display.unbind("<B1-Motion>")

        config = {
            'size': self.tl.size,
            'pos': self.tl.pos,
            'target': self.tl.target,
            'zoom': self.tl.zoom,
            'fps': self.tl.fps,
            'default_opacity': self.tl.default_opacity,
            'on_press_opacity': self.tl.on_press_opacity,
            'opacity_key': [str(hex(k)) for k in self.tl.opacity_key]
        }

        try:
            with open(config_path, 'w') as app_config_file:
                json.dump(config, app_config_file)
        except:
            pass

        self.tl.switch_editing()
        self.destroy()

    def validate_number_input(self, field_name, axis, value):
        if value.isdigit() or value == '':
            if len(value):
                axis = int(axis)
                value = int(value)
                tl_field = getattr(self.tl, field_name)
                tl_field[axis] = value

                if field_name in ('size', 'pos'):
                    self.tl.set_window()

            return True
        
        return False
    
    def draw_mini_display_cross(self, size=6, width=2, color='red'):
        x = self.tl.target[0] / self.mini_display_scale + width
        y = self.tl.target[1] / self.mini_display_scale + width
        equalization = 1 if width % 2 else 0
        return self.mini_display.create_line(x - size, y, x + size + equalization, y, width=width, fill=color), self.mini_display.create_line(x, y - size, x, y + size + equalization, width=width, fill=color)


    def update_zoom(self, zoom):
        self.tl.zoom = round(float(zoom), 1)

        self.zoom_value.config(text=self.tl.zoom)

        self.tl.set_bbox()


    def update_default_opacity(self, default_opacity):
        self.tl.default_opacity = round(float(default_opacity), 2)

        self.default_opacity_value.config(text=f'{self.tl.default_opacity:.02f}')


    def update_on_press_opacity(self, on_press_opacity):
        self.tl.on_press_opacity = round(float(on_press_opacity), 2)

        self.on_press_opacity_value.config(text=f'{self.tl.on_press_opacity:.02f}')
    

    def update_opacity_key(self):
        self.opacity_key_pressed = []
        
        self.opacity_key_listener()


    def opacity_key_listener(self):
        if self.opacity_key_pressed != None:
            if GetKeyState(0x1B) < 0:
                self.tl.opacity_key = []
                self.opacity_key_pressed = None

            else:
                for key in keys.keys:
                    if GetAsyncKeyState(key[0]) & 0x8000 and self.opacity_key_pressed != None and key[0] not in self.opacity_key_pressed:
                        self.opacity_key_pressed.append(key[0])
                        
                if len(self.opacity_key_pressed) and all([GetKeyState(k) >= 0 for k in self.opacity_key_pressed]):
                    self.tl.opacity_key = self.opacity_key_pressed
                    self.opacity_key_pressed = None
                
            self.after(50, self.opacity_key_listener)
        
        self.set_opacity_key_button_text()


    def set_opacity_key_button_text(self):
        if self.opacity_key_pressed != None and not len(self.opacity_key_pressed):
            return self.opacity_key.config(text='< Press opacity key >')
        
        if not len(self.tl.opacity_key):
            return self.opacity_key.config(text='< Undefined >')

        _keys = []
        for key in self.opacity_key_pressed if self.opacity_key_pressed != None else self.tl.opacity_key:
            key_info = keys.get(key)
            if key_info:
                _keys.append(key_info.desc)

        self.opacity_key.config(text=' + '.join(_keys))


    def update_mini_display_target(self, target):
        x = self.tl.target[0] / self.mini_display_scale
        if target.x >= 0 and target.x < self.element_width:
            x = target.x

        y = self.tl.target[1] / self.mini_display_scale
        if target.y >= 0 and target.y < self.mini_display_height:
            y = target.y

        self.target[0].delete(0, tk.END)
        self.target[0].insert(0, int(x * self.mini_display_scale))
        
        self.target[1].delete(0, tk.END)
        self.target[1].insert(0, int(y * self.mini_display_scale))

        for i in self.cross:
            self.mini_display.delete(i)
        self.cross = self.draw_mini_display_cross()

        self.tl.set_bbox()



class TheLoupe(tk.Tk):
    def __init__(self, size=[256, 256], pos=[0, 0], target=[512, 512], zoom=2, fps=120, default_opacity=0.2, on_press_opacity=1.0, opacity_key=[]):
        super().__init__()
        
        self.title(app_name)
        self.iconphoto(False, tk.PhotoImage(file=icon_path))

        self.running = True
        self.editing = False

        self.size = size
        self.pos = pos

        self.target = target
        self.zoom = zoom
        self.fps = fps
        self.default_opacity = default_opacity
        self.on_press_opacity = on_press_opacity
        self.opacity_key = opacity_key

        self.delay = int(1000 / self.fps) or 1

        self.set_window()
        
        self.overrideredirect(True)  # Убираем рамки окна
        self.attributes("-topmost", True)  # Делаем окно поверх всех других окон
        self.attributes("-alpha", self.default_opacity)

        

        self.canvas = tk.Canvas(self, width=self.size[0], height=self.size[1], highlightthickness=1)
        self.canvas.pack()

        self.set_bbox()

        self.shot = None
        self.new_shot = False
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor=tk.NW)

        self.grab_loop_thread = Thread(target=self.grab_loop, daemon=True)
        self.grab_loop_thread.start()

        self.check_opacity_key()

        self.draw_loop()

    def set_window(self):
        self.geometry(f"{int(self.size[0])}x{int(self.size[1])}+{int(self.pos[0])}+{int(self.pos[1])}")

    def switch_editing(self):
        self.editing = not self.editing
        self.attributes("-alpha", 1 if self.editing else self.default_opacity)



    def set_bbox(self):
        self.bbox = {
            "left": self.target[0] - int(self.size[0] / 2 / self.zoom),
            "top": self.target[1] - int(self.size[1] / 2 / self.zoom),
            "width": int(self.size[0] / self.zoom),
            "height": int(self.size[1] / self.zoom)
        }
    

    def grab_loop(self):
        with mss.mss() as sct:
            while self.running:
                self.shot = sct._grab_impl(self.bbox)
                self.new_shot = True


    def check_opacity_key(self):
        if not self.running:
            return
        
        if not self.editing:
            if all([GetKeyState(k) < 0 for k in self.opacity_key]):
                self.attributes("-alpha", self.on_press_opacity)
            else:
                self.attributes("-alpha", self.default_opacity)

        self.after(50, self.check_opacity_key)


    def draw_loop(self):
        if not self.running:
            return
        
        if self.new_shot:
            img = Image.frombytes("RGB", (self.shot.width, self.shot.height), self.shot.rgb)

            # img = ImageEnhance.Contrast(img).enhance(1.5)  # Повышение контраста
            # img = img.filter(ImageFilter.EDGE_ENHANCE)  # Увеличение контуров
            img = img.filter(ImageFilter.SHARPEN)  # Повышение резкости

            img = img.resize(self.size, Image.NEAREST)
            
            self.tk_image = ImageTk.PhotoImage(img)

            self.canvas.itemconfig(self.image_on_canvas, image=self.tk_image)

            self.new_shot = False
        
        self.after(self.delay, self.draw_loop)



class App():
    def __init__(self):
        self.icon = pystray.Icon(
            app_name, Image.open(icon_path),
            menu=pystray.Menu(
                pystray.MenuItem('Config', self.on_config),
                pystray.MenuItem('Quit', self.on_quit)
            ),
            HAS_DEFAULT_ACTION=False)
        
        self.icon.run_detached()

        self.config = {
            'size': [256, 256],
            'pos': [0, 0],
            'target': [512, 512],
            'zoom': 2,
            'fps': 60,
            'default_opacity': 1.0,
            'on_press_opacity': 1.0,
            'opacity_key': [0x2]
        }

        try:
            with open(config_path, 'r') as app_config_file:
                _app_config = json.load(app_config_file)
                opacity_key = _app_config.get('opacity_key')
                if opacity_key:
                    _app_config['opacity_key'] = [int(k, 16) for k in opacity_key]
                
                self.config.update(_app_config)
        except:
            pass

        self.tl = TheLoupe(**self.config)
        self.tls = None

        # self.on_config()
        self.tl.mainloop()


    def on_config(self):
        self.tl.switch_editing()
        if self.tl.editing:
            self.tls = TheLoupeConfig(self.tl)
            
        elif self.tls != None:
            self.tls.close()

            del self.tls
            self.tls = None
            
        
    def on_quit(self):
        self.tl.running = False
        self.tl.grab_loop_thread.join()
        # self.tl.destroy()
        self.icon.stop()

        sys.exit(0)

        


if __name__ == "__main__":
    App()