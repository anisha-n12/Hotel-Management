from tkinter import messagebox
from tkinter import ttk
import sqlite3
from datetime import datetime
from tkinter import *
from tkinter import messagebox, Tk, Frame, Entry, Button


mydb = sqlite3.connect('lodging6.db')
try:
    mydb.execute("CREATE TABLE if not exists `customer_data` (`custom_id` INTEGER Primary Key Autoincrement ,"
                 "`custom_name` TEXT DEFAULT NULL,`custom_ph_no` TEXT DEFAULT NULL,`custom_address` TEXT DEFAULT NULL,"
                 "`custom_email` TEXT DEFAULT NULL,`custom_gender` TEXT DEFAULT NULL,`custom_nationality` TEXT DEFAULT "
                 "NULL,`custom_checkin` date DEFAULT NULL,`custom_checkout` date DEFAULT NULL);")
    mydb.execute("CREATE TABLE if not exists `room_allot` (`room_no` int  NOT NULL,`preference` TEXT DEFAULT NULL,"
                 "`custom_id` int DEFAULT NULL,`occupied` TEXT DEFAULT NULL,PRIMARY KEY (`room_no`),FOREIGN KEY "
                 "(`custom_id`) REFERENCES `customer_data` (`custom_id`));")
    mydb.execute("INSERT INTO `room_allot`(`room_no`, `preference`, `occupied`)  VALUES (101,'S_N/AC','no'),"
                 "(102,'S_N/AC','no'),(103,'S_AC','no'),(104,'S_AC','no'),(201,'L_N/AC','no'),(202,'L_N/AC','no'),"
                 "(203,'L_AC','no'),(204,'L_AC','no');")
except:
    pass


