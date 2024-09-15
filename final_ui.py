import numpy as np
from tkinter import *
from PIL import Image,ImageTk

import pickle
log=pickle.load(open('models/LogisticRegression.pkl','rb'))



root = Tk()
root.title('Loan Approval prediction')
root.geometry('1500x750')
img=Image.open("bag.jpg")
img=img.resize((1500,750))
bg= ImageTk.PhotoImage(img)
lbl=Label(root,image = bg)
lbl.place(x=0,y=0)

label = Label( root, text = "Loan Approval Prediciton",font=('times',24,'bold underline'),bd=20,bg="black",fg="white")
label.place(x=400,y=10)



label_1 = Label(root, text =' Gender',font=("Helvetica", 16),bg="black",fg="white")
label_1.place(x=100,y=100)
   
Entry_1= Entry(root,bg="black",fg="white",font=("Helvetica", 16))
Entry_1.place(x=400,y=100)

label_11 = Label(root, text =' (male=1,female=0)',font=("Helvetica", 16),bg="black",fg="white")
label_11.place(x=700,y=100)



label_2 = Label(root, text ='Married',font=("Helvetica", 16),bg="black",fg="white")
label_2.place(x=100,y=150)
    
Entry_2 = Entry(root,bg="black",fg="white",font=("Helvetica", 16))
Entry_2.place(x=400,y=150)

label_22 = Label(root, text ='(no=0,yes=1)',font=("Helvetica", 16),bg="black",fg="white")
label_22.place(x=700,y=150)
    


label_3 = Label(root, text ='Dependents',font=("Helvetica", 16),bg="black",fg="white")
label_3.place(x=100,y=200)
   
Entry_3 = Entry(root,bg="black",fg="white",font=("Helvetica", 16))
Entry_3.place(x=400,y=200)

label_33 = Label(root, text ='no=0,yes=1',font=("Helvetica", 16),bg="black",fg="white")
label_33.place(x=700,y=200)



label_4 = Label(root, text ='Education',font=("Helvetica", 16),bg="black",fg="white")
label_4.place(x=100,y=250)
    
Entry_4= Entry(root,bg="black",fg="white",font=("Helvetica", 16))
Entry_4.place(x=400,y=250)

label_33 = Label(root, text ='no=0,yes=1',font=("Helvetica", 16),bg="black",fg="white")
label_33.place(x=700,y=200)




label_5 = Label(root, text ='Self_Employed',font=("Helvetica", 16),bg="black",fg="white")
label_5.place(x=100,y=300)

Entry_5 = Entry(root,bg="black",fg="white",font=("Helvetica", 16))
Entry_5.place(x=400,y=300)

label_5 = Label(root, text ='no=0,yes=1',font=("Helvetica", 16),bg="black",fg="white")
label_5.place(x=700,y=300)



label_6 = Label(root, text ='ApplicantIncome',font=("Helvetica", 16),bg="black",fg="white")
label_6.place(x=100,y=350)
   
Entry_6 = Entry(root,bg="black",fg="white",font=("Helvetica", 16))
Entry_6.place(x=400,y=350)



label_7 = Label(root, text ='CoapplicantIncome',font=("Helvetica", 16),bg="black",fg="white")
label_7.place(x=100,y=400)
    
Entry_7 = Entry(root,bg="black",fg="white",font=("Helvetica", 16))
Entry_7.place(x=400,y=400)



label_8 = Label(root, text ='LoanAmount',font=("Helvetica", 16),bg="black",fg="white")
label_8.place(x=100,y=450)
    
Entry_8 = Entry(root,bg="black",fg="white",font=("Helvetica", 16))
Entry_8.place(x=400,y=450)



label_9 = Label(root, text ='Loan_Amount_Term',font=("Helvetica", 16),bg="black",fg="white")
label_9.place(x=100,y=500)
   
Entry_9 = Entry(root,bg="black",fg="white",font=("Helvetica", 16))
Entry_9.place(x=400,y=500)



label_10 = Label(root, text ='Credit_History',font=("Helvetica", 16),bg="black",fg="white")
label_10.place(x=100,y=550)
    
Entry_10 = Entry(root,bg="black",fg="white",font=("Helvetica", 16))
Entry_10.place(x=400,y=550)



label_11 = Label(root, text ='Property_Area',font=("Helvetica", 16),bg="black",fg="white")
label_11.place(x=100,y=600)

Entry_11 = Entry(root,bg="black",fg="white",font=("Helvetica", 16))
Entry_11.place(x=400,y=600)

label_11 = Label(root, text ='rural=0 , urban=1',font=("Helvetica", 16),bg="black",fg="white")
label_11.place(x=700,y=600)







def logreg():
    var1 =  float(Entry_1.get())
    var2 = float( Entry_2.get())
    var3 = float( Entry_3.get())
    var4 = float( Entry_4.get())
    var5 = float( Entry_5.get())
    var6 = float( Entry_6.get())
    var7 = float( Entry_7.get())
    var8 = float( Entry_8.get())
    var9 = float( Entry_9.get())
    var10 = float( Entry_10.get())
    var11 = float( Entry_11.get())

       
    out = [[float(var1),
       float(var2),
       float(var3),
       float(var4),
       float(var5),
       float(var6),
       float(var7),
       float(var8),
       float(var9),
       float(var10),
       float(var11)]]

    prediction = log.predict(out)
    
    
    print(out)
    if prediction[0] == 'Y' :
        res="Approved"
    elif prediction[0] == "N":
        res="Not Approved"
    output.configure(text=res)

     
    

b1 = Button(root, text = 'logistic regression \n predict',font=("Helvetica", 16),bg="black",fg="white",activebackground= "cyan",command = logreg)
b1.place(x=100,y=650)


    

output = Label(root,bg="black",fg="white",font=("Helvetica", 16))
output.place(x=400,y=650)

    
root.mainloop()
