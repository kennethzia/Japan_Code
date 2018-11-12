;pro rothera_video
set_plot,'win'
device, decomposed=0
loadct,0
;STOP
;data4 = FINDGEN(301, 301, 100) * 0. + RANDOMN(seed, 301,301,100)

test = BYTSCL(data4 , TOP=!D.TABLE_SIZE , MAX=0.8, MIN=-0.8)
;test = BYTSCL(IMG_DIFF1 , TOP=!D.TABLE_SIZE , MAX=1500, MIN=500)

;STOP
ims = test;data4
s=size(ims)
x=2*s(1)
y=2*s(2)
fnum=s(3)

ims=rebin(ims,x,y,fnum)
print, x,y,fnum
;tvscl, ims(*,*,0)
;STOP
XINTERANIMATE,SET=[x,y,fnum],/SHOWLOAD
FOR I=0,fnum-1 DO begin
;  tvscl,ims(*,*,I)
  tv,ims(*,*,I)
  XINTERANIMATE,Window=!D.Window, Frame=I
ENDFOR
XINTERANIMATE,/KEEP_PIXMAPS

;stop

end