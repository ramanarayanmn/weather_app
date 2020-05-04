import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk


HEIGTH = 600
WIDTH = 700

def format_response(weather):
	try:
		name = weather['name']
		clouds = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature[C]: %s' %(name,clouds,temp)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str 

def get_weather(city):
	weather_key = '4c95087b61beee413c02eb800dd7aca2'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units':'metric'}
	response = requests.get(url,params=params)
	weather = response.json()
	label['text'] = format_response(weather)
	icon_name = weather['weather'][0]['icon']
	open_image(icon_name)

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img


root = tk.Tk()

canvas = tk.Canvas(root,height=HEIGTH,width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

# upper frame
frame = tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx= 0.5, rely=0.1, relheight=0.1,relwidth=0.75,anchor='n')

entry = tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame,text='Get weather',font=40,command=lambda: get_weather(entry.get()))
button.place(relx=0.7,relwidth=0.3,relheight=1)


# lower frame
lower_frame = tk.Frame(root,bg='#80c1ff',bd=10)
lower_frame.place(relx=0.5, rely=0.25, relheight=0.6,relwidth=0.75,anchor='n')

label = tk.Label(lower_frame,font=('courier',18),anchor='nw',justify='left')
label.place(relwidth=1,relheight=1)

weather_icon = tk.Canvas(label, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)



root.mainloop()