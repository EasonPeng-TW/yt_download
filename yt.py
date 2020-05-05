from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?time_continue=1&v=UV5WIyHuKgQ&feature=emb_title')
path = 'C:\\Users\\2058\\Desktop\\coding\\youtube_download\\'
# print(yt.streams.filter(progressive=True).all())
yt.streams.filter(res='720p', subtype='mp4', progressive=True).first().download(path)
print('檔案下載完成!')