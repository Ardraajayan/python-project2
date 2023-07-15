from tkinter import *
root = Tk()

root.geometry("400x250")

def getval():
    print("Accepted")

# create Heading
Label(root, text = "STUDENT REGISTRATION FORM", font ="arial 15 bold").grid(row=0, column=3)

# Field Names

name = Label(root, text ="Name")
gender = Label(root, text ="Gender")
course = Label(root, text ="Course")
mobile = Label(root, text ="Mobile")
mail = Label(root, text ="E-mail")
place = Label(root, text ="Location")

# Packing Fields

name.grid(row=1,column=2)
gender.grid(row=2,column=2)
course.grid(row=3,column=2)
mobile.grid(row=4,column=2)
mail.grid(row=5,column=2)
place.grid(row=6,column=2)

# Store it in variables

name_value = StringVar
gender_value = StringVar
course_value = StringVar
mobile_value = StringVar
mail_value = StringVar
location_value = StringVar
check_value = IntVar

# Creating entry Fields

name_entry = Entry(root, textvariable =name_value)
gen_entry = Entry(root, textvariable = gender_value)
course_entry = Entry(root, textvariable = course_value)
mob_entry = Entry(root, textvariable= mobile_value)
mail_entry = Entry(root, textvariable=mail_value)
place_entry = Entry(root, textvariable= location_value)

# Packing entry fields

name_entry.grid(row=1,column=3)
gen_entry.grid(row=2,column=3)
course_entry.grid(row=3,column=3)
mob_entry.grid(row=4,column=3)
mail_entry.grid(row=5,column=3)
place_entry.grid(row=6,column=3)

# Check box

check = Checkbutton(text = "confirm",variable= check_value)
check.grid(row=7,column=3)

#Submitt Button

Button(text = "Submit",command=getval).grid(row=8,column=3)

root.mainloop()