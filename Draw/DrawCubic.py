import tkinter as tk
import numpy as np

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.flag_ve_diem = True
        self.vertex = [[0, 0, 0],
                        [0, 0, 1],
                        [0, 1, 1],
                        [0, 1, 0],
                        [1, 0, 0],
                        [1, 0, 1],
                        [1, 1, 1],
                        [1, 1, 0]]

        self.face = [[4, 0, 1, 2, 3],
                    [4, 7, 6, 5, 4],
                    [4, 0, 4, 5, 1],
                    [4, 1, 5, 6, 2],
                    [4, 2, 6, 7, 3],
                    [4, 3, 7, 4, 0]]

        self.title('Bai Thuc Hanh So 17')
        self.geometry('670x620')

        self.cvs_figure = tk.Canvas(self, relief = tk.SUNKEN, bg = 'white', bd = 1, width = 600, height = 600)
        btn_cubic = tk.Button(self, text = 'Cubic', command = self.btn_cubic_click)

        self.cvs_figure.place(x = 5, y = 6)
        btn_cubic.place(x = 615, y = 6)

        self.cvs_figure.update()
    def btn_cubic_click(self):
        xc = (self.cvs_figure.winfo_width()-4) // 2
        yc = (self.cvs_figure.winfo_height()-4) // 2
        n_face = len(self.face)
        scale = 100
        L1 = 0.5
        phi = np.pi/4
        for i in range(0, n_face):
            k =  self.face[i][0]    
            temp = []
            for j in range(1, k+1):
                x = self.vertex[self.face[i][j]][0]*scale
                y = self.vertex[self.face[i][j]][1]*scale
                z = self.vertex[self.face[i][j]][2]*scale
                xp = x + -z*L1*np.cos(phi)
                yp = y + -z*L1*np.sin(phi)
                temp.append(xp +  xc)
                temp.append(-yp + yc)
            x = self.vertex[self.face[i][1]][0]*scale
            y = self.vertex[self.face[i][1]][1]*scale
            z = self.vertex[self.face[i][1]][2]*scale
            xp = x + -z*L1*np.cos(phi)
            yp = y + -z*L1*np.sin(phi)
            temp.append(xp +  xc)
            temp.append(-yp + yc)
            self.cvs_figure.create_line(temp)

            
if __name__ == "__main__":
    app = App()
    app.mainloop()
