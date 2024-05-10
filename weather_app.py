from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

import requests
from datetime import datetime


user_api = '9fd9bfa8a48d451eb8388d105d131e30'

def get_weather(location):
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    if api_data['cod'] == '404':
        return None
    else:
        #create variables to store and display data
        
        city = api_data['name']
        country = api_data['sys']['country']
        
        temp_cel = ((api_data['main']['temp']) - 273.15)
        temp_fer = ((api_data['main']['temp']))
        temp_min = ((api_data['main']['temp_min']) - 273.15)
        temp_max = ((api_data['main']['temp_max']) - 273.15)

        icon = api_data['weather'][0]['icon']
        
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_speed = api_data['wind']['speed']
        pressure = api_data['main']['pressure']

        # sea_level = api_data['main']['sea_level']
        # grnd_level = api_data['main']['grnd_level']

        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


        final_data = (city, country, temp_cel, temp_fer, icon, weather_desc, hmdt, wind_speed, date_time, temp_min, temp_max, pressure)

    return final_data

def search():
    city = city_text.get()
    weather = get_weather(city)
    
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])

        # load and display image "C:\Users\91911\Desktop\Weather app- Deploy\weather_icons"
        img = ImageTk.PhotoImage(Image.open('C:/Users/91911/Desktop/Weather app- Deploy/weather_icons/{}.png'.format(weather[4])))
        img_lbl.config(image=img)
        img_lbl.image = img

        temp_lbl['text'] = '{:.2f}°C , {:.2f}°F'.format(weather[2], weather[3])
        temp_min_max_lbl['text'] = 'Min: {:.2f}°C & Max: {:.2f}°C'.format(weather[9], weather[10])

        weather_lbl['text'] = f'Weather--{weather[5]}'
        hmdt_lbl['text'] = f'Humidity--{weather[6]} g.m-3'
        wind_speed_lbl['text'] = f'Wind Speed--{weather[7]} km/hour'
        pressure_lbl['text'] = f'Pressure Level--{weather[11]} pascal'

        # sea_level_lbl['text'] = f'Sea Level--{weather[12]}'
        # grnd_level_lbl['text'] = f'Ground Level--{weather[13]}'

        date_time_lbl['text'] = f'{weather[8]}'
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))

app = Tk()
app.title("Weather App")
app.geometry('400x500')

app.configure(bg='#BFACE2')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text="Search Weather", width=15, command=search)
search_btn.pack()

location_lbl = Label(app, text='', font=('bold', 20), bg='#BFACE2')
location_lbl.pack()


# create label for image
img_lbl = Label(app, bg='#BFACE2')
img_lbl.pack()

temp_lbl = Label(app, text='', bg='#BFACE2')
temp_lbl.pack()

temp_min_max_lbl = Label(app, text='', bg='#BFACE2')
temp_min_max_lbl.pack()

weather_lbl = Label(app, text='', bg='#BFACE2')
weather_lbl.pack()

hmdt_lbl = Label(app, text='', bg='#BFACE2')
hmdt_lbl.pack()

wind_speed_lbl = Label(app, text='', bg='#BFACE2')
wind_speed_lbl.pack()

pressure_lbl = Label(app, text='', bg='#BFACE2')
pressure_lbl.pack()

# sea_level_lbl = Label(app, text='', bg='#BFACE2')
# sea_level_lbl.pack()

# grnd_level_lbl = Label(app, text='', bg='#BFACE2')
# grnd_level_lbl.pack()

date_time_lbl = Label(app, text='', bg='#BFACE2')
date_time_lbl.pack()

app.mainloop()
