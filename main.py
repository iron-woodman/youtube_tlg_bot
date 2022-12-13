# https://pytube.io/en/latest/user/channel.html
import os.path

from pytube import YouTube

def mp3_download(link):
    print(f'{link}: MP3 downloading...')
    youtubeObject = YouTube(link)
    try:
        # output = youtubeObject.streams.get_audio_only().download(output_path='mp3')
        output = youtubeObject.streams.filter(only_audio=True).desc().first().download(output_path='mp3')
        base, ext = os.path.splitext(output)
        new_file = base + '.mp3'
        os.rename(output, new_file)
    except:
        print("An error has occurred")
    print("Download is completed successfully")

def mp4_download(link):
    print(f'{link}: MP3 downloading...')
    youtubeObject = YouTube(link)
    try:
        output = youtubeObject.streams.get_lowest_resolution().download(output_path='mp4')
    except:
        print("An error has occurred")
    print("Download is completed successfully")

def main():
    link = 'https://www.youtube.com/watch?v=4w4sSabOjl0' #input("Enter the YouTube video URL: ")''
    mp3_download(link)
    # mp4_download(link)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
