# 이미지/동영상/음악파일을 화면에 보여주는 방법

import streamlit as st

# 이미지 처리를 위한 라이브러리
from PIL import Image 


def main() :
    # 1. 저장되어있는 이미지 파일을 화면에 표시하는 방법
    img = Image.open('./data/image_03.jpg')

    st.image(img)

    st.image(img, width=500)

    st.image(img, use_column_width=True)

    # 2. 인터넷상에 있는 이미지를 화면에 표시하는 방법
    # 인터넷상의 ㅣ이미지 : URL 이 있다!!

    url = 'https://img.freepik.com/free-photo/close-up-athlete-playing-soccer_23-2150845600.jpg?t=st=1713855709~exp=1713859309~hmac=ae96cb9fdaeda7eac1d9caba3f213493f09a990e90025c3c2bf11ce1e07dcbcd&w=996'
    st.image(url)

    # 동영상 파일
    video_file = open('./data/video1.mp4','rb')
    st.video(video_file)

    # 오디오 파일
    audio_file = open('./data/song.mp3','rb')
    st.audio(audio_file.read(), format='audio/mp3')

    

if __name__ == '__main__':
    main()