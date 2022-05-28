from genericpath import exists
from pytube import YouTube
import sys
import os
import tkinter as tk



message = ""
def download_video(url):
    if not url:
        message = "Please Enter a video url from youtube"
    video_downloader = "VideoDownloader"
    save_path = "C:/Users/{}/Downloads/{}".format(os.getlogin(),video_downloader)

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    try:
        youtobe = YouTube(url)
        youtobe.streams.filter(file_extension="mp4").get_by_resolution("360p").download(save_path)
        message = "Task Completed!"
    except:
        message = "Connection Errore! or incorrect ULR"
    
    return message



windows  = tk.Tk()
windows.title("surey")
windows.geometry("600x400+400+180")

# Label
res_var = tk.StringVar()
lblurl = tk.Label(windows, text="enter YouTube URL").place(x=100, y=70)
lblres= tk.Label(windows,text=message, textvariable=res_var).place(x = 100, y = 160)

# Text Filed
url_var = tk.StringVar()
txturl = tk.Entry(windows, textvariable=url_var,font=("Helvetica", 16), width=40).place(x=100, y=100)

def down_video():
    res_var.set("please With")
    response = download_video(url_var.get())
    url_var.set("")
    res_var.set(response)
    print(response)
# Button 
btbDownload = tk.Button(windows, text="Download" ,command=down_video).place(x = 300, y = 150)

windows.mainloop()

