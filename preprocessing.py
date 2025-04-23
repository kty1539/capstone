import glob
from moviepy.editor import VideoFileClip, concatenate_videoclips

# make_clip_video(원본 경로, 저장할 클립명, 시작 시간, 끝 시간)
def make_clip_video(path, save_path, start_t, end_t):
    clip_video = VideoFileClip(path).subclip(start_t, end_t)
    clip_video.write_videofile(save_path)

paths = sorted(glob.glob('train_video/*.mp4'))
no = 1004

for path in paths:
    print(path)
    start_t = int(input('abnormal 1 - 시작 시간 :'))
    if start_t == 0:
        continue
    end_t = start_t + 10
    output = 'videos/' + str(no) + '_abnormal.mp4'
    make_clip_video(path, output, start_t, end_t)
    
    start_t = int(input('normal 1 - 시작 시간 :'))
    if start_t == 0:
        continue
    end_t = start_t + 10
    output = 'videos/' + str(no) + '_normal.mp4'
    make_clip_video(path, output, start_t, end_t)

    no = no + 1

    start_t = int(input('abnormal 2 - 시작 시간 :'))
    if start_t == 0:
        continue
    end_t = start_t + 10
    output = 'videos/' + str(no) + '_abnormal.mp4'
    make_clip_video(path, output, start_t, end_t)

    start_t = int(input('normal 2 - 시작 시간 :'))
    if start_t == 0:
        continue
    end_t = start_t + 10
    output = 'videos/' + str(no) + '_normal.mp4'
    make_clip_video(path, output, start_t, end_t)

    no = no + 1  