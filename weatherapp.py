from tkinter import*
from tkinter import ttk
import requests
from PIL import Image, ImageTk

class WeatherInfo:
   def __init__(self, temperature, description, pressure):
      self.temperature=temperature
      self.description=description
      self.pressure=pressure

def display(self):
      return f"Temperature: {self.temperature}°C\nDescription: {self.description}\nPressure{self.pressure}"

class WeatherApi(WeatherInfo):
  Weather_Api='&appid=f42d7fa031bcb367172550886864ef15'
  Url='https://api.openweathermap.org/data/2.5/weather?q='

  @staticmethod
  def data_weather(city):
    city=city_name.get() 
    data= requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=f42d7fa031bcb367172550886864ef15').json()
    try:
        response=requests.get(WeatherApi.Url, data=data)
        response.raise_for_status
        return response.json
    except requests.exceptions.RequestExceptions as e:
      print(f"error {e}")
      return None
       
class Location(WeatherInfo):
   def __init__(self, city, country):
      self.city=city
      self.country=country
def __str__(self): 
      return(f'{self.city} , {self.country}')

def data_get():
  city=city_name.get()
  data= requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=f42d7fa031bcb367172550886864ef15').json()
  label_w1.config(text=data['weather'][0]['main'])
  label_wd1.config(text=data['weather'][0]['description'])
  label_t1.config(text=str(int(data['main']['temp']-273.5)))
  label_p1.config(text=data['main']['pressure'])

class Gui:
  def __init__(self):
     super().__init__()

win=Tk()
win.title('Weather App')
win.config(bg= 'lightblue')
win.geometry('400x500')

img = Image.open("youyou.png")
img = img.resize((400, 500))
img.putalpha(255)  
photo = ImageTk.PhotoImage(img)

img_label = Label(win, image=photo, borderwidth=0, highlightthickness=0)
img_label.image = photo
img_label.place(x=0, y=0)


label_name= Label(win,text='Weather App', font=('time_new_roman',15,'bold'))
label_name.place(x=25,y=50,height=50,width=350)
city_name=StringVar()
list_name=['Adamzai',
    'Asc Colony',
    "Ahmadpur East",
    "Ahmed Nager Chatha",
    "Ali Khan Abad",
    "Alipur",
    "Arifwala",
    "Attock",
    "Bhera",
    "Bhalwal",
    "Bahawalnagar",
    "Bahawalpur",
    "Bhakkar",
    "Burewala",
    "Chenab Nagar",
    "Chillianwala",
    "Choa Saidanshah",
    "Chakwal",
    "Chak Jhumra",
    "Chichawatni",
    "Chiniot",
    "Chishtian",
    "Chunian",
    "Dajkot",
    "Daska",
    "Davispur",
    "Darya Khan",
    "Dera Ghazi Khan",
    "Dhaular",
    "Dina",
    "Dinga",
    "Dhudial Chakwal",
    "Dipalpur",
    "Faisalabad",
    "Fateh Jang",
    "Ghakhar Mandi",
    "Gojra",
    "Gujranwala",
    "Gujrat",
    "Gujar Khan",
    "Hakimabad",
    "Harappa",
    "Hafizabad",
    "Haroonabad",
    "Hasilpur",
    "Haveli Lakha",
    "Islamabad",
    "Jalalpur Jattan",
    "Jampur",
    "Jaranwala",
    "Jhang",
    "Jhelum",
    "Jauharabad",
    "Kallar Syedan",
    "Kalabagh",
    "Karor Lal Esan",
    "Karachi",
    "Kasur",
    "Kamalia",
    "Kāmoke",
    "Khanewal",
    "Khanpur",
    "Khanqah Sharif",
    "Kharian",
    "Khushab",
    "Kot Adu",
    "Lahore",
    "Lalamusa",
    "Layyah",
    "Lawa Chakwal",
    "Liaquat Pur",
    "Lodhran",
    "Malakwal",
    "Mamoori",
    "Mailsi",
    "Mandi Bahauddin",
    "Mian Channu",
    "Mianwali",
    "Miani",
    "Multan",
    "Murree",
    "Muridke",
    "Mianwali Bangla",
    "Muzaffargarh",
    "Narowal",
    "Nankana Sahib",
    'Nowshera',
    "Okara",
    "Pakpattan",
    "Pattoki",
    "Pindi Bhattian",
    "Pind Dadan Khan",
    "Pir Mahal",
    "Qaimpur",
    "Qila Didar Singh",
    "Raiwind",
    "Rajanpur",
    "Rahim Yar Khan",
    "Rawalpindi",
    "Renala Khurd",
    "Sadiqabad",
    "Sagri",
    "Sahiwal",
    "Sambrial",
    "Samundri",
    "Sangla Hill",
    "Sarai Alamgir",
    "Sargodha",
    "Shakargarh",
    'Shaidu',
    "Sheikhupura",
    "Shujaabad",
    "Sialkot",
    "Sohawa",
    "Soianwala",
    "Siranwali",
    "Tandlianwala",
    "Talagang",
    "Taxila",
    "Toba Tek Singh",
    "Vehari",
    "Wah Cantonment",
    "Wazirabad",
    "Yazman",
    "Zafarwal"
  ]
com=ttk.Combobox(win,text='Weather App', values= list_name, font=('time_new_roman',12,'bold'),textvariable=city_name)
com.place(x=25,y=120,height=50,width=350)

label_w= Label(win,text='Weather Climate', font=('time_new_roman',8))
label_w.place(x=25,y=260,height=30,width=150)

label_w1= Label(win,text='', font=('time_new_roman',8))
label_w1.place(x=190,y=260,height=30,width=150)

label_wd= Label(win,text='Weather Description', font=('time_new_roman',8))
label_wd.place(x=25,y=310,height=30,width=150)

label_wd1= Label(win,text='', font=('time_new_roman',8))
label_wd1.place(x=190,y=310,height=30,width=150)

label_t= Label(win,text='Temperature', font=('time_new_roman',8))
label_t.place(x=25,y=360,height=30,width=150)

label_t1= Label(win,text='', font=('time_new_roman',8))
label_t1.place(x=190,y=360,height=30,width=150)

label_p= Label(win,text='Pressure', font=('time_new_roman',8))
label_p.place(x=25,y=410,height=30,width=150)

label_p1= Label(win,text='', font=('time_new_roman',8))
label_p1.place(x=190,y=410,height=30,width=150)

done_button= Button (win,text='Search',font=('time_new_roman',12,'bold'), command=data_get)
done_button.place(y=190, h=32, w=100,x=155)
win.mainloop()
 