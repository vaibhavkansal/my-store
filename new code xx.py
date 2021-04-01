from tkinter import *
from tkinter import ttk
import PyPDF2
from PyPDF2 import PdfFileReader
from operator import add
from tkinter import filedialog  # to import a file name so that we can use that file
import xlrd
import xlsxwriter
import sqlite3
import tkinter.messagebox as tsmg
from datetime import date

root = Tk()
root.minsize(1200, 680)
import tkinter as tk

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.maxsize(screen_width, screen_height)

root.title("Stocks")
global f2
global f3
global f4
global from_date
global to_date
global datee
global pll
today = date.today()

from_date = '2000-01-01'
to_date = '2099-12-31'
f1 = Frame(root, background="bisque", height=100, borderwidth=6, relief=SUNKEN)
f2 = Frame(root, background="pink", width=10, height=100, borderwidth=6, relief=SUNKEN)
f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
f4 = Frame(root, background="pink", width=100, height=100, borderwidth=6, relief=SUNKEN)

f1.grid(row=0, column=0, sticky="nsew", rowspan=2)
f2.grid(row=0, column=1, sticky="nsew", rowspan=2)
f3.grid(row=0, column=2, sticky="nsew")
f4.grid(row=1, column=2, sticky="nsew")
Label(f2, text="                      ", bg="pink").pack()
root.grid_columnconfigure(0)
root.grid_columnconfigure(1)
root.grid_columnconfigure(2, weight=10)
root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(1, weight=1)
datefor = date.today()
month = datefor.strftime("%m")
month = int(month)
year = datefor.strftime("%Y")
year = int(year)
if (month < 4):
    year = year - 1
    year = str(year)
year = str(year)
print(year)


def createtable(tablename):
    connection = sqlite3.connect("mytables4.db")
    cursor = connection.cursor()
    sqlcommand = f"""CREATE TABLE {tablename}(
        Type varchar(50),
        den_size varchar(50),
        THKREMARK varchar(50),
        BUNDLE varchar(50) PRIMARY KEY,
        COVER varchar(50),
        STM varchar(50),
        R2 varchar(50),
        PCS varchar(50),
        MM varchar(50),
        KG varchar(50),
        PACKINGLIST varchar(50),
        DATE DATE,
        STATUS varchar(50));"""
    cursor.execute(sqlcommand)
    connection.commit()
    connection.close()

    pass


def showmax(eve):
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute(f"SELECT BUNDLE FROM stockfinal634")
    w = crsr.fetchall()
    connection.close()
    k = []
    q = []
    ep = []
    for i in w:
        if 'r-' in i[0] or 'R-' in i[0]:
            q.append(i[0])
        elif 'EP-' in i[0] or 'ep-' in i[0]:
            ep.append(i[0])
    j = []
    for i in q:
        i = i.split('-')
        i = i[1]
        j.append(int(i))
    we = max(j)
    we = 'R-' + str(we)
    j = []
    for i in ep:
        i = i.split('-')
        i = i[1]
        j.append(int(i))
    ew = max(j)
    ew = 'EP-' + str(ew)
    t1 = Toplevel(background="bisque")
    t1.title("RECORD")
    t1.minsize(250, 150)
    l1 = Label(t1, text="R-")
    l1.grid(row=0, column=0, padx=5, pady=5)
    e1 = Entry(t1)
    e1.grid(row=0, column=1)
    e1.focus()
    l2 = Label(t1, text="EP-")
    l2.grid(row=1, column=0, padx=5, pady=5)
    e2 = Entry(t1)
    e2.grid(row=1, column=1)
    e1.insert(0, we)
    e2.insert(0, ew)


def addbundle1(event):
    global f3
    global f4
    d = []
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute(f"SELECT * FROM stockfinal634")
    w = crsr.fetchall()
    connection.close()
    bunlis = []
    densiz = []
    remark = []
    for i in w:
        bunlis.append(i[0])
        densiz.append(i[1])
        remark.append(i[2])
    bunlis = list(set(bunlis))
    densiz = list(set(densiz))
    remark = list(set(remark))

    def check(*args):
        d.append(e1.get())
        d.append(e2.get())
        d.append(e3.get())
        d.append(e4.get())
        d.append(e5.get())
        d.append(e6.get())
        d.append(e7.get())
        d.append(e8.get())
        d.append(e9.get())
        d.append(e10.get())
        d.append(e11.get())

        as1 = e12.get()
        if as1.count('-') == 2 and as1.index('-') == 2 and as1.index('-', 3) == 5 and len(as1) == 10:
            date1 = as1.split('-')
            date1.reverse()
            date2 = "-".join(date1)
            d.append(date2)
        elif as1.count('-') == 2 and as1.index('-') == 4 and as1.index('-', 5) == 7 and len(as1) == 10:
            d.append(as1)
        else:
            tsmg.showinfo("FORMAT", "Wrong date format")
            return
        d.append(e13.get())

        d1 = tuple(d)
        connection = sqlite3.connect("mytables4.db")
        cursor = connection.cursor()
        row = d1
        sa = f'''INSERT INTO stockfinal634 VALUES ('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}','{row[9]}','{row[10]}','{row[11]}','{row[12]}')'''
        try:
            cursor.execute(sa)
            connection.commit()
            tsmg.showinfo("Saved", "your entry has been saved")

            # errorcanoccur
            addbundle(event)

        except Exception as e:
            print(e)
            tsmg.showinfo("Failed", "Bundle no. exist")
            # errorcanoccur

            addbundle(event)

        connection.close()

        # now i need to store data in sql

    l1 = Label(f4, text="Bundle type", width=8)
    l1.grid(row=0, column=0, padx=5, pady=5)
    e1 = ttk.Combobox(f4, values=bunlis, height=8, width=32)
    e1.grid(row=0, column=1)
    l2 = Label(f4, text="DEN SIZE", padx=5, width=8)
    l2.grid(row=1, column=0, padx=5, pady=5)
    e2 = ttk.Combobox(f4, values=densiz, height=8, width=31)
    e2.grid(row=1, column=1)
    l3 = Label(f4, text="THK REMARK", padx=5, width=8)
    l3.grid(row=2, column=0, padx=5, pady=5)
    e3 = ttk.Combobox(f4, values=remark, height=8, width=31)
    e3.grid(row=2, column=1)
    l4 = Label(f4, text="BUNDLE", padx=5, width=8)
    l4.grid(row=3, column=0, padx=5, pady=5)
    e4 = Entry(f4)
    e4.grid(row=3, column=1)
    l5 = Label(f4, text="COVER", padx=5, width=8)
    l5.grid(row=4, column=0, padx=5, pady=5)
    e5 = Entry(f4)
    e5.grid(row=4, column=1)
    l6 = Label(f4, text="STM", padx=5, width=8)
    l6.grid(row=0, column=5, padx=5, pady=5)
    e6 = Entry(f4)
    e6.grid(row=0, column=6)
    l7 = Label(f4, text="R2", padx=5, width=8)
    l7.grid(row=0, column=3, padx=20, pady=5)
    e7 = Entry(f4)
    e7.grid(row=0, column=4)
    l8 = Label(f4, text="PCS", padx=5, width=8)
    l8.grid(row=1, column=3, padx=5, pady=5)
    e8 = Entry(f4)
    e8.grid(row=1, column=4)
    l9 = Label(f4, text="MM", padx=5, width=8)
    l9.grid(row=2, column=3, padx=5, pady=5)
    e9 = Entry(f4)
    e9.grid(row=2, column=4)
    l10 = Label(f4, text="KGS", padx=5, width=8)
    l10.grid(row=3, column=3, padx=5, pady=5)
    e10 = Entry(f4)
    e10.grid(row=3, column=4)
    l11 = Label(f4, text="PACKINGNO", padx=5, width=8)
    l11.grid(row=4, column=3, padx=5, pady=5)
    e11 = Entry(f4)
    e11.grid(row=4, column=4)
    l12 = Label(f4, text="DATE ", padx=5, width=8)
    l12.grid(row=3, column=5, padx=5, pady=5)
    e12 = Entry(f4)
    e12.grid(row=3, column=6)
    l13 = Label(f4, text="STATUS", padx=5, width=8)
    l13.grid(row=1, column=5, padx=20, pady=5)
    e13 = Entry(f4)
    e13.grid(row=1, column=6, padx=5, pady=5)
    e1.focus()
    # deleteifwanttodelete
    e1.bind("<KP_Enter>", lambda x: e2.focus())
    e1.bind("<Return>", lambda x: e2.focus())
    e2.bind("<KP_Enter>", lambda x: e3.focus())
    e2.bind("<Return>", lambda x: e3.focus())
    e3.bind("<KP_Enter>", lambda x: e4.focus())
    e3.bind("<Return>", lambda x: e4.focus())
    e4.bind("<KP_Enter>", lambda x: e5.focus())
    e4.bind("<Return>", lambda x: e5.focus())
    e5.bind("<KP_Enter>", lambda x: e7.focus())
    e5.bind("<Return>", lambda x: e7.focus())
    e7.bind("<KP_Enter>", lambda x: e8.focus())
    e7.bind("<Return>", lambda x: e8.focus())
    e8.bind("<KP_Enter>", lambda x: e9.focus())
    e8.bind("<Return>", lambda x: e9.focus())
    e9.bind("<KP_Enter>", lambda x: e10.focus())
    e9.bind("<Return>", lambda x: e10.focus())
    e10.bind("<KP_Enter>", lambda x: e11.focus())
    e10.bind("<Return>", lambda x: e11.focus())
    e11.bind("<KP_Enter>", lambda x: e6.focus())
    e11.bind("<Return>", lambda x: e6.focus())
    e6.bind("<KP_Enter>", lambda x: e13.focus())
    e6.bind("<Return>", lambda x: e13.focus())
    e13.bind("<KP_Enter>", lambda x: e12.focus())
    e13.bind("<Return>", lambda x: e12.focus())

    def keydown(event):
        ba = e1.get()
        a = ba.upper()
        checklist = []
        for i in bunlis:
            if a in i:
                checklist.append(i)
        e1["values"] = checklist

    e1.bind("<KeyRelease>", keydown)

    def keyup(event):
        e1.event_generate("<Down>")




    e1.bind("<KP_Enter>", keyup)
    e1.bind("<Return>", keyup)


    def keyup2(event):
        e2.event_generate("<Down>")

    e2.bind("<KP_Enter>", keyup2)
    e2.bind("<Return>", keyup2)
    def keydown2(event):
        ba = e2.get()
        a = ba.upper()
        checklist = []
        for i in densiz:
            if a in i:
                checklist.append(i)
        e2["values"] = checklist

    e2.bind("<KeyRelease>", keydown2)

    def keyup3(event):
        e3.event_generate("<Down>")

    e3.bind("<KP_Enter>", keyup3)
    e3.bind("<Return>", keyup3)
    def keydown3(event):
        ba = e3.get()
        a = ba.upper()
        checklist = []
        for i in remark:
            if a in i:
                checklist.append(i)
        e3["values"] = checklist
    e3.bind("<KeyRelease>", keydown3)




    e12.bind("<KP_Enter>", check)
    e12.bind("<Return>", check)

    Button(f4, text="SAVE DATA", command=check).grid(row=4, column=5, columnspan=2, padx=25)

    pass


def addbundle(event):
    f3.destroy()
    f4.destroy()
    addbundle1(event)


def showstock1(events):
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute(f"SELECT * FROM stockfinal634 WHERE DATE >= '{from_date}' AND DATE <= '{to_date}'")
    d = crsr.fetchall()
    connection.close()
    d.reverse()
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    def showsoldstock1():
        global f3
        f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
        f3.grid(row=0, column=2, sticky="nsew")
        treev = ttk.Treeview(f3, selectmode='browse', height=19)
        treev.pack()
        scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
        scrollbar.pack(side=BOTTOM, fill=X)
        treev.configure(xscrollcommand=scrollbar.set)
        treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")

        # Defining heading
        treev['show'] = 'headings'

        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width=250, anchor='c')
        treev.column("2", width=300, anchor='c')
        treev.column("3", width=180, anchor='c')
        treev.column("4", width=110, anchor='c')
        treev.column("5", width=110, anchor='c')
        treev.column("6", width=100, anchor='c')
        treev.column("7", width=60, anchor='c')
        treev.column("8", width=60, anchor='c')
        treev.column("9", width=60, anchor='c')
        treev.column("10", width=60, anchor='c')
        treev.column("11", width=60, anchor='c')
        treev.column("12", width=100, anchor='c')
        treev.column("13", width=100, anchor='c')

        # Assigning the heading names to the
        # respective columns
        treev.heading("1", text="TYPE")
        treev.heading("2", text="DENSIZE")
        treev.heading("3", text="THK REMARK")
        treev.heading("4", text="BUNDLENO")
        treev.heading("5", text="COVER")
        treev.heading("6", text="STM")
        treev.heading("7", text="R2")
        treev.heading("8", text="PCS")
        treev.heading("9", text="MM")
        treev.heading("10", text="KGS")
        treev.heading("11", text="PACKINGLIST")
        treev.heading("12", text="DATE")
        treev.heading("13", text="STATUS")
        # Inserting the items and their features to the
        # columns built
        for row in d:
            s = tuple(row)
            if (s[12] == 'SOLD'):
                treev.insert("", 'end', values=s, tags=(s[12],))
        treev.tag_configure('SOLD', background='light green')
        treev.tag_configure('SPLIT', background='light blue')

        pass

        pass

    def showsoldstock():
        f3.destroy()
        showsoldstock1()

    def showinstock1():
        global f3

        f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
        f3.grid(row=0, column=2, sticky="nsew")
        treev = ttk.Treeview(f3, selectmode='browse', height=19)
        treev.pack()
        scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
        scrollbar.pack(side=BOTTOM, fill=X)
        treev.configure(xscrollcommand=scrollbar.set)
        treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")

        # Defining heading
        treev['show'] = 'headings'

        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width=250, anchor='c')
        treev.column("2", width=300, anchor='c')
        treev.column("3", width=180, anchor='c')
        treev.column("4", width=100, anchor='c')
        treev.column("5", width=110, anchor='c')
        treev.column("6", width=100, anchor='c')
        treev.column("7", width=60, anchor='c')
        treev.column("8", width=60, anchor='c')
        treev.column("9", width=60, anchor='c')
        treev.column("10", width=60, anchor='c')
        treev.column("11", width=60, anchor='c')
        treev.column("12", width=100, anchor='c')
        treev.column("13", width=100, anchor='c')

        # Assigning the heading names to the
        # respective columns
        treev.heading("1", text="TYPE")
        treev.heading("2", text="DENSIZE")
        treev.heading("3", text="THK REMARK")
        treev.heading("4", text="BUNDLENO")
        treev.heading("5", text="COVER")
        treev.heading("6", text="STM")
        treev.heading("7", text="R2")
        treev.heading("8", text="PCS")
        treev.heading("9", text="MM")
        treev.heading("10", text="KGS")
        treev.heading("11", text="PACKINGLIST")
        treev.heading("12", text="DATE")
        treev.heading("13", text="STATUS")
        # Inserting the items and their features to the
        # columns built
        for row in d:
            s = tuple(row)
            if (s[12] != "SOLD"):
                treev.insert("", 'end', values=s, tags=(s[12],))
        treev.tag_configure('SOLD', background='light green')
        treev.tag_configure('SPLIT', background='light blue')

        pass

        pass

    def showinstock():
        f3.destroy()
        showinstock1()

    def exporttoexcel():
        workbook = xlsxwriter.Workbook('stockupdate.xlsx')
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})

        alpa = ['TYPE', 'den_size', 'THKREMARK', 'BUNDLE', 'COVER', 'STM', 'R2', 'PCS', 'MM',
                'KG', 'PACKINGLIST', 'DATE', 'STATUS']

        d1 = d
        d1.insert(0, alpa)
        for i in range(len(d1)):
            d1[i] = list(d1[i])
        for i in range(len(d)):
            for j in range(len(d[0])):
                if (i == 0):
                    worksheet.write(i, j, f'''{d[i][j]}''', bold)
                else:
                    worksheet.write(i, j, f'''{d[i][j]}''')
        worksheet.set_column(0, 1, 25)
        worksheet.set_column(2, 2, 20)
        worksheet.set_column(4, 4, 15)
        worksheet.set_column(10, 12, 15)
        workbook.close()
        pass

    def clickedrow1(event):
        global f3
        global f4
        item = treev.identify_row(event.y)
        if item:
            a = treev.item(item, 'values')
            a = list(a)

            f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
            f4.grid(row=1, column=2, sticky="nsew")
            b1 = Button(f4, text="  TYPE  ")
            b1.grid(row=0, column=0, padx=5, pady=5)
            e1 = Entry(f4)
            e1.grid(row=0, column=1)
            l2 = Label(f4, text="DEN SIZE", padx=5, width=8)
            l2.grid(row=1, column=0, padx=5, pady=5)
            e2 = Entry(f4)
            e2.grid(row=1, column=1)
            l3 = Label(f4, text="THK REMARK", padx=5, width=8)
            l3.grid(row=2, column=0, padx=5, pady=5)
            e3 = Entry(f4)
            e3.grid(row=2, column=1)
            l4 = Label(f4, text="BUNDLE", padx=5, width=8)
            l4.grid(row=3, column=0, padx=5, pady=5)
            e4 = Entry(f4)
            e4.grid(row=3, column=1)
            l5 = Label(f4, text="COVER", padx=5, width=8)
            l5.grid(row=4, column=0, padx=5, pady=5)
            e5 = Entry(f4)
            e5.grid(row=4, column=1)
            l6 = Label(f4, text="STM", padx=5, width=8)
            l6.grid(row=0, column=5, padx=5, pady=5)
            e6 = Entry(f4)
            e6.grid(row=0, column=6)
            l7 = Label(f4, text="R2", padx=5, width=8)
            l7.grid(row=0, column=3, padx=20, pady=5)
            e7 = Entry(f4)
            e7.grid(row=0, column=4)
            l8 = Label(f4, text="PCS", padx=5, width=8)
            l8.grid(row=1, column=3, padx=5, pady=5)
            e8 = Entry(f4)
            e8.grid(row=1, column=4)
            l9 = Label(f4, text="MM", padx=5, width=8)
            l9.grid(row=2, column=3, padx=5, pady=5)
            e9 = Entry(f4)
            e9.grid(row=2, column=4)
            l10 = Label(f4, text="KGS", padx=5, width=8)
            l10.grid(row=3, column=3, padx=5, pady=5)
            e10 = Entry(f4)
            e10.grid(row=3, column=4)
            l11 = Label(f4, text="PACKINGNO", padx=5, width=8)
            l11.grid(row=4, column=3, padx=5, pady=5)
            e11 = Entry(f4)
            e11.grid(row=4, column=4)
            l12 = Label(f4, text="DATE", padx=5, width=8)
            l12.grid(row=3, column=5, padx=5, pady=5)
            e12 = Entry(f4)
            e12.grid(row=3, column=6)
            l13 = Label(f4, text="STATUS", padx=5, width=8)
            l13.grid(row=1, column=5, padx=20, pady=5)
            e13 = Entry(f4)
            e13.grid(row=1, column=6, padx=5, pady=5)

            e1.insert(0, a[0])
            e2.insert(0, a[1])
            e3.insert(0, a[2])
            e4.insert(0, a[3])
            e5.insert(0, a[4])
            e6.insert(0, a[5])
            e7.insert(0, a[6])
            e8.insert(0, a[7])
            e9.insert(0, a[8])
            e10.insert(0, a[9])
            e11.insert(0, a[10])
            e12.insert(0, a[11])
            e13.insert(0, a[12])

            def searchbundlenametype1(event):
                global f3
                global f4

                f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
                f3.grid(row=0, column=2, sticky="nsew")
                f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
                f4.grid(row=1, column=2, sticky="nsew")

                def check():
                    connection = sqlite3.connect("mytables4.db")
                    crsr = connection.cursor()
                    crsr.execute(f"SELECT * FROM stockfinal634 WHERE Type ='{e112}';")
                    w = crsr.fetchall()

                    if (len(w) == 0):
                        Button(f4, text="NOT FOUND").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')
                        pass

                    else:
                        d = []
                        for i in w:
                            d.append(list(i))
                        connection.close()

                        f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
                        f3.grid(row=0, column=2, sticky="nsew")

                        treev = ttk.Treeview(f3, selectmode='browse', height=20)
                        treev.pack(fill=BOTH)
                        scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
                        scrollbar.pack(side=BOTTOM, fill=X)
                        treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
                        treev.configure(xscrollcommand=scrollbar.set)
                        # Defining heading
                        treev['show'] = 'headings'

                        # Assigning the width and anchor to  the
                        # respective columns
                        treev.column("1", width=250, anchor='c')
                        treev.column("2", width=300, anchor='c')
                        treev.column("3", width=150, anchor='c')
                        treev.column("4", width=80, anchor='c')
                        treev.column("5", width=100, anchor='c')
                        treev.column("6", width=100, anchor='c')
                        treev.column("7", width=60, anchor='c')
                        treev.column("8", width=60, anchor='c')
                        treev.column("9", width=60, anchor='c')
                        treev.column("10", width=60, anchor='c')
                        treev.column("11", width=80, anchor='c')
                        treev.column("12", width=100, anchor='c')
                        treev.column("13", width=100, anchor='c')

                        # Assigning the heading names to the
                        # respective columns
                        treev.heading("1", text="TYPE")
                        treev.heading("2", text="DENSIZE")
                        treev.heading("3", text="THK REMARK")
                        treev.heading("4", text="BUNDLENO")
                        treev.heading("5", text="COVER")
                        treev.heading("6", text="STM")
                        treev.heading("7", text="R2")
                        treev.heading("8", text="PCS")
                        treev.heading("9", text="MM")
                        treev.heading("10", text="KGS")
                        treev.heading("11", text="PACKINGLIST")
                        treev.heading("12", text="DATE")
                        treev.heading("13", text="STATUS")
                        # Inserting the items and their features to the
                        # columns built

                        for row in d:
                            s = tuple(row)
                            treev.insert("", 'end', values=s, tags=(s[12],))
                        treev.tag_configure('SOLD', background='light green')
                        treev.tag_configure('SPLIT', background='light blue')

                        Button(f4, text=" FOUND   ").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')

                e112 = a[0]
                check()
                pass

            def searchbundlenametype(event):
                f3.destroy()
                f4.destroy()
                searchbundlenametype1(event)

            b1.bind("<Button-1>", searchbundlenametype)

            def updateduringchecking():
                d12 = []
                d12.append(e1.get())
                d12.append(e2.get())
                d12.append(e3.get())
                d12.append(e4.get())
                d12.append(e5.get())
                d12.append(e6.get())
                d12.append(e7.get())
                d12.append(e8.get())
                d12.append(e9.get())
                d12.append(e10.get())
                d12.append(e11.get())
                as1 = e12.get()
                if as1.count('-') == 2 and as1.index('-') == 2 and as1.index('-', 3) == 5 and len(as1) == 10:
                    date1 = as1.split('-')
                    date1.reverse()
                    date2 = "-".join(date1)
                    d12.append(date2)
                elif as1.count('-') == 2 and as1.index('-') == 4 and as1.index('-', 5) == 7 and len(as1) == 10:
                    d12.append(as1)
                else:
                    tsmg.showinfo("FORMAT", "Wrong date format")
                    return

                d12.append(e13.get())

                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(f"DELETE FROM stockfinal634 WHERE BUNDLE ='{e4.get()}';")
                connection.commit()

                row = d12
                sa = f'''INSERT INTO stockfinal634 VALUES ('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}','{row[9]}','{row[10]}','{row[11]}','{row[12]}')'''
                try:
                    crsr.execute(sa)
                    tsmg.showinfo("Saved", "your entry has been saved")
                    connection.commit()
                    showstock(events)

                except Exception as e:
                    row = a
                    sa = f'''INSERT INTO stockfinal634 VALUES ('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}','{row[9]}','{row[10]}','{row[11]}','{row[12]}')'''
                    crsr.execute(sa)
                    connection.commit()
                    print(e)
                    showstock(events)

                connection.close()

            if (a[12] == "SOLD"):
                Button(f4, text="CANT SAVE").grid(row=4, column=5, columnspan=2, padx=25)
            else:
                Button(f4, text="SAVE DATA", command=updateduringchecking).grid(row=4, column=5, columnspan=2, padx=25)

    def clickedrow(event):
        f4.destroy()
        clickedrow1(event)
        pass

    Button(f4, text="SOLD", command=showsoldstock).grid(row=0, column=0, sticky="nsew", pady=30, padx=100)
    Button(f4, text="IN STOCK", command=showinstock).grid(row=0, column=1, sticky="nsew", pady=30, padx=100)
    Button(f4, text="EXPORT TO EXCEL", command=exporttoexcel).grid(row=0, column=2, sticky="nsew", pady=30, padx=100)

    treev = ttk.Treeview(f3, selectmode='browse', height=19)
    treev.pack()
    treev.bind("<Double-Button-1>", clickedrow)
    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev.configure(xscrollcommand=scrollbar.set)
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=250, anchor='c')
    treev.column("2", width=300, anchor='c')
    treev.column("3", width=180, anchor='c')
    treev.column("4", width=100, anchor='c')
    treev.column("5", width=110, anchor='c')
    treev.column("6", width=100, anchor='c')
    treev.column("7", width=60, anchor='c')
    treev.column("8", width=60, anchor='c')
    treev.column("9", width=60, anchor='c')
    treev.column("10", width=60, anchor='c')
    treev.column("11", width=60, anchor='c')
    treev.column("12", width=100, anchor='c')
    treev.column("13", width=100, anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="TYPE")
    treev.heading("2", text="DENSIZE")
    treev.heading("3", text="THK REMARK")
    treev.heading("4", text="BUNDLENO")
    treev.heading("5", text="COVER")
    treev.heading("6", text="STM")
    treev.heading("7", text="R2")
    treev.heading("8", text="PCS")
    treev.heading("9", text="MM")
    treev.heading("10", text="KGS")
    treev.heading("11", text="PACKINGLIST")
    treev.heading("12", text="DATE")
    treev.heading("13", text="STATUS")

    # Inserting the items and their features to the
    # columns built
    for row in d:
        s = tuple(row)
        treev.insert("", 'end', values=s, tags=(s[12],))
    treev.tag_configure('SOLD', background='light green')
    treev.tag_configure('SPLIT', background='light blue')

    pass


def showstock(events):
    f3.destroy()
    f4.destroy()
    showstock1(events)


