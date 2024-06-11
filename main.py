from pytube import YouTube
from pytube.cli import on_progress

def salvar_videao(link_do_video):
    print('iniciando download...')

    try:
        yt = YouTube(link_do_video, on_progress_callback=on_progress)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download()


        return '\n Download completo!'
    except:
        return "Não foi possivel baixar o video."
if __name__ =="__main__":
    while True:
        link_do_video = input('Informe o link do YouTube para baixar ou aperte Enter para encerrar o programa:')
        
        if link_do_video != '':
            print(salvar_videao(link_do_video))
            continue
        else:
           print('Programa encerrado!')
        break


