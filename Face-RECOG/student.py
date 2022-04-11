from cProfile import label
from cgitb import handler, text
from tkinter import*
from tkinter import ttk
from tkinter import font
from turtle import title 
from PIL import Image,ImageTk
# from student import Student


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Img1
        img = Image.open(r"C:\Users\parit\OneDrive\Desktop\Face-RECOG\Images\StudentInfo.png")
        img = img.resize((500,130))
        self.photoimg = ImageTk.PhotoImage(img)


        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


# Img 2
        img1 = Image.open(r"C:\Users\parit\OneDrive\Desktop\Face-RECOG\Images\FaceRecog.jpg")
        img1 = img1.resize((500,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)


        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


# img 3
        img2 = Image.open(r"C:\Users\parit\OneDrive\Desktop\Face-RECOG\Images\database.png")
        img2 = img2.resize((500,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)


        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

# img bg

        img3 = Image.open(r"C:\Users\parit\OneDrive\Desktop\Face-RECOG\Images\project.png")
        img3 = img3.resize((1530,710))
        self.photoimg3 = ImageTk.PhotoImage(img3)


        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img, text="Student Management System.",font=("helvetica", 25,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=720,height=580)

        img_left=Image.open(r"C:\Users\parit\OneDrive\Desktop\Face-RECOG\Images\left.jpg")
        img_left=img_left.resize((720,130)) 
        self.photoimg_left=ImageTk.PhotoImage(img_left)


        f_lb1=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        
        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        current_course_frame.place(x=5,y=130,width=720,height=125)


        dep_label=Label(current_course_frame,text="Department",font=("time new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,font=("time new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("select Department","computer","it","entc","mech")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_combo=Label(current_course_frame,text="Department",font=("time new roman",12,"bold"),bg="white")
        course_combo.grid(row=0,column=0,padx=10,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,font=("time new roman",12,"bold"),state="readonly")
        course_combo["values"]=("select Courses","FE","SE","TE","Be")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #year
        year_combo=Label(current_course_frame,text="Department",font=("time new roman",12,"bold"),bg="white")
        year_combo.grid(row=0,column=0,padx=10)

        year_combo=ttk.Combobox(current_course_frame,font=("time new roman",12,"bold"),state="readonly")
        year_combo["values"]=("select Your Year","2020_21","2021 -22","2022_23","2023_24")
        year_combo.current(0)
        year_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Department",font=("time new roman",12,"bold"),bg="white")
        semester_label.grid(row=0,column=0,padx=10)

        semester_combo=ttk.Combobox(current_course_frame,font=("time new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("select Semester","Sem_2","Sem_2")
        semester_combo.current(0)
        semester_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #class student info
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("time new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)

        #studentid
        studentId_label=Label(current_course_frame,text="StudentID",font=("time new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student Name
        studentName_label=Label(current_course_frame,text="Student Name",font=("time new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(current_course_frame,text=" class division",font=("time new roman",12,"bold"),bg="white")
        class_div_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll number
        roll_no_label=Label(current_course_frame,text="Roll No",font=("time new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #gender
        gender_label=Label(current_course_frame,text="Gender",font=("time new roman",12,"bold"),bg="white")
        gender_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        gender_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #DOb
        dob_label=Label(current_course_frame,text="DOB",font=("time new roman",12,"bold"),bg="white")
        dob_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #phone no
        phone_label=Label(current_course_frame,text="Phone no",font=("time new roman",12,"bold"),bg="white")
        phone_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        phone_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(current_course_frame,text="fmail",font=("time new roman",12,"bold"),bg="white")
        email_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #adress
        adress_label=Label(current_course_frame,text="Adress",font=("time new roman",12,"bold"),bg="white")
        adress_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        adress_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        adress_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Teacher name
        teacher_label=Label(current_course_frame,text="Teacher Name",font=("time new roman",12,"bold"),bg="white")
        teacher_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #radio Buttons
        radionbtn1=ttk.Radiobutton(class_student_frame,text="take photo sample",value="yes")
        radionbtn1.grid(row=6,column=0)

        radionbtn2=ttk.Radiobutton(class_student_frame,text=" No photo sample",value="yes")
        radionbtn2.grid(row=6,column=1)

        #bbuttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=70)

        save_btn=Button(btn_frame,text="save",font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,text="Take a photo",font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=2)

        update_btn=Button(btn_frame,text="Update photo",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delet the photo",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)



        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame,text="Take a photo",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update photo",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=0)


        #right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=720,height=580)

        img_right=Image.open(r"C:\Users\parit\OneDrive\Desktop\Face-RECOG\Images\Exit.jpg")
        img_right=img_right.resize((720,130))
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lb1.Label=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #search system
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("time new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(search_frame,text="Search By:",font=("time new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        search_combo=ttk.Combobox(current_course_frame,font=("time new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("select", "Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry=ttk.Entry(search_frame,width=12,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)



        search_btn=Button(btn_frame,text="Delete",font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        showall_btn=Button(btn_frame,text="Reset",font=("times new roman",13,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4)


        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","phone","adress","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        # self.student_table.heading("fmail",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("adress",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"


        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.column("dep",width=100)


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()