def addpackingmanual1():
    global f3
    global f4
    f2 = Frame(root, background="pink", width=10, height=100, borderwidth=6, relief=SUNKEN)
    f2.grid(row=0, column=1, sticky="nsew", rowspan=2)
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    treev = ttk.Treeview(f3, selectmode='browse', height=20)
    treev.pack(fill=BOTH)
    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
    treev.configure(xscrollcommand=scrollbar.set)
    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=250, anchor='c')
    treev.column("2", width=300, anchor='c')
    treev.column("3", width=190, anchor='c')
    treev.column("4", width=80, anchor='c')
    treev.column("5", width=100, anchor='c')
    treev.column("6", width=100, anchor='c')
    treev.column("7", width=60, anchor='c')
    treev.column("8", width=60, anchor='c')
    treev.column("9", width=60, anchor='c')
    treev.column("10", width=60, anchor='c')
    treev.column("11", width=80, anchor='c')
    treev.column("12", width=100, anchor='c')
    treev.column("13", width=100, anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="TYPE")
    treev.heading("2", text="DENSIZE")
    treev.heading("3", text="THK REMARK")
    treev.heading("4", text="BUNDLENO")
    treev.heading("5", text="COVER")
    treev.heading("6", text="STM")
    treev.heading("7", text="R2")
    treev.heading("8", text="PCS")
    treev.heading("9", text="MM")
    treev.heading("10", text="KGS")
    treev.heading("11", text="PACKINGLIST")
    treev.heading("12", text="DATE")
    treev.heading("13", text="STATUS")

    l12 = Label(f2, text="DATE", width=8)
    l12.grid(row=0, column=0, padx=5, pady=5)
    e12 = Entry(f2)
    e12.grid(row=1, column=0)

    l22 = Label(f2, text="PL NO", padx=5, width=8)
    l22.grid(row=2, column=0, padx=5, pady=5)
    e22 = Entry(f2)
    e22.grid(row=3, column=0)
    e12.insert(0, datee)
    e22.insert(0, pll)
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute(f"SELECT * FROM stockfinal634")
    w = crsr.fetchall()
    connection.close()
    bunlis = []
    densiz=[]
    remark=[]
    for i in w:
        bunlis.append(i[0])
        densiz.append(i[1])
        remark.append(i[2])
    bunlis = list(set(bunlis))
    densiz = list(set(densiz))
    remark = list(set(remark))



    def check(*args):
        d = []
        d.append(e1.get())
        d.append(e2.get())
        d.append(e3.get())
        d.append(e4.get())
        d.append(e5.get())
        d.append(e6.get())
        d.append(e7.get())
        d.append(e8.get())
        d.append(e9.get())
        d.append(e10.get())
        d.append(e11.get())
        d.append(e12.get())
        d.append(e13.get())

        d1 = tuple(d)
        connection = sqlite3.connect("mytables4.db")
        cursor = connection.cursor()
        row = d1
        sa = f'''INSERT INTO stockfinal634 VALUES ('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}','{row[9]}','{row[10]}','{row[11]}','{row[12]}')'''
        try:
            cursor.execute(sa)
            connection.commit()
            tsmg.showinfo("Saved", "your entry has been saved")
            e1.delete(0, 'end')
            e2.delete(0, 'end')
            e3.delete(0, 'end')
            e4.delete(0, 'end')
            e5.delete(0, 'end')
            e6.delete(0, 'end')
            e7.delete(0, 'end')
            e8.delete(0, 'end')
            e9.delete(0, 'end')
            e10.delete(0, 'end')
            treev.insert("", 'end', values=d)

            # errorcanoccur

        except Exception as e:
            print(e)
            tsmg.showinfo("Failed", "Bundle no. exist")
            # errorcanoccur

        connection.close()

        # now i need to store data in sql

    l1 = Label(f4, text="Bundle type", width=8)
    l1.grid(row=0, column=0, padx=5, pady=5)
    e1 = ttk.Combobox(f4, values=bunlis, height=8, width=31)
    e1.grid(row=0, column=1)
    l2 = Label(f4, text="DEN SIZE", padx=5, width=8)
    l2.grid(row=1, column=0, padx=5, pady=5)
    e2 = ttk.Combobox(f4, values=densiz, height=8, width=31)
    e2.grid(row=1, column=1)
    l3 = Label(f4, text="THK REMARK", padx=5, width=8)
    l3.grid(row=2, column=0, padx=5, pady=5)
    e3 = ttk.Combobox(f4, values=remark, height=8, width=31)
    e3.grid(row=2, column=1)
    l4 = Label(f4, text="BUNDLE", padx=5, width=8)
    l4.grid(row=3, column=0, padx=5, pady=5)
    e4 = Entry(f4)
    e4.grid(row=3, column=1)
    l5 = Label(f4, text="COVER", padx=5, width=8)
    l5.grid(row=4, column=0, padx=5, pady=5)
    e5 = Entry(f4)
    e5.grid(row=4, column=1)
    l6 = Label(f4, text="STM", padx=5, width=8)
    l6.grid(row=0, column=5, padx=5, pady=5)
    e6 = Entry(f4)
    e6.grid(row=0, column=6)
    l7 = Label(f4, text="R2", padx=5, width=8)
    l7.grid(row=0, column=3, padx=20, pady=5)
    e7 = Entry(f4)
    e7.grid(row=0, column=4)
    l8 = Label(f4, text="PCS", padx=5, width=8)
    l8.grid(row=1, column=3, padx=5, pady=5)
    e8 = Entry(f4)
    e8.grid(row=1, column=4)
    l9 = Label(f4, text="MM", padx=5, width=8)
    l9.grid(row=2, column=3, padx=5, pady=5)
    e9 = Entry(f4)
    e9.grid(row=2, column=4)
    l10 = Label(f4, text="KGS", padx=5, width=8)
    l10.grid(row=3, column=3, padx=5, pady=5)
    e10 = Entry(f4)
    e10.grid(row=3, column=4)
    l11 = Label(f4, text="PACKINGNO", padx=5, width=8)
    l11.grid(row=4, column=3, padx=5, pady=5)
    e11 = Entry(f4)
    e11.grid(row=4, column=4)
    e11.insert(0, pll)
    l12 = Label(f4, text="DATE ", padx=5, width=8)
    l12.grid(row=3, column=5, padx=5, pady=5)
    e12 = Entry(f4)
    e12.grid(row=3, column=6)
    e12.insert(0, datee)
    l13 = Label(f4, text="STATUS", padx=5, width=8)
    l13.grid(row=1, column=5, padx=20, pady=5)
    e13 = Entry(f4)
    e13.grid(row=1, column=6, padx=5, pady=5)
    e13.insert(0, "INSTOCK")
    e1.focus()
    # deleteifwanttodelete
    e1.bind("<KP_Enter>", lambda x: e2.focus())
    e1.bind("<Return>", lambda x: e2.focus())
    e2.bind("<KP_Enter>", lambda x: e3.focus())
    e2.bind("<Return>", lambda x: e3.focus())
    e3.bind("<KP_Enter>", lambda x: e4.focus())
    e3.bind("<Return>", lambda x: e4.focus())
    e4.bind("<KP_Enter>", lambda x: e5.focus())
    e4.bind("<Return>", lambda x: e5.focus())
    e5.bind("<KP_Enter>", lambda x: e7.focus())
    e5.bind("<Return>", lambda x: e7.focus())
    e7.bind("<KP_Enter>", lambda x: e8.focus())
    e7.bind("<Return>", lambda x: e8.focus())
    e8.bind("<KP_Enter>", lambda x: e9.focus())
    e8.bind("<Return>", lambda x: e9.focus())
    e9.bind("<KP_Enter>", lambda x: e10.focus())
    e9.bind("<Return>", lambda x: e10.focus())
    e10.bind("<KP_Enter>", lambda x: e11.focus())
    e10.bind("<Return>", lambda x: e11.focus())
    e11.bind("<KP_Enter>", lambda x: e6.focus())
    e11.bind("<Return>", lambda x: e6.focus())
    e6.bind("<KP_Enter>", lambda x: e13.focus())
    e6.bind("<Return>", lambda x: e13.focus())
    e13.bind("<KP_Enter>", lambda x: e12.focus())
    e13.bind("<Return>", lambda x: e12.focus())

    def keydown(event):
        ba = e1.get()
        a = ba.upper()
        checklist = []
        for i in bunlis:
            if a in i:
                checklist.append(i)
        e1["values"] = checklist

    e1.bind("<KeyRelease>", keydown)

    def keyup(event):
        e1.event_generate("<Down>")

    e1.bind("<KP_Enter>", keyup)
    e1.bind("<Return>", keyup)

    def keyup2(event):
        e2.event_generate("<Down>")

    e2.bind("<KP_Enter>", keyup2)
    e2.bind("<Return>", keyup2)
    def keydown2(event):
        ba = e2.get()
        a = ba.upper()
        checklist = []
        for i in densiz:
            if a in i:
                checklist.append(i)
        e2["values"] = checklist

    e2.bind("<KeyRelease>", keydown2)

    def keyup3(event):
        e3.event_generate("<Down>")

    e3.bind("<KP_Enter>", keyup3)
    e3.bind("<Return>", keyup3)
    def keydown3(event):
        ba = e3.get()
        a = ba.upper()
        checklist = []
        for i in remark:
            if a in i:
                checklist.append(i)
        e3["values"] = checklist
    e3.bind("<KeyRelease>", keydown3)


    e12.bind("<KP_Enter>", check)
    e12.bind("<Return>", check)

    Button(f4, text="SAVE DATA", command=check).grid(row=4, column=5, columnspan=2, padx=25)

    pass


def addpackingmanual(event):
    f2.destroy()
    f3.destroy()
    f4.destroy()
    addpackingmanual1()


