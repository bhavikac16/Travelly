import tkinter as tk
from tkinter.ttk import Combobox
from myfile import L

import webbrowser

#creating window
root = tk.Tk()

root.title("Travelly")     #add name of the application
root.geometry("1920x1080")


    
frame1=tk.Frame(root,bd=0,bg="red")
frame1.place(x=400, y=30, height= 70, width=700)
lab1=tk.Label(frame1,text="TRAVELLY \n Find out the best hotel for you !!!", height=60,width=600,font=("Segoe UI Black",20))
lab1.pack()

name_lab=tk.Label(root, text="Search hotel by name:",font=("Courier New CYR",9),height=2,width=20, bg="#FF8000")
name_lab.place(x=30,y=150)

name_var=tk.StringVar()   ###
name_entry=tk.Entry(root,textvariable=name_var,bg="#FFFFCC")
name_entry.place(x=180,y=150,height=35, width= 300)
  

price_lab=tk.Label(root,text="Sort by Price",font=("Courier New CYR",9),height=2, width=10,bg="#FF8000")
price_lab.place(x=500,y=150)

frame2=tk.Frame(root,bd=1,bg="blue")
frame2.place(x=580, y=158, width=100)

v=["<3000","<6000","<8000","<10000","<12000"]
price_var=tk.StringVar()            ###
price_combo=Combobox(frame2,values=v,height=40,textvariable=price_var)
price_combo.set("<Select>")
price_combo.pack()
  
rating_lab=tk.Label(root,text="Sort by rating",font=("Courier New CYR",9),height=2,width=10,bg="#FF8000")
rating_lab.place(x=700,y=150)

frame3=tk.Frame(root,bd=1,bg="blue")
frame3.place(x=780, y=158, width=100)

v=list(range(1,6))
rating_var=tk.IntVar()   ###
rating_combo=Combobox(frame3,values=v,height=40,textvariable=rating_var)
rating_combo.set("<Select>")
rating_combo.pack()



loc_lab=tk.Label(root,text="Location",font=("Courier New CYR",9),height=2,width=8,bg="#FF8000")
loc_lab.place(x=920,y=150)

frame4=tk.Frame(root,bd=1,bg="blue")
frame4.place(x=1000,y=158,width=110)

v=["Bangalore","Delhi","Goa","Jammu & Kashmir","Mumbai","Udaipur"]
loc_var=tk.StringVar()  ###
loc_combo=Combobox(frame4,values=v,height=40,width=25,textvariable=loc_var)
loc_combo.set("<Select>")
loc_combo.pack()


guest_lab=tk.Label(root,text="Number of Guests",font=("Courier New CYR",9),height=2, width=15,bg="#FF8000")
guest_lab.place(x=50,y=200)

guest_var=tk.IntVar()    ###
guest_entry=tk.Entry(root,textvariable=guest_var,bg="#FFFFCC")
guest_entry.place(x=180,y=200,height=35,width=50)

more_filter=tk.Label(root,text="Popular filters",font=("Courier New CYR",9),height=2,width=15,bg="#FF8000")
more_filter.place(x=290, y=200)

frame5=tk.Frame(root,bd=1,bg="blue")
frame5.place(x=410,y=208)

v=["1. Free Breakfast","2. Car Park","3. Free Cancellation","4. Spa"]
filter_var=tk.StringVar()   ###
filter_combo=Combobox(frame5,values=v,height=40,textvariable=filter_var,font=("Courier New CYR",9))
filter_combo.pack()




main_frame=tk.Frame(root,bd=1,bg="light blue")
main_frame.place(x=50,y=300,height=480,width=1410)





