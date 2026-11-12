import numpy as np, wave
sr=44100; bpm=78; beat=60/bpm; bar=4*beat; dur=32
t=np.arange(int(sr*dur))/sr; out=np.zeros_like(t)
def f(n): return 440*2**((n-69)/12)
def ep(freq,start,length,amp):
    i0=int(start*sr)
    if i0>=len(out): return
    n=int(length*sr); tt=np.arange(n)/sr
    env=np.exp(-tt*1.8)*(1-np.exp(-tt*80))
    w=np.sin(2*np.pi*freq*tt)+0.35*np.sin(2*np.pi*2*freq*tt)*np.exp(-tt*3)+0.12*np.sin(2*np.pi*3*freq*tt)*np.exp(-tt*5)
    w*=1+0.003*np.sin(2*np.pi*5*tt)
    seg=amp*env*w; e=min(i0+n,len(out)); out[i0:e]+=seg[:e-i0]
def bell(freq,start,amp):
    i0=int(start*sr)
    if i0>=len(out): return
    n=int(2.5*sr); tt=np.arange(n)/sr
    w=(np.sin(2*np.pi*freq*tt)+0.5*np.sin(2*np.pi*freq*2.76*tt)+0.25*np.sin(2*np.pi*freq*5.4*tt))*np.exp(-tt*3)
    e=min(i0+n,len(out)); out[i0:e]+=amp*w[:e-i0]
# Cmaj7 - Am7 - Fmaj7 - G6 (C major), voicings
prog=[[48,64,67,71,76],[45,64,67,72,76],[41,64,69,72,76],[43,62,67,71,76]]
mel=[[79,76,74,76],[76,72,74,72],[72,69,72,76],[74,71,74,79]]
s=0.0; i=0
while s<dur:
    ch=prog[i%4]
    ep(f(ch[0]),s,bar*1.2,0.22)
    for k,n in enumerate(ch[1:]): ep(f(n),s+0.012*k,bar*1.1,0.10)
    ep(f(ch[0]+12),s+2*beat,bar*0.6,0.06)
    for k,n in enumerate(mel[i%4]):
        if (i//4)%2==1 or k%2==0: bell(f(n+12),s+k*beat+beat*0.5,0.035)
    s+=bar; i+=1
rng=np.random.default_rng(1); noise=rng.normal(0,1,len(t))
crackle=(rng.random(len(t))>0.9995)*rng.normal(0,0.6,len(t))
hiss=np.convolve(noise,np.ones(30)/30,'same')*0.01
out=out+hiss+crackle*0.05
# soft lowpass + fade
k=np.ones(6)/6; out=np.convolve(out,k,'same')
fade=np.minimum(1,np.minimum(t/1.5,(dur-t)/2.5)); out*=fade
out/=np.max(np.abs(out))*1.1
st=np.stack([out,np.roll(out,int(0.012*sr))*0.97],1)
w=wave.open('ads/music.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
w.writeframes((st*32767).astype('<i2').tobytes()); w.close()