def showstocksbeforesaving1(d):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    treev = ttk.Treeview(f3, selectmode='browse', height=30)
    treev.pack(fill=BOTH)
    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
    treev.configure(xscrollcommand=scrollbar.set)
    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=250, anchor='c')
    treev.column("2", width=300, anchor='c')
    treev.column("3", width=190, anchor='c')
    treev.column("4", width=80, anchor='c')
    treev.column("5", width=100, anchor='c')
    treev.column("6", width=100, anchor='c')
    treev.column("7", width=60, anchor='c')
    treev.column("8", width=60, anchor='c')
    treev.column("9", width=60, anchor='c')
    treev.column("10", width=60, anchor='c')
    treev.column("11", width=80, anchor='c')
    treev.column("12", width=100, anchor='c')
    treev.column("13", width=100, anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="TYPE")
    treev.heading("2", text="DENSIZE")
    treev.heading("3", text="THK REMARK")
    treev.heading("4", text="BUNDLENO")
    treev.heading("5", text="COVER")
    treev.heading("6", text="STM")
    treev.heading("7", text="R2")
    treev.heading("8", text="PCS")
    treev.heading("9", text="MM")
    treev.heading("10", text="KGS")
    treev.heading("11", text="PACKINGLIST")
    treev.heading("12", text="DATE")
    treev.heading("13", text="STATUS")

    # Inserting the items and their features to the
    # columns built
    for row in d:
        s = tuple(row)
        treev.insert("", 'end', values=s)
    s = ("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
    treev.insert("", 'end', values=s)
    s = ("", "TOTAL", "BUNDLE", len(treev.get_children()) - 1, "", "", "", "", "", "", "", "", "", "", "", "")
    treev.insert("", 'end', values=s)

    def savebutton(d):
        b1 = Button(f4, text="save data")

        def insertintotable(e):
            # tablename="stockfinal634"
            # createtable(tablename)
            # here d is the 2d array of excel
            connection = sqlite3.connect("mytables4.db")
            cursor = connection.cursor()
            te = 0
            for row in d:
                sa = f'''INSERT INTO stockfinal634 VALUES ('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}','{row[9]}','{row[10]}','{row[11]}','{row[12]}')'''
                try:
                    cursor.execute(sa)
                    connection.commit()

                except Exception as e:
                    print(e)
                    tsmg.showinfo("Failed", f"Packing list already exist\n {e}")
                    te = 1
                    break
            if (te == 0):
                tsmg.showinfo("success", f"Packing list saved")

            connection.close()
            pass

        b1.bind('<Button-1>', insertintotable)
        b1.pack()
        pass

    savebutton(d)
    pass


def showstocksbeforesaving(d):
    f3.destroy()
    f4.destroy()
    showstocksbeforesaving1(d)


def addpacking(event):
    loc = filedialog.askopenfilename()
    po = open(loc, 'rb')
    pr = PyPDF2.PdfFileReader(po)
    noofpages = pr.getNumPages()
    asqwa = True
    try:
        if (noofpages == 1):
            pob = pr.getPage(0)
            f = pob.extractText()
            d = f.split('\n')
            w = []

            def removespaces(l):
                no = l.count('')
                while (no > 0):
                    l.remove("")
                    no = no - 1
                return (l)

            for i in d:
                l = i.split("  ")
                li = removespaces(l)
                w.append(li)
            # popping the last three lines
            w.pop()
            w.pop()
            w.pop()
            # now we will find packing list no and date
            g = ""
            for i in w:
                try:
                    i.index('P.L.NO')
                    g = i
                except Exception as eas:
                    continue
            if (g == ""):
                for i in w:
                    try:
                        i.index('PL.No')
                        g = i
                    except:
                        continue
            plno = g[2]
            plno = plno.strip()
            dateindex = w.index(g) - 1
            dat = str(w[dateindex][0])
            i1 = dat.find(':')
            pldate = dat[i1 + 1:]
            pldate = pldate.strip()

            for i in w:
                try:
                    i.index('BUNDLE')
                    p = i
                except:
                    continue

            main = w.index(p)
            for i in range(main):
                w.pop(0)
            w.pop(0)
            new = []
            # now we will remove total column that contain total of type
            for i in w:
                if (i[0] == '1'):
                    continue
                elif (i[0] == '2'):
                    continue
                elif (i[0] == '3'):
                    continue
                elif (i[0] == '4'):
                    continue
                elif (i[0] == '5'):
                    continue
                elif (i[0] == '6'):
                    continue
                elif (i[0] == '7'):
                    continue
                elif (i[0] == '8'):
                    continue
                elif (i[0] == '9'):
                    continue
                elif (i[0] == '10'):
                    continue
                elif (i[0] == '11'):
                    continue
                elif (i[0] == '12'):
                    continue
                elif (i[0] == '13'):
                    continue
                elif (i[0] == '14'):
                    continue
                elif (i[0] == '15'):
                    continue
                elif (i[0] == '16'):
                    continue
                elif (i[0] == '17'):
                    continue
                else:
                    new.append(i)
            w = new
            new = []
            base = ""
            for i in w:
                if (len(i) == 1):
                    base = i[0]
                else:
                    e = []
                    e.append(base)
                    for j in i:
                        e.append(j)
                    new.append(e)
            w = new

            for i in range(len(w)):
                if (i % 2 == 0):
                    if (len(w[i]) > 3):
                        # i need to merge them
                        if (len(w[i]) == 4):
                            w[i][1] = w[i][1] + w[i][2]
                            w[i].pop(2)
                        elif (len(w[i]) == 5):
                            w[i][1] = w[i][1] + w[i][2] + w[i][3]
                            w[i].pop(2)
                            w[i].pop(2)
                    elif (len(w[i]) < 3):
                        w[i].append('')
                    else:
                        continue
                else:
                    w[i].pop(0)
                    if (w[i][0].count(" ") == 1):
                        we = w[i][0].split(" ")
                        w[i].pop(0)
                        w[i].insert(0, we[1])
                        w[i].insert(0, we[0])

                    if (len(w[i]) == 7):
                        continue
                    elif (len(w[i]) < 7):
                        while (len(w[i]) != 7):
                            w[i].insert(1, '')
                    else:
                        diff = len(w[i]) - 7
                        for i2 in range(diff):
                            w[i].pop(2)

            l1 = []
            l2 = []
            for i in range(len(w)):
                if (i % 2 == 0):
                    l1.append(w[i])
                else:
                    l2.append(w[i])
            l3 = []
            for i in range(len(l1)):
                l4 = l1[i] + l2[i]
                l3.append(l4)
            d = l3
            pldate = pldate.replace("/", "-")

            if pldate.count('-') == 2 and pldate.index('-') == 2 and pldate.index('-', 3) == 5 and len(pldate) == 10:
                date1 = pldate.split('-')
                date1.reverse()
                date2 = "-".join(date1)
                pldate = date2
            elif pldate.count('-') == 2 and pldate.index('-') == 4 and pldate.index('-', 5) == 7 and len(pldate) == 10:
                date2 = pldate
                pldate = date2
            else:
                tsmg.showinfo("FORMAT", "Wrong date format")
                t1 = Toplevel(background="bisque")
                t1.title("DATE")
                t1.minsize(250, 150)
                l1 = Label(t1, text=" DATE ")
                l1.grid(row=0, column=0, padx=5, pady=5)
                e1 = Entry(t1)
                e1.grid(row=0, column=1)
                e1.focus()

                def setdate(*eve):
                    global pldate
                    getd = e1.get()
                    if getd.count('-') == 2 and getd.index('-') == 2 and getd.index('-', 3) == 5 and len(
                            getd) == 10:
                        date1 = getd.split('-')
                        date1.reverse()
                        date2 = "-".join(date1)
                        pldate = date2
                    elif getd.count('-') == 2 and getd.index('-') == 4 and getd.index('-', 5) == 7 and len(
                            getd) == 10:
                        date2 = getd
                        pldate = date2
                    else:
                        tsmg.showinfo("FORMAT", "Wrong date format")
                    t1.destroy()

                b1 = Button(t1, text="    SET    ", command=setdate)
                b1.grid(row=1, column=0, columnspan=2)

            for i in d:
                i.append(plno)
                i.append(pldate)
                status = "INSTOCK"
                try:
                    qwa = int(i[7])
                except Exception as e:
                    i[7] = i[8]
                    i[8] = ''
                i.append(status)
            showstocksbeforesaving(d)
        else:
            pob = pr.getPage(0)
            f = pob.extractText()
            d = f.split('\n')
            w = []

            def removespaces(l):
                no = l.count('')
                while (no > 0):
                    l.remove("")
                    no = no - 1
                return (l)

            for i in d:
                l = i.split("  ")
                li = removespaces(l)
                w.append(li)

            # now we will find packing list no and date
            g = ""
            for i in w:
                try:
                    i.index('P.L.NO')
                    g = i
                except Exception as eas:
                    continue
            if (g == ""):
                for i in w:
                    try:
                        i.index('PL.No')
                        g = i
                    except:
                        continue
            plno = g[2]
            plno = plno.strip()
            dateindex = w.index(g) - 1
            dat = str(w[dateindex][0])
            i1 = dat.find(':')
            pldate = dat[i1 + 1:]
            pldate = pldate.strip()

            for i in w:
                try:
                    i.index('BUNDLE')
                    p = i
                except:
                    continue

            main = w.index(p)
            for i in range(main):
                w.pop(0)
            w.pop(0)
            new = []
            # now we will remove total column that contain total of type
            for i in w:
                if (i[0] == '1'):
                    continue
                elif (i[0] == '2'):
                    continue
                elif (i[0] == '3'):
                    continue
                elif (i[0] == '4'):
                    continue
                elif (i[0] == '5'):
                    continue
                elif (i[0] == '6'):
                    continue
                elif (i[0] == '7'):
                    continue
                elif (i[0] == '8'):
                    continue
                elif (i[0] == '9'):
                    continue
                elif (i[0] == '10'):
                    continue
                elif (i[0] == '11'):
                    continue
                elif (i[0] == '12'):
                    continue
                elif (i[0] == '13'):
                    continue
                elif (i[0] == '14'):
                    continue
                elif (i[0] == '15'):
                    continue
                elif (i[0] == '16'):
                    continue
                elif (i[0] == '17'):
                    continue
                else:
                    new.append(i)
            w = new
            new = []
            base = ""
            for i in w:
                if (len(i) == 1):
                    base = i[0]
                else:
                    e = []
                    e.append(base)
                    for j in i:
                        e.append(j)
                    new.append(e)
            w = new

            for i in range(len(w)):
                if (i % 2 == 0):
                    if (len(w[i]) > 3):
                        # i need to merge them
                        if (len(w[i]) == 4):
                            w[i][1] = w[i][1] + w[i][2]
                            w[i].pop(2)
                        elif (len(w[i]) == 5):
                            w[i][1] = w[i][1] + w[i][2] + w[i][3]
                            w[i].pop(2)
                            w[i].pop(2)
                    elif (len(w[i]) < 3):
                        w[i].append('')
                    else:
                        continue
                else:
                    w[i].pop(0)
                    if (w[i][0].count(" ") == 1):
                        we = w[i][0].split(" ")
                        w[i].pop(0)
                        w[i].insert(0, we[1])
                        w[i].insert(0, we[0])

                    if (len(w[i]) == 7):
                        continue
                    elif (len(w[i]) < 7):
                        while (len(w[i]) != 7):
                            w[i].insert(1, '')
                    else:
                        diff = len(w[i]) - 7
                        for i2 in range(diff):
                            w[i].pop(2)

            l1 = []
            l2 = []
            for i in range(len(w)):
                print(w[i])
                if (i % 2 == 0):
                    l1.append(w[i])
                else:
                    l2.append(w[i])
            l3 = []
            #modified
            # earlier it was only len(l1) now we are using min of l1 ans l2
            for i in range(min(len(l1),len(l2))):
                l4 = l1[i] + l2[i]
                l3.append(l4)
            d = l3
            pldate = pldate.replace("/", "-")

            if pldate.count('-') == 2 and pldate.index('-') == 2 and pldate.index('-', 3) == 5 and len(pldate) == 10:
                date1 = pldate.split('-')
                date1.reverse()
                date2 = "-".join(date1)
                pldate = date2
            elif pldate.count('-') == 2 and pldate.index('-') == 4 and pldate.index('-', 5) == 7 and len(pldate) == 10:
                date2 = pldate
                pldate = date2
            else:
                tsmg.showinfo("FORMAT", "Wrong date format")
                t1 = Toplevel(background="bisque")
                t1.title("DATE")
                t1.minsize(250, 150)
                l1 = Label(t1, text=" DATE ")
                l1.grid(row=0, column=0, padx=5, pady=5)
                e1 = Entry(t1)
                e1.grid(row=0, column=1)
                e1.focus()

                def setdate(*eve):
                    global pldate
                    getd = e1.get()
                    if getd.count('-') == 2 and getd.index('-') == 2 and getd.index('-', 3) == 5 and len(
                            getd) == 10:
                        date1 = getd.split('-')
                        date1.reverse()
                        date2 = "-".join(date1)
                        pldate = date2
                    elif getd.count('-') == 2 and getd.index('-') == 4 and getd.index('-', 5) == 7 and len(
                            getd) == 10:
                        date2 = getd
                        pldate = date2
                    else:
                        tsmg.showinfo("FORMAT", "Wrong date format")
                    t1.destroy()

                b1 = Button(t1, text="    SET    ", command=setdate)
                b1.grid(row=1, column=0, columnspan=2)

            for i in d:
                i.append(plno)
                i.append(pldate)
                status = "INSTOCK"
                i.append(status)
            dfortwopages = d.copy()

            pob = pr.getPage(1)
            f = pob.extractText()
            d = f.split('\n')
            w = []

            def removespaces(l):
                no = l.count('')
                while (no > 0):
                    l.remove("")
                    no = no - 1
                return (l)

            for i in d:
                l = i.split("  ")
                li = removespaces(l)
                w.append(li)
            # popping the last three lines
            w.pop()
            w.pop()
            w.pop()
            # now we will find packing list no and date
            g = ""
            for i in w:
                try:
                    i.index('P.L.NO')
                    g = i
                except Exception as eas:
                    continue
            if (g == ""):
                for i in w:
                    try:
                        i.index('PL.No')
                        g = i
                    except:
                        continue
            plno = g[2]
            plno = plno.strip()
            dateindex = w.index(g) - 1
            dat = str(w[dateindex][0])
            i1 = dat.find(':')
            pldate = dat[i1 + 1:]
            pldate = pldate.strip()

            for i in w:
                try:
                    i.index('BUNDLE')
                    p = i
                except:
                    continue

            main = w.index(p)
            for i in range(main):
                w.pop(0)
            w.pop(0)
            new = []
            # now we will remove total column that contain total of type
            for i in w:
                if (i[0] == '1'):
                    continue
                elif (i[0] == '2'):
                    continue
                elif (i[0] == '3'):
                    continue
                elif (i[0] == '4'):
                    continue
                elif (i[0] == '5'):
                    continue
                elif (i[0] == '6'):
                    continue
                elif (i[0] == '7'):
                    continue
                elif (i[0] == '8'):
                    continue
                elif (i[0] == '9'):
                    continue
                elif (i[0] == '10'):
                    continue
                elif (i[0] == '11'):
                    continue
                elif (i[0] == '12'):
                    continue
                elif (i[0] == '13'):
                    continue
                elif (i[0] == '14'):
                    continue
                elif (i[0] == '15'):
                    continue
                elif (i[0] == '16'):
                    continue
                elif (i[0] == '17'):
                    continue
                else:
                    new.append(i)
            w = new
            new = []
            base = ""
            for i in w:
                if (len(i) == 1):
                    base = i[0]
                else:
                    e = []
                    e.append(base)
                    for j in i:
                        e.append(j)
                    new.append(e)
            w = new

            for i in range(len(w)):
                if (i % 2 == 0):
                    if (len(w[i]) > 3):
                        # i need to merge them
                        if (len(w[i]) == 4):
                            w[i][1] = w[i][1] + w[i][2]
                            w[i].pop(2)
                        elif (len(w[i]) == 5):
                            w[i][1] = w[i][1] + w[i][2] + w[i][3]
                            w[i].pop(2)
                            w[i].pop(2)
                    elif (len(w[i]) < 3):
                        w[i].append('')
                    else:
                        continue
                else:
                    w[i].pop(0)
                    if (w[i][0].count(" ") == 1):
                        we = w[i][0].split(" ")
                        w[i].pop(0)
                        w[i].insert(0, we[1])
                        w[i].insert(0, we[0])

                    if (len(w[i]) == 7):
                        continue
                    elif (len(w[i]) < 7):
                        while (len(w[i]) != 7):
                            w[i].insert(1, '')
                    else:
                        diff = len(w[i]) - 7
                        for i2 in range(diff):
                            w[i].pop(2)

            l1 = []
            l2 = []
            for i in range(len(w)):
                if (i % 2 == 0):
                    l1.append(w[i])
                else:
                    l2.append(w[i])
            l3 = []
            for i in range(len(l1)):
                l4 = l1[i] + l2[i]
                l3.append(l4)
            d = l3
            pldate = pldate.replace("/", "-")

            if pldate.count('-') == 2 and pldate.index('-') == 2 and pldate.index('-', 3) == 5 and len(pldate) == 10:
                date1 = pldate.split('-')
                date1.reverse()
                date2 = "-".join(date1)
                pldate = date2
            elif pldate.count('-') == 2 and pldate.index('-') == 4 and pldate.index('-', 5) == 7 and len(pldate) == 10:
                date2 = pldate
                pldate = date2
            else:
                tsmg.showinfo("FORMAT", "Wrong date format")
                t1 = Toplevel(background="bisque")
                t1.title("DATE")
                t1.minsize(250, 150)
                l1 = Label(t1, text=" DATE ")
                l1.grid(row=0, column=0, padx=5, pady=5)
                e1 = Entry(t1)
                e1.grid(row=0, column=1)
                e1.focus()

                def setdate(*eve):
                    global pldate
                    getd = e1.get()
                    if getd.count('-') == 2 and getd.index('-') == 2 and getd.index('-', 3) == 5 and len(
                            getd) == 10:
                        date1 = getd.split('-')
                        date1.reverse()
                        date2 = "-".join(date1)
                        pldate = date2
                    elif getd.count('-') == 2 and getd.index('-') == 4 and getd.index('-', 5) == 7 and len(
                            getd) == 10:
                        date2 = getd
                        pldate = date2
                    else:
                        tsmg.showinfo("FORMAT", "Wrong date format")
                    t1.destroy()

                b1 = Button(t1, text="    SET    ", command=setdate)
                b1.grid(row=1, column=0, columnspan=2)

            for i in d:
                i.append(plno)
                i.append(pldate)
                status = "INSTOCK"
                i.append(status)
            for i in d:
                try:
                    qwa = int(i[7])
                except Exception as e:
                    i[7] = i[8]
                    i[8] = ''
                dfortwopages.append(i)
            showstocksbeforesaving(dfortwopages)
    except Exception as e:
        if (asqwa == True):
            pob = pr.getPage(0)
            f = pob.extractText()
            d = f.split('\n')
            w = []

            def removespaces(l):
                no = l.count('')
                while (no > 0):
                    l.remove("")
                    no = no - 1
                return (l)

            for i in d:
                l = i.split("  ")
                li = removespaces(l)
                w.append(li)
            # popping the last three lines
            w.pop()
            w.pop()
            w.pop()
            # now we will find packing list no and date
            g = ""
            for i in w:
                try:
                    i.index('P.L.NO')
                    g = i
                except Exception as eas:
                    continue
            if (g == ""):
                for i in w:
                    try:
                        i.index('PL.No')
                        g = i
                    except:
                        continue
            plno = g[2]
            plno = plno.strip()
            dateindex = w.index(g) - 1
            dat = str(w[dateindex][0])
            i1 = dat.find(':')
            pldate = dat[i1 + 1:]
            pldate = pldate.strip()

            for i in w:
                try:
                    i.index('BUNDLE')
                    p = i
                except:
                    continue

            main = w.index(p)
            for i in range(main):
                w.pop(0)
            w.pop(0)
            new = []
            # now we will remove total column that contain total of type
            for i in w:
                if (i[0] == '1'):
                    continue
                elif (i[0] == '2'):
                    continue
                elif (i[0] == '3'):
                    continue
                elif (i[0] == '4'):
                    continue
                elif (i[0] == '5'):
                    continue
                elif (i[0] == '6'):
                    continue
                elif (i[0] == '7'):
                    continue
                elif (i[0] == '8'):
                    continue
                elif (i[0] == '9'):
                    continue
                elif (i[0] == '10'):
                    continue
                elif (i[0] == '11'):
                    continue
                elif (i[0] == '12'):
                    continue
                elif (i[0] == '13'):
                    continue
                elif (i[0] == '14'):
                    continue
                elif (i[0] == '15'):
                    continue
                elif (i[0] == '16'):
                    continue
                elif (i[0] == '17'):
                    continue
                else:
                    new.append(i)
            w = new
            new = []
            base = ""
            for i in w:
                if (len(i) == 1):
                    base = i[0]
                else:
                    e = []
                    e.append(base)
                    for j in i:
                        e.append(j)
                    new.append(e)
            w = new

            for i in range(len(w)):
                if (i % 2 == 0):
                    if (len(w[i]) > 3):
                        # i need to merge them
                        if (len(w[i]) == 4):
                            w[i][1] = w[i][1] + w[i][2]
                            w[i].pop(2)
                        elif (len(w[i]) == 5):
                            w[i][1] = w[i][1] + w[i][2] + w[i][3]
                            w[i].pop(2)
                            w[i].pop(2)
                    elif (len(w[i]) < 3):
                        w[i].append('')
                    else:
                        continue
                else:
                    w[i].pop(0)
                    if (w[i][0].count(" ") == 1):
                        we = w[i][0].split(" ")
                        w[i].pop(0)
                        w[i].insert(0, we[1])
                        w[i].insert(0, we[0])

                    if (len(w[i]) == 7):
                        continue
                    elif (len(w[i]) < 7):
                        while (len(w[i]) != 7):
                            w[i].insert(1, '')
                    else:
                        diff = len(w[i]) - 7
                        for i2 in range(diff):
                            w[i].pop(2)

            l1 = []
            l2 = []
            for i in range(len(w)):
                if (i % 2 == 0):
                    l1.append(w[i])
                else:
                    l2.append(w[i])
            l3 = []
            for i in range(min(len(l1),len(l2))):
                l4 = l1[i] + l2[i]
                l3.append(l4)
            d = l3
            pldate = pldate.replace("/", "-")

            if pldate.count('-') == 2 and pldate.index('-') == 2 and pldate.index('-', 3) == 5 and len(pldate) == 10:
                date1 = pldate.split('-')
                date1.reverse()
                date2 = "-".join(date1)
                pldate = date2
            elif pldate.count('-') == 2 and pldate.index('-') == 4 and pldate.index('-', 5) == 7 and len(pldate) == 10:
                date2 = pldate
                pldate = date2
            else:
                tsmg.showinfo("FORMAT", "Wrong date format")
                t1 = Toplevel(background="bisque")
                t1.title("DATE")
                t1.minsize(250, 150)
                l1 = Label(t1, text=" DATE ")
                l1.grid(row=0, column=0, padx=5, pady=5)
                e1 = Entry(t1)
                e1.grid(row=0, column=1)
                e1.focus()

                def setdate(*eve):
                    global pldate
                    getd = e1.get()
                    if getd.count('-') == 2 and getd.index('-') == 2 and getd.index('-', 3) == 5 and len(
                            getd) == 10:
                        date1 = getd.split('-')
                        date1.reverse()
                        date2 = "-".join(date1)
                        pldate = date2
                    elif getd.count('-') == 2 and getd.index('-') == 4 and getd.index('-', 5) == 7 and len(
                            getd) == 10:
                        date2 = getd
                        pldate = date2
                    else:
                        tsmg.showinfo("FORMAT", "Wrong date format")
                    t1.destroy()

                b1 = Button(t1, text="    SET    ", command=setdate)
                b1.grid(row=1, column=0, columnspan=2)

            for i in d:
                i.append(plno)
                i.append(pldate)
                status = "INSTOCK"
                try:
                    qwa = int(i[7])
                except Exception as e:
                    i[7] = i[8]
                    i[8] = ''
                i.append(status)
            showstocksbeforesaving(d)

    pass


def importfromexcel(event):
    tsmg.showinfo("Warning", "it will read only first 13 column")
    loc = filedialog.askopenfilename()
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    mainlist = []
    for i in range(sheet.nrows):
        listimport = []
        for j in range(sheet.ncols):
            listimport.append(sheet.cell_value(i, j))
        mainlist.append(listimport)
    ques = tsmg.askquestion("Chose", "does first row contain heading ??")
    try:
        if (ques == 'no'):
            showstocksbeforesaving(mainlist)
        else:
            mainlist.pop(0)
            showstocksbeforesaving(mainlist)
    except Exception as e:
        print(e)


def splitbundle1(event):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    l = Label(f4, text="BUNDLE NUMBER YOU WANT TO SPLIT")
    l.grid(row=0, column=0, padx=5, pady=5)
    e = Entry(f4)
    e.grid(row=0, column=1)
    e.focus()

    def check(*args):
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM stockfinal634 WHERE BUNDLE ='{e.get()}';")
        w = crsr.fetchall()
        if (len(w) == 0):
            tsmg.showinfo("Warning", "NOT IN STOCK")
            pass

        else:
            d = list(w[0])
            connection.close()
            if (d[12] == "SOLD"):
                tsmg.showinfo("Warning", "ALREADY SOLD")
            else:
                e.grid_remove()
                l.grid_remove()
                strdat = str(d)
                Label(f4, text=strdat).grid()

                Label(f3, text=f"{d[3]}A").grid(row=1, column=0, columnspan=2, padx=10)
                Label(f3, text=f"{d[3]}B").grid(row=1, column=2, columnspan=2, padx=10)
                Label(f3, text="PCS").grid(row=2, column=0, padx=10, pady=15)
                e1 = Entry(f3)
                e1.grid(row=2, column=1)
                Label(f3, text="PCS").grid(row=2, column=2, padx=10, pady=15)
                e2 = Entry(f3)
                e2.grid(row=2, column=3)
                Label(f3, text="KGS").grid(row=3, column=0, padx=10, pady=15)
                e3 = Entry(f3)
                e3.grid(row=3, column=1)
                Label(f3, text="KGS").grid(row=3, column=2, padx=10, pady=15)
                e4 = Entry(f3)
                e4.grid(row=3, column=3)
                e1.focus()
                e1.bind("<KP_Enter>", lambda x: e2.focus())
                e1.bind("<Return>", lambda x: e2.focus())
                e2.bind("<KP_Enter>", lambda x: e3.focus())
                e2.bind("<KP_Enter>", lambda x: e3.focus())
                e3.bind("<KP_Enter>", lambda x: e4.focus())
                e3.bind("<Return>", lambda x: e4.focus())

                def checkewd(*args):

                    d1a = d.copy()
                    d1b = d.copy()
                    d1a[3] = f"{d[3]}A"
                    d1b[3] = f"{d[3]}B"
                    d1a[7] = e1.get()
                    d1b[7] = e2.get()
                    d1a[9] = e3.get()
                    d1b[9] = e4.get()
                    d1a[12] = "SPLIT"
                    d1b[12] = "SPLIT"
                    connection = sqlite3.connect("mytables4.db")
                    cursor = connection.cursor()
                    row = d1a
                    sa = f'''INSERT INTO stockfinal634 VALUES ('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}','{row[9]}','{row[10]}','{row[11]}','{row[12]}')'''
                    cursor.execute(sa)
                    connection.commit()
                    row = d1b
                    sa = f'''INSERT INTO stockfinal634 VALUES ('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}','{row[9]}','{row[10]}','{row[11]}','{row[12]}')'''
                    cursor.execute(sa)
                    connection.commit()
                    connection.close()
                    connection = sqlite3.connect("mytables4.db")
                    crsr = connection.cursor()
                    crsr.execute(f"DELETE FROM stockfinal634 WHERE BUNDLE ='{e.get()}';")
                    connection.commit()
                    connection.close()
                    tsmg.showinfo("completed", "Bundle Splited")
                    addbundle(event)

                    pass

                e4.bind("<KP_Enter>", checkewd)
                e4.bind("<Return>", checkewd)
                Button(f3, text="SLPIT", command=checkewd).grid(row=4, column=2, columnspan=2, padx=25)

        pass

    e.bind("<Return>", check)
    e.bind("<KP_Enter>", check)

    Button(f4, text="SEARCH", command=check).grid(row=2, column=0, columnspan=2, padx=25)

    pass


def splitbundle(event):
    f3.destroy()
    f4.destroy()
    splitbundle1(event)


def searchbundleno1(event):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute(f"SELECT * FROM stockfinal634")
    w = crsr.fetchall()
    connection.close()
    bunlis = []
    for i in w:
        bunlis.append(i[3])

    def check():

        # we will retrive our data from here
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM stockfinal634 WHERE BUNDLE ='{e.get()}';")
        w = crsr.fetchall()
        if (len(w) == 0):
            Button(f4, text="NOT FOUND").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')
            pass

        else:
            d = list(w[0])
            connection.close()

            # now we will set the values
            l1 = Label(f3, text="Bundle type", width=8)
            l1.grid(row=0, column=0, padx=5, pady=5)
            e1 = Entry(f3)
            e1.grid(row=0, column=1)
            l2 = Label(f3, text="DEN SIZE", padx=5, width=8)
            l2.grid(row=1, column=0, padx=5, pady=5)
            e2 = Entry(f3)
            e2.grid(row=1, column=1)
            l3 = Label(f3, text="THK REMARK", padx=5, width=8)
            l3.grid(row=2, column=0, padx=5, pady=5)
            e3 = Entry(f3)
            e3.grid(row=2, column=1)
            l4 = Label(f3, text="BUNDLE", padx=5, width=8)
            l4.grid(row=3, column=0, padx=5, pady=5)
            e4 = Entry(f3)
            e4.grid(row=3, column=1)
            l5 = Label(f3, text="COVER", padx=5, width=8)
            l5.grid(row=4, column=0, padx=5, pady=5)
            e5 = Entry(f3)
            e5.grid(row=4, column=1)
            l6 = Label(f3, text="STM", padx=5, width=8)
            l6.grid(row=0, column=5, padx=5, pady=5)
            e6 = Entry(f3)
            e6.grid(row=0, column=6)
            l7 = Label(f3, text="R2", padx=5, width=8)
            l7.grid(row=0, column=3, padx=20, pady=5)
            e7 = Entry(f3)
            e7.grid(row=0, column=4)
            l8 = Label(f3, text="PCS", padx=5, width=8)
            l8.grid(row=1, column=3, padx=5, pady=5)
            e8 = Entry(f3)
            e8.grid(row=1, column=4)
            l9 = Label(f3, text="MM", padx=5, width=8)
            l9.grid(row=2, column=3, padx=5, pady=5)
            e9 = Entry(f3)
            e9.grid(row=2, column=4)
            l10 = Label(f3, text="KGS", padx=5, width=8)
            l10.grid(row=3, column=3, padx=5, pady=5)
            e10 = Entry(f3)
            e10.grid(row=3, column=4)
            l11 = Label(f3, text="PACKINGNO", padx=5, width=8)
            l11.grid(row=4, column=3, padx=5, pady=5)
            e11 = Entry(f3)
            e11.grid(row=4, column=4)
            l12 = Label(f3, text="DATE", padx=5, width=8)
            l12.grid(row=3, column=5, padx=5, pady=5)
            e12 = Entry(f3)
            e12.grid(row=3, column=6)
            l13 = Label(f3, text="STATUS", padx=5, width=8)
            l13.grid(row=1, column=5, padx=20, pady=5)
            e13 = Entry(f3)
            e13.grid(row=1, column=6, padx=5, pady=5)

            e1.insert(0, d[0])
            e2.insert(0, d[1])
            e3.insert(0, d[2])
            e4.insert(0, d[3])
            e5.insert(0, d[4])
            e6.insert(0, d[5])
            e7.insert(0, d[6])
            e8.insert(0, d[7])
            e9.insert(0, d[8])
            e10.insert(0, d[9])
            e11.insert(0, d[10])
            e12.insert(0, d[11])
            e13.insert(0, d[12])

            def update():
                d1 = []
                d1.append(e1.get())
                d1.append(e2.get())
                d1.append(e3.get())
                d1.append(e4.get())
                d1.append(e5.get())
                d1.append(e6.get())
                d1.append(e7.get())
                d1.append(e8.get())
                d1.append(e9.get())
                d1.append(e10.get())
                d1.append(e11.get())

                as1 = e12.get()
                if as1.count('-') == 2 and as1.index('-') == 2 and as1.index('-', 3) == 5 and len(as1) == 10:
                    date1 = as1.split('-')
                    date1.reverse()
                    date2 = "-".join(date1)
                    d1.append(date2)
                elif as1.count('-') == 2 and as1.index('-') == 4 and as1.index('-', 5) == 7 and len(as1) == 10:
                    d1.append(as1)
                else:
                    tsmg.showinfo("FORMAT", "Wrong date format")
                    return
                d1.append(e13.get())
                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(f"DELETE FROM stockfinal634 WHERE BUNDLE ='{e.get()}';")
                connection.commit()

                row = d1
                sa = f'''INSERT INTO stockfinal634 VALUES ('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}','{row[9]}','{row[10]}','{row[11]}','{row[12]}')'''
                try:
                    crsr.execute(sa)
                    tsmg.showinfo("Saved", "your entry has been saved")
                    connection.commit()
                    searchbundleno(event)

                except Exception as eas:
                    row = d
                    sa = f'''INSERT INTO stockfinal634 VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}","{row[8]}","{row[9]}","{row[10]}","{row[11]}","{row[12]}")'''
                    crsr.execute(sa)
                    connection.commit()
                    tsmg.showinfo("Failed", "Bundle no. exist")
                connection.close()

            def showbill():
                bno = e.get()
                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(f"SELECT * FROM billstock5 WHERE BUNDLENO ='{bno}'")
                down = crsr.fetchall()
                connection.close()
                billno = down[0][0]
                bundlebuyer = down[0][1]
                f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
                f3.grid(row=0, column=2, sticky="nsew")
                treev1 = ttk.Treeview(f3, selectmode='browse', height=20)
                treev1.pack(fill=BOTH)
                scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev1.xview)
                scrollbar.pack(side=BOTTOM, fill=X)
                treev1["columns"] = ("1", "2", "3", "4", "5", "6", "7")
                treev1.configure(xscrollcommand=scrollbar.set)
                treev1['show'] = 'headings'

                treev1.column("1", anchor='c')
                treev1.column("2", width=200, anchor='c')
                treev1.column("3", width=80, anchor='c')
                treev1.column("4", width=80, anchor='c')
                treev1.column("5", width=80, anchor='c')
                treev1.column("6", width=80, anchor='c')
                treev1.column("7", width=80, anchor='c')
                na = bundlebuyer
                na = na.upper()
                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
                sel = crsr.fetchall()
                connection.close()
                sel = list(sel[0])
                r1 = ("NAME", sel[0], "", "BILLNO", billno, "", "")
                r2 = ("ADD1", sel[1], "", "MOBILENO", sel[5], "", "")
                r3 = ("ADD2", sel[2], "", "DATE", down[0][7], "", "")
                treev1.insert("", 'end', values=r1)
                treev1.insert("", 'end', values=r2)
                treev1.insert("", 'end', values=r3)
                r31 = ("", "", "", "", "", "", "")
                treev1.insert("", 'end', values=r31)
                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(f"SELECT * FROM billstock5 WHERE BILLNo ='{billno}'")
                d = crsr.fetchall()
                connection.close()
                total = []
                for i in d:
                    listforinsert = []
                    listforinsert.append(i[2])
                    listforinsert.append(i[3])
                    listforinsert.append(i[4])
                    listforinsert.append(i[5])
                    listforinsert.append(i[6])
                    listforinsert.append(i[8])
                    listforinsert.append(i[9])
                    total.append(int(i[9]))
                    treev1.insert("", 'end', values=listforinsert)
                r312 = ("", "", "", "", "", "", "")
                treev1.insert("", 'end', values=r312)
                r32 = ("", "", "", "", "", "", "")
                treev1.insert("", 'end', values=r32)
                r33 = ("", "", "", "", "TOTAL", "", sum(total))
                treev1.insert("", 'end', values=r33, tags=('tot',))
                treev1.tag_configure('tot', background='light blue')

            if (d[12] == "SOLD"):
                Button(f4, text=" SHOW BILL ", command=showbill).grid(row=2, column=3, columnspan=2, padx=250,
                                                                      sticky='nw')

            else:
                Button(f4, text="    UPDATE    ", command=update).grid(row=2, column=3, columnspan=2, padx=250,
                                                                       sticky='nw')

        pass

    l = Label(f4, text="BUNDLE NO", width=8)
    l.grid(row=0, column=0, padx=5, pady=5)
    e = ttk.Combobox(f4, values=bunlis, height=8)
    e.grid(row=0, column=1)
    e.focus()

    def keydown(event):
        ba = e.get()
        a = ba.upper()
        checklist = []
        for i in bunlis:
            if a in i:
                checklist.append(i)
        e["values"] = checklist

    e.bind("<KeyRelease>", keydown)

    def keyup(event):
        e.event_generate("<Down>")

    e.bind("<KP_Enter>", keyup)
    e.bind("<Return>", keyup)
    Button(f4, text="SEARCH", command=check).grid(row=2, column=0, columnspan=2, padx=25)

    pass


def searchbundleno(event):
    f3.destroy()
    f4.destroy()
    searchbundleno1(event)


def searchpl1(event):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    def check():
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM stockfinal634 WHERE PACKINGLIST ='{e.get()}';")
        w = crsr.fetchall()
        if (len(w) == 0):
            Button(f4, text="NOT FOUND").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')
            pass

        else:
            d = []
            for i in w:
                d.append(list(i))
            connection.close()

            def desa1(d):
                global f3
                f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
                f3.grid(row=0, column=2, sticky="nsew")

                treev = ttk.Treeview(f3, selectmode='browse', height=20)
                treev.pack(fill=BOTH)
                scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
                scrollbar.pack(side=BOTTOM, fill=X)
                treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
                treev.configure(xscrollcommand=scrollbar.set)
                # Defining heading
                treev['show'] = 'headings'

                # Assigning the width and anchor to  the
                # respective columns
                treev.column("1", width=250, anchor='c')
                treev.column("2", width=300, anchor='c')
                treev.column("3", width=150, anchor='c')
                treev.column("4", width=80, anchor='c')
                treev.column("5", width=100, anchor='c')
                treev.column("6", width=100, anchor='c')
                treev.column("7", width=60, anchor='c')
                treev.column("8", width=60, anchor='c')
                treev.column("9", width=60, anchor='c')
                treev.column("10", width=60, anchor='c')
                treev.column("11", width=80, anchor='c')
                treev.column("12", width=100, anchor='c')
                treev.column("13", width=100, anchor='c')

                # Assigning the heading names to the
                # respective columns
                treev.heading("1", text="TYPE")
                treev.heading("2", text="DENSIZE")
                treev.heading("3", text="THK REMARK")
                treev.heading("4", text="BUNDLENO")
                treev.heading("5", text="COVER")
                treev.heading("6", text="STM")
                treev.heading("7", text="R2")
                treev.heading("8", text="PCS")
                treev.heading("9", text="MM")
                treev.heading("10", text="KGS")
                treev.heading("11", text="PACKINGLIST")
                treev.heading("12", text="DATE")
                treev.heading("13", text="STATUS")
                # Inserting the items and their features to the
                # columns built
                for row in d:
                    s = tuple(row)
                    treev.insert("", 'end', values=s, tags=(s[12],))
                treev.tag_configure('SOLD', background='light green')
                treev.tag_configure('SPLIT', background='light blue')

            def desa(d):
                f3.destroy()
                desa1(d)

            desa(d)

            Button(f4, text=" FOUND   ").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')

    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute(f"SELECT * FROM stockfinal634 WHERE DATE >= '{from_date}' AND DATE <= '{to_date}' ")
    w = crsr.fetchall()
    connection.close()
    treev = ttk.Treeview(f3, selectmode='browse', height=19)
    treev.pack(fill=X)

    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev.configure(xscrollcommand=scrollbar.set)
    treev["columns"] = ("1", "2", "3")
    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", anchor='c')
    treev.column("2", anchor='c')
    treev.column("3", anchor='c')
    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="DATE")
    treev.heading("2", text="PACKING LIST")
    treev.heading("3", text="BUNDLES")
    dict = {}
    for s in w:
        if s[10] not in dict:
            dict[s[10]] = [s[11], s[10], 1]
        else:
            dict[s[10]][2] = dict[s[10]][2] + 1

    tes = dict.items()
    tes = list(tes)
    s = []
    for i in tes:
        asq = i[1][0].split('-')
        asq = ''.join(asq)
        i[1].append(asq)
        s.append(i[1])
    reswer = sorted(s, key=lambda x: x[3])
    reswer.reverse()
    for u in reswer:
        u.pop()
        treev.insert("", 'end', values=u)

    def clickedrow(event):
        item = treev.identify_row(event.y)
        if item:
            a = treev.item(item, 'values')
            a = list(a)
            e.insert(0, a[1])

        pass

    treev.bind("<Double-Button-1>", clickedrow)

    l = Label(f4, text=" PLNO  ", width=10)
    l.grid(row=0, column=0, padx=5, pady=5)
    e = Entry(f4)
    e.grid(row=0, column=1)
    Button(f4, text="SEARCH", command=check).grid(row=2, column=0, columnspan=2, padx=25)
    e.focus()

    pass


def searchpl(event):
    f3.destroy()
    f4.destroy()
    searchpl1(event)


def searchbundlename1(event):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute(f"SELECT * FROM stockfinal634")
    w = crsr.fetchall()
    connection.close()
    typelis = []
    for i in w:
        stri = str(i[0])
        typelis.append(stri.upper())
    typelist = set(typelis)
    listbox = Listbox(f3, bg="#FDEDEC", font=("Times", 15), fg="Green", height=15, selectmode=EXTENDED)
    listbox.pack(fill="both")
    l = Label(f4, text=" TYPE", width=20)
    l.grid(row=0, column=0, padx=5, pady=5)
    e = Entry(f4, width=20)
    e.grid(row=0, column=1)
    e.focus()
    for i in typelist:
        listbox.insert(END, i)

    def keydown(event):
        listbox.delete(0, END)
        a = e.get()
        a = a.upper()
        cheklist = []
        for i in typelist:
            if a in i:
                cheklist.append(i)
        for i in cheklist:
            listbox.insert(END, i)

    def sear(event):
        listbox.focus()

        def searw1(eve):
            indexselected = listbox.curselection()
            iteml = []
            for i in indexselected:
                iteml.append(listbox.get(i))
            d = []
            connection = sqlite3.connect("mytables4.db")
            crsr = connection.cursor()
            for ij in iteml:
                e112 = ij
                crsr.execute(f"SELECT * FROM stockfinal634 WHERE Type ='{e112}';")
                w = crsr.fetchall()
                if (len(w) == 0):
                    continue

                else:
                    d1 = []
                    for i in w:
                        d1.append(list(i))
                    d.append(d1)
            connection.close()

            # here we get list under alist which is under a list
            def chet1(d):
                global f3
                f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
                f3.grid(row=0, column=2, sticky="nsew")

                treev = ttk.Treeview(f3, selectmode='browse', height=20)
                treev.pack(fill=BOTH)
                scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
                scrollbar.pack(side=BOTTOM, fill=X)
                treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
                treev.configure(xscrollcommand=scrollbar.set)
                # Defining heading
                treev['show'] = 'headings'

                # Assigning the width and anchor to  the
                # respective columns
                treev.column("1", width=250, anchor='c')
                treev.column("2", width=300, anchor='c')
                treev.column("3", width=150, anchor='c')
                treev.column("4", width=80, anchor='c')
                treev.column("5", width=100, anchor='c')
                treev.column("6", width=100, anchor='c')
                treev.column("7", width=60, anchor='c')
                treev.column("8", width=60, anchor='c')
                treev.column("9", width=60, anchor='c')
                treev.column("10", width=60, anchor='c')
                treev.column("11", width=80, anchor='c')
                treev.column("12", width=100, anchor='c')
                treev.column("13", width=100, anchor='c')

                # Assigning the heading names to the
                # respective columns
                treev.heading("1", text="TYPE")
                treev.heading("2", text="DENSIZE")
                treev.heading("3", text="THK REMARK")
                treev.heading("4", text="BUNDLENO")
                treev.heading("5", text="COVER")
                treev.heading("6", text="STM")
                treev.heading("7", text="R2")
                treev.heading("8", text="PCS")
                treev.heading("9", text="MM")
                treev.heading("10", text="KGS")
                treev.heading("11", text="PACKINGLIST")
                treev.heading("12", text="DATE")
                treev.heading("13", text="STATUS")
                # Inserting the items and their features to the
                # columns built

                for rows1 in d:
                    for row in rows1:
                        s = tuple(row)
                        treev.insert("", 'end', values=s, tags=(s[12],))
                treev.tag_configure('SOLD', background='light green')
                treev.tag_configure('SPLIT', background='light blue')

            def chet(d):
                f3.destroy()
                chet1(d)

            chet(d)

            pass

        listbox.bind("<Return>", searw1)
        listbox.bind("<KP_Enter>", searw1)
        listbox.bind("<Double-Button-1>", searw1)

        nonlocal e

        def searw2(eve):
            nonlocal e
            e.focus()

        listbox.bind("<Right>", searw2)
        listbox.bind("<Left>", searw2)

    listbox.bind("<Button-1>", sear)

    e.bind("<KeyRelease>", keydown)
    e.bind("<Return>", sear)
    e.bind("<KP_Enter>", sear)
    e.bind("<Up>", sear)
    e.bind("<Down>", sear)

    pass


