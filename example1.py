from moviepy.editor import *
#Add movie as object in python
video = VideoFileClip('filename.mp4')
#Take clip between specific time range in s
clip = video.subclip(30,50)
#rotate video by specific amt
rotated = video.rotate(180)

#add text to video
#Creating text to add along with duration and where to appear
text_clip = TextClip('text', fontsize = 70, color = 'white').set_position('center').set_duration(10)
result = CompositeVideoClip([video,text_clip]) #overlays text onto video
#save as new video
result.write_videofile('new_filename.mp4',fps = 60)