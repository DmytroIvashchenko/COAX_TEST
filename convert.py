# You are working on a project for TikTok.
# The future project will be a web-site of all public GIF images.
# You need to write a function that converts TikTok video to GIF.
# The input parameter is url address of TikTok video, i.e. "TikTok example".
# The output parameter is path to GIF image, i.e. "/home/user/TikTok-example-1.gif".
# Use library moviepy for convert video MP4 to GIF
from moviepy.editor import *
from TikTokApi import TikTokApi

with TikTokApi() as api:
    # in url of video copy id this video
    video = api.video(id="7109616178955422982")

    # Bytes of the TikTok video
    video_data = video.bytes()

    # open and write out file
    with open("tiktok_video.mp4", "wb") as out_file:
        out_file.write(video_data)


# convert mp4 file to gif
def create_gif():
    clip = VideoFileClip('tiktok_video.mp4')
    # gif file length
    clip = clip.subclip(0, 9)
    # making a gif
    clip.write_gif("tiktok_video.gif")


create_gif()




