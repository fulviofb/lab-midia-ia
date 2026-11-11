import subprocess, sys, numpy as np
def frames(f):
    raw=subprocess.run(['ffmpeg','-loglevel','error','-i',f,'-f','rawvideo','-pix_fmt','gray','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.uint8).reshape(-1,540,960).astype(np.int16)
for f in sys.argv[1:]:
    F=frames(f)
    # região do morro já pronta e parada entre f31 e f95 (antes da sombra)
    r=F[31:95,330:420,450:960]
    d=np.abs(np.diff(r,axis=0)).mean(axis=(1,2))
    # região do sol depois de pronto (f97..f149)
    s=F[97:149,60:200,650:790]; ds=np.abs(np.diff(s,axis=0)).mean(axis=(1,2))
    print(f, 'linha parada: mudança média/quadro', round(d.mean(),3),'máx',round(d.max(),3),'| sol pronto:',round(ds.mean(),3),'máx',round(ds.max(),3))
