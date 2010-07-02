import base64
import gzip
import io
import xml.dom.minidom
from Tkinter import *
import Tkinter

class XFDL_doc:
    def __init__(self, filename):
        file = open(filename, 'rb')
        s = file.read()
        file.close()
        #strips the first line because it screws up base64 decoding
        st = s[52:len(s)]
        s1 = base64.b64decode(st)
        sio = io.BytesIO(s1)
        gzf = gzip.GzipFile(fileobj=sio)
        xfdl_xml = gzf.read()
        self.doc = minidom.parseString(xfdl_xml)
        assert self.doc.documentElement.tagName == "XFDL"

class Viewer(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        root = Tk()
        self.menu_frame = Frame(root)
    def help_menu(self):
        help_btn = Tkinter.Menubutton(menu_frame, text='Help', underline=0)
        help_btn.pack(side=Tkinter.LEFT, padx="2m")
        help_btn.menu = Tkinter.Menu(help_btn)
        help_btn.menu.add_command(label="How To", underline=0, command=HowTo)
        help_btn.menu.add_command(label="About", underline=0, command=About)
        help_btn['menu'] = help_btn.menu
        return help_btn
    def file_menu(self):
        file_btn = Tkinter.Menubutton(menu_frame, text='file', underline=0)
        file_btn.pack(side=Tkinter.LEFT, padx="2m")
        file_btn.menu = Tkinter.Menu(help_btn)
        file_btn.menu.add_command(label="Open", underline=0, command=HowTo)
        file_btn.menu.add_command(label="Save", underline=0, command=About)
        file_btn['menu'] = file_btn.menu
    def run(self):
        Frame.__init__(self, self.master)
        self.pack()
        root = Tk()
        root.title("XFDL Viewer")
        menu_frame = Frame(root)
        menu_frame.pack(fill=Tkinter.X, side=Tkinter.TOP)
        menu_frame.tk_menuBar(self.file_menu(),  self.help_menu())
        app = Application(master=root)      
        app.mainloop()
        root.destroy()
 
    
if __name__ == '__main__':
    v = Viewer()
    v.run()
