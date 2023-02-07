# youtube2mp3.py - 
# download list of YouTube videos, download and convert to MP3
# install ffmpeg: https://phoenixnap.com/kb/ffmpeg-windows

import os
import youtube_dl

def download_video(url, directory):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f"{directory}/%(title)s.%(ext)s"
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    directory_name = "videos"
    audio_directory_name = f"audio-{directory_name}"

# flute music source: https://www.classicfm.com/discover-music/instruments/flute/best-pieces-music-ever/
# videos have scores 

    urls = [
        "https://www.youtube.com/watch?v=fx1qmXawwWw", # doppler hungarian pastoral fantasy
        "https://www.youtube.com/watch?v=ZxC7mf10_tQ", # Taktakishvili: Sonata for Flute and Piano
        "https://www.youtube.com/watch?v=3BTLp-atekY", # Henri Dutilleux - Sonatine for Flute and Piano(1943)
        "https://www.youtube.com/watch?v=IOIHDI3NqEQ", # Robert Muczynski - Three Preludes for Flute, Op. 18 (1962) 
        "https://www.youtube.com/watch?v=MN4pvzT8C6k", # Cécile Chaminade - Concertino for Flute and Piano
        "https://www.youtube.com/watch?v=LURy0hnWIEQ", # Carl Reinecke - Flute Concerto, Op. 283 (1908)
        "https://www.youtube.com/watch?v=uq4wN39Mhsw", # Bohuslav Martinů - Sonata for Flute and Piano
        "https://www.youtube.com/watch?v=C2dXTfjYPbE", # Francis Poulenc - Sonata for Flute and Piano  
    ]
        
    """
        urls = [
            "https://www.youtube.com/watch?v=b-9xGnbBHMI", # Claude Debussy: Syrinx
            "https://www.youtube.com/watch?v=5yofqm7JZyA", # André Jolivet - Chant de Linos for Flute, String Trio and Harp (1944) 
            "https://www.youtube.com/watch?v=A_oVkSExZvA"  # Messiaen, Olivier (1952): Le merle noir pour flûte et piano 
            "https://www.youtube.com/watch?v=LkjmvFeQrB0", # Mozart: Flute Concerto in D major, K. 314 
            "https://www.youtube.com/watch?v=vnz4T33Jl7I", # Prélude à l'après-midi d'un faune - Debussy
            "https://www.youtube.com/watch?v=Evm0asqfd7U", # Paul Taffanel - Andante Pastoral et Scherzettino (1907) 
            "https://www.youtube.com/watch?v=u7wl43HBVPA", # Bach, BWV 1030 - Flute Sonata in B Minor 
            "https://www.youtube.com/watch?v=xlx-Ieisw0I", # Siegfried Karg: Elert Sonata (Appassionata) 
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "https://www.youtube.com/watch?v=xoTZGQDY1V8",
            "https://www.youtube.com/watch?v=d-diB65scQU"
        ]
    """

    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    if not os.path.exists(audio_directory_name):
        os.makedirs(audio_directory_name)

    for url in urls:
        video_filename = f"{url.split('=')[-1]}.mp4"
        audio_filename = f"{url.split('=')[-1]}.mp3"
        video_filepath = f"{directory_name}/{video_filename}"
        audio_filepath = f"{audio_directory_name}/{audio_filename}"
        if not os.path.exists(video_filepath):
            download_video(url, directory_name)
        if not os.path.exists(audio_filepath):
            os.system(f"ffmpeg -i {video_filepath} -vn -ab 192k {audio_filepath}")

if __name__ == '__main__':
    main()
