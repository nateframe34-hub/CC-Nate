import subprocess as sp, sys
R='/home/user/CC-Nate/retro-handheld/ads/batch-1/renders'
ADS={'8V_A_Best-find':('Best Christmas find','this year 🎄'),
     '8V_B_Husbands-gift':("Found my husband's",'Christmas gift 😭'),
     '8V_C_Original-RUN':("Gamers, RUN don't WALK",'to Target for this! 🎁')}
SC='scale=720:1280:flags=lanczos,fps=30,setsar=1'
# The Target footage has its old caption burned in (x 66-653, y 212-351 at 720x1280); delogo erases it after 3.3 s.
# Hook caption fades out at 3.3-3.7 s (after the store hook, like the Target ad's top text); CTA fades in at 18 s.
# voice segments kept from AD 7 (source seconds); the cut-out gaps are near-silent
A=[(0.00,3.30),(4.20,10.75),(11.05,15.70),(16.05,19.55),(19.90,24.40)]
af=''.join(f"[1:a]atrim={s}:{e},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.01,afade=t=out:st={e-s-0.012:.3f}:d=0.012[a{i}];" for i,(s,e) in enumerate(A))
af+=''.join(f'[a{i}]' for i in range(len(A)))+f'concat=n={len(A)}:v=0:a=1[au]'
vf=(f"[0:v]trim=0:3.3,setpts=PTS-STARTPTS,{SC}[v1];"
    f"[0:v]trim=3.3:11.8,setpts=(PTS-STARTPTS)/0.759,{SC},delogo=x=60:y=205:w=600:h=153[v2];"
    f"[1:v]trim=4.4:7.9,setpts=PTS-STARTPTS,{SC}[v3];"
    f"[1:v]trim=19.9:24.4,setpts=PTS-STARTPTS,{SC}[v4];"
    "[v1][v2][v3][v4]concat=n=4:v=1:a=0[vc];"
    "[2:v]format=rgba,fade=t=out:st=3.3:d=0.4:alpha=1[hb];[3:v]format=rgba,fade=t=in:st=18.0:d=0.3:alpha=1[cb];"
    "[vc][hb]overlay=4:145:shortest=1[o1];[o1][cb]overlay=4:145:shortest=1[v];")
sp.run(['python3.13','v4/big_bubble.py','v8/cta.png','Free shipping 🚚','Order by Dec 11 🎄'],check=True)
for name,(l1,l2) in ADS.items():
    sp.run(['python3.13','v4/big_bubble.py',f'v8/{name}.png',l1,l2],check=True)
    sp.run(['ffmpeg','-v','error','-y','-i','v/v7.mp4','-i','v/v6.mp4','-loop','1','-framerate','30','-t','22.5','-i',f'v8/{name}.png','-loop','1','-framerate','30','-t','22.5','-i','v8/cta.png',
            '-filter_complex',vf+af,'-map','[v]','-map','[au]','-t','22.5','-c:v','libx264','-crf','19','-preset','medium',
            '-c:a','aac','-b:a','160k','-movflags','+faststart',f'{R}/{name}.mp4'],check=True)
    print(name,'built')
