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
        root = Tk()
        self.menu_frame = Frame(root)
        self.pack()
        root.title("XFDL Viewer")
        self.menu_frame.pack(fill=Tkinter.X, side=Tkinter.TOP)
        self.main_frame = Frame(root, width=500, height=500)
        self.main_frame.pack()
        self.run()
        app = Application(master=root)      
        app.mainloop()
        root.destroy()
    def help_menu(self):
        help_btn = Tkinter.Menubutton(self.menu_frame, text='Help', underline=0)
        help_btn.pack(side=Tkinter.LEFT, padx="2m")
        help_btn.menu = Tkinter.Menu(help_btn)
        help_btn['menu'] = help_btn.menu
        return help_btn
    def file_menu(self):
        file_btn = Tkinter.Menubutton(self.menu_frame, text='File', underline=0)
        file_btn.pack(side=Tkinter.LEFT, padx="2m")
        file_btn.menu = Tkinter.Menu(file_btn)
        file_btn['menu'] = file_btn.menu
    def run(self):
        self.menu_frame.tk_menuBar(self.file_menu(),  self.help_menu())
 
  
 
    
if __name__ == '__main__':
    v = Viewer()
    v.run()
