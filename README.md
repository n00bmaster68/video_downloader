# 🎬 YouTube Video Downloader

## 🌐 Overview
This script allows you to download YouTube videos using the Pytube library. It reads video URLs and attempts to download each video in the highest resolution possible (1080p, 720p, 480p, or 360p with audio or only audio).

## ✅ Prerequisites
- Make sure your device has python 3.11
- Run `pip install -r requirements.txt`

## ✨ Usage
- Run `python app.py` in your termimal or command prompt
![[Starting UI]](images_for_readme/Screenshot%202024-04-28%20112933.png)

### 🔹 Download a video
1. Get your video url first, example: https://www.youtube.com/watch?v=C6SsborFYJw
2. Then put it in input url entry
3. Select your desired resolution and remember choose type as video
4. Click download, choose folder to save, and wait
![[Demo UI: downloading video]](images_for_readme/Screenshot%202024-04-28%20114203.png)

### 🔹 Download only audio of video
1. Get your video url first, example: https://www.youtube.com/watch?v=C6SsborFYJw
2. Then put it in input url entry
3. Select your desired resolution and remember choose type as audio
4. Click download, choose folder to save, and wait
![[Demo UI: downloading video audio]](images_for_readme/Screenshot%202024-04-28%20114426.png)

### 🔹 Show information of video
1. Get your video url first, example: https://www.youtube.com/watch?v=C6SsborFYJw
2. Then put it in input url entry
3. Click "show info"
![[Demo UI: show information of video]](images_for_readme/Screenshot%202024-04-28%20114652.png)

## 📤 Output
- Downloaded videos/audios will be stored in the chosen folders.
- If an error occurs during the download, the script will print an error message.

## ⚠️ Disclaimer
This script is for educational and personal use only. Respect the intellectual property rights of the content creators and adhere to YouTube's terms of service.

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🖥️ Author
Thang Le-Huy Nguyen

