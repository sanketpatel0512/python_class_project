import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
import tkinter as tk  
from PIL import ImageTk, Image
from tabulate import tabulate

def Reg():
    y = year.get()
    t = ptype.get()
    traindata = pd.read_csv('traindata_'+str(y)+'.csv')
    traindata = traindata[traindata['type'] == t]


#read and create testing dataframe
    testdata = pd.read_csv('testdata.csv')


#Run and plot correlation chart
    df = traindata.drop(['boro','Age','2010','2015','type'],axis = 1)
    corcol = df.columns
   
    
    
    plt.matshow(df.corr())
    plt.xticks(range(len(corcol)), corcol, rotation = 90)
    plt.yticks(range(len(corcol)), corcol)
    plt.colorbar()
    plt.xlabel('Correlation Matrix ('+ y +')', labelpad = 30, fontsize = 15, fontweight = 800)
    plt.savefig('Correl.png',bbox_inches="tight")
    
    img1 = ImageTk.PhotoImage(Image.open("Correl.png"))
    panel1 = tk.Label(master, image = img1)
    panel1.img = img1
    panel1.grid(row = 4,columnspan = 10,rowspan = 10, sticky = tk.W)
    
    
    
    

#Run linear regression
    Y_train = df['Price/sqft']
    X_train = df.drop('Price/sqft',axis = 1)
    X_test = testdata.drop(['boro','Age','2010','2015'],axis = 1)
    
    lm = LinearRegression()
    lm.fit(X_train,Y_train)
    testdata['Predicted Price'] = lm.predict(X_test)

#Compare prediction to actual results
    actprice = pd.read_csv('Actual_data.csv')
    actprice = actprice[actprice['type'] == t]
    actprice = actprice.merge(testdata,on = 'boro')
    
    
    fig = plt.figure()
    plt.plot(actprice['boro'],actprice[['Predicted Price','Price/sqft']])
    plt.legend(('Predicted Price','Actual Price'))
    plt.ylabel('Price/sqft(USD)')
    plt.xlabel('Prediction vs. Actual Price(2015)', labelpad = 30, fontsize = 15, fontweight = 800)
    fig.savefig('Reg.png',bbox_inches="tight")
    

    img2 = ImageTk.PhotoImage(Image.open("Reg.png"))
    panel2 = tk.Label(master, image = img2)
    panel2.img = img2
    panel2.grid(row = 13, column = 8,columnspan = 14, sticky = tk.W)
   
    #actprice = actprice.rename(columns = {'boro': 'Borough','Predicted Price':'Predicted Price/sqft(USD)'})
    t = tk.Label(master, text ="Price Prediction Table (2015)",font = "Verdana 15 bold")
    
    t.grid(row = 16,column = 1, sticky = tk.W)
    
    t = tk.Label(master, text = tabulate(actprice[['boro','Predicted Price']],\
                                         showindex = False, headers = ['Borough',\
                                                                       'Predicted Price/sqft(USD)'])) 
    t.grid(row = 18,column = 1, sticky = tk.W)
    


    
master = tk.Tk(className='NYC Borough Price Predictor')
master.geometry("1000x1000")
yearlist = [2013,2014]
proplist = ['Residential','Commercial','Industrial','Civic Use','Mixed Use']


t = tk.Label(master, text ="Select Training Data Year: " )
t.grid(row = 0, sticky = tk.W)

year = tk.StringVar(master)
year.set(yearlist[0])
r = tk.OptionMenu(master,year, *yearlist)
r.grid(row = 0, column=1,columnspan = 3,sticky = tk.W)

t = tk.Label(master, text ="Select Property Type: " )
t.grid(row = 1, sticky = tk.W)

ptype = tk.StringVar(master)
ptype.set(proplist[0])
r = tk.OptionMenu(master,ptype, *proplist)
r.grid(row = 1, column=1,columnspan = 3,sticky = tk.W)


s = tk.Button(master,text="Run Analysis", command=Reg)
s.grid(row = 3,column = 1, sticky = tk.W)


master.grid_columnconfigure(11, minsize=70)
master.grid_rowconfigure(15, minsize=50)
master.mainloop()