# importar as bibliotecas

from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

janela = Tk()
janela.title("TEMPO")
janela.geometry("900x500+300+200")
janela.resizable(False, False)


# Etc/GMT+1
def pegarTempo():
    try:
        cidade = pesqui.get()

        geolocator = Nominatim(user_agent="AppTempo")
        local = geolocator.geocode(cidade)
        obj = TimezoneFinder()
        resultado = obj.timezone_at(lng=local.latitude, lat=local.longitude)

        home = pytz.timezone(resultado)
        local_time = datetime.now()
        current_tempo = local_time.strftime("%I:%M%p")
        relogio.config(text=current_tempo)
        nome.config(text="TEMPO REAL")

        # tempo
        from chave_api import API_KEY
        api = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&APPID={API_KEY}&lang=pt_br'

        json_data = requests.get(api).json()
        condicao = json_data["weather"][0]['main']
        descricao = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressao = json_data['main']['pressure']
        humidade = json_data['main']['humidity']
        vento = json_data['wind']['speed']

        t.config(text=(temp,"°C"))
        c.config(text=(condicao,"|", "SENSAÇÃO", "DE", temp,"°C"))

        v.config(text=vento)
        h.config(text=humidade)
        d.config(text=descricao)
        p.config(text=pressao)

    except Exception as e:
        messagebox.showerror("TEMPO", "Não conseguimos realizar a busca, tente novamente")


# barra de pesquisa
pesquisa_img = PhotoImage(file="search.png")
my_img = Label(image=pesquisa_img)
my_img.place(x=20, y=20)

pesqui = tk.Entry(janela, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
pesqui.place(x=50, y=40)
pesqui.focus()

lupa_pesq = PhotoImage(file='search_icon.png')
my_img_lupa = Button(image=lupa_pesq, borderwidth=0, cursor="hand2", bg="#404040", command=pegarTempo)
my_img_lupa.place(x=400, y=34)

# logo
logo_img = PhotoImage(file="logo.png")
logo = Label(image=logo_img)
logo.place(x=150, y=100)

# Botão
box_img = PhotoImage(file="box.png")
box = Label(image=box_img)
box.pack(padx=5, pady=5, side=BOTTOM)

# time
nome = Label(janela, font=("arial", 15, "bold"))
nome.place(x=30, y=100)
relogio = Label(janela, font=("Helvietica", 20))
relogio.place(x=30, y=130)

# label
label1 = Label(janela, text="VENTO", font=("helvetica", 15, "bold"), fg="white", bg='#1ab5ef')
label1.place(x=120, y=400)

label2 = Label(janela, text="HUMIDADE", font=("helvetica", 15, "bold"), fg="white", bg='#1ab5ef')
label2.place(x=250, y=400)

label3 = Label(janela, text="DESCRIÇÃO", font=("helvetica", 15, "bold"), fg="white", bg='#1ab5ef')
label3.place(x=430, y=400)

label4 = Label(janela, text="PRESSÃO", font=("helvetica", 15, "bold"), fg="white", bg='#1ab5ef')
label4.place(x=650, y=400)

# t = temperatura
# c = condicao

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=('arial', 15, "bold"))
c.place(x=400, y=250)

v = Label(text="...", font=("arial", 20, "bold"), bg='#1ab5ef')
v.place(x=120, y=430)

h = Label(text="...", font=("arial", 20, "bold"), bg='#1ab5ef')
h.place(x=280, y=430)

d = Label(text="...", font=("arial", 20, "bold"), bg='#1ab5ef')
d.place(x=450, y=430)

p = Label(text="...", font=("arial", 20, "bold"), bg='#1ab5ef')
p.place(x=670, y=430)







janela.mainloop()
