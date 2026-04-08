from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class StudentDatabase:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2560x1600+0+0")  # screen size: width x height
        self.root.title("Student Database:")

        # VARIABLES
        self.var_id = StringVar()
        self.var_course = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_department = StringVar()
        self.var_semester = StringVar()
        self.var_year = StringVar()
        self.var_div = StringVar()

        # image path
        cover_img = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Face_Recognition_System\main_imgs\STUDENTDBPAGE.png")
        # image sizing and positioning
        # BG IMAGE
        cover_img = cover_img.resize((2560, 1600), Image.Resampling.LANCZOS)
        self.coverimg=ImageTk.PhotoImage(cover_img)
        bg_img =Label(self.root,image=self.coverimg)
        bg_img.place(x=0,y=0,width=2560,height=1600)

        # Main Frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=112,y=486,width=2333,height=1023)

        # DATA I/P FRAME

        # left label frame
        Left_frame= LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="STUDENT DETAILS:",font=("times new roman",20,"bold"))
        Left_frame.place(x=0,y=0,width=820,height=1018)
        
        # Current Course Frame
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information  ", font=("times new roman", 16, "bold"))
        current_course_frame.place(x=8, y=5, width=800, height=150)

        # Department
        dep_label = Label(current_course_frame, text="Department:", font=("times new roman", 15, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=15, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_department ,font=("times new roman", 15, "bold"), state="readonly", width=18)
        dep_combo["values"] = ("Select Department", "CSE-AIML", "CSE-AIDS", "IT", "CSBS")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=15, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course:", font=("times new roman", 15, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=15, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course ,font=("times new roman", 15, "bold"), state="readonly", width=18)
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=15, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year:", font=("times new roman", 15, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=15, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year ,font=("times new roman", 15, "bold"), state="readonly", width=18)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=15, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester:", font=("times new roman", 15, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=15, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester ,font=("times new roman", 15, "bold"), state="readonly", width=18)
        semester_combo["values"] = ("Select Semester", "Semester 1", "Semester 2", "Semester 3", "Semester 4","Semester 5", "Semester 6", "Semester 7", "Semester 8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=15, sticky=W)
        # Class Student Information Frame
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information  ", font=("times new roman", 16, "bold"))
        class_Student_frame.place(x=5, y=180, width=800, height=800)

        # Student ID
        studentId_label = Label(class_Student_frame, text="Student ID:", font=("times new roman",15, "bold"),bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_id, width=20, font=("times new roman",15, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_label = Label(class_Student_frame, text="Student Name:", font=("times new roman",15, "bold"),bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame,textvariable=self.var_name ,width=20, font=("times new roman",15, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_label = Label(class_Student_frame, text="Class Division:", font=("times new roman",15, "bold"),bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_div_entry = ttk.Entry(class_Student_frame,textvariable=self.var_div ,width=20, font=("times new roman",15, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(class_Student_frame, text="Roll No:", font=("times new roman",15, "bold"),bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll ,width=20, font=("times new roman",15, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_Student_frame, text="Gender:", font=("times new roman",15, "bold"),bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame,textvariable=self.var_gender ,font=("times new roman",15, "bold"), width=18, state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(class_Student_frame, text="DOB:", font=("times new roman",15, "bold"),bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob, width=20, font=("times new roman",15, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_Student_frame, text="Email:", font=("times new roman",15, "bold"),bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email ,width=20, font=("times new roman",15, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone
        phone_label = Label(class_Student_frame, text="Phone:", font=("times new roman",15, "bold"),bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame,textvariable=self.var_phone ,width=20, font=("times new roman",15, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_Student_frame, text="Address:", font=("times new roman",15, "bold"),bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address ,width=20, font=("times new roman",15, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacher_label = Label(class_Student_frame, text="Teacher Name:", font=("times new roman",15, "bold"),bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher ,width=20, font=("times new roman",15, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        #space
        teacher_label = Label(class_Student_frame, text="")
        teacher_label.grid(row=5, column=2)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1 ,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6, column=0)
        self.var_radio2 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1 ,text="No Photo Sample", value="No")
        radiobtn1.grid(row=6, column=1)

        # Buttons Frame
        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=265, width=787, height=44)

        save_btn = Button(btn_frame, text="Save",command=self.add_data ,width=15, font=("times new roman",15, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data ,width=16, font=("times new roman",15, "bold"), bg="green", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data ,width=16, font=("times new roman",15, "bold"), bg="red", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data ,width=16, font=("times new roman",15, "bold"), bg="orange", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame2 = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame2.place(x=5, y=320, width=787, height=44)
        
        takephotosample_btn = Button(btn_frame2, text="TAKE PHOTO SAMPLE",command=self.generate_dataset ,width=32, font=("times new roman",15, "bold"), bg="red", fg="white")
        takephotosample_btn.grid(row=0, column=0)

        updatephotosample_btn = Button(btn_frame2, text="UPDATE PHOTO SAMPLE", width=32, font=("times new roman",15, "bold"), bg="orange", fg="white")
        updatephotosample_btn.grid(row=0, column=1)

        #Image to cover space XD
        facerec_img = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Face_Recognition_System\main_imgs\facerecsamp.png")
        facerec_img = facerec_img.resize((780, 395), Image.Resampling.LANCZOS)
        self.facerecimg = ImageTk.PhotoImage(facerec_img)
        b1 = Button(self.root, image=self.facerecimg, cursor="hand2")
        b1.place(x=134, y=1100, width=780, height=395)

        # right label frame
        Right_frame= LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="DATABASE:",font=("times new roman",20,"bold"))
        Right_frame.place(x=830,y=0,width=1497,height=1018)

        # SEARCH SYSTEM
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System  ", font=("times new roman", 16, "bold"))
        search_frame.place(x=8, y=5, width=1478, height=73)

        searchby_label = Label(search_frame, text="Search by:",width=15, height=1, font=("times new roman",16, "bold"),bg="red", fg="white")
        searchby_label.grid(row=0, column=0,padx=15, sticky=W)

        # SEARCH COMBOBOX
        search_combo = ttk.Combobox(search_frame, font=("times new roman", 15, "bold"), state="readonly", width=25, height=55)
        search_combo["values"] = ("SELECT", "Roll Number", "Name", "Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=15, sticky=W)

        # ENTRY FILL
        search_entry = ttk.Entry(search_frame,width=35, font=("times new roman",15, "bold"))
        search_entry.grid(row=0, column=2, padx=22,sticky=W)

        # SEARCH BUTTONS
        search_btn = Button(search_frame, text="Search", width=20, font=("times new roman",15, "bold"), bg="red", fg="white")
        search_btn.grid(row=0, column=3,padx=15, sticky=W)

        searchall_btn = Button(search_frame, text="Search All", width=20, font=("times new roman",15, "bold"), bg="orange", fg="white")
        searchall_btn.grid(row=0, column=4,padx=15, sticky=W)

        #table frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=8, y=80, width=1478, height=900) 

        scroll_x= ttk.Scrollbar(table_frame, orient= HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame, orient= VERTICAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        #  Treeview 
        self.student_table = ttk.Treeview(table_frame,columns=("ID", "NAME", "ROLL", "GENDER", "DOB", "EMAIL", "PHONE", "ADDRESS", "TEACHER", "DEPARTMENT","COURSE" ,"SEMESTER","DIV", "YEAR", "PHOTO"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.configure(command=self.student_table.xview)
        scroll_y.configure(command=self.student_table.yview)
        self.student_table.heading("ID", text="Student ID")
        self.student_table.heading("NAME", text="Name")
        self.student_table.heading("ROLL", text="Roll No")
        self.student_table.heading("GENDER", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("EMAIL", text="Email")
        self.student_table.heading("PHONE", text="Phone")
        self.student_table.heading("ADDRESS", text="Address")
        self.student_table.heading("TEACHER", text="Teacher Name")
        self.student_table.heading("DEPARTMENT", text="Department")
        self.student_table.heading("COURSE", text="Course")
        self.student_table.heading("SEMESTER", text="Semester")
        self.student_table.heading("DIV", text="Division")
        self.student_table.heading("YEAR", text="Year")
        self.student_table.heading("PHOTO", text="Photo")

        self.student_table["show"] = "headings"

        self.student_table.column("ID", width=100, anchor="center")
        self.student_table.column("NAME", width=150)
        self.student_table.column("ROLL", width=100)
        self.student_table.column("GENDER", width=100, anchor="center")
        self.student_table.column("DOB", width=100, anchor="center")
        self.student_table.column("EMAIL", width=150)
        self.student_table.column("PHONE", width=120)
        self.student_table.column("ADDRESS", width=200)
        self.student_table.column("TEACHER", width=150)
        self.student_table.column("DEPARTMENT", width=150)
        self.student_table.column("COURSE", width=120, anchor="center")
        self.student_table.column("SEMESTER", width=120, anchor="center")
        self.student_table.column("DIV", width=120, anchor="center")
        self.student_table.column("YEAR", width=120, anchor="center")
        self.student_table.column("PHOTO", width=120, anchor="center")

        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.student_table.pack(fill=BOTH, expand=1)
        self.fetch_data()

        #Apply Styling
        style = ttk.Style()
        style.configure("Treeview",font=("times new roman", 13),rowheight=25)
        style.configure("Treeview.Heading",font=("times new roman", 15, "bold"))

    #FUNCTION DECLARATION
    def add_data(self):
        if self.var_department.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All feilds are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="127.0.0.1",user="root",password="@ArtasHteh1730",database="face_recognizer",auth_plugin="mysql_native_password")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (
                                    self.var_id.get(),
                                    self.var_name.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get(),
                                    self.var_teacher.get(),
                                    self.var_department.get(),
                                    self.var_course.get(),
                                    self.var_semester.get(),
                                    self.var_div.get(),
                                    self.var_year.get(),
                                    self.var_radio1.get(),
                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Data has been Saved!", parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}", parent=self.root)
        
    #FETCH,SAVE AND PRINT DATA
    def fetch_data(self):
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="@ArtasHteh1730",database="face_recognizer",auth_plugin="mysql_native_password")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close()

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        if data:   # only if row is not empty
            self.var_id.set(data[0])
            self.var_name.set(data[1])
            self.var_roll.set(data[2])
            self.var_gender.set(data[3])
            self.var_dob.set(data[4])
            self.var_email.set(data[5])
            self.var_phone.set(data[6])
            self.var_address.set(data[7])
            self.var_teacher.set(data[8])
            self.var_department.set(data[9])
            self.var_course.set(data[10])
            self.var_semester.set(data[11])
            self.var_div.set(data[12])
            self.var_year.set(data[13])
            self.var_radio1.set(data[14])

    def update_data(self):
        if self.var_name.get()=="" or self.var_id.get()=="":
                messagebox.showerror("Error", "All feilds are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student data?", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="127.0.0.1",user="root",password="@ArtasHteh1730",database="face_recognizer",auth_plugin="mysql_native_password")
                    my_cursor = conn.cursor()
                    my_cursor.execute("""
                        UPDATE student SET name=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, department=%s,course=%s, semester=%s, division=%s, year=%s, photoupload=%s WHERE studentid=%s""", 
                    (
                        self.var_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_department.get(),
                        self.var_course.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_year.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))
                    messagebox.showinfo("Success", "Student Data Updated Successfully!", parent=self.root)
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error", "Student ID is required for delete", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="127.0.0.1",user="root",password="@ArtasHteh1730",database="face_recognizer",auth_plugin="mysql_native_password")
                    my_cursor = conn.cursor()
                    my_cursor.execute("DELETE FROM student WHERE studentid=%s", (self.var_id.get(),))
                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo("Delete", "Student Data Deleted Successfully!", parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Male")   # default option
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_department.set("Select Department")
        self.var_course.set("")
        self.var_semester.set("")
        self.var_div.set("")
        self.var_year.set("")
        self.var_radio1.set("")

    # FACE DATA
    def generate_dataset(self):
        if self.var_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "Student ID and Name are required", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(host="127.0.0.1",user="root",password="@ArtasHteh1730",database="face_recognizer",auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()

            my_cursor.execute("""
                UPDATE student SET name=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, 
                teacher=%s, department=%s, course=%s, semester=%s, division=%s, year=%s, photoupload=%s 
                WHERE studentid=%s
            """, (
                self.var_name.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_department.get(),
                self.var_course.get(),
                self.var_semester.get(),
                self.var_div.get(),
                self.var_year.get(),
                "Yes",     
                self.var_id.get()
            ))
            conn.commit()
            conn.close()

            data_path = os.path.join(os.getcwd(), "data")
            if not os.path.exists(data_path):
                os.makedirs(data_path)
                
            face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

            def face_crop(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    return img[y:y+h, x:x+w]
                return None

            cap = cv2.VideoCapture(0)
            img_id = 0

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                cropped_face = face_crop(frame)

                if cropped_face is not None:
                    img_id += 1
                    face = cv2.resize(cropped_face, (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                    file_name_path = os.path.join(data_path, f"user.{self.var_id.get()}.{img_id}.jpg")
                    cv2.imwrite(file_name_path, face)

                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)

                if cv2.waitKey(1) == 13 or img_id == 100:  # ENTER key or 100 images
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Dataset Generation Completed!", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)






if __name__ == "__main__":
    root = Tk()
    obj = StudentDatabase(root)
    root.mainloop()
