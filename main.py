from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox

from AddBook import *
from DeleteBooks import *
from ReturnBook import returnBook
from ViewBook import *
from issueBook import *

#=================================connecting to a database=========================================================

mypass = "" #use your own password
mydatabase="lms" #The database name
con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)
#root is the username here
cur = con.cursor() #cur -> cursor

"""=================================Designing a window================================"""
root=Tk()
root.title("Library Management System")
root.minsize(width=1366,height=760)
root.geometry("600x500")
"""=================================Adding a background Image================================"""
same=True
n=1.95
"""The image"""
background_image=Image.open("R .jfif")
[imageSizeWidth,imageSizeHeight]=background_image.size
newImageSizeWidth=int(imageSizeHeight*n)
if same:
    newImageSizeHeight=int(imageSizeHeight*n)
else:
    newImageSizeHeight=int(imageSizeHeight/n)
background_image=background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img=ImageTk.PhotoImage(background_image)
Canvas1=Canvas(root)
Canvas1.create_image(300,340,image=img)
Canvas1.config(bg="white",width=newImageSizeWidth,height=newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

"""==============================================setting up head frame=========================="""
headingFrame1=Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel=Label(headingFrame1,text="Welcome to \n Baraka SoftMakers Library",bg='black',fg='white',font=('Courier',15))
headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

"""============================================adding Buttons==================================="""
btn1=Button(root,text="Add Book Details",bg='black',fg='white',command=addBook)
btn1.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)

btn2=Button(root,text="Delete Book",bg='black',fg='white',command=delete)
btn2.place(relx=0.28,rely=0.5,relwidth=0.45,relheight=0.1)

btn3=Button(root,text="View Book List",bg='black',fg='white',command=View)
btn3.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.1)

btn4=Button(root,text="Issue Book to student",bg='black',fg='white',command=issueBook)
btn4.place(relx=0.28,rely=0.7,relwidth=0.45,relheight=0.1)

btn5=Button(root,text="Return Book",bg='black',fg='white',command=returnBook)
btn5.place(relx=0.28,rely=0.8,relwidth=0.45,relheight=0.1)

root.mainloop()
