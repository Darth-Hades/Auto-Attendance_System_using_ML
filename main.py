from tkinter import* #tkinter is to make GUI apps
from tkinter import ttk #ttk provides stylish tools
from PIL import Image,ImageTk #to crop or change resolution of images
from student_database import StudentDatabase
from traindata import traindata
from face_recognition import FaceRecognition
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("2560x1600+0+0") #displays ratio screen size, x point, y point
        self.root.title("Face Recognition System:")

        #image path
        cover_img = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Face_Recognition_System\main_imgs\DYPUBLUR1.png")
        #image sizing and positioning
        #BG IMAGE
        cover_img = cover_img.resize((2560, 1600), Image.Resampling.LANCZOS)  #Lanczos converts img from high to low level
        self.coverimg=ImageTk.PhotoImage(cover_img)
        bg_img =Label(self.root,image=self.coverimg)
        bg_img.place(x=0,y=0,width=2560,height=1600)

        #StudentID Button
        stdb_img = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Face_Recognition_System\main_imgs\stdb.png")
        stdb_img = stdb_img.resize((500, 325), Image.Resampling.LANCZOS)
        self.stdbimg = ImageTk.PhotoImage(stdb_img)
        b1 = Button(self.root, image=self.stdbimg,command=self.student_details , cursor="hand2")
        b1.place(x=157, y=529, width=500, height=325)  

        #face recognition button
        facerec_img = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Face_Recognition_System\main_imgs\facerec.png")
        facerec_img = facerec_img.resize((500, 325), Image.Resampling.LANCZOS)
        self.facerecimg = ImageTk.PhotoImage(facerec_img)
        b1 = Button(self.root, image=self.facerecimg,command=self.face_recognition_cmd ,cursor="hand2")
        b1.place(x=1031, y=529, width=500, height=325)

        #Attendance button
        attd_img = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Face_Recognition_System\main_imgs\attd.png")
        attd_img = attd_img.resize((500, 325), Image.Resampling.LANCZOS)
        self.attdimg = ImageTk.PhotoImage(attd_img)
        b1 = Button(self.root, image=self.attdimg, cursor="hand2")
        b1.place(x=1905, y=529, width=500, height=325)

        #Student Photo Button
        stdimg_img = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Face_Recognition_System\main_imgs\stdimg.png")
        stdimg_img = stdimg_img.resize((500, 325), Image.Resampling.LANCZOS)
        self.stdimg = ImageTk.PhotoImage(stdimg_img)
        b1 = Button(self.root, image=self.stdimg,command=self.open_img ,cursor="hand2")
        b1.place(x=157, y=1078, width=500, height=325)

        #DATA TRAINING BUTTON button
        abtdev_img = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Face_Recognition_System\main_imgs\abtdev.png")
        abtdev_img = abtdev_img.resize((500, 325), Image.Resampling.LANCZOS)
        self.devimg = ImageTk.PhotoImage(abtdev_img)
        b1 = Button(self.root, image=self.devimg,command=self.train_data ,cursor="hand2")
        b1.place(x=1031, y=1078, width=500, height=325)

        #save and exit Button
        exitimg_img = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Face_Recognition_System\main_imgs\exitimg.png")
        exitimg_img = exitimg_img.resize((500, 325), Image.Resampling.LANCZOS)
        self.exitimg = ImageTk.PhotoImage(exitimg_img)
        b1 = Button(self.root, image=self.exitimg, cursor="hand2")
        b1.place(x=1905, y=1078, width=500, height=325)

     
     #BUTTON FUNCTION COMMANDS
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=StudentDatabase(self.new_window)
    
    def open_img(self):
        os.startfile("data")

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=traindata(self.new_window)

    def face_recognition_cmd(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceRecognition(self.new_window)







if __name__=="__main__": #call main fx
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
