from moviepy.editor import *
import whisper
import os

formato = "m4a"
diretorioA = "/content/Audios/"
diretorioT = "/content/Textos"

model = whisper.load_model("medium")
audios = []

if not os.path.exists(diretorioA):
    os.makedirs(diretorioA)
if not os.path.exists(diretorioT):
    os.makedirs(diretorioT)
  
def Conversor(formtato_x, mp3):
    wav_clip = AudioFileClip(formtato_x)
    wav_clip.write_audiofile(mp3)

for arquivo in os.listdir(diretorioA):
    if arquivo.endswith(f".{formato}"):
        audios.append(arquivo)
def Transcricao(i):
  Conversor(f"{diretorioA}{audios[i]}", f"{audios[i].split('.' + formato)[0]}.mp3")
  result = model.transcribe(f"{audios[i].split('.' + formato)[0]}.mp3")
  nome_arquivo = os.path.join(diretorioT, f"{audios[i].split('.' + formato)[0]}.txt")
  with open(nome_arquivo, "w") as arquivo:
      arquivo.write(result["text"])
  os.remove(f"{audios[i].split('.' + formato)[0]}.mp3")

for x in range(len(audios)):
    Transcricao(x)