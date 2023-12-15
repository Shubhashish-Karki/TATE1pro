import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x100")

label = ctk.CTkLabel(master=app, text="Welcome!")
label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

button = ctk.CTkButton(master=app, text="Start")
button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

app.mainloop()
