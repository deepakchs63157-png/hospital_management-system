import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox

class hospital():
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management")
        self.root.state('zoomed')  

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        title = tk.Label(self.root, bg=self.clr(220,180,190), text="Hospital Management System",bd=3,relief="groove", font=("Arial",50,"bold"))
        title.pack(side="top", fill="x")

        # input frame

        inFrame = tk.Frame(self.root, bd=4, relief="groove", bg=self.clr(190,180,220))
        inFrame.place(width=self.width/3, height=self.height-180,x=30, y=100 )

        idLbl = tk.Label(inFrame,text="Enter ID:", bg=self.clr(190,180,220),font=("Arial",15,"bold"))
        idLbl.grid(row=0,column=0, padx=20,pady=15)
        self.idIn = tk.Entry(inFrame, width=20, bd=2, font=("Arial",15))
        self.idIn.grid(row=0,column=1,padx=10, pady=15)

        nameLbl = tk.Label(inFrame,text="Enter Name:", bg=self.clr(190,180,220),font=("Arial",15,"bold"))
        nameLbl.grid(row=1, column=0, padx=20, pady=15)
        self.nameIn = tk.Entry(inFrame, width=20, bd=2, font=("Arial",15))
        self.nameIn.grid(row=1, column=1, padx=10, pady=15)

        bgLbl = tk.Label(inFrame,text="B_Group:", bg=self.clr(190,180,220),font=("Arial",15,"bold"))
        bgLbl.grid(row=2, column=0, padx=20, pady=15)
        self.bgIn = tk.Entry(inFrame, width=20, bd=2, font=("Arial",15))
        self.bgIn.grid(row=2, column=1, padx=10, pady=15)

        desLbl = tk.Label(inFrame,text="Desease:", bg=self.clr(190,180,220),font=("Arial",15,"bold"))
        desLbl.grid(row=3, column=0, padx=20, pady=15)
        self.desIn = tk.Entry(inFrame, width=20, bd=2, font=("Arial",15))
        self.desIn.grid(row=3, column=1, padx=10, pady=15)

        hpLbl = tk.Label(inFrame,text="Health Points:", bg=self.clr(190,180,220),font=("Arial",15,"bold"))
        hpLbl.grid(row=4, column=0,padx=20, pady=15)
        self.hpIn = tk.Entry(inFrame, width=20, bd=2, font=("Arial",15))
        self.hpIn.grid(row=4, column=1, padx=10, pady=15)

        medLbl = tk.Label(inFrame,text="Medication:", bg=self.clr(190,180,220),font=("Arial",15,"bold"))
        medLbl.grid(row=5, column=0, padx=20, pady=15)
        self.medIn = tk.Entry(inFrame, width=20, bd=2, font=("Arial",15))
        self.medIn.grid(row=5,column=1, padx=10, pady=15)

        addrLbl = tk.Label(inFrame,text="Address:", bg=self.clr(190,180,220),font=("Arial",15,"bold"))
        addrLbl.grid(row=6, column=0, padx=20, pady=15)
        self.addrIn = tk.Entry(inFrame, width=20, bd=2, font=("Arial",15))
        self.addrIn.grid(row=6, column=1, padx=10, pady=15)

        okBtn = tk.Button(inFrame, text="Admit",command=self.insertFun, bd=2, relief="raised", bg="gray", font=("Arial",20,"bold"), width=20)
        okBtn.grid(padx=30, pady=25,columnspan=2)

        # detail Frame

        self.detFrame = tk.Frame(self.root, bd=4, relief="groove",bg=self.clr(190,220,180))
        self.detFrame.place(width=self.width/2+110, height=self.height-180, x=self.width/3+60,y=100)
   

        pIdLbl = tk.Label(self.detFrame, text="Patient ID:", bg=self.clr(190,220,180), font=("Arial",15))
        pIdLbl.grid(row=0, column=0, padx=10, pady=15)
        self.pIdIn = tk.Entry(self.detFrame, bd=1, width=12, font=("Arial",15))
        self.pIdIn.grid(row=0, column=1, padx=7, pady=15)

        medicBtn = tk.Button(self.detFrame,command=self.medicsFun, text="Medication",width=10,font=("Arial",15,"bold"), bd=2, relief="raised")
        medicBtn.grid(row=0, column=2,padx=8, pady=15)

        hpBtn = tk.Button(self.detFrame,command=self.hPointFun, text="H_Point",width=10,font=("Arial",15,"bold"), bd=2, relief="raised")
        hpBtn.grid(row=0, column=3,padx=8, pady=15)

        disBtn = tk.Button(self.detFrame,command=self.disFun, text="Discharge",width=10,font=("Arial",15,"bold"), bd=2, relief="raised")
        disBtn.grid(row=0, column=4,padx=8, pady=15)



        updateBtn = tk.Button(self.detFrame, command=self.updateWindow, text="Update", width=10, font=("Arial",15,"bold"), bd=2, relief="raised")
        updateBtn.grid(row=0, column=5, padx=8, pady=15)


        
        self.tabFun()
        self.loadAllFun()   

    def tabFun(self):
        self.tabFrame = tk.Frame(self.detFrame, bd=3, relief="ridge", bg="cyan")
        self.tabFrame.place(width=self.width/2+80, height=self.height-280, x=12, y=80)

        x_scrol=tk.Scrollbar(self.tabFrame, orient="horizontal")
        x_scrol.pack(side="bottom", fill="x")

        y_scrol = tk.Scrollbar(self.tabFrame, orient="vertical")
        y_scrol.pack(side="right", fill="y")

        searchFrame = tk.Frame(self.tabFrame, bg="cyan")
        searchFrame.pack(fill="x", pady=5)
    
        tk.Label(searchFrame, text="Search Patient:", bg="cyan", font=("Arial", 12, "bold")).pack(side="left", padx=10)
        self.searchIn = tk.Entry(searchFrame, width=25, font=("Arial", 12))
        self.searchIn.pack(side="left", padx=10)
        tk.Button(searchFrame, text="Search", font=("Arial", 12, "bold"), command=self.searchPatient).pack(side="left", padx=10)
        self.searchIn.bind("<KeyRelease>", lambda e: self.searchPatient())


        self.table = ttk.Treeview(
    self.tabFrame,
    columns=("id","name","bGroup","desease","hPoint","medi","addr"),
    xscrollcommand=x_scrol.set,
    yscrollcommand=y_scrol.set
)
        self.table.pack(fill="both", expand=1)

        x_scrol.config(command=self.table.xview)
        y_scrol.config(command=self.table.yview)



        

    

        x_scrol.config(command=self.table.xview)
        y_scrol.config(command=self.table.yview)

        self.table.heading("id", text="Patient_Id")
        self.table.heading("name", text="Patient Name")
        self.table.heading("bGroup", text="B_Group")
        self.table.heading("desease", text="Desease")
        self.table.heading("hPoint", text="Points")
        self.table.heading("medi", text="Medication")
        self.table.heading("addr", text="Patient Address")
        self.table["show"]= "headings"

        self.table.column("id", width=100)
        self.table.column("name", width=150)
        self.table.column("bGroup", width=100)
        self.table.column("desease", width=120)
        self.table.column("hPoint", width=60)
        self.table.column("medi", width=150)
        self.table.column("addr", width=200)

        self.table.pack(fill="both", expand=1)

    def clr(self, r,g,b):
        return f"#{r:02x}{g:02x}{b:02x}"
    
    


    def searchPatient(self):
     try:
        keyword = self.searchIn.get().strip()  # Get search text
        self.dbFun()  # Connect to database

        if keyword:  # If user typed something, filter
            query = """
            SELECT * FROM hospital
            WHERE name LIKE %s OR b_group LIKE %s OR desease LIKE %s OR addr LIKE %s
            """
            search_term = f"%{keyword}%"
            self.cur.execute(query, (search_term, search_term, search_term, search_term))
            rows = self.cur.fetchall()
            if not rows:
                messagebox.showinfo("No Results", f"No patient found matching '{keyword}'")
        else:  # If search bar empty, show all patients
            self.cur.execute("SELECT * FROM hospital")
            rows = self.cur.fetchall()

        # Clear previous results
        self.table.delete(*self.table.get_children())

        # Insert rows
        for r in rows:
            self.table.insert('', tk.END, values=r)

        self.con.close()

     except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")


    
     
    
    def insertFun(self):
        """Insert a new patient into the database"""
        try:
            p_id = int(self.idIn.get())
            name = self.nameIn.get().strip()
            bGroup = self.bgIn.get().strip()
            desease = self.desIn.get().strip()
            point = int(self.hpIn.get())
            medics = self.medIn.get().strip()
            addr = self.addrIn.get().strip()

            if not (p_id and name and bGroup and desease and point and medics and addr):
                messagebox.showerror("Error", "Fill all input fields!")
                return

            self.dbFun()  # connect to database

            # Check if patient ID already exists
            self.cur.execute("SELECT * FROM hospital WHERE id=%s", (p_id,))
            existing = self.cur.fetchone()
            if existing:
                messagebox.showerror("Error", f"Patient ID {p_id} already exists!")
                self.con.close()
                return

            # Insert new patient
            query = """INSERT INTO hospital 
                       (id, name, b_group, desease, h_points, medication, addr) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            self.cur.execute(query, (p_id, name, bGroup, desease, point, medics, addr))
            self.con.commit()
            self.con.close()

            self.loadAllFun()  # Refresh table
            self.clearFun()    # Clear input fields

            messagebox.showinfo("Success", f"Patient {name} is admitted!")

        except ValueError:
            messagebox.showerror("Error", "ID and Health Points must be numeric")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

            


    def dbFun(self):
        self.con = pymysql.connect(host="localhost", user="root", passwd="Deepak@123", database="rec")
        self.cur = self.con.cursor()

    def clearFun(self):
        self.idIn.delete(0,tk.END)
        self.nameIn.delete(0,tk.END)
        self.bgIn.delete(0,tk.END)
        self.desIn.delete(0,tk.END)
        self.hpIn.delete(0,tk.END)
        self.medIn.delete(0,tk.END)
        self.addrIn.delete(0,tk.END)

    def medicsFun(self):
        pId = int(self.pIdIn.get())
        if pId:
            try:
                self.dbFun()
                query = f"select * from hospital where id=%s"
                self.cur.execute(query,pId)
                data = self.cur.fetchone()
            
                self.table.delete(*self.table.get_children())
                self.table.insert('',tk.END,values=data)


            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")
        else:
            tk.messagebox.showerror("Error","Must Enter Patient ID")

    def hPointFun(self): 
        # Create a new window instead of Frame
        self.pointWin = tk.Toplevel(self.root)
        self.pointWin.title("Update Health Points")
        self.pointWin.geometry("400x200")
        self.pointWin.config(bg="light gray")

        lbl = tk.Label(self.pointWin, text="Enter Point:", bg="light gray", font=("Arial",15,"bold"))
        lbl.grid(row=0, column=0, padx=20, pady=20)

        self.pointIn = tk.Entry(self.pointWin, width=17, bd=2,font=("Arial",15,"bold"))
        self.pointIn.grid(row=0, column=1, padx=10, pady=20)

        okBtn = tk.Button(self.pointWin,command=self.addPoint, text="Add Point", bd=3, relief="raised",font=("Arial",15,"bold"),width=12)
        okBtn.grid(row=1, column=0, padx=20, pady=20)

        exitBtn = tk.Button(self.pointWin, text="Exit", bd=3, relief="raised", bg="gray", font=("Arial",15,"bold"),width=12, command=self.pointWin.destroy)
        exitBtn.grid(row=1, column=1, padx=20, pady=20)


    def addPoint(self):
        pId = int(self.pIdIn.get())
        point = int(self.pointIn.get())
        if pId:
            try:
                self.dbFun()
                query = f"select h_points from hospital where id=%s"
                self.cur.execute(query,pId)
                val = self.cur.fetchone()

                newPoint = val[0]+point
                query2 = f"update hospital set h_points=%s where id=%s"
                self.cur.execute(query2,(newPoint,pId))
                self.con.commit()
                
                self.table.delete(*self.table.get_children())
                self.cur.execute("select * from hospital where id=%s", pId)
                row = self.cur.fetchone()
                self.table.insert('',tk.END,values=row)
                tk.messagebox.showinfo("Success",f"Health Position is updated for patien {pId}") 
                self.con.close()
                self.pointFrame.destroy()                                         
                              

            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")

        else:
            tk.messagebox.showerror("Error","Must Enter Patient ID")
    def disFun(self):
        """Handles patient discharge: shows total bill, paid status, and allows view/update"""
        pId = self.pIdIn.get().strip()
        if not pId:
            messagebox.showerror("Error", "Enter Patient ID to discharge")
            return

        try:
            pId = int(pId)
            self.dbFun()

            # --- Check if patient exists ---
            self.cur.execute("SELECT * FROM hospital WHERE id=%s", (pId,))
            patient = self.cur.fetchone()
            if not patient:
                messagebox.showerror("Error", "Patient not found!")
                self.con.close()
                return

            # --- Check if bill exists ---
            self.cur.execute(
                "SELECT treatment_cost, medication_cost, room_rent, doctor_fee, other_charges, total_bill, paid "
                "FROM bill WHERE patient_id=%s",
                (pId,)
            )
            bill = self.cur.fetchone()
            self.con.close()

            if not bill:
                # No bill → show save bill form (only once)
                self.openBillWindow(pId, save_only=True)
                return

            # --- Bill exists, show total and paid status ---
            total_bill = bill[5]  # total_bill column
            paid_status = bill[6]  # paid column
            msg = f"Total Bill for Patient {pId}: ₹{total_bill}\nPaid: {paid_status.upper()}"

            # Ask if want to mark paid now
            response = messagebox.askquestion("Bill Info", msg + "\n\nMark as paid now?")
            if response == "yes" and paid_status.lower() != "yes":
                self.markPaidAndDischarge(pId)
            elif paid_status.lower() == "yes":
                # Already paid → allow discharge
                self.markPaidAndDischarge(pId)
            else:
                # Not paid → offer to view/update bill
                view = messagebox.askyesno("View Bill", "Do you want to view/update the bill?")
                if view:
                    self.openBillWindow(pId, save_only=False, view_only=True)

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def openBillWindow(self, pId, save_only=False, view_only=False):
        """Create or view/update bill inside hospital class"""
        self.billWin = tk.Toplevel(self.root)
        self.billWin.title(f"Billing for Patient {pId}")
        self.billWin.geometry("450x500")
        self.billWin.config(bg="#f7f7f7")

        tk.Label(self.billWin, text=f"Patient ID: {pId}", bg="#f7f7f7",
                 font=("Arial", 14, "bold")).pack(pady=10)

        labels = ["Treatment Cost", "Medication Cost", "Room Rent", "Doctor Fee", "Other Charges"]
        self.billEntries = {}
        for lbl in labels:
            tk.Label(self.billWin, text=f"{lbl} (₹):", bg="#f7f7f7", font=("Arial", 12)).pack(pady=5)
            entry = tk.Entry(self.billWin, width=20, font=("Arial", 12))
            entry.pack(pady=2)
            self.billEntries[lbl] = entry

        # Load existing bill data if not first save
        if not save_only:
            try:
                self.dbFun()
                self.cur.execute(
                    "SELECT treatment_cost, medication_cost, room_rent, doctor_fee, other_charges, total_bill, paid FROM bill WHERE patient_id=%s",
                    (pId,)
                )
                data = self.cur.fetchone()
                self.con.close()
                if data:
                    for i, lbl in enumerate(labels):
                        self.billEntries[lbl].insert(0, str(data[i]))
                    tk.Label(self.billWin, text=f"Total Bill: ₹{data[5]}", bg="#f7f7f7",
                             font=("Arial", 13, "bold")).pack(pady=5)
                    tk.Label(self.billWin, text=f"Paid Status: {data[6]}", bg="#f7f7f7",
                             font=("Arial", 12, "bold")).pack(pady=5)
            except Exception as e:
                messagebox.showerror("Error", f"Error loading bill: {e}")

        # Save button only for first time
        if save_only:
            tk.Button(
                self.billWin, text="Save Bill", bg="gray", font=("Arial", 13, "bold"),
                command=lambda: self.saveBill(pId, save_only=True)
            ).pack(pady=10)
        elif view_only:
            # Update button when viewing existing bill
            tk.Button(
                self.billWin, text="Update Bill", bg="blue", font=("Arial", 13, "bold"),
                command=lambda: self.saveBill(pId, save_only=False)
            ).pack(pady=10)

        tk.Button(
            self.billWin, text="Exit", bg="red", font=("Arial", 13, "bold"),
            command=self.billWin.destroy
        ).pack(pady=5)

    def saveBill(self, pId, save_only=False):
        """Save or update bill inside hospital class"""
        try:
            treatment = float(self.billEntries["Treatment Cost"].get() or 0)
            medication = float(self.billEntries["Medication Cost"].get() or 0)
            room = float(self.billEntries["Room Rent"].get() or 0)
            doctor = float(self.billEntries["Doctor Fee"].get() or 0)
            other = float(self.billEntries["Other Charges"].get() or 0)
            total = treatment + medication + room + doctor + other

            self.dbFun()
            self.cur.execute("SELECT * FROM bill WHERE patient_id=%s", (pId,))
            exists = self.cur.fetchone()

            if exists:
                if save_only:
                    messagebox.showwarning("Warning", "Bill already exists! Cannot save again.")
                else:
                    self.cur.execute(
                        "UPDATE bill SET treatment_cost=%s, medication_cost=%s, room_rent=%s, doctor_fee=%s, other_charges=%s, total_bill=%s WHERE patient_id=%s",
                        (treatment, medication, room, doctor, other, total, pId)
                    )
                    messagebox.showinfo("Updated", f"Bill updated! Total: ₹{total}")
            else:
                self.cur.execute(
                    "INSERT INTO bill (patient_id, treatment_cost, medication_cost, room_rent, doctor_fee, other_charges, total_bill, paid) "
                    "VALUES (%s,%s,%s,%s,%s,%s,%s,'No')",
                    (pId, treatment, medication, room, doctor, other, total)
                )
                messagebox.showinfo("Saved", f"Bill saved! Total: ₹{total}")

            self.con.commit()
            self.con.close()
            self.billWin.destroy()
        except ValueError:
            messagebox.showerror("Error", "Enter valid numeric values for all charges")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def markPaidAndDischarge(self, pId):
        """Mark bill as paid and discharge patient safely"""
        try:
            self.dbFun()

            # --- Check if bill exists ---
            self.cur.execute("SELECT paid, total_bill FROM bill WHERE patient_id=%s", (pId,))
            bill_data = self.cur.fetchone()
            if not bill_data:
                messagebox.showerror("Error", "Bill not found! Cannot discharge.")
                self.con.close()
                return

            paid_status, total_bill = bill_data

            # --- If not paid, mark as paid ---
            if paid_status.lower() != "yes":
                self.cur.execute("UPDATE bill SET paid='Yes' WHERE patient_id=%s", (pId,))
                messagebox.showinfo("Payment Done", f"Bill of ₹{total_bill} marked as PAID.")

            # --- Delete bill first to satisfy foreign key ---
            self.cur.execute("DELETE FROM bill WHERE patient_id=%s", (pId,))
            # --- Delete patient ---
            self.cur.execute("DELETE FROM hospital WHERE id=%s", (pId,))
            self.con.commit()

            messagebox.showinfo("Discharged", f"Patient {pId} discharged successfully!")
            self.con.close()

            # Refresh GUI table/list
            self.loadAllFun()

            # Close bill window if open
            if hasattr(self, 'billWin') and self.billWin.winfo_exists():
                self.billWin.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

                # 🩹 Load All Records
    def loadAllFun(self):
        self.dbFun()
        self.cur.execute("SELECT * FROM hospital")
        rows = self.cur.fetchall()
        self.table.delete(*self.table.get_children())
        for r in rows:
            self.table.insert('', tk.END, values=r)
        self.con.close()

            # 🩹 Update Patient Details
    def updateWindow(self):
        # Get Patient ID and validate
        pId = self.pIdIn.get()
        if not pId:
            messagebox.showerror("Error", "Enter Patient ID to update")
            return

        try:
            pId = int(pId)  # Convert ID to integer
            self.dbFun()
            self.cur.execute("SELECT * FROM hospital WHERE id=%s", (pId,))
            data = self.cur.fetchone()
            if not data:
                messagebox.showerror("Error", "Patient not found!")
                self.con.close()
                return

            # Create popup window
            upd = tk.Toplevel(self.root)
            upd.title("Update Patient Details")
            upd.geometry("500x500")
            upd.config(bg="#f7e9c8")

            fields = ["Name", "B_Group", "Desease", "H_Points", "Medication", "Address"]
            entries = []

            for i, field in enumerate(fields):
                tk.Label(upd, text=field + ":", bg="#f7e9c8", font=("Arial", 15, "bold")).grid(row=i, column=0, padx=20, pady=10)
                e = tk.Entry(upd, width=25, font=("Arial", 15))
                e.grid(row=i, column=1, padx=10, pady=10)
                e.insert(0, data[i + 1])  # Skip ID at index 0
                entries.append(e)

            # Function to save updates
            def save_update():
                try:
                    vals = [
                        entries[0].get(),        # Name
                        entries[1].get(),        # B_Group
                        entries[2].get(),        # Desease
                        int(entries[3].get()),   # H_Points
                        entries[4].get(),        # Medication
                        entries[5].get()         # Address
                    ]
                    query = """UPDATE hospital 
                               SET name=%s, b_group=%s, desease=%s, h_points=%s, medication=%s, addr=%s 
                               WHERE id=%s"""
                    self.cur.execute(query, (*vals, pId))
                    self.con.commit()
                    self.loadAllFun()  # Refresh table
                    messagebox.showinfo("Success", "Patient details updated successfully")
                    upd.destroy()
                   
                except ValueError:
                    messagebox.showerror("Error", "H_Points must be a number")
                except Exception as e:
                    messagebox.showerror("Error", f"Error: {e}")

            # Buttons
            tk.Button(upd, text="Save Changes", bg="gray", font=("Arial", 15, "bold"), command=save_update)\
                .grid(row=7, column=0, columnspan=2, pady=30)
            tk.Button(upd, text="Exit", bg="red", font=("Arial", 15, "bold"), command=upd.destroy)\
                .grid(row=8, column=0, columnspan=2, pady=10)

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")






  


# 🧑‍💼 Admin Login Window
def login_window():
    login = tk.Tk()
    login.title("Admin Login")
    login.geometry("400x300")
    login.config(bg="#cfe2f3")

    tk.Label(login, text="Admin Login", bg="#cfe2f3", font=("Arial", 25, "bold")).pack(pady=20)
    tk.Label(login, text="Username:", bg="#cfe2f3", font=("Arial", 15)).pack(pady=5)
    username = tk.Entry(login, width=25, font=("Arial", 15))
    username.pack(pady=5)
    tk.Label(login, text="Password:", bg="#cfe2f3", font=("Arial", 15)).pack(pady=5)
    password = tk.Entry(login, width=25, show="*", font=("Arial", 15))
    password.pack(pady=5)

    def verify_login():
        if username.get() == "payal mahajan" and password.get() == "payal@123":
            login.destroy()
            main_window()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    tk.Button(login, text="Login", bg="gray", font=("Arial", 15, "bold"), command=verify_login).pack(pady=20)
    login.mainloop()


def main_window():
    root = tk.Tk()
    obj = hospital(root)
    root.mainloop()


# ✅ Start from login page instead of directly opening app
login_window()


