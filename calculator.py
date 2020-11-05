from tkinter import *

root=Tk()
root.title("simple calculator")
global math
global f_num
math="none"
f_num=0
e=Entry(root,width=40,borderwidth=2)
e.grid(row=0,column=0,columnspan=3)

def button_click(number):
	current=e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(number))
def button_add():
	current=e.get()
	global f_num
	global math
	if current=="":
		current=0
	
	math="add"
	e.delete(0,END)
	f_num=int(current)
def button_sub():
	current=e.get()
	global f_num
	global math
	if current=="":
		current=0
	
	math="sub"
	e.delete(0,END)
	f_num=int(current)
def button_pro():
	current=e.get()
	global f_num
	global math
	if current=="":
		current=0
	
	math="pro"
	e.delete(0,END)
	f_num=int(current)
def button_div():
	current=e.get()
	global f_num
	global math
	if current=="":
		current=0
	
	math="div"
	e.delete(0,END)
	f_num=int(current)
def button_equal():
	current=e.get()
	global f_num
	global math
	e.delete(0,END)
	
	if math=="none" and current=="":
		f_num=0
	if math=="none" and current!="":
		f_num=int(current)
	if math=="add" and current=="":
		current=0
	if math=="sub" and current=="":
		current=0
	if math=="pro" and current=="":
		current=0
	if math=="div" and current=="":
		current=0
	if math=="add":
		f_num=f_num+int(current)
	if math=="sub":
		f_num=f_num-int(current)
	if math=="pro":
		f_num=f_num*int(current)
	if math=="div":
		if int(current)==0:
			f_num=0
		else:
			f_num=f_num//int(current)

	e.insert(0,f_num)

def button_clr():
	e.delete(0,END)
def button_ans():
	e.delete(0,END)
	e.insert(0,f_num)
button_1=Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))


button_add=Button(root,text=" + ",padx=36,pady=20,command=button_add)
button_sub=Button(root,text=" -",padx=39,pady=20,command=button_sub)
button_pro=Button(root,text=" *",padx=39,pady=20,command=button_pro)
button_div=Button(root,text=" /",padx=39,pady=20,command=button_div)
button_clr=Button(root,text=" CLR",padx=31,pady=20,command=button_clr)
button_equal=Button(root,text="=",padx=134,pady=20,command=button_equal)
button_ans=Button(root,text="Ans",padx=128,pady=20,command=button_ans)
button_quit=Button(root,text="exit",padx=128,pady=20,command=root.quit)


button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=4,column=1)
button_sub.grid(row=4,column=2)
button_pro.grid(row=5,column=1)
button_div.grid(row=5,column=2)
button_clr.grid(row=5,column=0)
button_equal.grid(row=6,column=0,columnspan=3)
button_ans.grid(row=7,column=0,columnspan=3)
button_quit.grid(row=8,column=0,columnspan=3)




root.mainloop()
