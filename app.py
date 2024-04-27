import customtkinter as ctk
from tkinter import ttk, filedialog
from pytube import YouTube
import os

def show_info():
    try:
        url = entry_url.get()
        yt = YouTube(url)
        
        author_label.configure(text=f"Author: {yt.author}")
        length_label.configure(text=f"Length: {yt.length // 60} minutes {yt.length % 60} seconds") 
        title_label.configure(text=f"Title: {yt.title}")
        views_label.configure(text=f"Views: {yt.views:,}") 

        info_frame.pack(pady=(10, 5)) 
    except Exception as e:
        reset()
        status_label.configure(text=f"Error: {str(e)}")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    downloaded_bytes = total_size - bytes_remaining
    completed_percentage = downloaded_bytes / total_size * 100

    print(completed_percentage)

    progress_label.configure(text=str(int(completed_percentage)) + '%')
    progress_bar.update()
    progress_bar.set(completed_percentage / 100)
    
def reset():
    progress_label.pack(pady=(10, 5))
    progress_bar.pack(pady=(10, 5))
    status_label.pack(pady=(10, 5))
    progress_bar.update()
    progress_bar.set(0.0)
    progress_label.configure(text="0%")
    status_label.configure(text="")
    info_frame.pack_forget()
    

def download_video():
    url = entry_url.get()
    resolution = resolution_cmb.get()
    print(f'{url}, {resolution}')
    reset()
    entry_url.configure(state=ctk.DISABLED)
    download_button.configure(state=ctk.DISABLED)
    show_info_button.configure(state=ctk.DISABLED)

    download_dir = filedialog.askdirectory(title="Select Download Location")

    if not download_dir:  
        print("Download cancelled by user.")
        entry_url.configure(state=ctk.NORMAL)  
        download_button.configure(state=ctk.NORMAL)
        return

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        if file_type_cmb.get() == 'audio':
            stream = yt.streams.filter(only_audio=True).first() 
            file_name = stream.download(output_path=download_dir)
            base, ext = os.path.splitext(file_name)
            new_file = base + '.mp3'
            os.rename(file_name, new_file) 
        else:
            stream = yt.streams.filter(res=resolution).first()
            stream.download(output_path=download_dir)
        status_label.configure(text="Downloaded successfully!")
        print("success")
    except Exception as e:
        print(e)
        status_label.configure(text=f"Error: {str(e)}")
    finally:
        # Re-enable entry and button after download finishes
        entry_url.configure(state=ctk.NORMAL)
        download_button.configure(state=ctk.NORMAL)
        show_info_button.configure(state=ctk.NORMAL)

root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root.title("Youtube Downloader")

root.geometry("720x540")
root.minsize(720, 540)
root.maxsize(720, 540)

content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

url_label = ctk.CTkLabel(content_frame, text="Youtube URL: ")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=(10, 5))
entry_url.pack(pady=(10, 5))

option_frame = ctk.CTkFrame(content_frame, width=300, height=50, corner_radius=10)

resolutions = ["1080p", "720p", "480p", "360p"]
resolution_cmb = ctk.CTkComboBox(option_frame, values=resolutions, state='readonly')
resolution_cmb.set(resolutions[-1])

file_types = ["audio", "video"]
file_type_cmb = ctk.CTkComboBox(option_frame, values=file_types, state='readonly')
file_type_cmb.set(file_types[-1])

resolution_cmb.pack(side=ctk.RIGHT, pady=(10, 5), padx=10)
file_type_cmb.pack(side=ctk.LEFT, pady=(10, 5), padx=10)

option_frame.pack(pady=(10, 5))

button_frame = ctk.CTkFrame(content_frame, width=300, height=50, corner_radius=10)

show_info_button = ctk.CTkButton(button_frame, text="Show Info", command=show_info)
show_info_button.pack(side=ctk.RIGHT, pady=(10, 5), padx=10)

download_button = ctk.CTkButton(button_frame, text="Download", command=download_video)
download_button.pack(side=ctk.LEFT, pady=(10, 5), padx=10)

button_frame.pack(pady=(10, 5))

progress_label = ctk.CTkLabel(content_frame, text="0%")

progress_bar = ctk.CTkProgressBar(content_frame, width=400)

status_label = ctk.CTkLabel(content_frame, text="")

info_frame = ctk.CTkFrame(content_frame, width=400, height=250, corner_radius=10, border_width=1)
author_label = ctk.CTkLabel(info_frame)
length_label = ctk.CTkLabel(info_frame)
title_label = ctk.CTkLabel(info_frame)
views_label = ctk.CTkLabel(info_frame)
author_label.pack(pady=(5, 0), padx=10, anchor=ctk.W)
length_label.pack(pady=(5, 0), padx=10, anchor=ctk.W)
title_label.pack(pady=(5, 0), padx=10, anchor=ctk.W)
views_label.pack(pady=(5, 0), padx=10, anchor=ctk.W)

root.mainloop()