def searchbundlename(event):
    f3.destroy()
    f4.destroy()
    searchbundlename1(event)


def deletepacking1(event):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    def check():

        def delete():
            qw = tsmg.askquestion("Warning", f"Are you sure you want to delete packing list {e.get()}")
            if (qw == 'yes'):
                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                try:
                    crsr.execute(f"DELETE FROM stockfinal634 WHERE PACKINGLIST ='{e.get()}';")
                    connection.commit()
                    connection.close()
                    tsmg.showinfo("DELETED", f"Yor packing list - {e.get()} has been deleted");


                except Exception as eat:
                    print(eat)

        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM stockfinal634 WHERE PACKINGLIST ='{e.get()}';")
        w = crsr.fetchall()
        if (len(w) == 0):
            Button(f4, text="NOT FOUND").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')
            pass

        else:
            d = []
            for i in w:
                d.append(list(i))
            connection.close()

            def resd1(d):
                global f3
                f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
                f3.grid(row=0, column=2, sticky="nsew")

                treev = ttk.Treeview(f3, selectmode='browse', height=20)
                treev.pack(fill=BOTH)
                scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
                scrollbar.pack(side=BOTTOM, fill=X)
                treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
                treev.configure(xscrollcommand=scrollbar.set)
                # Defining heading
                treev['show'] = 'headings'

                # Assigning the width and anchor to  the
                # respective columns
                treev.column("1", width=250, anchor='c')
                treev.column("2", width=300, anchor='c')
                treev.column("3", width=150, anchor='c')
                treev.column("4", width=80, anchor='c')
                treev.column("5", width=100, anchor='c')
                treev.column("6", width=100, anchor='c')
                treev.column("7", width=60, anchor='c')
                treev.column("8", width=60, anchor='c')
                treev.column("9", width=60, anchor='c')
                treev.column("10", width=60, anchor='c')
                treev.column("11", width=80, anchor='c')
                treev.column("12", width=100, anchor='c')
                treev.column("13", width=100, anchor='c')

                # Assigning the heading names to the
                # respective columns
                treev.heading("1", text="TYPE")
                treev.heading("2", text="DENSIZE")
                treev.heading("3", text="THK REMARK")
                treev.heading("4", text="BUNDLENO")
                treev.heading("5", text="COVER")
                treev.heading("6", text="STM")
                treev.heading("7", text="R2")
                treev.heading("8", text="PCS")
                treev.heading("9", text="MM")
                treev.heading("10", text="KGS")
                treev.heading("11", text="PACKINGLIST")
                treev.heading("12", text="DATE")
                treev.heading("13", text="STATUS")
                # Inserting the items and their features to the
                # columns built
                for row in d:
                    s = tuple(row)
                    treev.insert("", 'end', values=s, tags=(s[12],))
                treev.tag_configure('SOLD', background='light green')
                treev.tag_configure('SPLIT', background='light blue')

            def resd(d):
                f3.destroy()
                resd1(d)

            resd(d)

            Button(f4, text="   DELETE    ", command=delete).grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')

    l = Label(f4, text=" PLNO  ", width=8)
    l.grid(row=0, column=0, padx=5, pady=5)
    e = Entry(f4)
    e.grid(row=0, column=1)
    e.focus()
    Button(f4, text="SEARCH", command=check).grid(row=2, column=0, columnspan=2, padx=25)
    pass


def deletepacking(event):
    f3.destroy()
    f4.destroy()
    deletepacking1(event)


def deletebundle1(event):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    def check():
        # we will retrive our data from here
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM stockfinal634 WHERE BUNDLE ='{e.get()}';")
        w = crsr.fetchall()
        if (len(w) == 0):
            Button(f4, text="NOT FOUND").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')
            pass

        else:
            d = list(w[0])
            connection.close()

            # now we will set the values

            l1 = Label(f3, text="Bundle type", width=8)
            l1.grid(row=0, column=0, padx=5, pady=5)
            e1 = Entry(f3)
            e1.grid(row=0, column=1)
            l2 = Label(f3, text="DEN SIZE", padx=5, width=8)
            l2.grid(row=1, column=0, padx=5, pady=5)
            e2 = Entry(f3)
            e2.grid(row=1, column=1)
            l3 = Label(f3, text="THK REMARK", padx=5, width=8)
            l3.grid(row=2, column=0, padx=5, pady=5)
            e3 = Entry(f3)
            e3.grid(row=2, column=1)
            l4 = Label(f3, text="BUNDLE", padx=5, width=8)
            l4.grid(row=3, column=0, padx=5, pady=5)
            e4 = Entry(f3)
            e4.grid(row=3, column=1)
            l5 = Label(f3, text="COVER", padx=5, width=8)
            l5.grid(row=4, column=0, padx=5, pady=5)
            e5 = Entry(f3)
            e5.grid(row=4, column=1)
            l6 = Label(f3, text="STM", padx=5, width=8)
            l6.grid(row=0, column=5, padx=5, pady=5)
            e6 = Entry(f3)
            e6.grid(row=0, column=6)
            l7 = Label(f3, text="R2", padx=5, width=8)
            l7.grid(row=0, column=3, padx=20, pady=5)
            e7 = Entry(f3)
            e7.grid(row=0, column=4)
            l8 = Label(f3, text="PCS", padx=5, width=8)
            l8.grid(row=1, column=3, padx=5, pady=5)
            e8 = Entry(f3)
            e8.grid(row=1, column=4)
            l9 = Label(f3, text="MM", padx=5, width=8)
            l9.grid(row=2, column=3, padx=5, pady=5)
            e9 = Entry(f3)
            e9.grid(row=2, column=4)
            l10 = Label(f3, text="KGS", padx=5, width=8)
            l10.grid(row=3, column=3, padx=5, pady=5)
            e10 = Entry(f3)
            e10.grid(row=3, column=4)
            l11 = Label(f3, text="PACKINGNO", padx=5, width=8)
            l11.grid(row=4, column=3, padx=5, pady=5)
            e11 = Entry(f3)
            e11.grid(row=4, column=4)
            l12 = Label(f3, text="DATE", padx=5, width=8)
            l12.grid(row=3, column=5, padx=5, pady=5)
            e12 = Entry(f3)
            e12.grid(row=3, column=6)
            l13 = Label(f3, text="STATUS", padx=5, width=8)
            l13.grid(row=1, column=5, padx=20, pady=5)
            e13 = Entry(f3)
            e13.grid(row=1, column=6, padx=5, pady=5)

            e1.insert(0, d[0])
            e2.insert(0, d[1])
            e3.insert(0, d[2])
            e4.insert(0, d[3])
            e5.insert(0, d[4])
            e6.insert(0, d[5])
            e7.insert(0, d[6])
            e8.insert(0, d[7])
            e9.insert(0, d[8])
            e10.insert(0, d[9])
            e11.insert(0, d[10])
            e12.insert(0, d[11])
            e13.insert(0, d[12])

            def delete():
                qw = tsmg.askquestion("Warning", f"Are you sure you want to delete packing list {e.get()}")
                if (qw == 'yes'):
                    connection = sqlite3.connect("mytables4.db")
                    crsr = connection.cursor()
                    crsr.execute(f"DELETE FROM stockfinal634 WHERE BUNDLE ='{e.get()}';")
                    connection.commit()
                    connection.close()
                    # recursivly calling the function againg so that it replace the screen
                    deletebundle(event)

            Button(f4, text="    DELETE    ", command=delete).grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')

        pass

    l = Label(f4, text="BUNDLE NO", width=8)
    l.grid(row=0, column=0, padx=5, pady=5)
    e = Entry(f4)
    e.grid(row=0, column=1)
    e.focus()
    Button(f4, text="SEARCH", command=check).grid(row=2, column=0, columnspan=2, padx=25)

    pass


def deletebundle(event):
    f3.destroy()
    f4.destroy()
    deletebundle1(event)


def updatebundleno(event):
    searchbundleno(event)
    pass


def createcustomertable(tablename):
    connection = sqlite3.connect("mytables4.db")
    cursor = connection.cursor()
    sqlcommand = f"""CREATE TABLE {tablename}(
            NAME varchar(50) PRIMARY KEY,
            ADD_LINE_1 varchar(50),
            ADD_LINE_2 varchar(50),
            CITY varchar(50),
            PINCODE varchar(50),
            MOBILE varchar(50),
            LIMIT_ varchar(50),
            TOTAL varchar(50));"""
    cursor.execute(sqlcommand)
    connection.commit()
    connection.close()
    pass


def addcustomer1(event):
    # sat="custom9"
    # createcustomertable(sat)
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")

    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM custom9")
    d = crsr.fetchall()
    connection.close()

    def check(*args):
        newdata = []
        newdata.append(e1.get().upper())
        newdata.append(e2.get().upper())
        newdata.append(e3.get().upper())
        newdata.append(e4.get().upper())
        newdata.append(e5.get().upper())
        newdata.append(e6.get().upper())
        try:
            aerw1 = float(e7.get())
            newdata.append(aerw1)
        except Exception as e:
            newdata.append('0')
        try:
            aerw = float(e8.get())
            newdata.append(aerw)
        except Exception as e:
            newdata.append('0')

        d1 = tuple(newdata)
        connection = sqlite3.connect("mytables4.db")
        cursor = connection.cursor()
        row = d1

        sa = f'''INSERT INTO custom9 VALUES ('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}')'''
        try:
            cursor.execute(sa)
            connection.commit()
            tsmg.showinfo("Saved", "your entry has been saved")

            # errorcanoccur
            addcustomer(event)

        except Exception as e:
            print(e)
            tsmg.showinfo("Failed", "Customer already exist")
            # errorcanoccur

            addcustomer(event)

        connection.close()
        # now i need to store data in sql
        pass

    l1 = Label(f4, text="NAME", width=8)
    l1.grid(row=0, column=0, padx=5, pady=5)
    e1 = Entry(f4)
    e1.grid(row=0, column=1)
    l2 = Label(f4, text="ADD_LINE_1", padx=5, width=8)
    l2.grid(row=1, column=0, padx=5, pady=5)
    e2 = Entry(f4)
    e2.grid(row=1, column=1)
    l3 = Label(f4, text="ADD_LINE_2", padx=5, width=8)
    l3.grid(row=2, column=0, padx=5, pady=5)
    e3 = Entry(f4)
    e3.grid(row=2, column=1)
    l4 = Label(f4, text="CITY", padx=5, width=8)
    l4.grid(row=0, column=2, padx=5, pady=5)
    e4 = Entry(f4)
    e4.grid(row=0, column=3)
    l5 = Label(f4, text="PINCODE", padx=5, width=8)
    l5.grid(row=1, column=2, padx=5, pady=5)
    e5 = Entry(f4)
    e5.grid(row=1, column=3)
    l6 = Label(f4, text="MOBILE NO", padx=5, width=8)
    l6.grid(row=2, column=2, padx=5, pady=5)
    e6 = Entry(f4)
    e6.grid(row=2, column=3)
    l7 = Label(f4, text="LIMIT_", padx=5, width=8)
    l7.grid(row=0, column=4, padx=20, pady=5)
    e7 = Entry(f4)
    e7.grid(row=0, column=5)
    l8 = Label(f4, text="TOTAL", padx=5, width=8)
    l8.grid(row=1, column=4, padx=5, pady=5)
    e8 = Entry(f4)
    e8.grid(row=1, column=5)
    e8.insert(0, '0')
    e1.focus()
    e1.bind("<KP_Enter>", lambda x: e2.focus())
    e1.bind("<Return>", lambda x: e2.focus())
    e2.bind("<KP_Enter>", lambda x: e3.focus())
    e2.bind("<KP_Enter>", lambda x: e3.focus())
    e3.bind("<KP_Enter>", lambda x: e4.focus())
    e3.bind("<Return>", lambda x: e4.focus())
    e4.bind("<KP_Enter>", lambda x: e5.focus())
    e4.bind("<Return>", lambda x: e5.focus())
    e5.bind("<KP_Enter>", lambda x: e7.focus())
    e5.bind("<Return>", lambda x: e7.focus())
    e7.bind("<KP_Enter>", lambda x: e8.focus())
    e7.bind("<Return>", lambda x: e8.focus())
    e8.bind("<KP_Enter>", check)
    e8.bind("<Return>", check)

    Button(f4, text="SAVE CUSTOMER", command=check).grid(row=2, column=4, columnspan=2, padx=25)

    treev = ttk.Treeview(f3, selectmode='browse', height=19)
    treev.pack(fill=BOTH)
    # treev.bind("<Double-Button-1>", clickedrow)
    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev.configure(xscrollcommand=scrollbar.set)
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=250, anchor='c')
    treev.column("2", width=300, anchor='c')
    treev.column("3", width=150, anchor='c')
    treev.column("4", width=100, anchor='c')
    treev.column("5", width=110, anchor='c')
    treev.column("6", width=100, anchor='c')
    treev.column("7", width=100, anchor='c')
    treev.column("8", width=100, anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="NAME")
    treev.heading("2", text="ADD_LINE_1")
    treev.heading("3", text="ADD_LINE_2")
    treev.heading("4", text="CITY")
    treev.heading("5", text="PINCODE")
    treev.heading("6", text="MOBILE")
    treev.heading("7", text="LIMIT_")
    treev.heading("8", text="TOTAL")

    # Inserting the items and their features to the
    # columns built
    for row in d:
        s = tuple(row)
        treev.insert("", 'end', values=s)

    pass


def addcustomer(event):
    f3.destroy()
    f4.destroy()
    addcustomer1(event)


def updatecustomer1(event):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM custom9")
    d = crsr.fetchall()

    connection.close()

    def clickedrow(event):
        item = treev.identify_row(event.y)
        if item:
            a = treev.item(item, 'values')
            a = list(a)

            def sgf1(a):
                global f4
                f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
                f4.grid(row=1, column=2, sticky="nsew")
                l1 = Label(f4, text="NAME", width=8)
                l1.grid(row=0, column=0, padx=5, pady=5)
                e1 = Entry(f4)
                e1.grid(row=0, column=1)
                l2 = Label(f4, text="ADD_LINE_1", padx=5, width=8)
                l2.grid(row=1, column=0, padx=5, pady=5)
                e2 = Entry(f4)
                e2.grid(row=1, column=1)
                l3 = Label(f4, text="ADD_LINE_2", padx=5, width=8)
                l3.grid(row=2, column=0, padx=5, pady=5)
                e3 = Entry(f4)
                e3.grid(row=2, column=1)
                l4 = Label(f4, text="CITY", padx=5, width=8)
                l4.grid(row=0, column=2, padx=5, pady=5)
                e4 = Entry(f4)
                e4.grid(row=0, column=3)
                l5 = Label(f4, text="PINCODE", padx=5, width=8)
                l5.grid(row=1, column=2, padx=5, pady=5)
                e5 = Entry(f4)
                e5.grid(row=1, column=3)
                l6 = Label(f4, text="MOBILE NO", padx=5, width=8)
                l6.grid(row=2, column=2, padx=5, pady=5)
                e6 = Entry(f4)
                e6.grid(row=2, column=3)
                l7 = Label(f4, text="LIMIT_", padx=5, width=8)
                l7.grid(row=0, column=4, padx=20, pady=5)
                e7 = Entry(f4)
                e7.grid(row=0, column=5)
                l8 = Label(f4, text="TOTAL", padx=5, width=8)
                l8.grid(row=1, column=4, padx=5, pady=5)
                e8 = Entry(f4)
                e8.grid(row=1, column=5)
                e1.insert(0, a[0])
                e2.insert(0, a[1])
                e3.insert(0, a[2])
                e4.insert(0, a[3])
                e5.insert(0, a[4])
                e6.insert(0, a[5])
                e7.insert(0, a[6])
                e8.insert(0, a[7])

                def update():
                    newdata = []
                    newdata.append(e1.get().upper())
                    newdata.append(e2.get().upper())
                    newdata.append(e3.get().upper())
                    newdata.append(e4.get().upper())
                    newdata.append(e5.get().upper())
                    newdata.append(e6.get().upper())
                    try:
                        aerw1 = float(e7.get())
                        newdata.append(aerw1)
                    except Exception as e:
                        newdata.append('0')
                    try:
                        aerw = float(e8.get())
                        newdata.append(aerw)
                    except Exception as e:
                        newdata.append('0')

                    d1 = tuple(newdata)

                    connection = sqlite3.connect("mytables4.db")
                    cursor = connection.cursor()
                    cursor.execute(f"DELETE FROM custom9 WHERE NAME ='{a[0]}';")
                    connection.commit()
                    row = d1
                    sa = f'''INSERT INTO custom9 VALUES ('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}')'''
                    try:
                        cursor.execute(sa)
                        connection.commit()
                        tsmg.showinfo("Saved", "your entry has been updated")
                        updatecustomer(event)
                        # errorcanoccur

                    except Exception as e:
                        row = a

                        sa = f'''INSERT INTO custom9 VALUES ('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}')'''
                        cursor.execute(sa)
                        connection.commit()

                        tsmg.showinfo("Failed", "Customer already exist")
                        updatecustomer(event)

                    d1 = tuple(newdata)

                Button(f4, text="UPDATE CUSTOMER", command=update).grid(row=2, column=4, columnspan=2, padx=25)

            def sgf(a):
                f4.destroy()
                sgf1(a)

            sgf(a)

        pass

    treev = ttk.Treeview(f3, selectmode='browse', height=19)
    treev.pack()
    treev.bind("<Double-Button-1>", clickedrow)
    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev.configure(xscrollcommand=scrollbar.set)
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=250, anchor='c')
    treev.column("2", width=300, anchor='c')
    treev.column("3", width=150, anchor='c')
    treev.column("4", width=100, anchor='c')
    treev.column("5", width=110, anchor='c')
    treev.column("6", width=100, anchor='c')
    treev.column("7", width=100, anchor='c')
    treev.column("8", width=100, anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="NAME")
    treev.heading("2", text="ADD_LINE_1")
    treev.heading("3", text="ADD_LINE_2")
    treev.heading("4", text="CITY")
    treev.heading("5", text="PINCODE")
    treev.heading("6", text="MOBILE")
    treev.heading("7", text="LIMIT_")
    treev.heading("8", text="TOTAL")

    # Inserting the items and their features to the
    # columns built
    for row in d:
        s = tuple(row)
        treev.insert("", 'end', values=s)

    l1 = Label(f4, text="SEARCH BY NAME", width=18)
    l1.grid(row=0, column=0, padx=65, pady=15)
    e123 = Entry(f4)
    e123.grid(row=0, column=1)

    def searchbyname1(qw):
        global f4
        nameaup = qw.upper()
        f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
        f4.grid(row=1, column=2, sticky="nsew")
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM custom9 WHERE NAME ='{nameaup}';")
        w = crsr.fetchall()
        if (len(w) == 0):
            Button(f4, text="NOT FOUND").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')
            pass

        else:
            a = list(w[0])
            connection.close()
            l1 = Label(f4, text="NAME", width=8)
            l1.grid(row=0, column=0, padx=5, pady=5)
            e1 = Entry(f4)
            e1.grid(row=0, column=1)
            l2 = Label(f4, text="ADD_LINE_1", padx=5, width=8)
            l2.grid(row=1, column=0, padx=5, pady=5)
            e2 = Entry(f4)
            e2.grid(row=1, column=1)
            l3 = Label(f4, text="ADD_LINE_2", padx=5, width=8)
            l3.grid(row=2, column=0, padx=5, pady=5)
            e3 = Entry(f4)
            e3.grid(row=2, column=1)
            l4 = Label(f4, text="CITY", padx=5, width=8)
            l4.grid(row=0, column=2, padx=5, pady=5)
            e4 = Entry(f4)
            e4.grid(row=0, column=3)
            l5 = Label(f4, text="PINCODE", padx=5, width=8)
            l5.grid(row=1, column=2, padx=5, pady=5)
            e5 = Entry(f4)
            e5.grid(row=1, column=3)
            l6 = Label(f4, text="MOBILE NO", padx=5, width=8)
            l6.grid(row=2, column=2, padx=5, pady=5)
            e6 = Entry(f4)
            e6.grid(row=2, column=3)
            l7 = Label(f4, text="LIMIT_", padx=5, width=8)
            l7.grid(row=0, column=4, padx=20, pady=5)
            e7 = Entry(f4)
            e7.grid(row=0, column=5)
            l8 = Label(f4, text="TOTAL", padx=5, width=8)
            l8.grid(row=1, column=4, padx=5, pady=5)
            e8 = Entry(f4)
            e8.grid(row=1, column=5)
            e1.insert(0, a[0])
            e2.insert(0, a[1])
            e3.insert(0, a[2])
            e4.insert(0, a[3])
            e5.insert(0, a[4])
            e6.insert(0, a[5])
            e7.insert(0, a[6])
            e8.insert(0, a[7])

            def update():
                newdata = []
                newdata.append(e1.get().upper())
                newdata.append(e2.get().upper())
                newdata.append(e3.get().upper())
                newdata.append(e4.get().upper())
                newdata.append(e5.get().upper())
                newdata.append(e6.get().upper())
                try:
                    aerw1 = float(e7.get())
                    newdata.append(aerw1)
                except Exception as e:
                    newdata.append('0')
                try:
                    aerw = float(e8.get())
                    newdata.append(aerw)
                except Exception as e:
                    newdata.append('0')
                d1 = tuple(newdata)

                connection = sqlite3.connect("mytables4.db")
                cursor = connection.cursor()
                cursor.execute(f"DELETE FROM custom9 WHERE NAME ='{a[0]}';")
                connection.commit()
                row = d1
                up = row[0]
                up = up.upper()
                sa = f'''INSERT INTO custom9 VALUES ("{up}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}")'''
                try:
                    cursor.execute(sa)
                    connection.commit()
                    tsmg.showinfo("Saved", "your entry has been updated")
                    updatecustomer(event)
                    # errorcanoccur

                except Exception as e:
                    row = a
                    sa = f'''INSERT INTO custom9 VALUES ("{row[0]}","{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}","{row[6]}","{row[7]}")'''
                    cursor.execute(sa)
                    connection.commit()

                    tsmg.showinfo("Failed", "Customer already exist")
                    updatecustomer(event)

                d1 = tuple(newdata)

            Button(f4, text="UPDATE CUSTOMER", command=update).grid(row=2, column=4, columnspan=2, padx=25)

        pass

    def searchbyname():
        namea = e123.get()
        f4.destroy()
        searchbyname1(namea)

    Button(f4, text="SEARCH", command=searchbyname).grid(row=0, column=3, columnspan=2, padx=25)
    l2 = Label(f4, text="SEARCH BY CITY", width=18)
    l2.grid(row=1, column=0, padx=5, pady=5)
    e234 = Entry(f4)
    e234.grid(row=1, column=1)

    def searchbycity1(namesa):
        global f3
        global f4
        f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
        f3.grid(row=0, column=2, sticky="nsew")
        f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
        f4.grid(row=1, column=2, sticky="nsew")
        treev = ttk.Treeview(f3, selectmode='browse', height=19)
        treev.pack()
        treev.bind("<Double-Button-1>", clickedrow)
        scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
        scrollbar.pack(side=BOTTOM, fill=X)
        treev.configure(xscrollcommand=scrollbar.set)
        treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
        treev['show'] = 'headings'

        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width=250, anchor='c')
        treev.column("2", width=300, anchor='c')
        treev.column("3", width=150, anchor='c')
        treev.column("4", width=100, anchor='c')
        treev.column("5", width=110, anchor='c')
        treev.column("6", width=100, anchor='c')
        treev.column("7", width=100, anchor='c')
        treev.column("8", width=100, anchor='c')

        # Assigning the heading names to the
        # respective columns
        treev.heading("1", text="NAME")
        treev.heading("2", text="ADD_LINE_1")
        treev.heading("3", text="ADD_LINE_2")
        treev.heading("4", text="CITY")
        treev.heading("5", text="PINCODE")
        treev.heading("6", text="MOBILE")
        treev.heading("7", text="LIMIT_")
        treev.heading("8", text="TOTAL")

        # Inserting the items and their features to the
        # columns built
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM custom9 WHERE CITY = '{namesa}'")
        d = crsr.fetchall()

        for row in d:
            s = tuple(row)
            treev.insert("", 'end', values=s)

        pass

    def searchbycity():
        namesa = e234.get()
        f3.destroy()
        f4.destroy()
        searchbycity1(namesa)

    Button(f4, text="SEARCH", command=searchbycity).grid(row=1, column=3, columnspan=2, padx=25)

    pass


def updatecustomer(event):
    f3.destroy()
    f4.destroy()
    updatecustomer1(event)


