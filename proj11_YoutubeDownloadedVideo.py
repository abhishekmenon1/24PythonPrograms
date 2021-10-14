from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Filelocation = ""

def fileLocator():
    global Filelocation
    Filelocation = filedialog.askdirectory()

    if (len(Filelocation) > 1):
        file_inst.config(text = Filelocation, fg= "green")
    else:
        file_inst.config(text = "Enter File Name", fg = "red")

def Download():
    url = user_input.get()
    val = videoQuality.get()
    print(url)

    if (len(url) > 1):
        inst.config(text="")
        youtubeVID = YouTube(url)

        if (val == choices[0]):
            sel = youtubeVID.streams.get_highest_resolution()
            sel.download(Filelocation)
            DownCom.config(text="Download Completed", fg="green")

        elif (val == choices[1]):
            sel = youtubeVID.streams.get_lowest_resolution()
            sel.download(Filelocation)
            DownCom.config(text="Download Completed", fg="green")

        elif (val == choices[2]):
            sel = youtubeVID.streams.get_audio_only()
            sel.download(Filelocation)
            DownCom.config(text="Download Completed", fg="green")

        else:
           # sel= ""
            inst.config(text = "Please enter a valid url", fg="red")

root = Tk()
root.title("Youtube Downloader")
root.geometry("400x450")
root.columnconfigure(0, weight = 1)

#TITlE
title = Label(root, text = "Download YouTube Videos\n", font=("calibri bold", 15))
title.grid()

#url box
user_input = StringVar()
url_box = Entry(root, width = 50, text = user_input)
url_box.grid()

#instruction
inst = Label(root, text="(Enter Url)\n\n", fg = "red", font=("calibri", 10))
inst.grid()

#Label for File location
File_location = Label(root, text="File Location", font=("calibri bold", 15))
File_location.grid()

#File Location Folder
Folder = Button(root, text="file locator", fg ="white", bg="red", width = 20, command = fileLocator)
Folder.grid()

#File instruction
file_inst = Label(root, text="(Enter File Location)\n\n", fg = "red", font=("calibri", 10))
file_inst.grid()

#Label for Quality
Vid_Quality = Label(root, text="Video Quality", font=("calibri bold", 15))
Vid_Quality.grid()

#Box for quality
choices = ["1080p", "144p", "Only Audio"]
videoQuality = ttk.Combobox(root, values = choices)
videoQuality.grid()

space = Label(text = "\n")
space.grid()

#Download Button
download = Button(root, text="Download", width = 20, fg ="white", bg="red", command= Download)
download.grid()

#Download Complete
DownCom = Label(root, text="", font=("calibri bold", 10))
DownCom.grid()

root.mainloop()