import tkinter as tk
from PIL import ImageTk, Image
import time


root = tk.Tk()
root.title("My Smart Home")

font = ("Arial", 10)

def music_control():

    pjesme = ["Michael Jackson - Billie Jean", "Queen - Bohemian Rhapsody", 
             "Led Zeppelin - Stairway to Heaven", "Pink Floyd - Comfortably Numb",
             "The Beatles - Hey Jude"]
    
    pjesme_index = 0
    
    
    

    
    music_frame = tk.Frame(root, bd=2, relief="groove")
    music_frame.pack(side="left", padx=10, pady=10)

    music_label = tk.Label(music_frame, text="Upravljanje Glazbom",font=("Arial bold", 12))
    music_label.pack(side="top", pady=10)

    promjena_frame = tk.Frame(music_frame, bd=2, relief="groove")
    promjena_frame.pack(side="left", padx=10, pady=10)
    promjena_label = tk.Label(promjena_frame, text="Promjena Pjesme:", font=font)
    promjena_label.pack(side="top", pady=10)

    def promjena_label():
        nonlocal pjesme_index
        song_label.config(text=pjesme[pjesme_index])

    def prijasnja_pjesma():
        nonlocal pjesme_index
        pjesme_index = (pjesme_index - 1)  % len(pjesme)
        promjena_label()

    def sljedeca_pjesma():
        nonlocal pjesme_index
        pjesme_index = (pjesme_index + 1)  % len(pjesme)
        promjena_label()
    
    

    last_song_button = tk.Button(promjena_frame, text="<",bg="white", command=prijasnja_pjesma)
    last_song_button.pack(side="left", padx=10, pady=10)    
    next_song_button = tk.Button(promjena_frame, text=">",bg="white", command=sljedeca_pjesma)    
    next_song_button.pack(side="right", padx=10, pady=10)
    song_label = tk.Label(promjena_frame, text=pjesme[pjesme_index], font=font)
    song_label.pack(side="bottom", padx=10, pady=10)

    
    
    volume_label = tk.Label(music_frame, text="Glasnoća:", font=font)
    volume_label.pack(side="left", padx=10, pady=10)
    
    volume_slider = tk.Scale(music_frame, from_=0, to=100, orient="horizontal")
    volume_slider.pack(side="left", padx=10, pady=10)
    volume_slider.set(30)

    def start():
        start_button.config(bg="green")
        pause_button.config(bg="white")
        stop_button.config(bg="white")

    def pause():
        start_button.config(bg="white")
        pause_button.config(bg="green")
        stop_button.config(bg="white")
    
    def stop():
        start_button.config(bg="white")
        pause_button.config(bg="white")
        stop_button.config(bg="green")
      
   
    start_button = tk.Button(music_frame, text="Start", bg="white", command=start, font=font)
    start_button.pack(side="left", padx=10, pady=10)    
    pause_button = tk.Button(music_frame, text="Pause",bg="white", command=pause, font=font)     
    pause_button.pack(side="left", padx=10, pady=10)
    stop_button = tk.Button(music_frame, text="Stop",bg="white", command=stop, font=font)    
    stop_button.pack(side="left", padx=10, pady=10)

    stop()

   

    