class Main_Menu:
    def __init__(self):
        self.window = Tk()
        self.window.configure(bg='#FAEBD7')
        self.window.title("Main Menu")
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.window.geometry('%dx%d' % (width, height))
        self.head_frame = Frame(self.window, bg="#A52A2A", highlightbackground="black", highlightthickness=5)
        self.head_frame.place(x=0, y=20, height=160, width=width)
        # project = Label(self.window,  text='''Python Project by-   Tanvi Chaudhari (206007)
        #                            Mandar Marathe (206017)
        #                            Anisha Nemade (206018)''', font="Times 15 bold", justify="left", bg="#A52A2A",
        #                 fg="#FFFFFF")
        # project.place(x=30, y=90)

        heading = Label(self.window, text="HOTEL MANAGEMENT SYSTEM", font="Times 40 bold", justify="center", bg="#A52A2A",
                        fg="#FFFFFF")
        heading.place(x=350, y=25)
        welcome = Label(self.window, text="WELCOME", font="Times 48 bold", justify="center",
                        bg="#FAEBD7",
                        fg="#000000")
        welcome.place(x=600, y=200)
        b_Restaurant = Button(self.window, text="Restaurant", font="Times 30 bold", justify="center", command= self.open_restro)
        b_Lodging = Button(self.window, text="Lodging", font="Times 30 bold", justify="center", command= self.open_lodge)
        b_Lodging.place(x=500, y=330, width=500, height=70)
        b_Restaurant.place(x=500, y=430, width=500, height=70)
        b_Exit = Button(self.window, text="Exit", font="Times 30 bold", justify="center", command=self.Exit_System)
        b_Exit.place(x=500, y=530, width=500, height=70)
        self.window.mainloop()
    def Exit_System(self):
        self.window.destroy()

    def open_restro(self):
        self.window.destroy()
        self.restaurant()

    def open_lodge(self):#074463
        self.window.destroy()
        MainMenu()

    def restaurant(self):
        root = Tk()
        root.configure(bg='#A52A2A')
        root.title("Restaurant System")
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry('%dx%d' % (width, height))

        bg_color = "#A52A2A"

        # label=Label(root,text="clicked").place(x=0,y=0)

        # variables
        pizza1 = IntVar()
        pizza2 = IntVar()
        pizza3 = IntVar()
        pizza4 = IntVar()

        sandwich1 = IntVar()
        sandwich2 = IntVar()
        sandwich3 = IntVar()
        sandwich4 = IntVar()

        icecream1 = IntVar()
        icecream2 = IntVar()
        icecream3 = IntVar()
        icecream4 = IntVar()

        amount = StringVar()
        tax = StringVar()
        totalamt = StringVar()
        customer_name= StringVar()
        customer_id= IntVar()

        # functions
        def totalbutton():
            if pizza1.get() == 0 and pizza2.get() == 0 and pizza3.get() == 0 and pizza4.get() == 0 and icecream1.get() == 0 and icecream2.get() == 0 and icecream3.get() == 0 and icecream4.get() == 0 and sandwich1.get() == 0 and sandwich2.get() == 0 and sandwich3.get() == 0 and sandwich4.get() == 0:
                messagebox.showerror('error')
            else:

                t = (pizza1.get() * 200 +
                     pizza2.get() * 220 +
                     pizza3.get() * 300 +
                     pizza4.get() * 250 +
                     icecream1.get() * 50 +
                     icecream2.get() * 50 +
                     icecream3.get() * 50 +
                     icecream4.get() * 50 +
                     sandwich1.get() * 30 +
                     sandwich2.get() * 35 +
                     sandwich3.get() * 40 +
                     sandwich4.get() * 30
                     )
                amount.set(t)
                tx = (t * 0.2)
                tax.set(tx)
                ta = tx + t
                totalamt.set(ta)

        def end_button():
            root.destroy()
            Main_Menu()
        def clear_all():
            rec.delete("1.0", "end")
            pizza1.set(0)
            pizza2.set(0)
            pizza3.set(0)
            pizza4.set(0)
            icecream1.set(0)
            icecream2.set(0)
            icecream4.set(0)
            icecream3.set(0)
            sandwich1.set(0)
            sandwich2.set(0)
            sandwich3.set(0)
            sandwich4.set(0)
            amount.set('0')
            tax.set('0')
            totalamt.set('0')

        def receipt():
            rec.delete(1.0, END)
            # l=Label(root,text="skdjf").place(x=0,y=0)
            rec.insert(END, '===============Receipt===============\n\n')
            rec.insert(END, "Customer Name : {}\n".format(customer_name.get()))
            rec.insert(END, "Customer ID : {}\n\n".format(customer_id.get()))
            rec.insert(END, '***************************************\n')
            rec.insert(END, ' Item Name        ')
            rec.insert(END, 'Quantities         ')
            rec.insert(END, ' Rate\n')
            rec.insert(END, '\n')
            if pizza1.get() != 0:
                rec.insert(END, f' pizza\t\t{pizza1.get()}\t {int(pizza1.get() * 200)} \n')

            if pizza2.get() != 0:
                rec.insert(END, f' pizza\t\t{pizza2.get()}\t {int(pizza2.get() * 220)} \n')
            if pizza3.get() != 0:
                rec.insert(END, f' pizza\t\t{pizza3.get()}\t {int(pizza3.get() * 300)} \n')
            if pizza4.get() != 0:
                rec.insert(END, f' pizza\t\t{pizza4.get()}\t {int(pizza4.get() * 250)} \n')

            if icecream1.get() != 0:
                rec.insert(END, f' icecream1\t\t{icecream1.get()}\t {int(icecream1.get() * 50)}\n')
            if icecream2.get() != 0:
                rec.insert(END, f' icecream1\t\t{icecream2.get()}\t {int(icecream2.get() * 50)}\n')
            if icecream3.get() != 0:
                rec.insert(END, f' icecream1\t\t{icecream3.get()}\t {int(icecream3.get() * 50)}\n')
            if icecream4.get() != 0:
                rec.insert(END, f' icecream1\t\t{icecream4.get()}\t {int(icecream4.get() * 50)}\n')

            if sandwich1.get() != 0:
                rec.insert(END, f' sandwich1\t\t{sandwich1.get()}\t {int(sandwich1.get() * 30)}\n')
            if sandwich2.get() != 0:
                rec.insert(END, f' sandwich2\t\t{sandwich2.get()}\t {int(sandwich2.get() * 35)}\n')
            if sandwich3.get() != 0:
                rec.insert(END, f' sandwich3\t\t{sandwich3.get()}\t {int(sandwich3.get() * 40)}\n')
            if sandwich4.get() != 0:
                rec.insert(END, f' sandwich4\t\t{sandwich4.get()}\t {int(sandwich4.get() * 30)}\n')
            rec.insert(END, '***************************************\n')
            rec.insert(END, f'Amount :\t\t {amount.get()}\n')
            rec.insert(END, f'Tax :\t\t {tax.get()}\n')
            rec.insert(END, f'Total :\t\t {totalamt.get()}\n')

        title = Label(root, text="Restaurant", bd=12, relief=RIDGE, bg=bg_color, fg="white",
                      font=("times new roman", 30, "bold"), pady=2)
        title.pack(fill=X)

        F1 = LabelFrame(root, text="Customer Details", font=("times new roman", 15, "bold"), bd=4, fg="gold",
                        bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", font=("times new roman", 15, "bold"), bg=bg_color, fg="white")
        cname_lbl.grid(row=0, column=0, padx=5)
        cname_txt = Entry(F1, width=20, font="arial 15", textvariable=customer_name)
        cname_txt.grid(row=0, column=1, padx=10, pady=5)

        cno_lbl = Label(F1, text="Customer Number", font=("times new roman", 15, "bold"), bg=bg_color, fg="white")
        cno_lbl.grid(row=0, column=2, padx=5)
        cno_txt = Entry(F1, width=20, font="arial 15", textvariable=customer_id)
        cno_txt.grid(row=0, column=3, padx=10, pady=5)

        #cbill_lbl = Label(F1, text="Bill No.", font=("times new roman", 15, "bold"), bg=bg_color, fg="white").grid(
        #    row=0, column=4, padx=5)
        #cbill_txt = Entry(F1, width=20, font="arial 15", textvariable=customer_id).grid(row=0, column=5, padx=10, pady=5)

        #search_btn = Button(F1, text="Search", font="arial 16 bold", width=10).grid(row=0, column=6, padx=10, pady=5)

        ##########  Pizza Frame #############
        F2 = LabelFrame(root, text=" Pizza", font=("times new roman", 15, "bold"), bd=4, fg="gold",
                        bg=bg_color)
        F2.place(x=0, y=170, width=325, height=380)

        pizza1_lbl = Label(F2, text="Cheese Pizza", font=("times new roman ", 16, "bold"), bg=bg_color,
                           fg="white")
        pizza1_lbl.grid(row=0, column=0, padx=10, pady=5)
        pizza1_txt = Entry(F2, textvariable=pizza1, width=10, font="arial 15", bd=4)
        pizza1_txt.grid(row=0, column=1, padx=10, pady=5)

        pizza2_lbl = Label(F2, text="Corn Pizza", font=("times new roman ", 16, "bold"), bg=bg_color, fg="white")
        pizza2_lbl.grid(row=1, column=0, padx=10, pady=5)
        pizza2_txt = Entry(F2, textvariable=pizza2, width=10, font="arial 15", bd=4)
        pizza2_txt.grid(row=1, column=1, padx=10, pady=5)

        pizza3_lbl = Label(F2, text="Onion Pizza", font=("times new roman ", 16, "bold"), bg=bg_color, fg="white")
        pizza3_lbl.grid( row=2, column=0, padx=10, pady=5)
        pizza3_txt = Entry(F2, textvariable=pizza3, width=10, font="arial 15", bd=4)
        pizza3_txt.grid(row=2, column=1, padx=10, pady=5)

        pizza4_lbl = Label(F2, text="Paneer Pizza", font=("times new roman ", 16, "bold"), bg=bg_color,fg="white")
        pizza4_lbl.grid( row=3, column=0, padx=10, pady=5)
        pizza4_txt = Entry(F2, textvariable=pizza4, width=10, font="arial 15", bd=4)
        pizza4_txt.grid(row=3, column=1, padx=10, pady=5)

        ##########  Sandwich  Frame #############
        F3 = LabelFrame(root, text=" Sandwich", font=("times new roman", 15, "bold"), bd=4, fg="gold",
                        bg=bg_color)
        F3.place(x=325, y=170, width=325, height=380)

        sandwich1_lbl = Label(F3, text="Cheese Sandwich", font=("times new roman ", 16, "bold"), bg=bg_color,
                              fg="white").grid(
            row=0, column=0, padx=10, pady=5)
        sandwich1_txt = Entry(F3, textvariable=sandwich1, width=8, font="arial 15", bd=4).grid(row=0, column=1, padx=5,
                                                                                               pady=5)

        sandwich2_lbl = Label(F3, text="Corn Sandwich", font=("times new roman ", 16, "bold"), bg=bg_color,
                              fg="white").grid(
            row=1, column=0, padx=5, pady=5)
        sandwich2_txt = Entry(F3, textvariable=sandwich2, width=8, font="arial 15", bd=4).grid(row=1, column=1, padx=10,
                                                                                               pady=5)

        sandwich3_lbl = Label(F3, text="Onion Sandwich", font=("times new roman ", 16, "bold"), bg=bg_color,
                              fg="white").grid(
            row=2, column=0, padx=5, pady=5)
        sandwich3_txt = Entry(F3, textvariable=sandwich3, width=8, font="arial 15", bd=4).grid(row=2, column=1, padx=5,
                                                                                               pady=5)

        sandwich4_lbl = Label(F3, text="Paneer Sandwich", font=("times new roman ", 16, "bold"), bg=bg_color,
                              fg="white").grid(
            row=3, column=0, padx=5, pady=5)
        sandwich4_txt = Entry(F3, textvariable=sandwich4, width=8, font="arial 15", bd=4).grid(row=3, column=1, padx=5,
                                                                                               pady=5)

        ##########  Ice cream Frame #############
        F4 = LabelFrame(root, text=" Ice Cream", font=("times new roman", 15, "bold"), bd=4, fg="gold", bg=bg_color)
        F4.place(x=650, y=170, width=325, height=380)

        icecream1_lbl = Label(F4, text="Chocolate", font=("times new roman ", 16, "bold"), bg=bg_color,
                              fg="white").grid(row=0, column=0, padx=10, pady=5)
        icecream1__txt = Entry(F4, textvariable=icecream1, width=8, font="arial 15", bd=4).grid(row=0, column=1, padx=5,
                                                                                                pady=5)

        icecream2_lbl = Label(F4, text="Vanilla", font=("times new roman ", 16, "bold"), bg=bg_color, fg="white")
        icecream2_lbl.grid(row=1, column=0, padx=5, pady=5)
        icecream2_txt = Entry(F4, textvariable=icecream2, width=8, font="arial 15", bd=4)
        icecream2_txt.grid(row=1, column=1, padx=10,
                                                                                               pady=5)

        icecream3_lbl = Label(F4, text="Butter Scotch", font=("times new roman ", 16, "bold"), bg=bg_color,
                              fg="white")
        icecream3_lbl.grid(row=2, column=0, padx=5, pady=5)
        icecream3_txt = Entry(F4, textvariable=icecream3, width=8, font="arial 15", bd=4)
        icecream3_txt.grid(row=2, column=1, padx=5,pady=5)

        icecream4_lbl = Label(F4, text="Mango", font=("times new roman ", 16, "bold"), bg=bg_color, fg="white").grid(
            row=3, column=0, padx=5, pady=5)
        icecream4_txt = Entry(F4, textvariable=icecream4, width=8, font="arial 15", bd=4).grid(row=3, column=1, padx=5,
                                                                                               pady=5)

        F5 = Frame(root, bd=4, relief=RIDGE).place(x=1000, y=180, width=405, height=480)
        bill_lbl = Label(F5, text="Bill", font=("times new roman", 16, "bold"), bg="white", width=26).place(x=1003,
                                                                                                                 y=183, width=400)

        F6 = LabelFrame(root, text=" Calculation", font=("times new roman", 15, "bold"), bd=4, fg="gold", bg=bg_color)
        F6.place(x=0, y=560, width=975, height=380)

        amt_lbl = Label(F6, text="Amount", font=("times new roman", 15, "bold"), bg=bg_color, fg="white").grid(row=0,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=5)
        amt_txt = Entry(F6, textvariable=amount, font="arial 15", bd=4, width=10).grid(row=0, column=1, padx=10)

        tax_lbl = Label(F6, text="Tax", font=("times new roman", 15, "bold"), bg=bg_color, fg="white").grid(row=1,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=5)
        tax_txt = Entry(F6, textvariable=tax, font="arial 15", bd=4, width=10).grid(row=1, column=1, padx=10)

        total_lbl = Label(F6, text="Total", font=("times new roman", 15, "bold"), bg=bg_color, fg="white")
        total_lbl.grid(row=2, column=0, padx=10, pady=5)
        total_txt = Entry(F6, textvariable=totalamt, font="arial 15", bd=4, width=10)
        total_txt.grid(row=2, column=1, padx=10)

        F7 = LabelFrame(root, text=" Buttons", font=("times new roman", 15, "bold"), bd=4, fg="gold", bg=bg_color)
        F7.place(x=480, y=550, width=495, height=380)

        btn1 = Button(F7, text="total", font=("times new roman", 15, "bold"), width=15, command=totalbutton)
        btn1.grid(row=0, column=0, padx=20, pady=10)
        btn2 = Button(F7, text="Generate bill", font=("times new roman", 15, "bold"), width=15, command=receipt)
        btn2.grid( row=0, column=1, padx=20, pady=10)
        btn3 = Button(F7, text="Clear", font=("times new roman", 15, "bold"), width=15, command= clear_all)
        btn3.grid(row=1, column=0, padx=20, pady=10)
        btn4 = Button(F7, text="Exit", font=("times new roman", 15, "bold"), width=15, command= end_button)
        btn4.grid(row=1, column=1, padx=20, pady=10)
        rec = Text(root, font=("times new roman", 15, "bold"))
        rec.place(x=1004, y=217, width=400, height=550)
        root.mainloop()



class MainMenu:
    def __init__(self):
        self.window = Tk()
        self.window.configure(bg='#FAEBD7')
        self.window.title("Lodging System")
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.window.geometry('%dx%d' % (width, height))
        side_menu = Frame(self.window, bg='#FAEBD7')
        side_menu.place(x=0, y=100, height=800, width=200)
        self.head_frame = Frame(self.window, bg="#A52A2A", highlightbackground="black", highlightthickness=5)
        self.head_frame.place(x=0, y=20, height=80, width=width)
        heading = Label(self.window, text="~LODGING SYSTEM~", font="Times 40 bold", justify="center", bg="#A52A2A",
                        fg="#FFFFFF")
        heading.place(x=450, y=25)
        self.show_pr_data = Frame(self.window, bg='#FAEBD7')
        self.show_pr_data.place(x=1060, y=100, height=800, width=500)
        b_roominfo = Button(side_menu, text="Rooms", font="Times 15 bold", justify="center", command=self.room_command)
        b_booking = Button(side_menu, text="Booking", font="Times 15 bold", justify="center",
                           command=self.booking_command)
        b_customers = Button(side_menu, text="Customers", font="Times 15 bold", justify="center",
                             command=self.customers_command)
        b_billing = Button(side_menu, text="Billing", font="Times 15 bold", justify="center",
                           command=self.billing_command)
        b_Exit = Button(side_menu, text="Exit", font="Times 15 bold", justify="center",
                           command=self.end_button)
        b_roominfo.place(x=10, y=10, width=190, height=50)
        b_booking.place(x=10, y=70, width=190, height=50)
        b_customers.place(x=10, y=140, width=190, height=50)
        b_billing.place(x=10, y=210, width=190, height=50)
        b_Exit.place(x=10, y=280, width=190, height=50)
        self.window.mainloop()

    def booking_command(self):
        GetCustomInfo(self)

    def customers_command(self):
        DisplayCustomInfo(self)

    def room_command(self):
        DisplayRoomInfo(self)

    def billing_command(self):
        BillingSystem(self)

    def end_button(self):
        self.Exit(self.window)

    def Exit(self,root):
        root.destroy()
        Main_Menu()



class BillingSystem:
    def __init__(self, root):
        self.main = root
        self.info = Toplevel(root.head_frame)
        self.info.title("Billing")
        self.info.configure(bg='#FAEBD7')
        self.info.geometry("1200x640+230+140")
        self.info.resizable(width=False, height=False)
        self.head_frame = Frame(self.info, bg="#A52A2A", highlightbackground="black", highlightthickness=5)
        self.head_frame.place(x=0, y=0, height=60, width=1200)
        heading = Label(self.head_frame, font='Times 30 bold', fg='#FFFFFF', bg="#A52A2A", justify='center', text='CHECK-OUT')
        heading.place(x=450, y=0)
        l_select = Label(self.info,  bg="#FAEBD7", font='Times 18 bold', fg='#333333', justify='left', text='Select the Room: ')
        l_select.place(x=40, y=70)
        l_name = Label(self.info, font='Times 18 bold',  bg="#FAEBD7", fg='#333333', justify='left', text='Name: ')
        l_name.place(x=40, y=110)
        l_ph_no = Label(self.info, font='Times 18 bold',  bg="#FAEBD7", fg='#333333', justify='left', text='Contact: ')
        l_ph_no.place(x=40, y=190)
        l_address = Label(self.info, font='Times 18 bold', bg="#FAEBD7", fg='#333333', justify='left', text='Address: ')
        l_address.place(x=40, y=150)
        l_email_label = Label(self.info, font='Times 18 bold',  bg="#FAEBD7", fg='#333333', justify='left', text='Email: ')
        l_email_label.place(x=40, y=230)
        #l_nation = Label(self.info, font='Times 18 bold', fg='#333333', justify='left', text='Nationality: ')
        #l_nation.place(x=40, y=180)
        l_checkin = Label(self.info,  bg="#FAEBD7", font='Times 18 bold', fg='#333333', justify='left', text='Check in date: ')
        l_checkin.place(x=40, y=270)
        l_checkout = Label(self.info,  bg="#FAEBD7", font='Times 18 bold', fg='#333333', justify='left', text='Check out date: ')
        l_checkout.place(x=40, y=310)
        #l_gender = Label(self.info, font='Times 18 bold', fg='#333333', justify='left', text='Gender: ')
        #l_gender.place(x=600, y=180)
        self.t_name = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px',
                            justify='left')
        self.t_name.place(x=270, y=110, width=266, height=30)
        self.t_phn = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px',
                           justify='left')
        self.t_phn.place(x=270, y=190, width=263, height=30)
        self.t_email = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px',
                             justify='left')
        self.t_email.place(x=270, y=230, width=263, height=30)
        #self.t_nation = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px',
                            #  justify='left')
        #self.t_nation.place(x=270, y=180, width=263, height=30)
        #self.t_gen = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px',
          #                 justify='left')
        #self.t_gen.place(x=700, y=180, width=263, height=30)
        self.t_addr = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px',
                            justify='left')
        self.t_addr.place(x=270, y=150, width=263, height=30)
        self.t_checkin = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px',
                               justify='left')
        self.t_checkin.place(x=270, y=270, width=263, height=30)
        self.t_checkout = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px',
                                justify='left')
        self.t_checkout.place(x=270, y=310, width=263, height=30)
        combo_list = []
        try:
            obj = mydb.cursor()
            query = "Select room_no from room_allot where occupied='yes'"
            obj.execute(query)
            record = obj.fetchall()
            for i in range(len(record)):
                data1 = record[i]
                data = data1[0]
                combo_list.append(data)
        except:
            messagebox.showerror("", "Error while fetching data!")
        self.selection = StringVar()
        cb1 = ttk.Combobox(self.info, values=combo_list, width=10, height=30, textvariable=self.selection,
                           state='readonly', font='Times 12 bold' )
        cb1.place(x=270, y=75)
        b_select = Button(self.info, font='Times 12 bold', fg='#000000', bg='#68bc38', borderwidth='2px',
                          justify='center', text='Select', command=self.process_select)
        b_select.place(x=550, y=70, width=50, height=25)
        self.record_list = []
        self.total_list = []
        l_totaldays = Label(self.info,  bg="#FAEBD7", font='Times 16 bold', fg='#333333', justify='left', text='Total Days: ')
        l_totaldays.place(x=40, y=390)
        l_totalrent = Label(self.info,  bg="#FAEBD7", font='Times 16 bold', fg='#333333', justify='left', text='Rent Amount: ')
        l_totalrent.place(x=40, y=430)
        l_totalgst = Label(self.info,  bg="#FAEBD7", font='Times 16 bold', fg='#333333', justify='left', text='GST Amount: ')
        l_totalgst.place(x=40, y=510)
        l_payable = Label(self.info,  bg="#FAEBD7", font='Times 16 bold', fg='#333333', justify='left', text='Total Amount: ')
        l_payable.place(x=40, y=550)
        l_gst = Label(self.info, font='Times 16 bold',  bg="#FAEBD7", fg='#333333', justify='left',
                      text='GST Percentage:               12%')
        l_gst.place(x=40, y=470)
        self.total_days = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px',
                                justify='left')
        self.total_days.place(x=270, y=390, width=263, height=30)
        self.totalren = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px',
                              justify='left')
        self.totalren.place(x=270, y=430, width=263, height=30)
        self.totalgst = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px',
                              justify='left')
        self.totalgst.place(x=270, y=510, width=263, height=30)
        self.totaldays = 1
        self.total_amount = 1
        self.totalamount = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px',
                                 justify='left')
        self.totalamount.place(x=270, y=550, width=263, height=30)
        self.total_rent = 1
        self.total_GST = 1
        self.customid= 1
        b_generate = Button(self.info, font='Times 12 bold', fg='#000000', bg='#68bc38', borderwidth='2px',
                            justify='center', text='Bill', command=self.process_bill)
        b_generate.place(x=550, y=310, width=100, height=30)
        b_pay = Button(self.info, font='Times 12 bold', fg='#000000', bg='#68bc38', borderwidth='2px',
                            justify='center', text='Paid', command=self.process_paid)
        b_pay.place(x=550, y=550, width=100, height=30)
        b_bill = Button(self.info, font='Times 12 bold', fg='#000000', bg='#68bc38', borderwidth='2px',
                       justify='center', text='''Generate 
Receipt''', command=self.process_generate)
        b_bill.place(x=550, y=390, width=100, height=50)
        ##############################
        bill_frame = Frame(self.info, relief=GROOVE, bd=10)
        bill_frame.place(x=700, y=110, height= 500, width=400)
        bill_title=Label(bill_frame, text= "Bill", font="arial 18 bold", bd=7, relief=GROOVE).pack(fill=X)
        self.textarea = Text(bill_frame, font="arial 14 bold")
        self.textarea.pack(fill=BOTH)

        self.info.mainloop()

    def process_generate(self):
        self.textarea.insert(END, "--------------------------Receipt-------------------------\n\n\n")
        self.textarea.insert(END, " Customer Name :   {}\n".format(self.record_list[0][0]))
        self.textarea.insert(END, " Customer ID :       {}\n\n\n".format(self.customid))
        self.textarea.insert(END, "*****************************************************\n")
        self.textarea.insert(END, "Rent charges :  Rs.{}\n".format(self.total_rent))
        self.textarea.insert(END, "GST :     12%\n")
        self.textarea.insert(END, "Total GST :   Rs.{}\n".format(self.total_GST))
        self.textarea.insert(END, "Total Amount :   Rs.{}\n".format(self.total_amount))
        self.textarea.insert(END, "*****************************************************")

    def process_paid(self):
        try:
            obj = mydb.cursor()
            list = [int(self.selection.get())]
            obj.execute("Update room_allot set custom_id= null, occupied= 'no' where room_no=?", list)
            list2 = str(list)
            mydb.commit()
        except:
            messagebox.showerror("", "Error occured!")
        else:
            messagebox.showinfo('Success', 'Customer checked out! ' + list2 + ' is now vaccant.....')
            self.info.destroy()

    def process_bill(self):
        self.totalren.insert(0, "Rs.{}".format(self.total_rent))
        self.totalgst.insert(0, "Rs.{}".format(self.total_GST))
        self.totalamount.insert(0, "Rs.{}".format(self.total_amount))
        self.total_days.insert(0, "{} Days".format(self.totaldays))

    def process_select(self):
        mycursor = mydb.cursor()
        list = [int(self.selection.get())]
        mycursor.execute("select custom_id, preference from room_allot where room_no= ?", list)
        cid = mycursor.fetchall()

        mycursor.execute("SELECT custom_name, custom_ph_no, custom_address, custom_email, custom_gender, "
                         "custom_nationality, custom_checkin, custom_checkout  FROM customer_data where custom_id= "
                         "?", (cid[0][0],))
        self.customid = cid[0][0]
        pre = cid[0][1]
        if pre == "L_AC":
            rent = 2500
        elif pre == "L_N/AC":
            rent = 2000
        elif pre == "S_AC":
            rent = 1500
        else:
            rent = 1000
        records = mycursor.fetchall()
        print(records)
        for i in range(len(records)):
            data = records[i]
            self.record_list.append(data)
        self.t_name.delete(0, END)
        self.t_phn.delete(0, END)
        self.t_addr.delete(0, END)
        self.t_email.delete(0, END)
        #self.t_gen.delete(0, END)
        #self.t_nation.delete(0, END)
        self.t_checkin.delete(0, END)
        self.t_checkout.delete(0, END)
        self.t_name.insert(0, "{}".format(self.record_list[0][0]))
        self.t_phn.insert(0, "{}".format(self.record_list[0][1]))
        self.t_addr.insert(0, "{}".format(self.record_list[0][2]))
        self.t_email.insert(0, "{}".format(self.record_list[0][3]))
        #self.t_gen.insert(0, "{}".format(self.record_list[0][4]))
        #self.t_nation.insert(0, "{}".format(self.record_list[0][5]))
        self.t_checkin.insert(0, "{}".format(self.record_list[0][6]))
        self.t_checkout.insert(0, "{}".format(self.record_list[0][7]))
        date1 = datetime.strptime(self.record_list[0][7], '%Y-%m-%d')
        date2 = datetime.strptime(self.record_list[0][6], '%Y-%m-%d')
        self.totaldays = (date1 - date2).days
        self.total_list.append(self.totaldays)
        self.total_list.append(rent)
        self.total_rent = self.total_list[0] * self.total_list[1]
        self.total_GST = self.total_rent * 12 / 100
        self.total_amount = self.total_GST + self.total_rent


