from tkinter import *
from tkinter import messagebox
import random
import json
# search particular site detail in data
reps =0
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass_input.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [random.choice(letters) for _ in range(random.randint(1,8))]
    no_of_digits = [random.choice(numbers) for _ in range(random.randint(1,5))]
    no_of_symbols =[random.choice(symbols) for _ in range(random.randint(1,5))]

    password_list = pass_letters + no_of_digits+ no_of_symbols

    random.shuffle(password_list)
    final="".join(password_list)

    pass_input.insert(0,final)

# ---------------------------- SEARCH WEBSITES DETAIL ------------------------------- #

def search():
    website = web_input.get()
    try:
        with open("data.json") as data:
            details = json.load(data)
    except:
        messagebox.showerror(title=f'file missing',message="file is missing")
    else:
        
        if website in details:
            email = details[website]["email"]
            password = details[website]["password"]
            messagebox.showinfo(title="search detail", message=f"the detail of  {website} :"
                                                               f"\nEmail = {email}\nPassword = {password}")
        else:
            messagebox.showinfo(title="Details not found", message=f"the detail of {website} is not in data")






# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_input.get()
    email = mail_input.get()
    password = pass_input.get()
    details ={website : {
                    "email": email,
                    "password": password
    }}

    if len(website) == 0 or len(email)==0 or len(password) ==0:
        messagebox.showwarning(title="OOPS",message="please make sure no fields are empty")



    else:

        # it gives value in boolean
        user_answer = messagebox.askokcancel(title="User Details", message=f'The details you filled are\n'
                     f'Website = {website}\nEmail = {email}\nPassword = {password}\ndo you want to save ?')

        if user_answer:
            try:
                with open("data.json",'r') as data_file:
                    my_data = json.load(data_file)
                    if website in my_data:
                            already_filled_mail = my_data[website]["email"]
                            already_filled_pass = my_data[website]["password"]

                            wish_to_change = messagebox.askyesno(title="Oops",
                                                                    message=f"details for this {website} is already in data"
                                                                        f"\nhere are the details"
                                                                        f"\nemail = { already_filled_mail}"
                                                                        f"\npassword = {already_filled_pass}"
                                                                        f"\ndo you wish to change it ?")
                            if not wish_to_change:
                              return


            except :
                with open("data.json", 'w') as data_file:
                    json.dump(details, data_file, indent=4)

            else:

                my_data.update(details)

                with open("data.json",'w') as data_file:
                    json.dump(my_data,data_file,indent=4)

            finally:
                    web_input.delete(0,END)
                    mail_input.delete(0,END)
                    pass_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("my password manager")
window.config(padx=40, pady=40)


canvas = Canvas(width=200, height=200, highlightthickness=0)
img_location = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img_location)
canvas.grid(column=1, row=0)



# labels
website_name = Label(text = "Website:", font=('courier', 12, "normal"))
website_name.grid(column=0,row=1)
website_user_id = Label(text = "Email/Username:", font=('courier', 12, "normal"))
website_user_id.grid(column=0,row=2)
pass_name = Label(text ="Password:", font=('courier', 12, "normal"))
pass_name.grid(column=0,row=3)

# entries

web_input = Entry(width=32)
web_input.focus()
web_input.grid(row=1,column=1,columnspan = 2,sticky="w", pady=5)

mail_input = Entry(width=40)
mail_input.grid(row=2,column=1,columnspan = 2,sticky="ew", pady=5)

pass_input = Entry(width=32)
pass_input.grid(row=3,column=1,sticky="w",pady=5)



# buttons
pass_generate = Button(text='Generate',font=('courier',8,'normal'),width=14,bg='#3d85c6'
                       ,highlightthickness=0, command=generate_password)
pass_generate.grid(row=3, column=2, sticky="e",pady=5)
add_button =  Button(text='Add',width=40,command= save_data,bg='#8fce00',
                       highlightthickness=0)
add_button.grid(row=4, column=1,columnspan = 2,sticky="ew",pady=5)
search_generate = Button(text='Search',font=('courier',8,'normal'),width=14,highlightthickness=0,
                         bg='#3d85c6',command=search)
search_generate.grid(row=1, column=2, sticky="e",pady=5)


window.mainloop()