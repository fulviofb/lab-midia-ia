"""Folha de conferência: quadro-chave + 1º, meio e último quadro de cada clipe (uma linha por plano).
uso: python folha_quadros.py saida.png clipe1.mp4 [clipe2.mp4 ...]"""
import subprocess, sys, json, io
from PIL import Image, ImageDraw
def dur(f):
    return float(json.loads(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","json",f],capture_output=True,text=True).stdout)["format"]["duration"])
def quadro(f,t):
    b=subprocess.run(["ffmpeg","-v","error","-ss",f"{t:.3f}","-i",f,"-frames:v","1","-f","image2pipe","-vcodec","png","-"],capture_output=True).stdout
    return Image.open(io.BytesIO(b)).convert("RGB")
out,clips=sys.argv[1],sys.argv[2:]
linhas=[]
for c in clips:
    d=dur(c); ims=[quadro(c,t) for t in (0,d/2,max(d-0.1,0))]
    w=480; ims=[i.resize((w,int(i.height*w/i.width))) for i in ims]
    linhas.append(ims)
W=480*3+40; H=sum(l[0].height for l in linhas)+20*(len(linhas)-1)
folha=Image.new("RGB",(W,H),"white"); y=0
for l in linhas:
    for k,i in enumerate(l): folha.paste(i,(k*500,y))
    y+=l[0].height+20
folha.save(out); print(out, folha.size)
