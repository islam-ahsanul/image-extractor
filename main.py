import cv2
import os


def extract_frames_opencv(video_path, output_folder, interval=2):
    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
    frame_interval = int(fps * interval)  # Frames to skip

    count = 0
    saved_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if count % frame_interval == 0:
            output_path = os.path.join(output_folder, f'frame{saved_count}.jpg')
            cv2.imwrite(output_path, frame)
            saved_count += 1
        count += 1

    cap.release()
    print("Extraction complete.")


# Usage
video_path = 'video.mp4' 
output_folder = './frames'
extract_frames_opencv(video_path, output_folder)
