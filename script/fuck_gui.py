import tkinter as tk
import rospy

class fuck_gui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.wheleDistance_Lable = tk.Label(self,text="wheleDistance")
        self.wheleDistance_Lable.grid(row=0,column=0)

        self.wheleDistance_input = tk.Entry(self)
        self.wheleDistance_input.grid(row=0,column=1,columnspan=3)

        self.wheleDistance_button = tk.Button(self,text="set")
        self.wheleDistance_button['command'] = self.fuck_button
        self.wheleDistance_button.grid(row=0, column=4)

        self.wheleDistance_scale = tk.Scale(self,orient=tk.HORIZONTAL, length=200, from_=1.0, to=100.0,command=self.hit_scale)
        self.wheleDistance_scale.grid(row=1,column=0)

    def fuck_button(self):
        print("hit the button")

    def hit_scale(self,value):
        print("hit the Scale. Value:%s" % (value))


if __name__ == '__main__':
    root = tk.Tk()
    app = fuck_gui(master=root)
    app.mainloop()
