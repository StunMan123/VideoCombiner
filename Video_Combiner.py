from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

# Directory containing the video files
directory = "C:/Users/ASUS/Desktop/FYP_image_photo/RecFiles/20240507/h00"

#since directory shows the path but dont know what is inside, below shows and extract what is inside
#os.listdir(directory) if f.endswith(('.mp4', '.avi', '.mov')) list all video (.mp4, .avi, .mov) files in specific directory
video_files = [f for f in os.listdir(directory) if f.endswith(('.avi'))] #output list of filesname, filter out videos
video_files.sort() # Sort files alphabetically and numerically

# Check each file for compatibility issues
for file in video_files:
    filepath = os.path.join(directory, file) #combine directory with files name 
    #VideoFileClip - create object representing video in 'filepath', after this step then we can access properties and perform operations on those videos (duration, audio track, video content, etc.)
    clip = VideoFileClip(filepath) 
    video_duration = clip.duration #output videos duration
    audio_duration = clip.audio.duration if clip.audio is not None else 0

    print(f"File: {file} - Video Duration: {video_duration}, Audio Duration: {audio_duration}")

    #good practice, close the clip to free resources so that other program can also run
    clip.close()

video_files.sort()
print(f"Files to concatenate: {video_files}")

# Create a list of VideoFileClip objects
clips = [VideoFileClip(os.path.join(directory, file)) for file in video_files] #different from above, this is list, above is not

# Concatenate the video clips
final_clip = concatenate_videoclips(clips)

# Write the result to a new file
final_output = os.path.join(directory, "combined_video.mp4")
#video codec (coder-decoder :encoder and decoder) is a technology or software that compresses and decompresses digital video
final_clip.write_videofile(final_output, codec='libx264')

# Close all the clips
for c in clips:
    c.close()
print("Video has been successfully created at:", final_output)