def tv_control():   
    tv_frame = tk.Frame(root, bd=2, relief="groove", width=400, height=400)
    tv_frame.pack(side="left", padx=10, pady=10)
   
    tv_label = tk.Label(tv_frame, text="Upravljanje TV-om",font=("Arial bold", 12))
    tv_label.pack(side="top", pady=10)

    def turn_on():
        turn_on_button.config(bg="green")
        turn_off_button.config(bg="white")
      
    
    def turn_off():
        turn_off_button.config(bg="red")
        turn_on_button.config(bg="white")

    turn_on_button = tk.Button(tv_frame, text="Upali TV", command=turn_on, font=font)
    turn_off_button = tk.Button(tv_frame, text="Ugasi TV", command=turn_off, font=font)
    turn_on_button.pack(side="top", padx=10, pady=10)
    turn_off_button.pack(side="top", padx=10, pady=10)

    turn_off()

    channel_frame = tk.Frame(tv_frame)
    channel_frame.pack(side="top", pady=10)
    channel_label = tk.Label(channel_frame, text="Kanal:")
    channel_label.pack(side="left", padx=10)
    
    prev_channel_button = tk.Button(channel_frame, text="<", bg="white", font=font)
    next_channel_button = tk.Button(channel_frame, text=">", bg="white", font=font)
    prev_channel_button.pack(side="left")
    next_channel_button.pack(side="left")

  
    volume_label = tk.Label(tv_frame, text="Glasnoća:", font=font)
    volume_label.pack(side="left", padx=10, pady=10)
    volume_slider = tk.Scale(tv_frame, from_=0, to=100, orient="horizontal")
    volume_slider.pack(side="left", padx=10, pady=10)
    volume_slider.set(30)


    

def air_condition_control():   
    air_condition_frame = tk.Frame(root, bd=2, relief="groove", width=400, height=400)
    air_condition_frame.pack(side="left", padx=10, pady=10)
 
    air_condition_label = tk.Label(air_condition_frame, text="Upravljanje klima uređajem",font=("Arial bold", 12))
    air_condition_label.pack(side="top", pady=10)

    temperature_label = tk.Label(air_condition_frame, text="Temperatura sobe: 25°C", font=font)
    temperature_label.pack(side="top", padx=10, pady=10)

    def increase_temperature():
        temperature_slider.set(temperature_slider.get() + 1)
        increase_button.config(bg="green")
        increase_button.after(200, lambda: increase_button.config(bg="white"))
    
    def decrease_temperature():
        temperature_slider.set(temperature_slider.get() - 1)
        decrease_button.config(bg='red')
        decrease_button.after(200, lambda: decrease_button.config(bg="white"))


 
        
    increase_button = tk.Button(air_condition_frame, text="Povećaj temperaturu", command=increase_temperature, bg="white", font=font)
    decrease_button = tk.Button(air_condition_frame, text="Smanji temperaturu", command=decrease_temperature, bg="white", font=font)
    increase_button.pack(side="top", padx=10, pady=10)
    decrease_button.pack(side="top", padx=10, pady=10)
   
    temperature_slider = tk.Scale(air_condition_frame, from_=10, to=40, orient="horizontal")
    temperature_slider.pack(side="top", padx=10, pady=10)
    temperature_slider.set(21)

    



def lights_control():
    
    lights_frame = tk.Frame(root, bd=2, relief="groove", width=400, height=400)
    lights_frame.pack(side="left", padx=10, pady=10)
   
    lights_label = tk.Label(lights_frame, text="Upravljanje rasvjetom",font=("Arial bold", 12))
    lights_label.pack(side="top", pady=10)  

    def turn_on():
        turn_on_button.config(bg="green")
        turn_off_button.config(bg="white")
      
    
    def turn_off():
        turn_off_button.config(bg="red")
        turn_on_button.config(bg="white")

        
    
    turn_on_button = tk.Button(lights_frame, text="Upali svijetlo", command=turn_on, font=font)
    turn_off_button = tk.Button(lights_frame, text="Ugasi svijetlo", command=turn_off, font=font)
    turn_on_button.pack(side="top", padx=10, pady=10)
    turn_off_button.pack(side="top", padx=10, pady=10)

    turn_off()  
   
    dimmer_label = tk.Label(lights_frame, text="Regulator rasvjete:", font=font)
    dimmer_label.pack(side="left", padx=10, pady=10)
    dimmer_slider = tk.Scale(lights_frame, from_=0, to=100, orient="horizontal")
    dimmer_slider.pack(side="left", padx=10, pady=10)
    dimmer_slider.set(50)





music_control()
tv_control()
air_condition_control()
lights_control()

root.mainloop()
