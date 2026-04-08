from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class traindata:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2560x1600+0+0")  # screen size: width x height
        self.root.title("Data Training:")

        cover_img = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Face_Recognition_System\main_imgs\DATATRAININGPAGE.png")
        cover_img = cover_img.resize((2560, 1600), Image.Resampling.LANCZOS)
        self.coverimg = ImageTk.PhotoImage(cover_img)
        bg_img = Label(self.root, image=self.coverimg)
        bg_img.place(x=0, y=0, width=2560, height=1600)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=265, y=825, width=2031, height=243)

        train_frame = Frame(main_frame, bd=2, relief=RIDGE, bg="white")
        train_frame.place(x=0, y=0, width=2027, height=241)
        train_btn = Button(train_frame, text="CLICK TO TRAIN DATA",command=self.train_classifier,width=29, font=("times new roman", 90, "bold"), bg="red", fg="white")
        train_btn.grid(row=0, column=0)


    # Train Classifier method
    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir) or len(os.listdir(data_dir)) == 0:
            messagebox.showerror("Error", "No training data found in 'data' folder", parent=self.root)
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            filename = os.path.split(image)[1] 
            parts = filename.split('.')

            if len(parts) >= 4 and parts[0] == "user":
                try:
                    id = int(parts[1])  
                    img = Image.open(image).convert('L')  # grayscale
                    imageNp = np.array(img, 'uint8')
                    faces.append(imageNp)
                    ids.append(id)
                    cv2.imshow("Training", imageNp)
                    cv2.waitKey(1)
                except Exception as e:
                    print(f"Skipping {filename}: {e}")
                    continue
            else:
                print(f"Skipping invalid file format: {filename}")

        if len(faces) == 0 or len(ids) == 0:
            messagebox.showerror("Error", "No valid training images found!", parent=self.root)
            return

        ids = np.array(ids)

        # Train classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)

        # Save in project folder
        save_path = os.path.join(os.getcwd(), "classifier.xml")
        clf.write(save_path)
        print(f"Classifier saved at: {save_path}")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", f"Training Completed!\nSaved as: {save_path}", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = traindata(root)
    root.mainloop()
