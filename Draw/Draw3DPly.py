import tkinter as tk
import numpy as np

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.vertex = None
        self.face = None
        self.title('Bai Thuc Hanh So 17')
        self.geometry('690x620')

        self.cvs_figure = tk.Canvas(self, relief = tk.SUNKEN, bg = 'white', bd = 1, width = 600, height = 600)
        btn_ply = tk.Button(self, text = 'Draw .PLY', command = self.btn_ply_click)

        self.cvs_figure.place(x = 5, y = 6)
        btn_ply.place(x = 615, y = 6)

        self.cvs_figure.update()
    def btn_ply_click(self):
        self.cvs_figure.delete('all')
        self.cvs_figure.update()
        xc = (self.cvs_figure.winfo_width()-4) // 2
        yc = (self.cvs_figure.winfo_height()-4) // 2

        f = open('ketchup.ply', 'r')
        data = f.readlines()
        f.close()

        s = data[2][:-1].split()
        n_vertex = int(s[2])
        s = data[6][:-1].split()
        n_face = int(s[2])

        self.vertex = []
        for i in range(9, n_vertex + 9):
            s = data[i][:-1].split()
            temp = []
            temp.append(float(s[0]))
            temp.append(float(s[1]))
            temp.append(float(s[2]))
            self.vertex.append(temp)

        self.face = []
        for i in range(n_vertex + 9, n_vertex + 9 + n_face):
            s = data[i][:-1].split()
            temp = []
            for item in s:
                temp.append(int(item))
            self.face.append(temp)

        n_face = len(self.face)
        scale = 75
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
