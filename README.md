# 🎬 YouTube Video Downloader

## 🌐 Overview
This script allows you to download YouTube videos using the Pytube library. It reads a list of YouTube video URLs from a file (`urls.txt`) and attempts to download each video in the highest resolution possible (1080p, 720p, 480p, or 360p with audio or only audio ).

## ✅ Prerequisites
- Make sure your device has python 3.11
- Run `pip install -r requirements.txt`

## ✨ Usage
- Run `python app.py` in your termimal or command prompt
![Alt text](images_for_readme\Screenshot 2024-04-28 112933.png?raw=true "Title")


### 🔹 Download a video
1. Get your video url first, example: https://www.youtube.com/watch?v=C6SsborFYJw

2. 

### 🔹 Download a playlist
1. Run the script using the command `python playlist.py` in your terminal or command prompt.
2. Enter the playlist URL when prompted.

## 📤 Output
- Downloaded videos will be stored in the 'Youtube_Videos' folder in the script's directory.
- The script will remove successfully downloaded video URLs from the `urls.txt` file.
- If an error occurs during the download, the script will print an error message and continue to the next video.

## 🖊️ Note
- If the 'Youtube_Videos' folder does not exist, the script will create it.
- The script prioritizes downloading videos in the following resolutions: 720p, 480p, and 360p with audio.
- If a video cannot be downloaded due to an error, the error message will be displayed, and the script will proceed to the next video.

## ⚠️ Disclaimer
This script is for educational and personal use only. Respect the intellectual property rights of the content creators and adhere to YouTube's terms of service.

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🖥️ Author
Thang Le-Huy Nguyen

