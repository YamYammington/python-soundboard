import tkinter as tk
import pygame
import os


# Gets sfx files from <current directory>/sfx
sfx_dir = './sfx'


def get_sfx():
    if os.path.exists(sfx_dir):
        sfx_files = os.listdir(sfx_dir)
        sfx_filenames = [f.split('.')[0] for f in sfx_files]
        return list(zip(sfx_files, sfx_filenames))
    else:
        os.mkdir(sfx_dir)
        raise RuntimeError(f'There is no sfx directory. One has been created at {os.path.join(os.getcwd(), "sfx")}')


class Grid(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)
        data = get_sfx()

        self.grid_columnconfigure(1, weight=1)
        tk.Label(self, text="Nr.", anchor="w").grid(row=0, column=0, sticky="ew")
        tk.Label(self, text="Sound Effects", anchor="w").grid(row=0, column=3, sticky="ew")

        row = 1
        for (file, name) in data:
            nr_label = tk.Label(self, text=str(row), anchor="w")
            action_button = tk.Button(self, text=name, command=lambda f=file: play(f))

            nr_label.grid(row=row, column=0, sticky="ew")
            action_button.grid(row=row, column=3, sticky="ew")

            row += 1


def play(sfx):
    pygame.mixer.music.unload()
    pygame.mixer.music.load('sfx/' + sfx)
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(width=True, height=True)
    root.title("Soundboard")
    # root.geometry("720x480")
    pygame.mixer.init()

    # controls
    tk.Button(root, command=stop, text="Stop", padx=10).pack()

    # sounds
    Grid(root, text="Sounds").pack(side="top", fill="both", expand=True, padx=10, pady=10)

    root.mainloop()