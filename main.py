import customtkinter
import psutil
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


screen_width = 800

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

def get_storage(): 
    global used_storage_barline

    total_storage = psutil.disk_usage('/').total / (1024 ** 3)  # Total storage in GB
    free_storage = psutil.disk_usage('/').free / (1024 ** 3)    # Free storage in GB
    used_storage = total_storage - free_storage

    storage_info = f"Total storage: {total_storage:.2f} GB\n"
    storage_info += f"Used storage: {used_storage:.2f} GB\n"
    storage_info += f"Free storage: {free_storage:.2f} GB"

   
    storage_label.configure(text=storage_info)

    create_pie_chart(used_storage, free_storage)

def create_pie_chart(used_storage, free_storage):
    labels = ['Used', 'Free']
    sizes = [used_storage, free_storage]
    colors = ['pink', 'grey']

    fig = Figure(figsize=(90, 90),facecolor='#2b2b2b')
    ax = fig.add_subplot(111)
    pie = ax.pie(sizes, labels=labels, colors=colors, autopct='%d%%', startangle=140)
    ax.axis("equal")
    ax.set_frame_on(False)
    for text in pie[1]:
        text.set_color('white')

    chart = FigureCanvasTkAgg(fig, data_frame)
    chart.get_tk_widget().pack()
    

root = customtkinter.CTk()
root.title("Device storage Checker")
root.geometry(f"{screen_width}x500")

# FRAMES
title_frame = customtkinter.CTkFrame(master=root, corner_radius=20, height=60)
title_frame.pack(pady=15, padx=20, fill="x")

data_frame = customtkinter.CTkFrame(master=root, corner_radius=20)
data_frame.pack(pady=20, padx=20, fill="both", expand="true")

# TEXTS
title = customtkinter.CTkLabel(title_frame, text="Device storage", font=("Arial", 40))
title.pack(expand=True, anchor=customtkinter.CENTER, pady=10)

storage_label = customtkinter.CTkLabel(data_frame, text="", font=("Arial", 14))

get_storage()

storage_label.pack()

root.mainloop()