import customtkinter as ctk
from tkinter import filedialog
from pytube import YouTube
import os

class YoutubeDownloader:
    def __init__(self):
        self.root = ctk.CTk()
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        self.setup_gui()
    
    def setup_gui(self):
        self.root.title("Youtube Downloader")
        self.root.geometry("720x540")
        self.root.minsize(720, 540)
        self.root.maxsize(720, 540)
        self.content_frame = ctk.CTkFrame(self.root)
        self.content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)
        self.url_label = ctk.CTkLabel(self.content_frame, text="Youtube URL: ")
        self.entry_url = ctk.CTkEntry(self.content_frame, width=400, height=40)
        self.url_label.pack(pady=(10, 5))
        self.entry_url.pack(pady=(10, 5))
        self.option_frame = ctk.CTkFrame(self.content_frame, width=300, height=50, corner_radius=10)
        self.resolutions = ["1080p", "720p", "480p", "360p"]
        self.resolution_cmb = ctk.CTkComboBox(self.option_frame, values=self.resolutions, state='readonly')
        self.resolution_cmb.set(self.resolutions[-1])
        self.file_types = ["audio", "video"]
        self.file_type_cmb = ctk.CTkComboBox(self.option_frame, values=self.file_types, state='readonly', command=self.update_res_cmb)
        self.file_type_cmb.set(self.file_types[-1])
        self.resolution_cmb.pack(side=ctk.RIGHT, pady=(10, 5), padx=10)
        self.file_type_cmb.pack(side=ctk.LEFT, pady=(10, 5), padx=10)
        self.option_frame.pack(pady=(10, 5))
        self.button_frame = ctk.CTkFrame(self.content_frame, width=300, height=50, corner_radius=10)
        self.show_info_button = ctk.CTkButton(self.button_frame, text="Show Info", command=self.show_info)
        self.show_info_button.pack(side=ctk.RIGHT, pady=(10, 5), padx=10)
        self.download_button = ctk.CTkButton(self.button_frame, text="Download", command=self.download_video)
        self.download_button.pack(side=ctk.LEFT, pady=(10, 5), padx=10)
        self.button_frame.pack(pady=(10, 5))
        self.progress_label = ctk.CTkLabel(self.content_frame, text="0%")
        self.progress_bar = ctk.CTkProgressBar(self.content_frame, width=400)
        self.status_label = ctk.CTkLabel(self.content_frame, text="")
        self.info_frame = ctk.CTkFrame(self.content_frame, width=400, height=250, corner_radius=10, border_width=1)
        self.author_label = ctk.CTkLabel(self.info_frame)
        self.length_label = ctk.CTkLabel(self.info_frame)
        self.title_label = ctk.CTkLabel(self.info_frame)
        self.views_label = ctk.CTkLabel(self.info_frame)
        self.author_label.pack(pady=(5, 0), padx=10, anchor=ctk.W)
        self.length_label.pack(pady=(5, 0), padx=10, anchor=ctk.W)
        self.title_label.pack(pady=(5, 0), padx=10, anchor=ctk.W)
        self.views_label.pack(pady=(5, 0), padx=10, anchor=ctk.W)
        
    def run(self):
        self.root.mainloop()
        
    def update_res_cmb(self, selected):
        if selected == 'audio':
            self.resolution_cmb.configure(state=ctk.DISABLED)
        else:
            self.resolution_cmb.configure(state=ctk.NORMAL)

    def show_info(self):
        try:
            url = self.entry_url.get()
            yt = YouTube(url)
            self.author_label.configure(text=f"Author: {yt.author}")
            self.length_label.configure(text=f"Length: {yt.length // 60} minutes {yt.length % 60} seconds")
            self.title_label.configure(text=f"Title: {yt.title}")
            self.views_label.configure(text=f"Views: {yt.views:,}")
            self.info_frame.pack(pady=(10, 5))
        except Exception as e:
            self.reset()
            self.status_label.configure(text=f"Error: {str(e)}")

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        downloaded_bytes = total_size - bytes_remaining
        completed_percentage = downloaded_bytes / total_size * 100
        print(completed_percentage)
        self.progress_label.configure(text=str(int(completed_percentage)) + '%')
        self.progress_bar.update()
        self.progress_bar.set(completed_percentage / 100)

    def reset(self):
        self.progress_label.pack(pady=(10, 5))
        self.progress_bar.pack(pady=(10, 5))
        self.status_label.pack(pady=(10, 5))
        self.progress_bar.update()
        self.progress_bar.set(0.0)
        self.progress_label.configure(text="0%")
        self.status_label.configure(text="")
        self.info_frame.pack_forget()

    def download_video(self):
        url = self.entry_url.get()
        resolution = self.resolution_cmb.get()
        print(f'{url}, {resolution}')
        self.reset()
        self.entry_url.configure(state=ctk.DISABLED)
        self.download_button.configure(state=ctk.DISABLED)
        self.show_info_button.configure(state=ctk.DISABLED)
        download_dir = filedialog.askdirectory(title="Select Download Location")
        if not download_dir:
            print("Download cancelled by user.")
            self.entry_url.configure(state=ctk.NORMAL)
            self.download_button.configure(state=ctk.NORMAL)
            return
        try:
            yt = YouTube(url, on_progress_callback=self.on_progress)
            if self.file_type_cmb.get() == 'audio':
                stream = yt.streams.filter(only_audio=True).first()
                file_name = stream.download(output_path=download_dir)
                base, ext = os.path.splitext(file_name)
                new_file = base + '.mp3'
                os.rename(file_name, new_file)
            else:
                stream = yt.streams.filter(res=resolution, only_audio=False).first()
                stream.download(output_path=download_dir)
            self.status_label.configure(text="Downloaded successfully!")
            print("success")
        except Exception as e:
            print(e)
            self.status_label.configure(text=f"Error: {str(e)}")
        finally:
            self.entry_url.configure(state=ctk.NORMAL)
            self.download_button.configure(state=ctk.NORMAL)
            self.show_info_button.configure(state=ctk.NORMAL)

if __name__ == "__main__":
    downloader = YoutubeDownloader()
    downloader.run()
