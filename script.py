from pytubefix import YouTube

url = input("Enter video url: ")
video = YouTube(url)
downloader = video.streams.get_highest_resolution()
downloader.download()