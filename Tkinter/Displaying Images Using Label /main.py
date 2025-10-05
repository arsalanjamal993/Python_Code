from tkinter import *
arsalan_root = Tk()
arsalan_root.geometry("1255x944")
photo = PhotoImage(file="1.png")

# For .jpg formats
# image = Image.open("2.jpg")
# photo = ImageTk.PhotoImage(image)
larry_label = Label(image=photo)
larry_label.pack()
arsalan_root.mainloop()
  