def showcustomer1(event):
    # we will show customer now
    global f3
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, rowspan=2, sticky="nsew")
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM custom9")
    d = crsr.fetchall()
    connection.close()
    treev = ttk.Treeview(f3, selectmode='browse', height=34)
    treev.pack(fill=BOTH)
    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev.configure(xscrollcommand=scrollbar.set)
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=150, anchor='c')
    treev.column("2", width=60, anchor='c')
    treev.column("3", width=60, anchor='c')
    treev.column("4", width=80, anchor='c')
    treev.column("5", width=80, anchor='c')
    treev.column("6", width=80, anchor='c')
    treev.column("7", width=80, anchor='c')
    treev.column("8", width=80, anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="NAME")
    treev.heading("2", text="ADD_LINE_1")
    treev.heading("3", text="ADD_LINE_2")
    treev.heading("4", text="CITY")
    treev.heading("5", text="PINCODE")
    treev.heading("6", text="MOBILE")
    treev.heading("7", text="LIMIT_")
    treev.heading("8", text="TOTAL")

    # Inserting the items and their features to the
    # columns built
    for row in d:
        s = tuple(row)
        if (float(s[7]) > float(s[6])):
            treev.insert("", 'end', values=s, tags=("outoflimit",))
        else:
            treev.insert("", 'end', values=s)
    treev.tag_configure('outoflimit', background='red', foreground="white")

    pass

    def clickedrow(event):
        item = treev.identify_row(event.y)
        if item:
            a = treev.item(item, 'values')
            a = list(a)

            def qwsax1(a):
                global f3
                f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
                f3.grid(row=0, column=2, rowspan=2, sticky="nsew")

                treev1 = ttk.Treeview(f3, selectmode='browse', height=34)
                treev1.pack(fill=BOTH)
                scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev1.xview)
                scrollbar.pack(side=BOTTOM, fill=X)
                treev1.configure(xscrollcommand=scrollbar.set)
                treev1.configure(xscrollcommand=scrollbar.set)
                treev1["columns"] = ("1", "2", "3", "4", "5")

                # Defining heading
                treev1['show'] = 'headings'

                # Assigning the width and anchor to  the
                # respective columns
                treev1.column("1", anchor='c')
                treev1.column("2", anchor='c')
                treev1.column("3", anchor='c')
                treev1.column("4", anchor='c')
                treev1.column("5", anchor='c')

                # Assigning the heading names to the
                # respective columns
                treev1.heading("1", text="BILLNO")
                treev1.heading("2", text="BUYER")
                treev1.heading("3", text="DATE")
                treev1.heading("4", text="CREDIT")
                treev1.heading("5", text="DEBIT")

                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(
                    f"SELECT * FROM billstock5 WHERE BUYER = '{a[0]}' AND DATE >= '{from_date}' AND DATE <= '{to_date}' ")
                d = crsr.fetchall()
                connection.close()

                dict = {}
                for row in d:
                    if row[0] not in dict:
                        dict[row[0]] = [row[1], row[7], "", row[9]]
                    else:
                        tot = dict[row[0]][3]
                        dict[row[0]][3] = float(tot) + float(row[9])
                tes = dict.items()
                tes = list(tes)
                tot_deb = 0
                newres = []
                for i in tes:
                    k = []
                    j = list(i)
                    k.append(j[0])
                    for h in j[1]:
                        k.append(h)
                    if 'C' in j[0]:
                        pass
                    else:
                        tot_deb = tot_deb + float(j[1][3])

                    newres.append(k)

                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(
                    f"SELECT * FROM credittable WHERE NAME = '{a[0]}' AND DATE >= '{from_date}' AND DATE <= '{to_date}'")
                dome = crsr.fetchall()
                connection.close()
                tot_cre = 0
                for erw in dome:
                    s = []
                    if (erw[2] == 'CANCEL BILLED'):
                        s.append(f"CANCEL BILL {erw[1]}")
                    else:
                        s.append('CREDIT')
                    s.append(erw[0])
                    s.append(erw[4])
                    s.append(erw[3])
                    s.append("")
                    newres.append(s)
                    tot_cre = tot_cre + float(erw[3])
                reswer = []
                for s in newres:
                    qwq = s[2].split('-')
                    re = ''.join(qwq)
                    s.append(int(re))
                reswer = sorted(newres, key=lambda x: x[5])
                reswer.reverse()
                for s in reswer:
                    s.pop()
                    asz = s[0]
                    if s[0] == 'CREDIT':
                        treev1.insert("", 'end', values=s, tags=(s[0],))
                    elif asz[0] == "C" and asz != 'CREDIT':
                        treev1.insert("", 'end', values=s, tags=('Car',))
                    else:
                        treev1.insert("", 'end', values=s, tags=('sale',))
                s12 = ["", "", "", "", ""]
                treev1.insert("", 'end', values=s12)
                s23 = ["", "", "TOTAL", tot_cre, tot_deb]
                treev1.insert("", 'end', values=s23)

                treev1.tag_configure('CREDIT', background='light green')
                treev1.tag_configure('Car', background='light blue')

                def opencustbill(event):

                    item = treev1.identify_row(event.y)
                    if item:
                        a = treev1.item(item, 'values')
                        a = list(a)
                        if a[2] != "TOTAL":
                            if a[2] != '':
                                def qwaaz1(a):
                                    global f3
                                    global f4
                                    if a[0] != "CREDIT":

                                        f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
                                        f3.grid(row=0, column=2, sticky="nsew")

                                        f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
                                        f4.grid(row=1, column=2, sticky="nsew")
                                        treev2 = ttk.Treeview(f3, selectmode='browse', height=20)
                                        treev2.pack(fill=BOTH)
                                        scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev2.xview)
                                        scrollbar.pack(side=BOTTOM, fill=X)
                                        treev2["columns"] = ("1", "2", "3", "4", "5", "6", "7")
                                        treev2.configure(xscrollcommand=scrollbar.set)
                                        treev2['show'] = 'headings'

                                        treev2.column("1", anchor='c')
                                        treev2.column("2", width=200, anchor='c')
                                        treev2.column("3", width=80, anchor='c')
                                        treev2.column("4", width=80, anchor='c')
                                        treev2.column("5", width=80, anchor='c')
                                        treev2.column("6", width=80, anchor='c')
                                        treev2.column("7", width=80, anchor='c')
                                        na = a[1]
                                        na = na.upper()
                                        connection = sqlite3.connect("mytables4.db")
                                        crsr = connection.cursor()
                                        crsr.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
                                        sel = crsr.fetchall()
                                        connection.close()
                                        sel = list(sel[0])
                                        r1 = ("NAME", sel[0], "", "BILLNO", a[0], "", "")
                                        r2 = ("ADD1", sel[1], "", "MOBILENO", sel[5], "", "")
                                        r3 = ("ADD2", sel[2], "", "DATE", a[2], "", "")
                                        treev2.insert("", 'end', values=r1)
                                        treev2.insert("", 'end', values=r2)
                                        treev2.insert("", 'end', values=r3)
                                        r31 = ("", "", "", "", "", "", "")
                                        treev2.insert("", 'end', values=r31)

                                        connection = sqlite3.connect("mytables4.db")
                                        crsr = connection.cursor()
                                        crsr.execute(f"SELECT * FROM billstock5 WHERE BILLNo ='{a[0]}'")
                                        d = crsr.fetchall()
                                        connection.close()
                                        total = []
                                        for i in d:
                                            listforinsert = []
                                            listforinsert.append(i[2])
                                            listforinsert.append(i[3])
                                            listforinsert.append(i[4])
                                            listforinsert.append(i[5])
                                            listforinsert.append(i[6])
                                            listforinsert.append(i[8])
                                            listforinsert.append(i[9])
                                            total.append(int(i[9]))
                                            treev2.insert("", 'end', values=listforinsert)
                                        r312 = ("", "", "", "", "", "", "")
                                        treev2.insert("", 'end', values=r312)
                                        r32 = ("", "", "", "", "", "", "")
                                        treev2.insert("", 'end', values=r32)
                                        r33 = ("", "", "", "", "TOTAL", "", sum(total))
                                        treev2.insert("", 'end', values=r33, tags=('tot',))
                                        treev2.tag_configure('tot', background='light blue')
                                    else:
                                        f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
                                        f3.grid(row=0, column=2, sticky="nsew")
                                        f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
                                        f4.grid(row=1, column=2, sticky="nsew")
                                        connection = sqlite3.connect("mytables4.db")
                                        crsr = connection.cursor()
                                        crsr.execute(
                                            f"SELECT * FROM credittable WHERE NAME = '{a[1]}' AND AMOUNT = '{a[3]}' AND DATE ='{a[2]}'")
                                        damw = crsr.fetchall()
                                        connection.close()
                                        dawn = list(damw[0])
                                        l1 = Label(f4, text=f"NAME", width=8)
                                        l1.grid(row=0, column=0, padx=5, pady=5)
                                        e1 = Entry(f4)
                                        e1.grid(row=0, column=1)
                                        l2 = Label(f4, text="TYPE", padx=5, width=8)
                                        l2.grid(row=1, column=0, padx=5, pady=5)
                                        e2 = Entry(f4)
                                        e2.grid(row=1, column=1)
                                        l3 = Label(f4, text="TRANSAC. NO", padx=5, width=8)
                                        l3.grid(row=2, column=0, padx=5, pady=5)
                                        e3 = Entry(f4)
                                        e3.grid(row=2, column=1)
                                        l4 = Label(f4, text="AMOUNT", padx=5, width=8)
                                        l4.grid(row=0, column=2, padx=5, pady=5)
                                        e4 = Entry(f4)
                                        e4.grid(row=0, column=3)
                                        l5 = Label(f4, text="DATE", padx=5, width=8)
                                        l5.grid(row=1, column=2, padx=5, pady=5)
                                        e5 = Entry(f4)
                                        e5.grid(row=1, column=3)
                                        e1.insert(0, dawn[0])
                                        e2.insert(0, dawn[1])
                                        e3.insert(0, dawn[2])
                                        e4.insert(0, dawn[3])
                                        e5.insert(0, dawn[4])

                                        pass

                                def qwaaz():
                                    f3.destroy()
                                    f4.destroy()
                                    qwaaz1(a)

                                qwaaz()

                    pass

                treev1.bind("<Double-Button-1>", opencustbill)

            def qwsax():
                f3.destroy()
                qwsax1(a)

            qwsax()


        else:
            print("Nothing it have")

        pass

    treev.bind("<Double-Button-1>", clickedrow)


def showcustomer(event):
    f3.destroy()
    f4.destroy()
    showcustomer1(event)


def createbilltable(tablename):
    connection = sqlite3.connect("mytables4.db")
    cursor = connection.cursor()
    sqlcommand = f"""CREATE TABLE {tablename}(
            BILLNO varchar(50),
            BUYER varchar(50),
            BUNDLENO varchar(50),
            PRODUCT varchar(50),
            SIZE varchar(50),
            PCS varchar(50),
            KG varchar(50),
            DATE DATE,
            RATE varchar(50),
            TOTAL varchar(50));"""
    cursor.execute(sqlcommand)
    connection.commit()
    connection.close()


def createbillnotable(tablename):
    connection = sqlite3.connect("mytables4.db")
    cursor = connection.cursor()
    sqlcommand = f"""CREATE TABLE {tablename}(
            NAME varchar(50),
            BILLNO varchar(50));"""
    cursor.execute(sqlcommand)
    connection.commit()
    connection.close()


def createcredittable(tablename):
    connection = sqlite3.connect("mytables4.db")
    cursor = connection.cursor()
    sqlcommand = f"""CREATE TABLE {tablename}(
            NAME varchar(50),
            TYPE varchar(50),
            TRANSACTION_NO varchar(50),
            AMOUNT varchar(50),
            DATE DATE);"""
    cursor.execute(sqlcommand)
    connection.commit()
    connection.close()


def addpayment1(event):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM custom9")
    d = crsr.fetchall()
    connection.close()

    namelist = []
    for i in d:
        namelist.append(i[0])
    namelist = sorted(namelist)
    drop = ttk.Combobox(f4, values=namelist)
    drop.pack()

    def keydown(e):
        ba = drop.get()
        a = ba.upper()
        checklist = []
        for i in namelist:
            if a in i:
                checklist.append(i)
        drop["values"] = checklist

    def keyup(e):
        drop.event_generate("<Down>")

    def contin1(name):
        global f2
        global f3
        global f4

        f2 = Frame(root, background="pink", width=10, height=100, borderwidth=6, relief=SUNKEN)
        f2.grid(row=0, column=1, sticky="nsew", rowspan=2)
        # here we will create the bill

        f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
        f3.grid(row=0, column=2, sticky="nsew")
        f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
        f4.grid(row=1, column=2, sticky="nsew")
        l1 = Label(f4, text=f"{name}", width=8)
        l1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        l2 = Label(f4, text="TYPE", padx=5, width=8)
        l2.grid(row=1, column=0, padx=5, pady=5)
        e2 = Entry(f4)
        e2.grid(row=1, column=1)
        e2.focus()
        e2.bind("<KP_Enter>", lambda x: e3.focus())
        e2.bind("<Return>", lambda x: e3.focus())

        l3 = Label(f4, text="TRANSAC. NO", padx=5, width=8)
        l3.grid(row=2, column=0, padx=5, pady=5)
        e3 = Entry(f4)
        e3.grid(row=2, column=1)
        l4 = Label(f4, text="AMOUNT", padx=5, width=8)
        l4.grid(row=0, column=2, padx=5, pady=5)
        e4 = Entry(f4)
        e4.grid(row=0, column=3)
        l5 = Label(f4, text="DATE", padx=5, width=8)
        l5.grid(row=1, column=2, padx=5, pady=5)
        e5 = Entry(f4)
        e5.grid(row=1, column=3)

        e3.bind("<KP_Enter>", lambda x: e4.focus())
        e3.bind("<Return>", lambda x: e4.focus())
        e4.bind("<KP_Enter>", lambda x: e5.focus())
        e4.bind("<Return>", lambda x: e5.focus())

        def savecredit():
            connection = sqlite3.connect("mytables4.db")
            cursor = connection.cursor()
            asd = []
            asd.append(name)
            asd.append(e2.get())
            asd.append(e3.get())
            try:
                we = float(e4.get())
                asd.append(we)
            except Exception as e:
                asd.append('0')
            try:
                as1 = e5.get()
                if as1.count('-') == 2 and as1.index('-') == 2 and as1.index('-', 3) == 5 and len(as1) == 10:
                    date1 = as1.split('-')
                    date1.reverse()
                    date2 = "-".join(date1)
                    asd.append(date2)
                elif as1.count('-') == 2 and as1.index('-') == 4 and as1.index('-', 5) == 7 and len(as1) == 10:
                    asd.append(as1)
                else:
                    tsmg.showinfo("FORMAT", "Wrong date format")
                    return
            except Exception as e:
                print(e)
                return

            sa = f'''INSERT INTO credittable VALUES ("{asd[0]}","{asd[1]}","{asd[2]}","{asd[3]}","{asd[4]}")'''
            try:
                cursor.execute(sa)
                connection.commit()
                connection.close()
                connection = sqlite3.connect('mytables4.db')
                conn = connection.cursor()
                conn.execute(f"SELECT * FROM custom9 WHERE NAME = '{name}'")
                sele = conn.fetchall()
                selecate = list(sele[0])
                total = float(selecate[7])
                newtotal = total - float(asd[3])
                conn.execute(f"UPDATE custom9 SET TOTAL = '{newtotal}' where NAME='{name}'")

                connection.commit()
                connection.close()
                tsmg.showinfo("successful", "your credis has been saved")
            except Exception as e:
                tsmg.showinfo("warning !", "something went wrong")
                print(e)

            pass

        Button(f4, text="SAVE CREDIT", command=savecredit).grid(row=2, column=2, columnspan=2, padx=25)
        pass

    def contin():
        name = drop.get()
        f2.destroy()
        f3.destroy()
        f4.destroy()
        contin1(name)

    drop.bind("<KeyRelease>", keydown)
    drop.bind("<Return>", keyup)
    drop.focus()
    Button(f4, text="UPDATE CUSTOMER", command=contin).pack(pady=30)

    pass


def addpayment(event):
    f3.destroy()
    f4.destroy()
    addpayment1(event)


def showbill1(event):
    global f3
    global f4
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute(f"SELECT * FROM billstock5 WHERE DATE >= '{from_date}' AND DATE <= '{to_date}'")
    d = crsr.fetchall()
    connection.close()
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    treev = ttk.Treeview(f3, selectmode='browse', height=19)
    treev.pack(fill=X)

    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev.configure(xscrollcommand=scrollbar.set)
    treev["columns"] = ("1", "2", "3", "4")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", anchor='c')
    treev.column("2", anchor='c')
    treev.column("3", anchor='c')
    treev.column("4", anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="BILLNO")
    treev.heading("2", text="BUYER")
    treev.heading("3", text="DATE")
    treev.heading("4", text="TOTAL")

    # # showing bill only one time
    # res = []
    # for row in d:
    #     s = []
    #     s.append(row[0])
    #     s.append(row[1])
    #     s.append(row[7])
    #     s.append(row[9])
    #     res.append(s)
    # newres = []
    # #we need to comment this out
    # for row in res:
    #     if row not in newres:
    #         newres.append(row)
    # #till here
    # for s in newres:
    #     treev.insert("", 'end', values=s)

    dict = {}
    for row in d:
        if row[0] not in dict:
            dict[row[0]] = [row[1], row[7], row[9]]
        else:
            tot = dict[row[0]][2]
            dict[row[0]][2] = float(tot) + float(row[9])
    tes = dict.items()
    tes = list(tes)
    newres = []
    for i in tes:
        k = []
        j = list(i)
        k.append(j[0])
        for h in j[1]:
            k.append(h)
        newres.append(k)

    for s in newres:
        if 'C-' in s[0]:
            treev.insert("", 'end', values=s, tags=('cancelbill',))
        else:
            treev.insert("", 'end', values=s)
    treev.tag_configure('cancelbill', background='red', foreground='white')

    def clickedrow(event):
        item = treev.identify_row(event.y)
        if item:
            a = treev.item(item, 'values')
            a = list(a)

            def qwertfd(a):
                global f3
                f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
                f3.grid(row=0, column=2, sticky="nsew")
                treev1 = ttk.Treeview(f3, selectmode='browse', height=20)
                treev1.pack(fill=BOTH)
                scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev1.xview)
                scrollbar.pack(side=BOTTOM, fill=X)
                treev1["columns"] = ("1", "2", "3", "4", "5", "6", "7")
                treev1.configure(xscrollcommand=scrollbar.set)
                treev1['show'] = 'headings'

                treev1.column("1", width=50, anchor='c')
                treev1.column("2", width=150, anchor='c')
                treev1.column("3", width=200, anchor='c')
                treev1.column("4", width=50, anchor='c')
                treev1.column("5", width=50, anchor='c')
                treev1.column("6", width=50, anchor='c')
                treev1.column("7", width=50, anchor='c')
                na = a[1]
                na = na.upper()
                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
                sel = crsr.fetchall()
                connection.close()
                sel = list(sel[0])
                r1 = ("NAME", sel[0], "", "BILLNO", a[0], "", "")
                r2 = ("ADD1", sel[1], "", "MOBILENO", sel[5], "", "")
                r3 = ("ADD2", sel[2], "", "DATE", a[2], "", "")
                treev1.insert("", 'end', values=r1)
                treev1.insert("", 'end', values=r2)
                treev1.insert("", 'end', values=r3)
                r31 = ("", "", "", "", "", "", "")
                treev1.insert("", 'end', values=r31)

                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(f"SELECT * FROM billstock5 WHERE BILLNo ='{a[0]}'")
                d = crsr.fetchall()
                connection.close()
                total = []
                for i in d:
                    listforinsert = []
                    listforinsert.append(i[2])
                    listforinsert.append(i[3])
                    listforinsert.append(i[4])
                    listforinsert.append(i[5])
                    listforinsert.append(i[6])
                    listforinsert.append(i[8])
                    listforinsert.append(i[9])
                    try:
                        total.append(int(i[9]))
                    except Exception as e:
                        print(e)
                    treev1.insert("", 'end', values=listforinsert)
                r312 = ("", "", "", "", "", "", "")
                treev1.insert("", 'end', values=r312)
                r32 = ("", "", "", "", "", "", "")
                treev1.insert("", 'end', values=r32)
                r33 = ("", "", "", "", "TOTAL", "", sum(total))
                treev1.insert("", 'end', values=r33, tags=('tot',))
                treev1.tag_configure('tot', background='light blue')

            def qsar(a):
                f3.destroy()
                qwertfd(a)

            qsar(a)

        pass

    treev.bind("<Double-Button-1>", clickedrow)
    pass


def showbill(event):
    f3.destroy()
    f4.destroy()
    showbill1(event)


def showpayments1(events):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute(f"SELECT * FROM credittable WHERE DATE >='{from_date}' AND DATE <= '{to_date}'")
    d = crsr.fetchall()
    connection.close()
    treev = ttk.Treeview(f3, selectmode='browse', height=19)
    treev.pack()
    scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    treev.configure(xscrollcommand=scrollbar.set)
    treev["columns"] = ("1", "2", "3", "4", "5")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", anchor='c')
    treev.column("2", anchor='c')
    treev.column("3", anchor='c')
    treev.column("4", anchor='c')
    treev.column("5", anchor='c')

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="NAME")
    treev.heading("2", text="TYPE")
    treev.heading("3", text="TRANSACTION NO")
    treev.heading("4", text="AMOUNT")
    treev.heading("5", text="DATE")
    for r in d:
        treev.insert("", 'end', values=r)

    pass


def showpayments(events):
    f3.destroy()
    f4.destroy()
    showpayments1(events)