class DisplayRoomInfo:
    def __init__(self, root):
        self.main = root
        self.info = Toplevel(root.head_frame)
        self.info.title("Rooms")
        self.info.geometry("1250x610+230+140")
        self.info.configure(bg="#A52A2A" )
        self.info.resizable(width=False, height=False)
        heading = Label(self.info, font='Times 39 bold', fg='#FFFFFF', bg="#A52A2A", justify='center', text='ROOM INFORMATION')
        heading.place(x=420, y=10)
        tables = Frame(self.info, highlightthickness=3, highlightbackground="black")
        tables.place(x=0, y=90, height=517, width=1250)
        cols = ('Room No.', 'Type', 'Customer ID', 'Customer Name', 'Contact', 'Occupied')
        self.listbox = ttk.Treeview(tables, columns=cols, show='headings')
        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 16), fill='y', expand=True)
        style.configure("Treeview", font=(None, 14), rowhieght=50, hieght=50)

        for col in cols:
            self.listbox.heading(col, text=col)
            self.listbox.column(col, width=210)
            self.listbox.pack(fill='y', expand=True)

        self.show()

        self.info.mainloop()

    def show(self):
        try:
            mycursor = mydb.cursor()
            mycursor.execute(
                "SELECT room_allot.room_no, room_allot.preference, room_allot.custom_id, customer_data.custom_name, "
                "customer_data.custom_ph_no, room_allot.occupied  FROM room_allot LEFT JOIN customer_data ON "
                "room_allot.custom_id=customer_data.custom_id")
            records = mycursor.fetchall()
            print(records)
            for i, (room_no, preference, custom_id, custom_name, custom_ph_no, occupied) in enumerate(records, start=1):
                self.listbox.insert("", "end",
                                    values=(room_no, preference, custom_id, custom_name, custom_ph_no, occupied))
        except:
            messagebox.showerror("", "Error while displaying room information!")


