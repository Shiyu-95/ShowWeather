'''
This program is created only for trying to use Tkinter module
'''

from tkinter import *
import requests
window = Tk()


def get_weather():
    city = city_field.get()
    key = '84aeaa5777ba1e78fda752d4f02e95d9'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()
    info['text'] = f'{str(weather["name"])} : {weather["main"]["temp"]}C'


window['bg'] = '#fafafa'
window.title('Weather program')
window.geometry('300x250')
window.resizable(width=False, height=False)

frame_top = Frame(window, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(window, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

city_field = Entry(frame_top, bg='white', font=30)
city_field.pack()

button = Button(frame_top, text='Show the weather', command=get_weather)
button.pack()

info = Label(frame_bottom, text="Weather info", bg='#ffb700', font=40)
info.pack()

window.mainloop()