def billallexcel(event):
    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute(f"SELECT * FROM billstock5 WHERE DATE > '{from_date}' AND DATE < '{to_date}'")
    d = crsr.fetchall()
    connection.close()
    # ['CREDIT', 'EWRS', '10-11-2019', '30000.0']
    workbook = xlsxwriter.Workbook('BILLLIST.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})

    alpa = ['BILLNO', 'BUYER', 'BUNDLE', 'TYPE', 'DIMENSION', 'PCS', 'KG', 'DATE', 'RATE', 'TOTAL']

    d1 = d
    d1.insert(0, alpa)
    for i in range(len(d1)):
        d1[i] = list(d1[i])
    for i in range(len(d1)):
        for j in range(len(d1[0])):
            if (i == 0):
                worksheet.write(i, j, f'''{d1[i][j]}''', bold)
            else:
                worksheet.write(i, j, f'''{d1[i][j]}''')
    worksheet.set_column(2, 3, 25)
    worksheet.set_column(4, 4, 20)
    worksheet.set_column(7, 7, 15)
    worksheet.set_column(10, 12, 15)
    workbook.close()
    tsmg.showinfo("converted", "created a file name BILLLIST")


def exportbill1(event):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    l = Label(f4, text="BILL NUMBER", width=8)
    l.grid(row=0, column=0, padx=5, pady=5)
    e1 = Entry(f4)
    e1.focus()
    e1.grid(row=0, column=1)

    def check():
        try:
            # we will create a folder to store bill
            file = open('bill_location.txt', 'r')
            for e in file:
                mainloc = e
            workbook = xlsxwriter.Workbook(f'{mainloc}{e1.get()}.xlsx')
            worksheet = workbook.add_worksheet()
            bold = workbook.add_format({'bold': True})

            connection = sqlite3.connect("mytables4.db")
            crsr = connection.cursor()
            crsr.execute(f"SELECT * FROM billstock5 WHERE BILLNO = '{e1.get()}'")
            w = crsr.fetchall()
            connection.close()
            d = list(w[0])
            na = d[1]
            connection = sqlite3.connect("mytables4.db")
            crsr = connection.cursor()
            crsr.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
            sel = crsr.fetchall()
            connection.close()
            sel = list(sel[0])
            worksheet.set_column('A:A', 10)
            worksheet.set_column('B:B', 30)
            worksheet.set_column('C:C', 40)

            cell_format = workbook.add_format()
            cell_format.set_bottom(2)
            cell_format.set_top(2)

            cell_format2 = workbook.add_format()
            cell_format2.set_bottom(2)
            cell_format2.set_top(2)
            cell_format2.set_right(2)

            cell_format3 = workbook.add_format()
            cell_format3.set_bottom(2)
            cell_format3.set_top(2)
            cell_format3.set_right(2)
            cell_format3.set_left(2)

            cell_leftright = workbook.add_format()
            cell_leftright.set_right(2)
            cell_leftright.set_left(2)

            cell_leftbottom = workbook.add_format()
            cell_leftbottom.set_bottom(2)
            cell_leftbottom.set_bold(True)
            cell_leftbottom.set_left(2)

            cell_rightbottom = workbook.add_format()
            cell_rightbottom.set_bottom(2)
            cell_rightbottom.set_bold(True)
            cell_rightbottom.set_right(2)

            cell_bottom = workbook.add_format()
            cell_bottom.set_bottom(2)

            cell_bottom1 = workbook.add_format()
            cell_bottom1.set_bottom(2)
            cell_bottom1.set_bold(True)

            cell_right = workbook.add_format()
            cell_right.set_right(2)

            cell_left = workbook.add_format()
            cell_left.set_left(2)

            cell_righttop = workbook.add_format()
            cell_righttop.set_right(2)
            cell_righttop.set_top(2)

            cell_lefttop = workbook.add_format()
            cell_lefttop.set_left(2)
            cell_lefttop.set_top(2)

            cell_leftrighttop1 = workbook.add_format()
            cell_leftrighttop1.set_left(2)
            cell_leftrighttop1.set_top(2)
            cell_leftrighttop1.set_right(2)
            cell_leftrighttop1.set_font_size(20)
            cell_leftrighttop1.set_bold(True)
            cell_leftrighttop1.set_align('center')

            cell_leftrighttop = workbook.add_format()
            cell_leftrighttop.set_left(2)
            cell_leftrighttop.set_top(2)
            cell_leftrighttop.set_right(2)
            cell_leftrighttop.set_bold(True)

            cell_top = workbook.add_format()
            cell_top.set_top(2)
            cell_leftrighttop.set_bold(True)

            worksheet.merge_range('A1:G3', "JAI MATA DI", cell_leftrighttop1)

            worksheet.write(3, 0, "NAME", cell_lefttop)
            worksheet.write(3, 1, sel[0], cell_righttop)
            worksheet.write(4, 0, "ADD1", cell_left)
            worksheet.write(4, 1, sel[1], cell_right)
            worksheet.write(5, 0, "ADD2", cell_left)
            worksheet.write(5, 1, sel[2], cell_right)
            worksheet.write(3, 2, "BILLNO", cell_top)
            worksheet.write(3, 4, "", cell_top)
            worksheet.write(3, 5, "", cell_top)
            worksheet.write(3, 6, "", cell_righttop)
            worksheet.write(4, 6, "", cell_right)
            worksheet.write(5, 6, "", cell_right)

            worksheet.write(3, 3, e1.get(), cell_top)
            worksheet.write(4, 2, "MOBILENO")
            worksheet.write(4, 3, sel[5])
            worksheet.write(5, 2, "DATE")
            worksheet.write(5, 3, d[7])
            num = 6
            worksheet.write(num, 0, "BUNDLENO", cell_format3)
            worksheet.write(num, 1, "PRODUCT", cell_format)
            worksheet.write(num, 2, "SIZE", cell_format2)
            worksheet.write(num, 3, "PCS", cell_format2)
            worksheet.write(num, 4, "KG", cell_format2)
            worksheet.write(num, 5, "RATE", cell_format2)
            worksheet.write(num, 6, "TOTAL", cell_format2)

            worksheet.write(7, 0, "", cell_leftright)
            worksheet.write(7, 2, "", cell_right)
            worksheet.write(7, 3, "", cell_right)
            worksheet.write(7, 4, "", cell_right)
            worksheet.write(7, 5, "", cell_right)
            worksheet.write(7, 6, "", cell_right)
            num = 7
            total = []
            for i in w:
                num += 1
                worksheet.write(num, 0, i[2], cell_leftright)
                worksheet.write(num, 1, i[3])
                worksheet.write(num, 2, i[4], cell_right)
                worksheet.write(num, 3, i[5], cell_right)
                worksheet.write(num, 4, i[6], cell_right)
                worksheet.write(num, 5, i[8], cell_right)
                worksheet.write(num, 6, i[9], cell_right)
                total.append(int(i[9]))
            worksheet.write(num + 1, 0, "", cell_leftright)
            worksheet.write(num + 1, 2, "", cell_right)
            worksheet.write(num + 1, 3, "", cell_right)
            worksheet.write(num + 1, 4, "", cell_right)
            worksheet.write(num + 1, 5, "", cell_right)
            worksheet.write(num + 1, 6, "", cell_right)
            worksheet.write(num + 2, 0, "", cell_lefttop)
            worksheet.write(num + 2, 1, "", cell_top)
            worksheet.write(num + 2, 2, "", cell_righttop)
            worksheet.write(num + 2, 3, "", cell_top)
            worksheet.write(num + 2, 4, "", cell_top)
            worksheet.write(num + 2, 5, "TOTAL", cell_top)
            worksheet.write(num + 2, 6, str(sum(total)), cell_righttop)
            worksheet.write(num + 3, 0, "", cell_left)
            worksheet.write(num + 3, 5, "", cell_top)
            worksheet.write(num + 3, 6, "", cell_top)
            worksheet.write(num + 4, 0, "", cell_left)
            worksheet.write(num + 5, 0, "RECIVER SIGNATURE", cell_leftbottom)
            worksheet.write(num + 5, 1, "", cell_bottom)
            worksheet.write(num + 5, 2, "", cell_bottom)
            worksheet.write(num + 5, 3, "", cell_bottom)
            worksheet.write(num + 5, 4, "", cell_bottom)
            worksheet.write(num + 5, 6, "", cell_rightbottom)
            worksheet.write(num + 3, 0, "", cell_left)

            worksheet.write(num + 3, 1, "", cell_right)
            worksheet.write(num + 4, 1, "", cell_right)
            worksheet.write(num + 5, 2, "", cell_rightbottom)
            worksheet.write(num + 3, 6, "", cell_righttop)
            worksheet.write(num + 4, 6, "", cell_right)
            worksheet.write(num + 5, 5, "   SIGNATURE", cell_bottom1)

            worksheet.write(num + 2, 2, f"                               ", cell_leftrighttop)
            worksheet.write(num + 3, 2, f"    ", cell_leftright)
            worksheet.write(num + 4, 2, f"     BALANCE                                 {float(sel[7])}",
                            cell_leftrighttop)

            workbook.close()
            tsmg.showinfo("CREATED", "File has been created")
            exportbill(event)
        except Exception as e:
            tsmg.showinfo("Oops!", "Something went wrong ")
            exportbill(event)
            print(e)

    Button(f4, text="SEARCH", command=check).grid(row=2, column=0, columnspan=2, padx=25)

    pass


def exportbill(event):
    f3.destroy()
    f4.destroy()
    exportbill1(event)


def updatebill1(event):
    global f3
    global f4
    f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    l = Label(f4, text="BILL NUMBER", width=10)
    l.grid(row=0, column=0, padx=5, pady=5)
    e1 = Entry(f4)
    e1.grid(row=0, column=1)
    e1.focus()

    def upbill1(e1get):
        global f3
        global f4
        f3 = Frame(root, background="bisque", width=100, height=100, borderwidth=6, relief=SUNKEN)
        f3.grid(row=0, column=2, sticky="nsew")
        f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
        f4.grid(row=1, column=2, sticky="nsew")
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        qwwq = e1get
        qwerewq = qwwq.split('-')
        if (len(qwerewq) == 2):
            crsr.execute(f"SELECT * FROM billstock5 WHERE BILLNO= '{e1get}'")
            d = crsr.fetchall()
            connection.close()

            treev1 = ttk.Treeview(f3, selectmode='browse', height=20)
            treev1.pack(fill=BOTH)
            scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev1.xview)
            scrollbar.pack(side=BOTTOM, fill=X)
            treev1["columns"] = ("1", "2", "3", "4", "5", "6", "7")
            treev1.configure(xscrollcommand=scrollbar.set)
            treev1['show'] = 'headings'

            treev1.column("1", anchor='c')
            treev1.column("2", width=200, anchor='c')
            treev1.column("3", width=80, anchor='c')
            treev1.column("4", width=80, anchor='c')
            treev1.column("5", width=80, anchor='c')
            treev1.column("6", width=80, anchor='c')
            treev1.column("7", width=80, anchor='c')
            na = d[0][1]
            na = na.upper()
            connection = sqlite3.connect("mytables4.db")
            crsr = connection.cursor()
            crsr.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
            sel = crsr.fetchall()
            connection.close()
            sel = list(sel[0])
            billnoforadd = d[0][0]
            buyernameforadd = sel[0]
            dateforadd = d[0][7]
            r1 = ("NAME", sel[0], "", "BILLNO", d[0][0], "", "")
            r2 = ("ADD1", sel[1], "", "MOBILENO", sel[5], "", "")
            r3 = ("ADD2", sel[2] + "," + sel[3], "", "DATE", d[0][7], "", "")
            treev1.insert("", 'end', values=r1)
            treev1.insert("", 'end', values=r2)
            treev1.insert("", 'end', values=r3)
            r31 = ("", "", "", "", "", "", "")
            treev1.insert("", 'end', values=r31)

            de = d.copy()
            total = []
            for i in de:
                listforinsert = []
                listforinsert.append(i[2])
                listforinsert.append(i[3])
                listforinsert.append(i[4])
                listforinsert.append(i[5])
                listforinsert.append(i[6])
                listforinsert.append(i[8])
                listforinsert.append(i[9])
                try:
                    total.append(int(i[9]))
                except Exception as e:
                    print(e)

                treev1.insert("", 'end', values=listforinsert)
            r312 = ("", "", "", "", "", "", "")
            treev1.insert("", 'end', values=r312)
            r32 = ("", "", "", "", "", "", "")
            treev1.insert("", 'end', values=r32)
            r33 = ("", "", "", "", "TOTAL", "", sum(total))
            treev1.insert("", 'end', values=r33, tags=('tot',))
            treev1.tag_configure('tot', background='light blue')
            lengthofde = len(de)

            def changedate1():
                global f4
                f4 = Frame(root, background="pink", width=100, height=15, borderwidth=6, relief=SUNKEN)
                f4.grid(row=1, column=2, sticky="nsew")
                l = Label(f4, text="ENTER NEW DATE", width=15)
                l.grid(row=0, column=0, padx=5, pady=5)
                e12 = Entry(f4)
                e12.grid(row=0, column=1)

                def face():
                    as1 = e12.get()
                    if as1.count('-') == 2 and as1.index('-') == 2 and as1.index('-', 3) == 5 and len(as1) == 10:
                        date1 = as1.split('-')
                        date1.reverse()
                        date2 = "-".join(date1)
                        connection = sqlite3.connect('mytables4.db')
                        connection.execute(f"UPDATE billstock5 SET DATE = '{date2}' where BILLNO='{d[0][0]}'")
                        connection.commit()
                        connection.close()
                        tsmg.showinfo("completed", "DATE CHANGED")
                    elif as1.count('-') == 2 and as1.index('-') == 4 and as1.index('-', 5) == 7 and len(as1) == 10:
                        connection = sqlite3.connect('mytables4.db')
                        connection.execute(f"UPDATE billstock5 SET DATE = '{as1}' where BILLNO='{d[0][0]}'")
                        connection.commit()
                        connection.close()
                        tsmg.showinfo("completed", "DATE CHANGED")
                    else:
                        tsmg.showinfo("FORMAT", "Wrong date format")
                        # UPDATE DATE

                Button(f4, text="CHANGE DATE", command=face).grid(row=1, column=0, columnspan=2)

                pass

            def changedate():
                f4.destroy()
                changedate1()

            m = Menu(root, tearoff=0)
            m = Menu(root, tearoff=0)
            yaxis = 0

            def delete():
                item = treev1.identify_row(yaxis)

                if lengthofde != 1:
                    a = treev1.item(item, 'values')
                    a = list(a)
                    connection = sqlite3.connect("mytables4.db")
                    cursor = connection.cursor()
                    sa = f'''DELETE FROM billstock5 WHERE BUNDLENO = '{a[0]}' AND PRODUCT ='{a[1]}' AND SIZE = '{a[2]}' AND PCS = '{a[3]}' AND KG = '{a[4]}';'''
                    cursor.execute(sa)
                    connection.commit()
                    connection.close()
                    connection = sqlite3.connect('mytables4.db')
                    conn = connection.cursor()
                    conn.execute(f"UPDATE stockfinal634 SET STATUS = 'INSTOCK' where BUNDLE='{a[0]}'")
                    connection.commit()
                    conn.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
                    sele = conn.fetchall()
                    selecate = list(sele[0])
                    totale121 = float(selecate[7])
                    totka121 = int(a[6])
                    new_tot121 = totale121 - float(totka121)
                    conn.execute(f"UPDATE custom9 SET TOTAL = '{new_tot121}' where NAME='{na}'")
                    connection.commit()
                    connection.close()
                    treev1.delete(item)
                else:
                    tsmg.showinfo("WARNING", "U can't delete it but cancel it")

            def update():
                item = treev1.identify_row(yaxis)
                if item:
                    a = treev1.item(item, 'values')
                    a = list(a)

                    connection = sqlite3.connect("mytables4.db")
                    cursor = connection.cursor()
                    t1 = Toplevel(background="bisque")
                    t1.minsize(250, 150)
                    l1 = Label(t1, text="RATE")
                    l1.grid(row=0, column=0, padx=5, pady=5)
                    e1 = Entry(t1)
                    e1.grid(row=0, column=1)
                    e1.focus()
                    l2 = Label(t1, text="TOTAL")
                    l2.grid(row=1, column=0, padx=5, pady=5)
                    e2 = Entry(t1)
                    e2.grid(row=1, column=1)
                    e1.insert(0, '0')
                    e2.insert(0, '0')

                    def setrate():
                        try:
                            qwaszx = int(e1.get())
                            qwaszx2 = int(e2.get())
                            sa = f'''UPDATE billstock5 SET RATE = '{e1.get()}',TOTAL = '{e2.get()}' WHERE BUNDLENO = '{a[0]}' AND PRODUCT ='{a[1]}' AND SIZE = '{a[2]}' AND PCS = '{a[3]}' AND KG = '{a[4]}';'''
                            cursor.execute(sa)
                            connection.commit()
                            cursor.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
                            sele = cursor.fetchall()
                            selecate = list(sele[0])
                            totale121 = float(selecate[7])
                            new_tot121 = totale121 - int(a[6])
                            new_tot121 = new_tot121 + int(e2.get())

                            sa = f'''UPDATE custom9 SET TOTAL = '{new_tot121}' where NAME='{na}';'''
                            cursor.execute(sa)
                            connection.commit()
                            connection.close()
                            a[5] = e1.get()
                            a[6] = e2.get()
                            t1.destroy()
                            nonlocal treev1
                            g = (a[0], a[1], a[2], a[3], a[4], a[5], a[6])
                            treev1.item(item, values=g)


                        except Exception as e:
                            tsmg.showinfo("warn", "something went wrong")

                        pass

                    b11 = Button(t1, text="    SET    ", command=setrate)
                    b11.grid(row=2, column=0, columnspan=2, pady=20)

                print("update")

            m.add_command(label="Delete", command=delete)
            m.add_separator()
            m.add_command(label="Update", command=update)

            def do_popup(event):
                nonlocal yaxis
                yaxis = event.y
                m.tk_popup(event.x_root, event.y_root)

            treev1.bind("<Button-2>", do_popup)

            Button(f4, text="CHANGE DATE", command=changedate).grid(row=1, column=0, columnspan=2, padx=150)

            def cancelbill():
                chos = tsmg.askquestion("sure!", "Are you sure you want to cancel bill")
                if chos == "yes":
                    try:
                        kite = []
                        totka = total
                        for i in de:
                            kite.append(i[2])
                        conn = sqlite3.connect('mytables4.db')
                        for i in kite:
                            conn.execute(f"UPDATE stockfinal634 SET STATUS = 'INSTOCK' where BUNDLE='{i}'")
                            conn.commit()
                        conn.close()

                        connection = sqlite3.connect('mytables4.db')
                        conn = connection.cursor()
                        conn.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
                        sele = conn.fetchall()
                        selecate = list(sele[0])
                        totale = float(selecate[7])
                        new_tot = totale - float(sum(totka))
                        conn.execute(f"UPDATE custom9 SET TOTAL = '{new_tot}' where NAME='{na}'")
                        connection.commit()
                        connection.close()
                        # connection = sqlite3.connect("mytables4.db")
                        # cursor = connection.cursor()
                        # sa = f'''INSERT INTO credittable VALUES ("{na}","C-{de[0][0]}","CANCEL BILLED","{sum(totka)}","{de[0][7]}")'''
                        # cursor.execute(sa)
                        # connection.commit()
                        # connection.close()

                        connection = sqlite3.connect('mytables4.db')
                        connection.execute(f"UPDATE billstock5 SET BILLNO = 'C-{d[0][0]}' where BILLNO='{d[0][0]}'")
                        connection.commit()
                        connection.close()
                        tsmg.showinfo("Completed", "your bill has been canceled")
                        addbundle(event)
                    except Exception as e:
                        print(e)
                        tsmg.showinfo("error", f"{e}")
                        addbundle(event)

                pass

            Button(f4, text="CANCEL BILL", command=cancelbill).grid(row=1, column=3, columnspan=2, padx=150)

            def addbundlea():
                t1 = Toplevel()
                t1.minsize(450, 450)
                f3 = Frame(t1, background="bisque", borderwidth=6, relief=SUNKEN)
                f3.grid(row=0, column=2, sticky="nsew")
                f4 = Frame(t1, background="pink", borderwidth=6, relief=SUNKEN)
                f4.grid(row=1, column=2, sticky="nsew")
                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(f"SELECT * FROM stockfinal634")
                w = crsr.fetchall()
                connection.close()
                bunlis = []
                for i in w:
                    bunlis.append(i[3])

                l = Label(f4, text="BUNDLE NO", width=8)
                l.grid(row=0, column=0, padx=5, pady=5)
                e = ttk.Combobox(f4, values=bunlis, height=8)
                e.grid(row=0, column=1)
                e.focus()

                def check():
                    connection = sqlite3.connect("mytables4.db")
                    crsr = connection.cursor()
                    crsr.execute(f"SELECT * FROM stockfinal634 WHERE BUNDLE ='{e.get()}';")
                    w = crsr.fetchall()
                    if (len(w) == 0):
                        Button(f4, text="NOT FOUND").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')
                        pass
                    else:
                        d = list(w[0])
                        connection.close()
                        if (d[12] == 'SOLD'):
                            tsmg.showinfo("warning", "Bundle already SOLD!")
                        else:
                            l1 = Label(f3, text="Bundle type", width=8)
                            l1.grid(row=0, column=0, padx=5, pady=5)
                            e1 = Entry(f3)
                            e1.grid(row=0, column=1)
                            l2 = Label(f3, text="DEN SIZE", padx=5, width=8)
                            l2.grid(row=1, column=0, padx=5, pady=5)
                            e2 = Entry(f3)
                            e2.grid(row=1, column=1)
                            l3 = Label(f3, text="THK REMARK", padx=5, width=8)
                            l3.grid(row=2, column=0, padx=5, pady=5)
                            e3 = Entry(f3)
                            e3.grid(row=2, column=1)
                            l4 = Label(f3, text="BUNDLE", padx=5, width=8)
                            l4.grid(row=3, column=0, padx=5, pady=5)
                            e4 = Entry(f3)
                            e4.grid(row=3, column=1)
                            l5 = Label(f3, text="COVER", padx=5, width=8)
                            l5.grid(row=4, column=0, padx=5, pady=5)
                            e5 = Entry(f3)
                            e5.grid(row=4, column=1)
                            l6 = Label(f3, text="STM", padx=5, width=8)
                            l6.grid(row=0, column=5, padx=5, pady=5)
                            e6 = Entry(f3)
                            e6.grid(row=0, column=6)
                            l7 = Label(f3, text="R2", padx=5, width=8)
                            l7.grid(row=0, column=3, padx=20, pady=5)
                            e7 = Entry(f3)
                            e7.grid(row=0, column=4)
                            l8 = Label(f3, text="PCS", padx=5, width=8)
                            l8.grid(row=1, column=3, padx=5, pady=5)
                            e8 = Entry(f3)
                            e8.grid(row=1, column=4)
                            l9 = Label(f3, text="MM", padx=5, width=8)
                            l9.grid(row=2, column=3, padx=5, pady=5)
                            e9 = Entry(f3)
                            e9.grid(row=2, column=4)
                            l10 = Label(f3, text="KGS", padx=5, width=8)
                            l10.grid(row=3, column=3, padx=5, pady=5)
                            e10 = Entry(f3)
                            e10.grid(row=3, column=4)
                            l11 = Label(f3, text="PACKINGNO", padx=5, width=8)
                            l11.grid(row=4, column=3, padx=5, pady=5)
                            e11 = Entry(f3)
                            e11.grid(row=4, column=4)
                            l12 = Label(f3, text="RATE", padx=5, width=8)
                            l12.grid(row=1, column=5, padx=5, pady=5)
                            e12 = Entry(f3)
                            e12.grid(row=1, column=6)
                            l13 = Label(f3, text="TOTAL", padx=5, width=8)
                            l13.grid(row=2, column=5, padx=20, pady=5)
                            e13 = Entry(f3)
                            e13.grid(row=2, column=6, padx=5, pady=5)

                            e1.insert(0, d[0])
                            e2.insert(0, d[1])
                            e3.insert(0, d[2])
                            e4.insert(0, d[3])
                            e5.insert(0, d[4])
                            e6.insert(0, d[5])
                            e7.insert(0, d[6])
                            e8.insert(0, d[7])
                            e9.insert(0, d[8])
                            e10.insert(0, d[9])
                            e11.insert(0, d[10])

                            def addbillto():
                                r4 = []
                                r4.append(billnoforadd)
                                r4.append(buyernameforadd)
                                r4.append(d[3])
                                r4.append(d[0])
                                r4.append(d[1] + d[2] + 'x' + d[8] + 'mm')
                                r4.append(d[7])
                                r4.append(d[9])
                                r4.append(dateforadd)
                                if e12.get() == '':
                                    r4.append('0')
                                else:
                                    try:
                                        ew = e12.get()
                                        eew = float(ew)
                                        r4.append(int(eew))
                                    except Exception as e:
                                        print(e)
                                        r4.append('0')
                                        tsmg.showinfo("info", "sorry wrong input price")

                                if e13.get() == '':
                                    r4.append('0')
                                else:
                                    try:
                                        ew1 = e13.get()
                                        eew1 = float(ew1)
                                        r4.append(int(eew1))
                                    except Exception as e:
                                        r4.append('0')
                                        tsmg.showinfo("info", "sorry wrong input price")
                                pass

                                connection = sqlite3.connect('mytables4.db')
                                conn = connection.cursor()
                                conn.execute(f"UPDATE stockfinal634 SET STATUS = 'SOLD' where BUNDLE='{d[3]}'")
                                connection.commit()
                                i = r4
                                sa = f'''INSERT INTO billstock5 VALUES ('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}','{i[8]}','{i[9]}')'''
                                conn.execute(sa)
                                connection.commit()
                                conn.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
                                sele = conn.fetchall()
                                selecate = list(sele[0])
                                tot = float(selecate[7])
                                new_tot = tot + int(i[9])
                                connection.close()

                                connection = sqlite3.connect("mytables4.db")
                                crsr = connection.cursor()
                                crsr.execute(f"UPDATE custom9 SET TOTAL = '{new_tot}' where NAME='{na}'")
                                connection.commit()
                                connection.close()
                                connection.close()
                                nonlocal treev1
                                r4.pop(0)
                                r4.pop(0)
                                r4.pop(5)

                                treev1.insert('', 'end', values=tuple(r4))

                                t1.destroy()

                            Button(f4, text=" ADD TO BILl ", command=addbillto).grid(row=2, column=3, columnspan=2,
                                                                                     padx=250, sticky='nw')

                def keydown(event):
                    ba = e.get()
                    a = ba.upper()
                    checklist = []
                    for i in bunlis:
                        if a in i:
                            checklist.append(i)
                    e["values"] = checklist

                e.bind("<KeyRelease>", keydown)

                def keyup(event):
                    e.event_generate("<Down>")

                e.bind("<KP_Enter>", keyup)
                e.bind("<Return>", keyup)
                Button(f4, text="SEARCH", command=check).grid(row=2, column=0, columnspan=2, padx=25)

            Button(f4, text="ADD BUNDLE", command=addbundlea).grid(row=1, column=5, columnspan=2, padx=150)

        else:
            tsmg.showinfo("Sorry", "Can't update cancelled bill ! ")

    def upbill():
        e1get = e1.get()
        f3.destroy()
        f4.destroy()
        upbill1(e1get)

    Button(f4, text="UPDATE BILL", command=upbill).grid(row=1, column=0, columnspan=2)

    pass


def updatebill(event):
    f3.destroy()
    f4.destroy()
    updatebill1(event)