class DisplayCustomInfo:
    def __init__(self, root):
        self.main = root
        self.info = Toplevel(root.head_frame)
        self.info.title("Customer Database")
        self.info.geometry("1250x610+230+140")
        self.info.configure(bg="#A52A2A")
        self.info.resizable(width=False, height=False)
        heading = Label(self.info, font='Times 39 bold',fg='#FFFFFF', bg="#A52A2A", justify='center', text='Customer Data')
        heading.place(x=450, y=0)
        tables = Frame(self.info, highlightthickness=3, highlightbackground="black")
        tables.place(x=0, y=70, height=538, width=1250)
        cols = ('Customer ID', 'Name', 'Contact', 'Address', 'Email ID', 'Gender', 'Nationality', 'Check-in date',
                'Check-out date')
        self.listbox = ttk.Treeview(tables, columns=cols, show='headings')
        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 12), fill='y', expand=True)
        style.configure("Treeview", font=(None, 12), rowhieght=40, hieght=40)

        for col in cols:
            self.listbox.heading(col, text=col)
            self.listbox.column(col, width=140)
            self.listbox.pack(fill='y', expand=True)

        self.show()

        self.info.mainloop()

    def show(self):
        try:
            mycursor = mydb.cursor()
            mycursor.execute(
                "SELECT custom_id, custom_name, custom_ph_no, custom_address, custom_email, custom_gender, "
                "custom_nationality, custom_checkin, custom_checkout FROM customer_data")
            records = mycursor.fetchall()
            print(records)
            for i, (
                    custom_id, custom_name, custom_ph_no, custom_address, custom_email, custom_gender,
                    custom_nationality,
                    custom_checkin, custom_checkout) in enumerate(records, start=1):
                self.listbox.insert("", "end", values=(
                    custom_id, custom_name, custom_ph_no, custom_address, custom_email, custom_gender,
                    custom_nationality,
                    custom_checkin, custom_checkout))
        except:
            messagebox.showerror("", "Error while displaying Data!")


