import tkinter as tk
import requests



def formatas(weather):

    name = weather['name']
    desc = weather['weather'][0]['description']
    temp = weather['main']['temp']

    return str(name) + ' '+str(desc) + ' '+str(temp)

def orai(city):
    raktas = '2f2ed8664ae5c40d47b72596fba2e3c4'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': raktas, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = formatas(weather)

def radijas():
    url = 'https://www.m-1.fm/playing.json?_=1606062035923'
    parame= {}
    response = requests.get(url, parame=parame)
    response.json()




root = tk.Tk()

#Backgroundas
root.geometry("500x400")

background_image = tk.PhotoImage(file='orai.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relheight=1, relwidth=1)

#Remai
frame = tk.Frame(root, bg='#23ae1d', bd='5')
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

lower_frame = tk.Frame(root, bg='#23ae1d', bd='10')
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relheight=1, relwidth=1)

#Suvdimas
entry = tk.Entry(frame, font='40')
entry.place(relheight=1, relwidth=0.65)

#Knopkes
button = tk.Button(frame, text="Weather Check", bg="#61b4a1", command=lambda: orai(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)




#Radijo Stotis M1
label = tk.Label(root, text='Radijo stotis M-1', bg='#4bce37')
label.pack(side='left', anchor='n')

button = tk.Button(root, text='M1', bg='blue', command=radijas)
button.place(anchor='nw')



root.title("Weather Check 0.0001 version beta")
root.mainloop()