def createbill1(event):
    global f2
    global f3
    global f4
    # tablename="billstock5"
    # createbilltable(tablename)
    # billtablename="billno9"
    # createbillnotable(billtablename)
    f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
    f3.grid(row=0, column=2, sticky="nsew")
    f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
    f4.grid(row=1, column=2, sticky="nsew")
    f2 = Frame(root, background="pink", width=10, height=100, borderwidth=6, relief=SUNKEN)
    f2.grid(row=0, column=1, sticky="nsew", rowspan=2)

    connection = sqlite3.connect("mytables4.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM custom9")
    d = crsr.fetchall()
    connection.close()

    namelist = []
    for i in d:
        namelist.append(i[0])
    namelist = sorted(namelist)
    drop = ttk.Combobox(f4, values=namelist, width=20)
    drop.pack()

    def keydown(e):
        ba = drop.get()
        a = ba.upper()
        checklist = []
        for i in namelist:
            if a in i:
                checklist.append(i)
        drop["values"] = checklist

    def keyup(e):
        drop.event_generate("<Down>")

    def contin12(na):
        global f2
        global f3
        global f4
        na = na.upper()
        billbundlelist = []
        bnolist = []
        poplino = 0
        f2 = Frame(root, background="pink", width=10, height=100, borderwidth=6, relief=SUNKEN)
        f2.grid(row=0, column=1, sticky="nsew", rowspan=2)
        # here we will create the bill

        f3 = Frame(root, background="bisque", width=100, borderwidth=6, relief=SUNKEN)
        f3.grid(row=0, column=2, sticky="nsew")
        f4 = Frame(root, background="pink", width=100, borderwidth=6, relief=SUNKEN)
        f4.grid(row=1, column=2, sticky="nsew")

        treev = ttk.Treeview(f3, selectmode='browse', height=20)
        treev.pack(fill=BOTH)
        scrollbar = ttk.Scrollbar(f3, orient='horizontal', command=treev.xview)
        scrollbar.pack(side=BOTTOM, fill=X)
        treev["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        treev.configure(xscrollcommand=scrollbar.set)
        treev['show'] = 'headings'

        treev.column("1", anchor='c')
        treev.column("2", width=200, anchor='c')
        treev.column("3", width=200, anchor='c')
        treev.column("4", width=50, anchor='c')
        treev.column("5", width=50, anchor='c')
        treev.column("6", width=50, anchor='c')
        treev.column("7", width=50, anchor='c')

        try:

            connection = sqlite3.connect("mytables4.db")
            crsr = connection.cursor()
            crsr.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
            sel = crsr.fetchall()
            connection.close()
            sel = list(sel[0])
        except Exception as eas:
            tsmg.showinfo("Error !", "Wrong name entered")
            return

        # we will fatch bundle no now

        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM billno9 WHERE NAME = '{year}'")
        w = crsr.fetchall()
        connection.close()
        wai = list(w[0])
        yearlasttwo = year[2:]
        billno = str(yearlasttwo) + '-' +str(wai[1])

        # remember to upgrade bill no
        r1 = ("NAME", sel[0], "", "BILLNO", billno, "", "")
        r2 = ("ADD1", sel[1], "", "MOBILENO", sel[5], "", "")
        r3 = ("ADD2", sel[2] + ',' + sel[3], "", "", "", "", "")
        treev.insert("", 'end', values=r1)
        treev.insert("", 'end', values=r2)
        treev.insert("", 'end', values=r3)
        r31 = ("", "", "", "", "", "", "")
        treev.insert("", 'end', values=r31)

        # new edit
        connection = sqlite3.connect("mytables4.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM stockfinal634")
        w = crsr.fetchall()
        connection.close()
        bunlis = []
        for i in w:
            if (i[12] != 'SOLD'):
                bunlis.append(i[3])
        bunlis.reverse()

        l = Label(f2, text="BUNDLE NO", width=8)
        l.pack(pady=5)
        ese = ttk.Combobox(f2, values=bunlis, width=10)
        ese.pack(pady=5)

        def keydown(event):
            ba = ese.get()
            a = ba.upper()
            checklist = []
            for i in bunlis:
                if a in i:
                    checklist.append(i)
            checklist.append("NEW BUNDLE")
            ese["values"] = checklist

        ese.bind("<KeyRelease>", keydown)

        def keyup(event):
            ese.event_generate("<Down>")

        ese.bind("<Return>", keyup)

        def check():

            if ese.get() == "NEW BUNDLE":
                f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
                f4.grid(row=1, column=2, sticky="nsew")
                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(f"SELECT * FROM stockfinal634")
                waq = crsr.fetchall()
                connection.close()
                bunlistype = []
                for i in waq:
                    bunlistype.append(i[0])
                bunlistype = list(set(bunlistype))

                l1 = Label(f4, text="Bundle type", width=8)
                l1.grid(row=0, column=0, padx=5, pady=5)
                e1 = ttk.Combobox(f4, values=bunlistype, height=8, width=25)
                e1.grid(row=0, column=1)
                l2 = Label(f4, text="DEN SIZE", padx=5, width=8)
                l2.grid(row=1, column=0, padx=5, pady=5)
                e2 = Entry(f4)
                e2.grid(row=1, column=1)
                l3 = Label(f4, text="THK REMARK", padx=5, width=8)
                l3.grid(row=2, column=0, padx=5, pady=5)
                e3 = Entry(f4)
                e3.grid(row=2, column=1)
                l4 = Label(f4, text="BUNDLE", padx=5, width=8)
                l4.grid(row=3, column=0, padx=5, pady=5)
                e4 = Entry(f4)
                e4.grid(row=3, column=1)
                l5 = Label(f4, text="COVER", padx=5, width=8)
                l5.grid(row=4, column=0, padx=5, pady=5)
                e5 = Entry(f4)
                e5.grid(row=4, column=1)
                l6 = Label(f4, text="STM", padx=5, width=8)
                l6.grid(row=0, column=5, padx=5, pady=5)
                e6 = Entry(f4)
                e6.grid(row=0, column=6)
                l7 = Label(f4, text="R2", padx=5, width=8)
                l7.grid(row=0, column=3, padx=20, pady=5)
                e7 = Entry(f4)
                e7.grid(row=0, column=4)
                l8 = Label(f4, text="PCS", padx=5, width=8)
                l8.grid(row=1, column=3, padx=5, pady=5)
                e8 = Entry(f4)
                e8.grid(row=1, column=4)
                l9 = Label(f4, text="MM", padx=5, width=8)
                l9.grid(row=2, column=3, padx=5, pady=5)
                e9 = Entry(f4)
                e9.grid(row=2, column=4)
                l10 = Label(f4, text="KGS", padx=5, width=8)
                l10.grid(row=3, column=3, padx=5, pady=5)
                e10 = Entry(f4)
                e10.grid(row=3, column=4)
                l11 = Label(f4, text="PACKINGNO", padx=5, width=8)
                l11.grid(row=4, column=3, padx=5, pady=5)
                e11 = Entry(f4)
                e11.grid(row=4, column=4)
                l12 = Label(f4, text="RATE", padx=5, width=8)
                l12.grid(row=2, column=5, padx=5, pady=5)
                e12 = Entry(f4)
                e12.grid(row=2, column=6)
                l13 = Label(f4, text="STATUS", padx=5, width=8)
                l13.grid(row=1, column=5, padx=20, pady=5)
                e13 = Entry(f4)
                e13.insert(0, 'INSTOCK')
                e13.grid(row=1, column=6, padx=5, pady=5)
                l14 = Label(f4, text="TOTAL", padx=5, width=8)
                l14.grid(row=3, column=5, padx=5, pady=5)
                e14 = Entry(f4)
                e14.grid(row=3, column=6)

                def keydown(event):
                    ba = e1.get()
                    a = ba.upper()
                    checklistas = []
                    for i in bunlistype:
                        if a in i:
                            checklistas.append(i)
                    e1["values"] = checklistas

                e1.bind("<KeyRelease>", keydown)

                def keyup(event):
                    e1.event_generate("<Down>")

                e1.bind("<KP_Enter>", keyup)
                e1.bind("<Return>", keyup)

                def checkasw():
                    today = date.today()
                    datetodayqs = today.strftime("%Y-%m-%d")
                    try:
                        d1a = []
                        d1a.append(e1.get())
                        d1a.append(e2.get())
                        d1a.append(e3.get())
                        d1a.append(e4.get())
                        d1a.append(e5.get())
                        d1a.append(e6.get())
                        d1a.append(e7.get())
                        d1a.append(e8.get())
                        d1a.append(e9.get())
                        d1a.append(e10.get())
                        d1a.append(e11.get())
                        d1a.append(datetodayqs)
                        d1a.append(e13.get())
                        d1a2 = tuple(d1a)
                        connection = sqlite3.connect("mytables4.db")
                        cursor = connection.cursor()
                        row = d1a2
                        sa = f'''INSERT INTO stockfinal634 VALUES ('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}','{row[9]}','{row[10]}','{row[11]}','{row[12]}')'''
                        cursor.execute(sa)
                        connection.commit()

                        def addtobill(*args):
                            d = d1a
                            nonlocal poplino
                            nonlocal bunlis
                            poplino = 1
                            r4 = []
                            r4.append(d[3])
                            r4.append(d[0])
                            r4.append(d[1] + d[2] + 'x' + d[8] + 'mm')
                            r4.append(d[7])
                            r4.append(d[9])
                            if e12.get() == '':
                                r4.append('0')
                            else:
                                try:
                                    ew = e12.get()
                                    eew = float(ew)
                                    r4.append(int(eew))
                                except Exception as e:
                                    print(e)
                                    r4.append('0')
                                    tsmg.showinfo("info", "sorry wrong input price")

                            if e14.get() == '':
                                r4.append('0')
                            else:
                                try:
                                    ew1 = e14.get()
                                    eew1 = float(ew1)
                                    r4.append(int(eew1))
                                except Exception as e:
                                    r4.append('0')
                                    tsmg.showinfo("info", "sorry wrong input price")
                            r5 = []

                            r5 = r4.copy()
                            r5.insert(0, billno)
                            if r5 not in billbundlelist:
                                treev.insert("", 'end', values=r4)
                                billbundlelist.append(r5)
                                bnolist.append(d[3])
                            else:
                                pass
                            f4.destroy()

                        addtobill()

                        def savebill(event):
                            nonlocal poplino
                            if poplino == 0:
                                tsmg.showinfo("alert", "no entry")
                                createbill(event)

                            else:
                                f2 = Frame(root, background="pink", width=10, height=100, borderwidth=6, relief=SUNKEN)
                                f2.grid(row=0, column=1, sticky="nsew", rowspan=2)

                                today = date.today()
                                datetoday = today.strftime("%Y-%m-%d")
                                bnolist1 = list(set(bnolist))
                                conn = sqlite3.connect('mytables4.db')
                                for i in bnolist1:
                                    conn.execute(f"UPDATE stockfinal634 SET STATUS = 'SOLD' where BUNDLE='{i}'")
                                    conn.commit()
                                conn.close()
                                # now will update bill no
                                connection = sqlite3.connect('mytables4.db')
                                conn = connection.cursor()
                                conn.execute(f"SELECT * FROM billno9 WHERE NAME = '{year}'")
                                temp = conn.fetchall()
                                tempno = int(temp[0][1])
                                tempno = tempno + 1
                                conn.execute(f"UPDATE billno9 SET BILLNO = '{tempno}' where NAME='{year}'")
                                connection.commit()
                                connection = sqlite3.connect("mytables4.db")
                                cursor = connection.cursor()
                                for i in billbundlelist:
                                    i.insert(6, datetoday)
                                    i.append(sel[0])
                                    sa = f'''INSERT INTO billstock5 VALUES ('{i[0]}','{i[9]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}','{i[8]}')'''
                                    cursor.execute(sa)
                                    connection.commit()
                                connection.close()

                                file = open('bill_location.txt', 'r')
                                for e in file:
                                    mainloc = e
                                workbook = xlsxwriter.Workbook(f'{mainloc}{billbundlelist[0][0]}.xlsx')
                                worksheet = workbook.add_worksheet()

                                connection = sqlite3.connect("mytables4.db")
                                crsr = connection.cursor()
                                crsr.execute(f"SELECT * FROM billstock5 WHERE BILLNO = '{billbundlelist[0][0]}'")
                                w = crsr.fetchall()
                                connection.close()
                                d = list(w[0])
                                na = d[1]
                                connection = sqlite3.connect("mytables4.db")
                                crsr = connection.cursor()
                                crsr.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
                                selec = crsr.fetchall()
                                connection.close()
                                selec = list(selec[0])
                                worksheet.set_column('A:A', 10)
                                worksheet.set_column('B:B', 30)
                                worksheet.set_column('C:C', 40)

                                cell_format = workbook.add_format()
                                cell_format.set_bottom(2)
                                cell_format.set_top(2)

                                cell_format2 = workbook.add_format()
                                cell_format2.set_bottom(2)
                                cell_format2.set_top(2)
                                cell_format2.set_right(2)

                                cell_format3 = workbook.add_format()
                                cell_format3.set_bottom(2)
                                cell_format3.set_top(2)
                                cell_format3.set_right(2)
                                cell_format3.set_left(2)

                                cell_leftright = workbook.add_format()
                                cell_leftright.set_right(2)
                                cell_leftright.set_left(2)

                                cell_leftbottom = workbook.add_format()
                                cell_leftbottom.set_bottom(2)
                                cell_leftbottom.set_bold(True)
                                cell_leftbottom.set_left(2)

                                cell_rightbottom = workbook.add_format()
                                cell_rightbottom.set_bottom(2)
                                cell_rightbottom.set_bold(True)
                                cell_rightbottom.set_right(2)

                                cell_bottom = workbook.add_format()
                                cell_bottom.set_bottom(2)

                                cell_bottom1 = workbook.add_format()
                                cell_bottom1.set_bottom(2)
                                cell_bottom1.set_bold(True)

                                cell_right = workbook.add_format()
                                cell_right.set_right(2)

                                cell_left = workbook.add_format()
                                cell_left.set_left(2)

                                cell_righttop = workbook.add_format()
                                cell_righttop.set_right(2)
                                cell_righttop.set_top(2)

                                cell_lefttop = workbook.add_format()
                                cell_lefttop.set_left(2)
                                cell_lefttop.set_top(2)

                                cell_leftrighttop1 = workbook.add_format()
                                cell_leftrighttop1.set_left(2)
                                cell_leftrighttop1.set_top(2)
                                cell_leftrighttop1.set_right(2)
                                cell_leftrighttop1.set_font_size(20)
                                cell_leftrighttop1.set_bold(True)
                                cell_leftrighttop1.set_align('center')

                                cell_leftrighttop = workbook.add_format()
                                cell_leftrighttop.set_left(2)
                                cell_leftrighttop.set_top(2)
                                cell_leftrighttop.set_right(2)
                                cell_leftrighttop.set_bold(True)

                                cell_top = workbook.add_format()
                                cell_top.set_top(2)
                                worksheet.merge_range('A1:G3', "JAI MATA DI", cell_leftrighttop1)

                                worksheet.write(3, 0, "NAME", cell_lefttop)
                                worksheet.write(3, 1, selec[0], cell_righttop)
                                worksheet.write(4, 0, "ADD1", cell_left)
                                worksheet.write(4, 1, selec[1], cell_right)
                                worksheet.write(5, 0, "ADD2", cell_left)
                                worksheet.write(5, 1, selec[2], cell_right)
                                worksheet.write(3, 2, "BILLNO", cell_top)
                                worksheet.write(3, 4, "", cell_top)
                                worksheet.write(3, 5, "", cell_top)
                                worksheet.write(3, 6, "", cell_righttop)
                                worksheet.write(4, 6, "", cell_right)
                                worksheet.write(5, 6, "", cell_right)

                                worksheet.write(3, 3, temp[0][1], cell_top)
                                worksheet.write(4, 2, "MOBILENO")
                                worksheet.write(4, 3, selec[5])
                                worksheet.write(5, 2, "DATE")
                                worksheet.write(5, 3, d[7])

                                num = 6
                                worksheet.write(num, 0, "BUNDLENO", cell_format3)
                                worksheet.write(num, 1, "PRODUCT", cell_format)
                                worksheet.write(num, 2, "SIZE", cell_format2)
                                worksheet.write(num, 3, "PCS", cell_format2)
                                worksheet.write(num, 4, "KG", cell_format2)
                                worksheet.write(num, 5, "RATE", cell_format2)
                                worksheet.write(num, 6, "TOTAL", cell_format2)

                                worksheet.write(7, 0, "", cell_leftright)
                                worksheet.write(7, 2, "", cell_right)
                                worksheet.write(7, 3, "", cell_right)
                                worksheet.write(7, 4, "", cell_right)
                                worksheet.write(7, 5, "", cell_right)
                                worksheet.write(7, 6, "", cell_right)
                                num = 7
                                total = []
                                for i in w:
                                    num += 1
                                    worksheet.write(num, 0, i[2], cell_leftright)
                                    worksheet.write(num, 1, i[3])
                                    worksheet.write(num, 2, i[4], cell_right)
                                    worksheet.write(num, 3, i[5], cell_right)
                                    worksheet.write(num, 4, i[6], cell_right)
                                    worksheet.write(num, 5, i[8], cell_right)
                                    worksheet.write(num, 6, i[9], cell_right)
                                    total.append(int(i[9]))
                                # worksheet.write(num + 1, 0, "", cell_leftright)
                                # worksheet.write(num + 1, 2, "", cell_right)
                                # worksheet.write(num + 1, 3, "", cell_right)
                                # worksheet.write(num + 1, 4, "", cell_right)
                                # worksheet.write(num + 1, 5, "", cell_right)
                                # worksheet.write(num + 1, 6, "", cell_right)
                                # worksheet.write(num + 2, 0, "", cell_lefttop)
                                # worksheet.write(num + 2, 3, "", cell_top)
                                # worksheet.write(num + 2, 4, "", cell_top)
                                # worksheet.write(num + 2, 5, "TOTAL",cell_top)
                                # worksheet.write(num + 2, 1, "BALANCE")
                                # worksheet.write(num + 2,3,selec[7] )
                                # worksheet.write(num + 3, 1, "NEW")
                                # worksheet.write(num + 3, 2, f"+ {str(sum(total))}")
                                # worksheet.write(num + 4, 1, "NEW BALC.")
                                # worksheet.write(num + 4, 2, f"{ float(selec[7])+(total)}")
                                #
                                # worksheet.write(num + 2, 6, str(sum(total)), cell_righttop)
                                # worksheet.write(num + 3, 0, "", cell_left)
                                # worksheet.write(num + 3, 5, "", cell_top)
                                # worksheet.write(num + 3, 6, "", cell_top)
                                # worksheet.write(num + 4, 0, "", cell_left)
                                # worksheet.write(num + 5, 0, "RECIVER SIGNATURE", cell_leftbottom)
                                # worksheet.write(num + 5, 1, "", cell_bottom)
                                # worksheet.write(num + 5, 2, "", cell_bottom)
                                # worksheet.write(num + 5, 3, "", cell_bottom)
                                # worksheet.write(num + 5, 4, "", cell_bottom)
                                # worksheet.write(num + 5, 6, "", cell_rightbottom)
                                #
                                # worksheet.write(num + 5, 2, "", cell_rightbottom)
                                # worksheet.write(num + 3, 6, "", cell_righttop)
                                # worksheet.write(num + 4, 6, "", cell_right)
                                # worksheet.write(num + 5, 5, "   SIGNATURE", cell_bottom1)
                                worksheet.write(num + 1, 0, "", cell_leftright)
                                worksheet.write(num + 1, 2, "", cell_right)
                                worksheet.write(num + 1, 3, "", cell_right)
                                worksheet.write(num + 1, 4, "", cell_right)
                                worksheet.write(num + 1, 5, "", cell_right)
                                worksheet.write(num + 1, 6, "", cell_right)
                                worksheet.write(num + 2, 0, "", cell_lefttop)
                                worksheet.write(num + 2, 1, "", cell_top)
                                worksheet.write(num + 2, 2, "", cell_righttop)
                                worksheet.write(num + 2, 3, "", cell_top)
                                worksheet.write(num + 2, 4, "", cell_top)
                                worksheet.write(num + 2, 5, "TOTAL", cell_top)
                                worksheet.write(num + 2, 6, str(sum(total)), cell_righttop)
                                worksheet.write(num + 3, 0, "", cell_left)
                                worksheet.write(num + 3, 5, "", cell_top)
                                worksheet.write(num + 3, 6, "", cell_top)
                                worksheet.write(num + 4, 0, "", cell_left)
                                worksheet.write(num + 5, 0, "RECIVER SIGNATURE", cell_leftbottom)
                                worksheet.write(num + 5, 1, "", cell_bottom)
                                worksheet.write(num + 5, 2, "", cell_bottom)
                                worksheet.write(num + 5, 3, "", cell_bottom)
                                worksheet.write(num + 5, 4, "", cell_bottom)
                                worksheet.write(num + 5, 6, "", cell_rightbottom)
                                worksheet.write(num + 3, 0, "", cell_left)

                                worksheet.write(num + 3, 1, "", cell_right)
                                worksheet.write(num + 4, 1, "", cell_right)
                                worksheet.write(num + 5, 2, "", cell_rightbottom)
                                worksheet.write(num + 3, 6, "", cell_righttop)
                                worksheet.write(num + 4, 6, "", cell_right)
                                worksheet.write(num + 5, 5, "   SIGNATURE", cell_bottom1)
                                worksheet.write(num + 2, 2,
                                                f"     BALANCE                                   {selec[7]}",
                                                cell_leftrighttop)
                                worksheet.write(num + 3, 2,
                                                f"     NEW                                             + {str(sum(total))}",
                                                cell_leftright)

                                totka = sum(total)

                                connection = sqlite3.connect('mytables4.db')
                                conn = connection.cursor()
                                conn.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
                                sele = conn.fetchall()
                                selecate = list(sele[0])
                                totalW = float(selecate[7])
                                newtotal = totalW + totka
                                worksheet.write(num + 4, 2,
                                                f"     NEW BALC.                                 {newtotal}",
                                                cell_leftrighttop)

                                conn.execute(f"UPDATE custom9 SET TOTAL = '{newtotal}' where NAME='{na}'")
                                workbook.close()

                                connection.commit()
                                connection.close()

                                tsmg.showinfo("Saved", "Your bill has been saved successfully")

                                createbill(event)
                                pass

                        b4 = Button(f2, text="SAVE BILL")
                        b4.pack(pady=150)
                        b4.bind('<Button-1>', savebill)

                        def mixcheck():
                            if (var1.get() == 1):
                                # errorcanoccur
                                e14.delete(0, END)
                                tot = float(e12.get()) * float(e10.get())
                                e14.insert(0, int(tot))
                                e14.focus()
                            else:
                                # errorcanoccur
                                e14.delete(0, END)
                                tot = float(e12.get()) * float(e8.get())
                                e14.insert(0, int(tot))
                                e14.focus()

                        Checkbutton(f4, text="BY KG", variable=var1, command=mixcheck).grid(row=4, column=5, padx=25)

                    except Exception as e:
                        tsmg.showinfo("info", "bundle already exists")
                        print(e)
                    pass

                Button(f4, text="SAVE & ADD", command=checkasw).grid(row=4, column=5, columnspan=2, padx=25)

                pass
            else:
                connection = sqlite3.connect("mytables4.db")
                crsr = connection.cursor()
                crsr.execute(f"SELECT * FROM stockfinal634 WHERE BUNDLE ='{ese.get()}';")
                w = crsr.fetchall()
                if (len(w) == 0):

                    f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
                    f4.grid(row=1, column=2, sticky="nsew")
                    Button(f4, text="NOT FOUND").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')
                    pass

                else:
                    d = list(w[0])
                    connection.close()
                    if (d[12] != "SOLD"):
                        f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
                        f4.grid(row=1, column=2, sticky="nsew")
                        l1 = Label(f4, text="Bundle type", width=8)
                        l1.grid(row=0, column=0, padx=5, pady=5)
                        e1 = Entry(f4)
                        e1.grid(row=0, column=1)
                        l2 = Label(f4, text="DEN SIZE", padx=5, width=8)
                        l2.grid(row=1, column=0, padx=5, pady=5)
                        e2 = Entry(f4)
                        e2.grid(row=1, column=1)
                        l3 = Label(f4, text="THK REMARK", padx=5, width=8)
                        l3.grid(row=2, column=0, padx=5, pady=5)
                        e3 = Entry(f4)
                        e3.grid(row=2, column=1)
                        l4 = Label(f4, text="BUNDLE", padx=5, width=8)
                        l4.grid(row=3, column=0, padx=5, pady=5)
                        e4 = Entry(f4)
                        e4.grid(row=3, column=1)
                        l5 = Label(f4, text="COVER", padx=5, width=8)
                        l5.grid(row=4, column=0, padx=5, pady=5)
                        e5 = Entry(f4)
                        e5.grid(row=4, column=1)
                        l6 = Label(f4, text="STM", padx=5, width=8)
                        l6.grid(row=0, column=5, padx=5, pady=5)
                        e6 = Entry(f4)
                        e6.grid(row=0, column=6)
                        l7 = Label(f4, text="R2", padx=5, width=8)
                        l7.grid(row=0, column=3, padx=20, pady=5)
                        e7 = Entry(f4)
                        e7.grid(row=0, column=4)
                        l8 = Label(f4, text="PCS", padx=5, width=8)
                        l8.grid(row=1, column=3, padx=5, pady=5)
                        e8 = Entry(f4)
                        e8.grid(row=1, column=4)
                        l9 = Label(f4, text="MM", padx=5, width=8)
                        l9.grid(row=2, column=3, padx=5, pady=5)
                        e9 = Entry(f4)
                        e9.grid(row=2, column=4)
                        l10 = Label(f4, text="KGS", padx=5, width=8)
                        l10.grid(row=3, column=3, padx=5, pady=5)
                        e10 = Entry(f4)
                        e10.grid(row=3, column=4)
                        l11 = Label(f4, text="PACKINGNO", padx=5, width=8)
                        l11.grid(row=4, column=3, padx=5, pady=5)
                        e11 = Entry(f4)
                        e11.grid(row=4, column=4)
                        l14 = Label(f4, text="TOTAL", padx=5, width=8)
                        l14.grid(row=3, column=5, padx=5, pady=5)
                        e14 = Entry(f4)
                        e14.grid(row=3, column=6)
                        l12 = Label(f4, text="RATE", padx=5, width=8)
                        l12.grid(row=2, column=5, padx=5, pady=5)
                        e12 = Entry(f4)
                        e12.grid(row=2, column=6)
                        l13 = Label(f4, text="STATUS", padx=5, width=8)
                        l13.grid(row=1, column=5, padx=20, pady=5)
                        e13 = Entry(f4)
                        e13.grid(row=1, column=6, padx=5, pady=5)
                        e1.insert(0, d[0])
                        e2.insert(0, d[1])
                        e3.insert(0, d[2])
                        e4.insert(0, d[3])
                        e5.insert(0, d[4])
                        e6.insert(0, d[5])
                        e7.insert(0, d[6])
                        e8.insert(0, d[7])
                        e9.insert(0, d[8])
                        e10.insert(0, d[9])
                        e11.insert(0, d[10])
                        e13.insert(0, d[12])
                        e12.focus()
                        e12.bind("<KP_Enter>", lambda x: e14.focus())
                        e12.bind("<Return>", lambda x: e14.focus())

                        def addtobill(*args):
                            nonlocal poplino
                            nonlocal bunlis
                            bunlis.remove(d[3])
                            poplino = 1
                            r4 = []
                            r4.append(d[3])
                            r4.append(d[0])
                            r4.append(d[1] + d[2] + 'x' + d[8] + 'mm')
                            r4.append(d[7])
                            r4.append(d[9])
                            if e12.get() == '':
                                r4.append('0')
                            else:
                                try:
                                    ew = e12.get()
                                    eew = float(ew)
                                    r4.append(int(eew))
                                except Exception as e:
                                    print(e)
                                    r4.append('0')
                                    tsmg.showinfo("info", "sorry wrong input price")

                            if e14.get() == '':
                                r4.append('0')
                            else:
                                try:
                                    ew1 = e14.get()
                                    eew1 = float(ew1)
                                    r4.append(int(eew1))
                                except Exception as e:
                                    r4.append('0')
                                    tsmg.showinfo("info", "sorry wrong input price")
                            r5 = []

                            r5 = r4.copy()
                            r5.insert(0, billno)
                            if r5 not in billbundlelist:
                                treev.insert("", 'end', values=r4)
                                billbundlelist.append(r5)
                                bnolist.append(d[3])
                            else:
                                tsmg.showinfo("info", "bundle no already in the bill")
                            f4.destroy()

                        b4 = Button(f2, text="SAVE BILL")
                        b4.pack(pady=150)

                        def savebill(event):
                            nonlocal poplino
                            if poplino == 0:
                                tsmg.showinfo("alert", "no entry")
                                createbill(event)

                            else:
                                f2 = Frame(root, background="pink", width=10, height=100, borderwidth=6, relief=SUNKEN)
                                f2.grid(row=0, column=1, sticky="nsew", rowspan=2)

                                today = date.today()
                                datetoday = today.strftime("%Y-%m-%d")
                                bnolist1 = list(set(bnolist))
                                conn = sqlite3.connect('mytables4.db')
                                for i in bnolist1:
                                    conn.execute(f"UPDATE stockfinal634 SET STATUS = 'SOLD' where BUNDLE='{i}'")
                                    conn.commit()
                                conn.close()
                                # now will update bill no
                                connection = sqlite3.connect('mytables4.db')
                                conn = connection.cursor()
                                conn.execute(f"SELECT * FROM billno9 WHERE NAME = '{year}'")
                                temp = conn.fetchall()
                                tempno = int(temp[0][1])
                                tempno = tempno + 1
                                conn.execute(f"UPDATE billno9 SET BILLNO = '{tempno}' where NAME='{year}'")
                                connection.commit()
                                connection = sqlite3.connect("mytables4.db")
                                cursor = connection.cursor()
                                for i in billbundlelist:
                                    i.insert(6, datetoday)
                                    i.append(sel[0])
                                    sa = f'''INSERT INTO billstock5 VALUES ('{i[0]}','{i[9]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}','{i[8]}')'''
                                    cursor.execute(sa)
                                    connection.commit()
                                connection.close()

                                file = open('bill_location.txt', 'r')
                                for e in file:
                                    mainloc = e
                                workbook = xlsxwriter.Workbook(f'{mainloc}{billbundlelist[0][0]}.xlsx')
                                worksheet = workbook.add_worksheet()

                                connection = sqlite3.connect("mytables4.db")
                                crsr = connection.cursor()
                                crsr.execute(f"SELECT * FROM billstock5 WHERE BILLNO = '{billbundlelist[0][0]}'")
                                w = crsr.fetchall()
                                connection.close()
                                d = list(w[0])
                                na = d[1]
                                connection = sqlite3.connect("mytables4.db")
                                crsr = connection.cursor()
                                crsr.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
                                selec = crsr.fetchall()
                                connection.close()
                                selec = list(selec[0])
                                worksheet.set_column('A:A', 10)
                                worksheet.set_column('B:B', 30)
                                worksheet.set_column('C:C', 40)

                                cell_format = workbook.add_format()
                                cell_format.set_bottom(2)
                                cell_format.set_top(2)

                                cell_format2 = workbook.add_format()
                                cell_format2.set_bottom(2)
                                cell_format2.set_top(2)
                                cell_format2.set_right(2)

                                cell_format3 = workbook.add_format()
                                cell_format3.set_bottom(2)
                                cell_format3.set_top(2)
                                cell_format3.set_right(2)
                                cell_format3.set_left(2)

                                cell_leftright = workbook.add_format()
                                cell_leftright.set_right(2)
                                cell_leftright.set_left(2)

                                cell_leftbottom = workbook.add_format()
                                cell_leftbottom.set_bottom(2)
                                cell_leftbottom.set_bold(True)
                                cell_leftbottom.set_left(2)

                                cell_rightbottom = workbook.add_format()
                                cell_rightbottom.set_bottom(2)
                                cell_rightbottom.set_bold(True)
                                cell_rightbottom.set_right(2)

                                cell_bottom = workbook.add_format()
                                cell_bottom.set_bottom(2)

                                cell_bottom1 = workbook.add_format()
                                cell_bottom1.set_bottom(2)
                                cell_bottom1.set_bold(True)

                                cell_right = workbook.add_format()
                                cell_right.set_right(2)

                                cell_left = workbook.add_format()
                                cell_left.set_left(2)

                                cell_righttop = workbook.add_format()
                                cell_righttop.set_right(2)
                                cell_righttop.set_top(2)

                                cell_lefttop = workbook.add_format()
                                cell_lefttop.set_left(2)
                                cell_lefttop.set_top(2)

                                cell_leftrighttop1 = workbook.add_format()
                                cell_leftrighttop1.set_left(2)
                                cell_leftrighttop1.set_top(2)
                                cell_leftrighttop1.set_right(2)
                                cell_leftrighttop1.set_font_size(20)
                                cell_leftrighttop1.set_bold(True)
                                cell_leftrighttop1.set_align('center')

                                cell_leftrighttop = workbook.add_format()
                                cell_leftrighttop.set_left(2)
                                cell_leftrighttop.set_top(2)
                                cell_leftrighttop.set_right(2)
                                cell_leftrighttop.set_bold(True)

                                cell_top = workbook.add_format()
                                cell_top.set_top(2)
                                worksheet.merge_range('A1:G3', "JAI MATA DI", cell_leftrighttop1)

                                worksheet.write(3, 0, "NAME", cell_lefttop)
                                worksheet.write(3, 1, selec[0], cell_righttop)
                                worksheet.write(4, 0, "ADD1", cell_left)
                                worksheet.write(4, 1, selec[1], cell_right)
                                worksheet.write(5, 0, "ADD2", cell_left)
                                worksheet.write(5, 1, selec[2], cell_right)
                                worksheet.write(3, 2, "BILLNO", cell_top)
                                worksheet.write(3, 4, "", cell_top)
                                worksheet.write(3, 5, "", cell_top)
                                worksheet.write(3, 6, "", cell_righttop)
                                worksheet.write(4, 6, "", cell_right)
                                worksheet.write(5, 6, "", cell_right)

                                worksheet.write(3, 3, temp[0][1], cell_top)
                                worksheet.write(4, 2, "MOBILENO")
                                worksheet.write(4, 3, selec[5])
                                worksheet.write(5, 2, "DATE")
                                worksheet.write(5, 3, d[7])

                                num = 6
                                worksheet.write(num, 0, "BUNDLENO", cell_format3)
                                worksheet.write(num, 1, "PRODUCT", cell_format)
                                worksheet.write(num, 2, "SIZE", cell_format2)
                                worksheet.write(num, 3, "PCS", cell_format2)
                                worksheet.write(num, 4, "KG", cell_format2)
                                worksheet.write(num, 5, "RATE", cell_format2)
                                worksheet.write(num, 6, "TOTAL", cell_format2)

                                worksheet.write(7, 0, "", cell_leftright)
                                worksheet.write(7, 2, "", cell_right)
                                worksheet.write(7, 3, "", cell_right)
                                worksheet.write(7, 4, "", cell_right)
                                worksheet.write(7, 5, "", cell_right)
                                worksheet.write(7, 6, "", cell_right)
                                num = 7
                                total = []
                                for i in w:
                                    num += 1
                                    worksheet.write(num, 0, i[2], cell_leftright)
                                    worksheet.write(num, 1, i[3])
                                    worksheet.write(num, 2, i[4], cell_right)
                                    worksheet.write(num, 3, i[5], cell_right)
                                    worksheet.write(num, 4, i[6], cell_right)
                                    worksheet.write(num, 5, i[8], cell_right)
                                    worksheet.write(num, 6, i[9], cell_right)
                                    total.append(int(i[9]))
                                # worksheet.write(num + 1, 0, "", cell_leftright)
                                # worksheet.write(num + 1, 2, "", cell_right)
                                # worksheet.write(num + 1, 3, "", cell_right)
                                # worksheet.write(num + 1, 4, "", cell_right)
                                # worksheet.write(num + 1, 5, "", cell_right)
                                # worksheet.write(num + 1, 6, "", cell_right)
                                # worksheet.write(num + 2, 0, "", cell_lefttop)
                                # worksheet.write(num + 2, 3, "", cell_top)
                                # worksheet.write(num + 2, 4, "", cell_top)
                                # worksheet.write(num + 2, 5, "TOTAL",cell_top)
                                # worksheet.write(num + 2, 1, "BALANCE")
                                # worksheet.write(num + 2,3,selec[7] )
                                # worksheet.write(num + 3, 1, "NEW")
                                # worksheet.write(num + 3, 2, f"+ {str(sum(total))}")
                                # worksheet.write(num + 4, 1, "NEW BALC.")
                                # worksheet.write(num + 4, 2, f"{ float(selec[7])+(total)}")
                                #
                                # worksheet.write(num + 2, 6, str(sum(total)), cell_righttop)
                                # worksheet.write(num + 3, 0, "", cell_left)
                                # worksheet.write(num + 3, 5, "", cell_top)
                                # worksheet.write(num + 3, 6, "", cell_top)
                                # worksheet.write(num + 4, 0, "", cell_left)
                                # worksheet.write(num + 5, 0, "RECIVER SIGNATURE", cell_leftbottom)
                                # worksheet.write(num + 5, 1, "", cell_bottom)
                                # worksheet.write(num + 5, 2, "", cell_bottom)
                                # worksheet.write(num + 5, 3, "", cell_bottom)
                                # worksheet.write(num + 5, 4, "", cell_bottom)
                                # worksheet.write(num + 5, 6, "", cell_rightbottom)
                                #
                                # worksheet.write(num + 5, 2, "", cell_rightbottom)
                                # worksheet.write(num + 3, 6, "", cell_righttop)
                                # worksheet.write(num + 4, 6, "", cell_right)
                                # worksheet.write(num + 5, 5, "   SIGNATURE", cell_bottom1)
                                worksheet.write(num + 1, 0, "", cell_leftright)
                                worksheet.write(num + 1, 2, "", cell_right)
                                worksheet.write(num + 1, 3, "", cell_right)
                                worksheet.write(num + 1, 4, "", cell_right)
                                worksheet.write(num + 1, 5, "", cell_right)
                                worksheet.write(num + 1, 6, "", cell_right)
                                worksheet.write(num + 2, 0, "", cell_lefttop)
                                worksheet.write(num + 2, 1, "", cell_top)
                                worksheet.write(num + 2, 2, "", cell_righttop)
                                worksheet.write(num + 2, 3, "", cell_top)
                                worksheet.write(num + 2, 4, "", cell_top)
                                worksheet.write(num + 2, 5, "TOTAL", cell_top)
                                worksheet.write(num + 2, 6, str(sum(total)), cell_righttop)
                                worksheet.write(num + 3, 0, "", cell_left)
                                worksheet.write(num + 3, 5, "", cell_top)
                                worksheet.write(num + 3, 6, "", cell_top)
                                worksheet.write(num + 4, 0, "", cell_left)
                                worksheet.write(num + 5, 0, "RECIVER SIGNATURE", cell_leftbottom)
                                worksheet.write(num + 5, 1, "", cell_bottom)
                                worksheet.write(num + 5, 2, "", cell_bottom)
                                worksheet.write(num + 5, 3, "", cell_bottom)
                                worksheet.write(num + 5, 4, "", cell_bottom)
                                worksheet.write(num + 5, 6, "", cell_rightbottom)
                                worksheet.write(num + 3, 0, "", cell_left)

                                worksheet.write(num + 3, 1, "", cell_right)
                                worksheet.write(num + 4, 1, "", cell_right)
                                worksheet.write(num + 5, 2, "", cell_rightbottom)
                                worksheet.write(num + 3, 6, "", cell_righttop)
                                worksheet.write(num + 4, 6, "", cell_right)
                                worksheet.write(num + 5, 5, "   SIGNATURE", cell_bottom1)
                                worksheet.write(num + 2, 2,
                                                f"     BALANCE                                   {selec[7]}",
                                                cell_leftrighttop)
                                worksheet.write(num + 3, 2,
                                                f"     NEW                                             + {str(sum(total))}",
                                                cell_leftright)

                                totka = sum(total)

                                connection = sqlite3.connect('mytables4.db')
                                conn = connection.cursor()
                                conn.execute(f"SELECT * FROM custom9 WHERE NAME = '{na}'")
                                sele = conn.fetchall()
                                selecate = list(sele[0])
                                totalW = float(selecate[7])
                                newtotal = totalW + totka
                                worksheet.write(num + 4, 2,
                                                f"     NEW BALC.                                 {newtotal}",
                                                cell_leftrighttop)

                                conn.execute(f"UPDATE custom9 SET TOTAL = '{newtotal}' where NAME='{na}'")
                                workbook.close()

                                connection.commit()
                                connection.close()

                                tsmg.showinfo("Saved", "Your bill has been saved successfully")

                                createbill(event)
                                pass

                        b4.bind('<Button-1>', savebill)
                        var1 = IntVar()

                        b5 = Button(f2, text="SPLIT BUNDLE")
                        b5.pack(pady=20)

                        def splitbundlewhilecreatingbill(event):
                            t1 = Toplevel()
                            t1.title("Split Bundle")
                            t1.minsize(500, 500)
                            f3 = Frame(t1, background="bisque", borderwidth=6, relief=SUNKEN)
                            f3.grid(row=0, rowspan=2, column=0, sticky="nsew")
                            f4 = Frame(t1, background="pink", borderwidth=6, relief=SUNKEN)
                            f4.grid(row=2, column=0, sticky="nsew")
                            t1.grid_columnconfigure(0)
                            t1.grid_rowconfigure(0, weight=2)
                            t1.grid_rowconfigure(1, weight=2)
                            t1.grid_rowconfigure(2, weight=3)
                            l1 = Label(f4, text="BUNDLE NUMBER YOU WANT TO SPLIT")
                            l1.grid(row=0, column=0, padx=5, pady=5)
                            e = Entry(f4)
                            e.grid(row=0, column=1)
                            e.focus()

                            def checkewq():
                                connection = sqlite3.connect("mytables4.db")
                                crsr = connection.cursor()
                                crsr.execute(f"SELECT * FROM stockfinal634 WHERE BUNDLE ='{e.get()}';")
                                w = crsr.fetchall()
                                if (len(w) == 0):
                                    tsmg.showinfo("Warning", "NOT IN STOCK")
                                    pass

                                else:
                                    d = list(w[0])
                                    connection.close()
                                    if (d[12] == "SOLD"):
                                        tsmg.showinfo("Warning", "ALREADY SOLD")
                                    else:
                                        f4 = Frame(t1, background="pink", width=100, height=15, borderwidth=6,
                                                   relief=SUNKEN)
                                        f4.grid(row=2, column=0, sticky="nsew")
                                        strdat = str(d)
                                        Label(f4, text=strdat).grid()

                                        Label(f3, text=f"{d[3]}A").grid(row=1, column=0, columnspan=2, padx=10)
                                        Label(f3, text=f"{d[3]}B").grid(row=1, column=2, columnspan=2, padx=10)
                                        Label(f3, text="PCS").grid(row=2, column=0, padx=10, pady=15)
                                        e1 = Entry(f3)
                                        e1.grid(row=2, column=1)
                                        Label(f3, text="PCS").grid(row=2, column=2, padx=10, pady=15)
                                        e2 = Entry(f3)
                                        e2.grid(row=2, column=3)
                                        Label(f3, text="KGS").grid(row=3, column=0, padx=10, pady=15)
                                        e3 = Entry(f3)
                                        e3.grid(row=3, column=1)
                                        Label(f3, text="KGS").grid(row=3, column=2, padx=10, pady=15)
                                        e4 = Entry(f3)
                                        e4.grid(row=3, column=3)
                                        e1.focus()
                                        # deleteifwanttodelete
                                        e1.bind("<KP_Enter>", lambda x: e2.focus())
                                        e1.bind("<Return>", lambda x: e2.focus())
                                        e2.bind("<KP_Enter>", lambda x: e3.focus())
                                        e2.bind("<Return>", lambda x: e3.focus())
                                        e3.bind("<KP_Enter>", lambda x: e4.focus())
                                        e3.bind("<Return>", lambda x: e4.focus())

                                        def checkewd(*args):

                                            d1a = d.copy()
                                            d1b = d.copy()
                                            d1a[3] = f"{d[3]}A"
                                            d1b[3] = f"{d[3]}B"
                                            d1a[7] = e1.get()
                                            d1b[7] = e2.get()
                                            d1a[9] = e3.get()
                                            d1b[9] = e4.get()
                                            d1a[12] = "SPLIT"
                                            d1b[12] = "SPLIT"
                                            connection = sqlite3.connect("mytables4.db")
                                            cursor = connection.cursor()
                                            row = d1a
                                            sa = f'''INSERT INTO stockfinal634 VALUES ('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}','{row[9]}','{row[10]}','{row[11]}','{row[12]}')'''
                                            cursor.execute(sa)
                                            connection.commit()
                                            row = d1b
                                            sa = f'''INSERT INTO stockfinal634 VALUES ('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}','{row[9]}','{row[10]}','{row[11]}','{row[12]}')'''
                                            cursor.execute(sa)
                                            connection.commit()
                                            connection.close()
                                            connection = sqlite3.connect("mytables4.db")
                                            crsr = connection.cursor()
                                            crsr.execute(f"DELETE FROM stockfinal634 WHERE BUNDLE ='{e.get()}';")
                                            connection.commit()
                                            connection.close()
                                            tsmg.showinfo("completed", "Bundle Splited")
                                            nonlocal bunlis
                                            bunlis.append(f"{d[3]}A")
                                            bunlis.append(f"{d[3]}B")
                                            bunlis.remove(d[3])

                                            t1.destroy()

                                        e4.bind("<KP_Enter>", checkewd)
                                        e4.bind("<Return>", checkewd)

                                        Button(f3, text="SLPIT", command=checkewd).grid(row=4, column=2, columnspan=2,
                                                                                        padx=25)

                            Button(f4, text="SEARCH", command=checkewq).grid(row=2, column=0, columnspan=2, padx=25)

                        b5.bind('<Button-1>', splitbundlewhilecreatingbill)

                        def mixcheck():
                            if (var1.get() == 1):
                                # errorcanoccur
                                e14.delete(0, END)
                                tot = float(e12.get()) * float(e10.get())
                                e14.insert(0, int(tot))
                                e14.focus()
                            else:
                                # errorcanoccur
                                e14.delete(0, END)
                                tot = float(e12.get()) * float(e8.get())
                                e14.insert(0, int(tot))
                                e14.focus()

                        Checkbutton(f4, text="BY KG", variable=var1, command=mixcheck).grid(row=4, column=5, padx=25)
                        e14.bind("<KP_Enter>", addtobill)
                        e14.bind("<Return>", addtobill)
                        Button(f4, text="ADD TO BILL", command=addtobill).grid(row=4, column=6, padx=25)
                    else:
                        f4 = Frame(root, background="pink", width=80, borderwidth=6, relief=SUNKEN)
                        f4.grid(row=1, column=2, sticky="nsew")

                        Button(f4, text="ALREADY SOLD").grid(row=2, column=3, columnspan=2, padx=250, sticky='nw')

            pass

        Button(f2, text="SEARCH", command=check).pack(pady=10)

    def contin(eve):
        na = drop.get()
        f2.destroy()
        f3.destroy()
        f4.destroy()

        contin12(na)

    pass
    drop.bind("<KeyRelease>", keydown)
    drop.bind("<Return>", keyup)
    drop.focus()
    b1k = Button(f4, text="UPDATE CUSTOMER")
    b1k.pack(pady=30)
    b1k.bind('<Button-1>', contin)

    pass


def createbill(event):
    f3.destroy()
    f4.destroy()
    f2.destroy()
    createbill1(event)


def f2f4destroy1(event):
    t = event.widget.cget("text")
    f2 = Frame(root, background="pink", width=10, height=100, borderwidth=6, relief=SUNKEN)
    f2.grid(row=0, column=1, sticky="nsew", rowspan=2)

    if (t == "ADDED"):
        b1 = Button(f2, text="  BUNDLE ", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>", addbundle)
        b2 = Button(f2, text="PACKING LIST", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>", addpacking)
        b3 = Button(f2, text="IMPORT EXCEL", bg="white")
        b3.pack(pady=50)
        b3.bind("<Button-1>", importfromexcel)
        b4 = Button(f2, text="SPLIT BUN.", bg="white")
        b4.pack(pady=50)
        b4.bind("<Button-1>", splitbundle)
        b5 = Button(f2, text="ADD LOT", bg="white")
        b5.pack(pady=50)
        b5.bind("<Button-1>", addpackingmanual)



    elif (t == "SEARCH"):
        b1 = Button(f2, text="  BY PL ", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>", searchpl)

        b2 = Button(f2, text="BY BUNDLE NO.", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>", searchbundleno)

        b3 = Button(f2, text="  BY NAME ", bg="white")
        b3.pack(pady=50)
        b3.bind("<Button-1>", searchbundlename)

    elif (t == "DELETE"):
        b1 = Button(f2, text="PACKING LIST", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>", deletepacking)

        b2 = Button(f2, text="BUNDLE", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>", deletebundle)

    elif (t == "UPDATE"):
        b1 = Button(f2, text="BUNDLE NO. ", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>", updatebundleno)
        b2 = Button(f2, text="SHOW STOCK", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>", showstock)

    elif (t == "SELL"):
        # even function name not created
        b1 = Button(f2, text="SHOW BILL", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>", showbill)
        b2 = Button(f2, text="CREAT BILL", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>", createbill)
        b3 = Button(f2, text="EXPORT BILL", bg="white")
        b3.pack(pady=50)
        b3.bind("<Button-1>", exportbill)
        b4 = Button(f2, text="UPDATE BILL", bg="white")
        b4.pack(pady=50)
        b4.bind("<Button-1>", updatebill)
        b5 = Button(f2, text="ALL EXCEL", bg="white")
        b5.pack(pady=50)
        b5.bind("<Button-1>", billallexcel)



    elif (t == "CUSTOMER"):
        b1 = Button(f2, text="ADD CUSTO.", bg="white")
        b1.pack(pady=50)
        b1.bind("<Button-1>", addcustomer)

        b2 = Button(f2, text="UPDATE CUST.", bg="white")
        b2.pack(pady=50)
        b2.bind("<Button-1>", updatecustomer)

        b3 = Button(f2, text="SHOW CUSTO.", bg="white")
        b3.pack(pady=50)
        b3.bind("<Button-1>", showcustomer)

        b4 = Button(f2, text="ADD PAY.", bg="white")
        b4.pack(pady=50)
        b4.bind("<Button-1>", addpayment)

        b4 = Button(f2, text="PAYMENTS", bg="white")
        b4.pack(pady=50)
        b4.bind("<Button-1>", showpayments)
    else:
        pass


def f2f4destroy(event):
    f2.destroy()
    f2f4destroy1(event)


try:
    tablename = "stockfinal634"
    createtable(tablename)
    qwe = "credittable"
    createcredittable(qwe)

    sat = "custom9"
    createcustomertable(sat)

    tablename1 = "billstock5"
    createbilltable(tablename1)
    billtablename = "billno9"
    createbillnotable(billtablename)
    connection = sqlite3.connect("mytables4.db")
    cursor = connection.cursor()
    sa = f'''INSERT INTO billno9 VALUES ('2020','1')'''
    cursor.execute(sa)
    connection.commit()
    sa = f'''INSERT INTO billno9 VALUES ('2021','1')'''
    cursor.execute(sa)
    connection.commit()
    sa = f'''INSERT INTO billno9 VALUES ('2022','1')'''
    cursor.execute(sa)
    connection.commit()
    sa = f'''INSERT INTO billno9 VALUES ('2023','1')'''
    cursor.execute(sa)
    connection.commit()
    sa = f'''INSERT INTO billno9 VALUES ('2024','1')'''
    cursor.execute(sa)
    connection.commit()
    sa = f'''INSERT INTO billno9 VALUES ('2025','1')'''
    cursor.execute(sa)
    connection.commit()
    sa = f'''INSERT INTO billno9 VALUES ('2026','1')'''
    cursor.execute(sa)
    connection.commit()
    sa = f'''INSERT INTO billno9 VALUES ('2027','1')'''
    cursor.execute(sa)
    connection.commit()
    sa = f'''INSERT INTO billno9 VALUES ('2028','1')'''
    cursor.execute(sa)
    connection.commit()
    sa = f'''INSERT INTO billno9 VALUES ('2029','1')'''
    cursor.execute(sa)
    connection.commit()
    sa = f'''INSERT INTO billno9 VALUES ('2030','1')'''
    cursor.execute(sa)
    connection.commit()
    tsmg.showinfo("Setup", "Create a folder where you want to save bill")
    chos = tsmg.askquestion("Created", "if created click yes and select it from file")
    if chos == "yes":
        mainloc = filedialog.askdirectory()
        file = open('bill_location.txt', 'w')
        file.write(f"{mainloc}/")
        file.close()
    else:
        quit()

except Exception as e:
    file = open('bill_location.txt', 'r')
    for each in file:
        mainloc = each
    print(e)

    b1 = Button(f1, text="ADDED", bg="white")
    b1.pack(pady=25, padx=10, anchor="w")
    b1.bind("<Button-1>", f2f4destroy)


    def b1b6(event):
        b6.focus()


    b1.bind("<Up>", b1b6)


    def b1b2(event):
        b2.focus()


    b1.bind("<Down>", b1b2)
    b2 = Button(f1, text="SEARCH", bg="white")
    b2.pack(pady=25, padx=10, anchor="w")
    b2.bind("<Button-1>", f2f4destroy)


    def b2b1(event):
        b1.focus()


    b2.bind("<Up>", b2b1)


    def b2b3(event):
        b3.focus()


    b2.bind("<Down>", b2b3)

    b3 = Button(f1, text="DELETE", bg="white")
    b3.pack(pady=25, padx=10, anchor="w")
    b3.bind("<Button-1>", f2f4destroy)


    def b3b2(event):
        b2.focus()


    b3.bind("<Up>", b3b2)


    def b3b4(event):
        b4.focus()


    b3.bind("<Down>", b3b4)

    b4 = Button(f1, text="UPDATE", bg="white")
    b4.pack(pady=25, padx=10, anchor="w")
    b4.bind("<Button-1>", f2f4destroy)


    def b4b3(event):
        b3.focus()


    b4.bind("<Up>", b4b3)


    def b4b5(event):
        b5.focus()


    b4.bind("<Down>", b4b5)

    b5 = Button(f1, text="SELL", bg="white")
    b5.pack(pady=25, padx=15, anchor="w")
    b5.bind("<Button-1>", f2f4destroy)


    def b5b4(event):
        b4.focus()


    b5.bind("<Up>", b5b4)


    def b5b6(event):
        b6.focus()


    b5.bind("<Down>", b5b6)

    b6 = Button(f1, text="CUSTOMER", bg="white")
    b6.pack(pady=25, anchor="w")
    b6.bind("<Button-1>", f2f4destroy)


    def b6b5(event):
        b5.focus()


    b6.bind("<Up>", b6b5)


    def b6b1(event):
        b1.focus()


    b6.bind("<Down>", b6b1)

    b1.bind("<Return>", f2f4destroy)
    b2.bind("<Return>", f2f4destroy)
    b3.bind("<Return>", f2f4destroy)
    b4.bind("<Return>", f2f4destroy)
    b5.bind("<Return>", f2f4destroy)
    b6.bind("<Return>", f2f4destroy)

    b1.focus()


def changedate(event):
    t1 = Toplevel(background="bisque")
    t1.title("DATE")
    t1.minsize(250, 150)

    l1 = Label(t1, text="FROM DATE")
    l1.grid(row=0, column=0, padx=5, pady=5)
    e1 = Entry(t1)
    e1.grid(row=0, column=1)
    e1.focus()
    l2 = Label(t1, text="TO DATE")
    l2.grid(row=1, column=0, padx=5, pady=5)
    e2 = Entry(t1)
    e2.grid(row=1, column=1)
    e1.bind("<KP_Enter>", lambda x: e2.focus())
    e1.bind("<Return>", lambda x: e2.focus())

    def setdate(*eve):
        global from_date
        global to_date
        getfrom = e1.get()
        getto = e2.get()
        if getfrom.count('-') == 2 and getfrom.index('-') == 2 and getfrom.index('-', 3) == 5 and len(getfrom) == 10:
            date1 = getfrom.split('-')
            date1.reverse()
            date2 = "-".join(date1)
            from_date = date2
        elif getfrom.count('-') == 2 and getfrom.index('-') == 4 and getfrom.index('-', 5) == 7 and len(getfrom) == 10:
            date2 = getfrom
            from_date = date2
        else:
            tsmg.showinfo("FORMAT", "Wrong date format")

        if getto.count('-') == 2 and getto.index('-') == 2 and getto.index('-', 3) == 5 and len(getto) == 10:
            date12 = getto.split('-')
            date12.reverse()
            date21 = "-".join(date12)
            to_date = date21
        elif getto.count('-') == 2 and getto.index('-') == 4 and getto.index('-', 5) == 7 and len(getto) == 10:
            date21 = getto
            to_date = date21
        else:
            tsmg.showinfo("FORMAT", "Wrong date format")
        try:
            root.title(f"stock {from_date} TO {to_date}")
        except Exception as e:
            print(e)
        t1.destroy()

    b1 = Button(t1, text="    SET    ", command=setdate)
    b1.grid(row=2, column=0, columnspan=2, pady=20)
    e2.bind("<KP_Enter>", lambda x: b1.focus())
    e2.bind("<Return>", lambda x: b1.focus())
    b1.bind("<KP_Enter>", setdate)

    pass


def changepldate(eve):
    t1 = Toplevel(background="bisque")
    t1.title("DATE")
    t1.minsize(250, 150)

    l1 = Label(t1, text="DATE")
    l1.grid(row=0, column=0, padx=5, pady=5)
    e1 = Entry(t1)
    e1.grid(row=0, column=1)
    e1.focus()
    l2 = Label(t1, text="PL")
    l2.grid(row=1, column=0, padx=5, pady=5)
    e2 = Entry(t1)
    e2.grid(row=1, column=1)
    e1.bind("<KP_Enter>", lambda x: e2.focus())
    e1.bind("<Return>", lambda x: e2.focus())

    def setdate(*eve):
        global datee
        global pll
        getfrom = e1.get()
        pll = e2.get()
        if getfrom.count('-') == 2 and getfrom.index('-') == 2 and getfrom.index('-', 3) == 5 and len(getfrom) == 10:
            date1 = getfrom.split('-')
            date1.reverse()
            date2 = "-".join(date1)
            datee = date2
        elif getfrom.count('-') == 2 and getfrom.index('-') == 4 and getfrom.index('-', 5) == 7 and len(getfrom) == 10:
            date2 = getfrom
            datee = date2
        else:
            tsmg.showinfo("FORMAT", "Wrong date format")

        t1.destroy()

    b1 = Button(t1, text="    SET    ", command=setdate)
    b1.grid(row=2, column=0, columnspan=2, pady=20)
    e2.bind("<KP_Enter>", lambda x: b1.focus())
    e2.bind("<Return>", lambda x: b1.focus())
    b1.bind("<KP_Enter>", setdate)

    pass


root.bind("<F3>", changepldate)
root.bind("<F4>", showmax)
root.bind("<F2>", changedate)
root.mainloop()

