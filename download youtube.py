from pytube import YouTube

link = input("Salin link disini : ")
video = YouTube(link)

print("List resolution:")
print("1. lowest resolutio (144p)")
print("2. lownresolution (240p)")
print("3. Medest resolution (360p)")
print("4. mediumest resolution (480p)")
print("5. higest resolution (720p)")
print("6. highest resolution (1080p)")
resolution = input("Pilih resolusi: ")

if resolution == "1":
    print("downloading video ",video.title)
    video = video.streams.get_highest_resolution()
    video.download()
    print("Successfully Downloaded")

elif resolution == "2":
    print("Downloading video ",video.title)
    video = video.streams.get_lowest_resolution()
    video.download()
    print("Successfully Downloaded")

elif resolution == "3":
    print("Downloading video ",video.title)
    video = video.streams.get_lowest_resolution()
    video.download()
    print("Successfully Downloaded")


elif resolution == "4":
    print("Downloading video ",video.title)
    video = video.streams.get_lowest_resolution()
    video.download()
    print("Successfully Downloaded")


elif resolution == "5":
    print("Downloading video ",video.title)
    video = video.streams.get_lowest_resolution()
    video.download()
    print("Successfully Downloaded")    


elif resolution == "6":
    print("Downloading video ",video.title)
    video = video.streams.get_lowest_resolution()
    video.download()
    print("Successfully Downloaded")
else:
    print("pilih diantara 1,2,3,4,5,6 :")