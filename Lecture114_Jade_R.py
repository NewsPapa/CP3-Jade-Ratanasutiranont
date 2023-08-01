import datetime
import currency_converter
from currency_converter import CurrencyConverter

c = currency_converter.CurrencyConverter()
d = datetime.date

from tkinter import*
import math

def Left_Click_Button_1(event):
    from currency_converter import CurrencyConverter
    from datetime import date
    conversion_1 = c.convert(text_box_amount.get(),text_box_currency_1.get(),text_box_currency_2.get(),date=date(int(text_box_start_year.get()),int(text_box_start_month.get()),int(text_box_start_date.get())))
    conversion_2 = c.convert(text_box_amount.get(),text_box_currency_1.get(),text_box_currency_2.get(),date=date(int(text_box_start_year_2.get()),int(text_box_start_month_2.get()),int(text_box_start_date_2.get())))
    conversion_3 = ((conversion_2/conversion_1)-1)*100
    print(conversion_1)
    print(conversion_2)
    labelresult_1.configure(text = '%.2f'%(conversion_1))
    labelresult_2.configure(text = '%.2f'%(conversion_2))
    labelresult_3.configure(text='%.2f' % (conversion_3))


MainWindow = Tk()
label_title_1 = Label(MainWindow, text="Conver Cunrrency")
label_title_1.grid()
label_currency_1 = Label(MainWindow, text="Currency Amount")
label_currency_1.grid(row=2,column=0)
text_box_currency_1 = Entry(MainWindow)
text_box_currency_1.grid(row=2,column=1)
label_title_to = Label(MainWindow, text="to")
label_title_to.grid(row=2,column=2)
label_currency_2 = Label(MainWindow, text="Currency")
label_currency_2.grid(row=2,column=3)
text_box_currency_2 = Entry(MainWindow)
text_box_currency_2.grid(row=2,column=4)
label_start_year = Label(MainWindow, text="Year")
label_start_year.grid(row=3,column=0)
text_box_start_year = Entry(MainWindow)
text_box_start_year.grid(row=3,column=1)
label_start_month = Label(MainWindow, text="Month")
label_start_month.grid(row=3,column=2)
text_box_start_month = Entry(MainWindow)
text_box_start_month.grid(row=3,column=3)
label_start_day = Label(MainWindow, text="Day")
label_start_day.grid(row=3,column=4)
text_box_start_date = Entry(MainWindow)
text_box_start_date.grid(row=3,column=5)

label_money = Label(MainWindow, text = "Value")
label_money.grid(row=5,column=0)
text_box_amount = Entry(MainWindow)
text_box_amount.grid(row=5,column=1)
label_title_2 = Label(MainWindow, text="Compare Period")
label_title_2.grid(row=6,column=0)
label_start_year_2 = Label(MainWindow, text="Year")
label_start_year_2.grid(row=7,column=0)
text_box_start_year_2 = Entry(MainWindow)
text_box_start_year_2.grid(row=7,column=1)
label_start_month_2 = Label(MainWindow, text="Month")
label_start_month_2.grid(row=7,column=2)
text_box_start_month_2 = Entry(MainWindow)
text_box_start_month_2.grid(row=7,column=3)
label_start_day_2 = Label(MainWindow, text="Day")
label_start_day_2.grid(row=7,column=4)
text_box_start_date_2 = Entry(MainWindow)
text_box_start_date_2.grid(row=7,column=5)

label_title_result_1 = Label(MainWindow, text = "Current value")
label_title_result_1.grid(row=8,column=0)
labelresult_1 = Label(MainWindow, text="Result")
labelresult_1.grid(row=8,column=1)
label_title_result_2 = Label(MainWindow, text = "Compare value")
label_title_result_2.grid(row=8,column=2)
labelresult_2 = Label(MainWindow, text="Result")
labelresult_2.grid(row=8,column=3)
label_title_result_3 = Label(MainWindow, text = "%Change")
label_title_result_3.grid(row=8,column=4)
labelresult_3 = Label(MainWindow, text="Result")
labelresult_3.grid(row=8,column=5)
calculateButton = Button(MainWindow,text = "Calculate")
calculateButton.bind('<Button-1>', Left_Click_Button_1)
calculateButton.grid(row=9, column=0)

MainWindow.mainloop()
