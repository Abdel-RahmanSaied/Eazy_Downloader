# from pytube import Playlist
#
# class Play_list_download():
#     def __init__(self  ):
#
#         # self.playlist_url = playlist_url
#         # self.playlist_url = input("Enter th url of the playlist")
#         # purl = Playlist(self.playlist_url)
#         self.download_progress = True
#         self.video_name = ''
#         # self.start_download()
#
#     def start_download(self , playlist_url):
#         # self.playlist_url = input("Enter th url of the playlist")
#         play_list = Playlist(playlist_url)
#         print(f'Downloading: {playlist_url.title}')
#         while self.download_progress == True :
#             for video in play_list.videos:
#                 if self.download_progress == True:
#                     self.video_name = video.title
#                     print(self.video_name)
#                     st = video.streams.get_highest_resolution()
#                     st.download()
#                     video.streams.first().download()
#                 else:
#                     break
#
#             self.download_progress = False
#             print(self.download_progress)
#
# Play_list_download().start_download("https://www.youtube.com/watch?v=UPFKAG9rYOE&list=PLknwEmKsW8OtK_n48UOuYGxJPbSFrICxm")


text = "https://www.youtube.com/watch?v="

print(len(text))