class GetCustomInfo:
    def __init__(self, root):
        self.main = root
        self.info = Toplevel(root.head_frame)
        self.info.title("Customer Registration")
        self.info.configure(bg='#FAEBD7')
        self.info.geometry("1250x640+230+140")
        self.info.resizable(width=False, height=False)
        self.head_frame = Frame(self.info, bg="#A52A2A", highlightbackground="black", highlightthickness=5)
        self.head_frame.place(x=0, y=0, height=80, width=600)
        heading = Label(self.head_frame, font='Times 40 bold', fg='#FFFFFF', bg="#A52A2A", justify='center', text='Add Customer Data')
        heading.place(x=70, y=0)
        frame1 = Frame(self.info, bg="#FAEBD7")
        frame1.place(x=690, y=20, width= 470, height=300 )
        img1 = PhotoImage(file="G:\\Mini Project\\python\\Luxury_room_withimg.png")
        Label(frame1, image= img1, bg="#FAEBD7").place(x=0, y=0, width=470, height=300)
        frame2 = Frame(self.info, bg="#FAEBD7")
        frame2.place(x=690, y=330, width=470, height=300)
        img2 = PhotoImage(file="G:\\Mini Project\\python\\Standardroomsed_withimg.png")
        Label(frame2, image=img2, bg="#FAEBD7").place(x=0, y=0, width=470, height= 300)
        name = Label(self.info,  bg="#FAEBD7", font='Times 16 bold', fg='#333333', justify='left', text='Name: ')
        name.place(x=40, y=100)
        ph_no = Label(self.info, font='Times 16 bold',  bg="#FAEBD7", fg='#333333', justify='left', text='Contact: ')
        ph_no.place(x=40, y=140)
        address = Label(self.info, font='Times 16 bold', bg="#FAEBD7", fg='#333333', justify='left', text='Address: ')
        address.place(x=40, y=180)
        email_label = Label(self.info,  bg="#FAEBD7", font='Times 16 bold', fg='#333333', justify='left', text='Email: ')
        email_label.place(x=40, y=220)
        l_nation = Label(self.info, font='Times 16 bold',  bg="#FAEBD7", fg='#333333', justify='left', text='Nationality: ')
        l_nation.place(x=40, y=260)
        l_checkin = Label(self.info,  bg="#FAEBD7", font='Times 16 bold', fg='#333333', justify='left', text='Check in date: ')
        l_checkin.place(x=40, y=340)
        l_checkout = Label(self.info, font='Times 16 bold',  bg="#FAEBD7", fg='#333333', justify='left', text='Check out date: ')
        l_checkout.place(x=40, y=380)
        l_gender = Label(self.info, font='Times 16 bold',  bg="#FAEBD7", fg='#333333', justify='left', text='Gender: ')
        l_gender.place(x=40, y=300)
        l_preference = Label(self.info, font='Times 16 bold',  bg="#FAEBD7", fg='#333333', justify='left', text='Room Preference: ')
        l_preference.place(x=40, y=420)
        l_cid = Label(self.info, font='Times 16 bold', fg='#333333',  bg="#FAEBD7", justify='left', text='Customer ID: ')
        l_cid.place(x=40, y=540)
        l_roomno = Label(self.info, font='Times 16 bold', fg='#333333',  bg="#FAEBD7", justify='left', text='Room number alloted: ')
        l_roomno.place(x=40, y=590)
        self.cname = StringVar()
        t_name = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px', justify='left',
                       textvariable=self.cname)
        t_name.place(x=270, y=100, width=266, height=30)
        self.cphn = StringVar()
        t_phn = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px', justify='left',
                      textvariable=self.cphn)
        t_phn.place(x=270, y=140, width=263, height=30)
        self.cemail = StringVar()
        t_email = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px', justify='left',
                        textvariable=self.cemail)
        t_email.place(x=270, y=220, width=263, height=30)
        self.cnationality = StringVar()
        t_nation = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px', justify='left',
                         textvariable=self.cnationality)
        t_nation.place(x=270, y=300, width=263, height=30)
        self.cgender = StringVar()
        t_gen = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px', justify='left',
                      textvariable=self.cgender)
        t_gen.place(x=270, y=260, width=263, height=30)
        self.caddr = StringVar()
        t_addr = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px', justify='left',
                       textvariable=self.caddr)
        t_addr.place(x=270, y=180, width=263, height=30)
        self.checkin = StringVar()
        t_checkin = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px',
                          justify='left',
                          textvariable=self.checkin)
        t_checkin.place(x=270, y=340, width=263, height=30)
        self.checkout = StringVar()
        self.preference = StringVar()
        t_checkout = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px',
                           justify='left',
                           textvariable=self.checkout)
        t_checkout.place(x=270, y=380, width=263, height=30)
        self.preference_list = {1: 'Luxury AC                   Rs.2500/-', 2: 'Luxury Non AC          Rs.2000/-', 3: 'Standard AC               Rs.1500/-',
                                4: 'Standard Non AC       Rs.1000/-'}
        self.selection = StringVar()
        cb1 = ttk.Combobox(self.info, values=list(self.preference_list.values()), width=30,
                           textvariable=self.selection, font='Times 12 bold',
                           state='readonly')
        cb1.place(x=270, y=420)
        b_submit = Button(self.info, font='Times 16 bold', fg='#000000', bg='#68bc38', borderwidth='2px',
                          justify='center',
                          text='Submit', command=self.process_submit)
        b_submit.place(x=200, y=460, width=108, height=32)
        l_allotment=Label(self.info,  bg="#FAEBD7", font="Times 16 bold", text="Allotment :")
        l_allotment.place(x=40 , y=500 )
        self.cid = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px',
                         justify='left')
        self.cid.place(x=270, y=540, width=263, height=30)
        self.room_no = Entry(self.info, font='Times 16 bold', fg='#333333', bg='#f9f7f7', borderwidth='2px',
                             justify='left')
        self.room_no.place(x=270, y=590, width=263, height=30)

        self.info.mainloop()

    def get_key(self, val):
        for key, value in self.preference_list.items():
            if val == value:
                return key

    def preference1(self):
        try:
            obj = mydb.cursor()
            query = 'Select custom_id from customer_data where custom_name= ?; '
            obj.execute(query, (self.cname.get(),))
            cid = obj.fetchone()
            id = cid[0]
            query2 = "Select room_no from room_allot where preference= ? and occupied='no'"
            selected = self.get_key(self.selection.get())
            if (selected == 1):
                sele = 'L_AC'
            elif (selected == 2):
                sele = 'L_N/AC'
            elif (selected == 3):
                sele = 'S_AC'
            else:
                sele = 'S_N/AC'
            print(sele)
            obj.execute(query2, (sele,))
            room_no = obj.fetchone()
            try:
                room = room_no[0]
                print(id)
                print(room)
                self.cid.insert(0, "{}".format(id))
                self.room_no.insert(0, "{}".format(room))
                query2 = "Update room_allot set custom_id= ?, occupied= 'yes' where room_no=?"
                obj.execute(query2, (id, room))
                mydb.commit()
            except:
                messagebox.showinfo("", "No room Available, try another preference!")

        except:
            messagebox.showerror("", "Select valid preference!")

    def process_submit(self):
        if (
                self.cname.get() != "" and self.cphn.get() != "" and self.caddr.get() != "" and self.cemail.get() != "" and self.cgender.get() != "" and
                self.cnationality.get() != "" and self.checkin.get() != "" and self.checkout.get() != ""):
            try:
                obj = mydb.cursor()
                query = "INSERT INTO customer_data('custom_name', 'custom_ph_no', 'custom_address', 'custom_email', 'custom_gender', 'custom_nationality', 'custom_checkin', 'custom_checkout') VALUES(?,?,?,?,?,?,?,?); "
                obj.execute(query, (
                    self.cname.get(), self.cphn.get(), self.caddr.get(), self.cemail.get(), self.cgender.get(),
                    self.cnationality.get(), self.checkin.get(), self.checkout.get()))
                self.preference1()


            except:
                messagebox.showerror("", "Enter date in the format: year-month-day"
                                         "eg. 2012-11-3")
        else:
            messagebox.showerror("", "Enter all the fields!")


Main_Menu()