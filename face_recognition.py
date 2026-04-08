from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import cv2
import os
import mysql.connector
import numpy as np
import tensorflow as tf

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2560x1600+0+0")
        self.root.title("Face Recognition:")

        self.attendance_cache = set()
        
        try:
            cover_img = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Face_Recognition_System\main_imgs\FACERECOGNITIONPAGE.png")
            cover_img = cover_img.resize((2560, 1600), Image.Resampling.LANCZOS)
            self.coverimg = ImageTk.PhotoImage(cover_img)
            bg_img = Label(self.root, image=self.coverimg)
            bg_img.place(x=0, y=0, width=2560, height=1600)
        except FileNotFoundError:
            messagebox.showerror("Error", "Background image not found. Please check the file path.")

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=265, y=825, width=2031, height=243)

        face_rec_frame = Frame(main_frame, bd=2, relief=RIDGE, bg="white")
        face_rec_frame.place(x=0, y=0, width=2027, height=241)

        face_rec_btn = Button(face_rec_frame, text="START FACE RECOGNITION", command=self.face_recog,
                              width=29, font=("times new roman", 90, "bold"), bg="red", fg="white")
        face_rec_btn.grid(row=0, column=0)

    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, clf):
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
        coords = []

        for (x, y, w, h) in faces:
            id, predict = clf.predict(gray_img[y:y+h, x:x+w])
            confidence = int(100 * (1 - predict / 300))

            try:
                conn = mysql.connector.connect(host="127.0.0.1", user="root", password="@ArtasHteh1730", database="face_recognizer",auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT name, roll, department FROM student WHERE studentid=%s", (id,))
                result = my_cursor.fetchone()

                if result:
                    n, r, d = result
                else:
                    n, r, d = "Unknown", "N/A", "N/A"

                conn.close()
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Failed to connect to MySQL: {e}")
                n, r, d = "Unknown", "N/A", "N/A"

            if confidence > 74:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.putText(img, f"Name: {n}", (x, y - 50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                cv2.putText(img, f"Roll: {r}", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                cv2.putText(img, f"Dept: {d}", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                self.mark_attendance(id, r, n, d)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

            coords.append([x, y, w, h])

        return coords

    def recognize(self, img, clf, faceCascade):
        self.draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), clf)
        return img

    from datetime import datetime

    def mark_attendance(self, i, r, n, d):
        try:
            now = datetime.now()
            date_str = now.strftime("%d/%m/%Y")
            time_str = now.strftime("%H:%M:%S")
            hour_str = now.strftime("%H")  # Only hour part

            #Unique key for one entry per hour
            key = (i, date_str, hour_str)

            #Check cache first (fast)
            if key in self.attendance_cache:
                return  #Already marked in this session

            # Otherwise check the file
            try:
                with open("attendance.csv", "r+", newline="\n") as f:
                    myDataList = f.readlines()

                    existing_records = []
                    for line in myDataList:
                        if line.strip():
                            parts = line.strip().split(",")
                            if len(parts) >= 6:
                                marked_id = parts[0]
                                marked_date = parts[5]
                                marked_hour = parts[4].split(":")[0]
                                existing_records.append((marked_id, marked_date, marked_hour))

                    if key not in existing_records:
                        f.seek(0, 2)  #move cursor to end
                        f.write(f"\n{i},{r},{n},{d},{time_str},{date_str},Present")
                        f.flush()  #force write
                        self.attendance_cache.add(key)  #store in cache

            except FileNotFoundError:
                # File doesn't exist, create it with headers
                with open("attendance.csv", "w", newline="\n") as f:
                    f.write("ID,Roll,Name,Dept,Time,Date,Status")
                    f.write(f"\n{i},{r},{n},{d},{time_str},{date_str},Present")
                    self.attendance_cache.add(key)

        except Exception as e:
            print(f"[Attendance Error] {e}")    


    def face_recog(self):
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            img = self.recognize(img, clf, faceCascade)
            cv2.imshow("WELCOME TO FACE RECOGNITION || PRESS ENTER KEY TO CLOSE", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