def apply_filter():

    #main_frame.destroy()
    

    n=name_entry.get()   #
    price=price_var.get()
    p=eval(price[1:])   #
    r=rating_var.get()  #
    l=loc_var.get()   #
    g=guest_var.get()  #
    hello=filter_var.get()
    f=eval(hello[0])   #

    main_list=[]

    #main_frame=tk.Frame(root,bd=1,bg="light blue")
    #main_frame.place(x=50,y=300,height=480,width=1410)
    
                    
                
    

    
    
    

    def display(root,l):
        
        # ************************
        # Scrollable Frame Class
        # ************************
        class ScrollFrame(tk.Frame):
            def __init__(self, parent):
                super().__init__(parent) # create a frame (self)

                self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")          #place canvas on self
                self.viewPort = tk.Frame(self.canvas, background="#ffffff")                    #place a frame on the canvas, this frame will hold the child widgets 
                self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview) #place a scrollbar on self 
                self.canvas.configure(yscrollcommand=self.vsb.set)                          #attach scrollbar action to scroll of canvas

                self.vsb.pack(side="right", fill="y")                                       #pack scrollbar to right of self
                self.canvas.pack(side="left", fill="both", expand=True)                     #pack canvas to left of self and expand to fil
                self.canvas_window = self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",            #add view port frame to canvas
                                          tags="self.viewPort")

                self.viewPort.bind("<Configure>", self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.
                self.canvas.bind("<Configure>", self.onCanvasConfigure)                       #bind an event whenever the size of the viewPort frame changes.

                self.onFrameConfigure(None)                                                 #perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize

            def onFrameConfigure(self, event):                                              
                '''Reset the scroll region to encompass the inner frame'''
                self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.

            def onCanvasConfigure(self, event):
                '''Reset the canvas window to encompass inner frame when required'''
                canvas_width = event.width
                self.canvas.itemconfig(self.canvas_window, width = canvas_width)            #whenever the size of the canvas changes alter the window region respectively.


        # ********************************
        # Example usage of the above class
        # ********************************

        class Example(tk.Frame):
            def __init__(self, root):

                tk.Frame.__init__(self, root)
                self.scrollFrame = ScrollFrame(self) # add a new scrollable frame.
                
                # Now add some controls to the scrollframe. 
                # NOTE: the child controls are added to the view port (scrollFrame.viewPort, NOT scrollframe itself)
                for row in range(len(l)):
                    a = row
                    tk.Label(self.scrollFrame.viewPort, text=(l[a][5]+'\n\nPRICE (per night) : Rs'+str(l[a][6])+'\t\tRating (out of 5): '+str(l[a][7])+'\nLocation: '+l[a][8]+'\t\tGuests (per room):'+str(l[a][9])) ,font=("Segoe UI Black",10), borderwidth="1", 
                             bg="#99FF33",relief="solid",width=150,height=5).grid(row=row, column=0)
                    t="this is the second column for row %s" %row
                    tk.Button(self.scrollFrame.viewPort, text="Check \n Website",font=("Segoe UI Black",10),bg="#FFFF00", command=lambda: webbrowser.open(l[a][10]),width=10,height=5).grid(row=row, column=1)

                # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
                self.scrollFrame.pack(side="top", fill="both", expand=True)
        
     
        if __name__ == "__main__":
           #root=tk.Tk()
           Example(root).pack(side="top", fill="both", expand=True)
           


    for i in L:
        if n=="":
            if hello=="":
                if i[6]<=p and i[7]>=r and i[8]==l and i[9]>=g:
                    main_list.append(i)
            else:
                if i[6]<=p and i[7]>=r and i[8]==l and i[9]>=g and i[f]=="Yes":
                    main_list.append(i)
        else:
            if hello=="":
                if i[6]<=p and i[7]>=r and i[8]==l and i[9]>=g and i[5]==n:
                    main_list.append(i)
            else:
                if i[6]<=p and i[7]>=r and i[8]==l and i[9]>=g and i[5]==n and i[f]=="Yes":
                    main_list.append(i)

    display(main_frame,main_list)
    #main_frame.destroy()
    



apply_filter=tk.Button(root,text="Apply Filters",height=2,width=30,command=apply_filter,bg="#00CC00")
apply_filter.place(x=800,y=200)



root.mainloop()













