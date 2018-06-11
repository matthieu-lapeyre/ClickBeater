#DATASET

YT_CB = [
'https://www.youtube.com/watch?v=pvXsvUOfgfo',
'https://www.youtube.com/watch?v=hjKvFNKgGNM',
'https://www.youtube.com/watch?v=AwTYgqwJNpw',
'https://www.youtube.com/watch?v=QZfO5bJSFWc',
'https://www.youtube.com/watch?v=GA3rsaHKqeY',
'https://www.youtube.com/watch?v=eJvoIIeeCVU',
'https://www.youtube.com/watch?v=Ap4MdMWbD1E',
'https://www.youtube.com/watch?v=qrmC1AWtAZk',
'https://www.youtube.com/watch?v=wXLpGEWrAWc',
'https://www.youtube.com/watch?v=9tqBR3yktG4',
'https://www.youtube.com/watch?v=09GjC67NF7s',
'https://www.youtube.com/watch?v=sqPYJkKnVNc',
'https://www.youtube.com/watch?v=CxbK9trGaMw',
'https://www.youtube.com/watch?v=oWlPbC3azz4',
'https://www.youtube.com/watch?v=208xkv6OtUk',
'https://www.youtube.com/watch?v=YNfTM0Eulbk',
'https://www.youtube.com/watch?v=yj1TtBz5urM',
'https://www.youtube.com/watch?v=z9NWsXqIQoQ',
'https://www.youtube.com/watch?v=UzmppP3BKOk',
'https://www.youtube.com/watch?v=ODZgSAeLlEQ',
'https://www.youtube.com/watch?v=JGNiafLl0iA',
'https://www.youtube.com/watch?v=Ohd7jGr26xk',
'https://www.youtube.com/watch?v=YXrAxtX7Q4M',
'https://www.youtube.com/watch?v=dKGovKb2tbA',
'https://www.youtube.com/watch?v=iIuIsdb_X1Q',
'https://www.youtube.com/watch?v=f7E3EVpjjSo',
'https://www.youtube.com/watch?v=l9z3shm_Ses',
'https://www.youtube.com/watch?v=5gAehKgG_mY',
'https://www.youtube.com/watch?v=56jXh_z7Ja0',
'https://www.youtube.com/watch?v=Z_T5FAZjMEI',
'https://www.youtube.com/watch?v=3u_J1P-DkN0',
'https://www.youtube.com/watch?v=3yWFNvQUv5c',
'https://www.youtube.com/watch?v=HiwAVOLoJKc',
'https://www.youtube.com/watch?v=XfLQ7wrwobo',
'https://www.youtube.com/watch?v=eSRYWDyybqg',
'https://www.youtube.com/watch?v=G1fZFCUKb5s',
'https://www.youtube.com/watch?v=fzspGt2WzgU',
'https://www.youtube.com/watch?v=y5YRzetgNjI',
'https://www.youtube.com/watch?v=3kPUyFEOMGM',
'https://www.youtube.com/watch?v=fZhIovdr8tM',
'https://www.youtube.com/watch?v=17-afg3YQ0Y',
'https://www.youtube.com/watch?v=RkSr_9D6fXs',
'https://www.youtube.com/watch?v=C-6FGEkeUag',
]

YT_Genuine = [
'https://www.youtube.com/watch?v=37StRy0LEbI',
'https://www.youtube.com/watch?v=VYOjWnS4cMY',
'https://www.youtube.com/watch?v=7whm4gM_KEY',
'https://www.youtube.com/watch?v=QcgyEVrYgNU',
]

if __name__ == '__main__':
    import shutil

    import requests 

    for link in YT_CB:
        url = 'https://img.youtube.com/vi/'+ link[-11:] +'/0.jpg'
        response = requests.get(url, stream=True)
        with open('data/clickbait_thumbnails/'+link[-11:] +'.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

    for link in YT_Genuine:
        url = 'https://img.youtube.com/vi/'+ link[-11:] +'/0.jpg'
        response = requests.get(url, stream=True)
        with open('data/YT_genuine_thumbnails/'+link[-11:] +'.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
