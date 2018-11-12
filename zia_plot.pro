pro ZIA_PLOT,data1,min1=min1,max1=max1,$
  wn=wn,title1=title1,ticknum=ticknum
  
  
  

  TIC
  set_plot,'ps'
  file_mkdir,'C:\Matsuda_FFT'
  DEVICE,filename='C:\Matsuda_FFT\Change2.ps'
  !except=0
  device, decomposed=0
  restore,'C:\Matsuda_FFT\7_24_0-59.sav'
  restore,'C:\Matsuda_FFT\VANESSA08_15_0-239.sav'
  
  change=FINAL_DATA-VANESSA4hr
  
  
;-------------plot the result-------------------------------------------------------
if not (keyword_set(Vp_min)) then Vp_min= 0.0            ;Wave speed minimum (m/s)
if not (keyword_set(Vp_max)) then Vp_max= 150.            ;Wave speed maximum (m/s)
xy2=Vp_max * 2 + 1 ;1201
;---------------------keyword setting------------------------------------------------
 wn=2 ;window number
  bw=33 ;color table
  if not(keyword_set(ticknum)) then ticknum=5
;---------------------circle setting------------------------------------------------
;make circle
nnew=vp_max/10
xcir=fltarr(nnew,(xy2-1)*2) & ycir=fltarr(nnew,(xy2-1)*2)
  xc=0.0 & yc=0.0
  cent=fltarr((xy2-1)*2) & cent(*)=0.0
 
  
  rad=(findgen(nnew)+1)*10.0
  pts=(2*!PI/((xy2-1)*2))*FINDGEN((xy2-1)*2)
  
 
    for r1=0,nnew-1 do begin
    xcir(r1,*)=xc+rad(r1)*cos(pts)
    ycir(r1,*)=yc+rad(r1)*sin(pts)
  endfor
  lin=FINDGEN((xy2-1)*2)-(xy2-1)

;================================================================================
;window setting
  !P.FONT=1
  DEVICE,/color,bits=8
  loadct,0,/silent
  !p.color=0 & !p.background=255 & !p.charsize=1.2
  p1=[5000,3000]  ;contour position(left bottom)
  b1=[p1(0),p1(1)-1000] ;colorbar position(left bottom)
;  wsize=[530,500]   ;window size
  cxy=[8000,8000]   ;contour boxes size
  bxy=[8000,500]   ;colorbar size  
  DEVICE,xsize=5.  *5.6/5.,ysize=5,/times,/INCHES;,/times;,yoffset=28.;,/landscape
;======================draw results==============================================
 ;make axis
            ;data1=total_result_new
data1=change

xlen_hurf = LONG((xy2 - 1) * 0.5)
  ax1=findgen(cxy(0))/float(cxy(0))*(float(xlen_hurf*2)+1.0)-float(xlen_hurf)
  ax1=fix(ax1)
  axr=[min(ax1),max(ax1)]
  data2=fltarr(cxy(0),cxy(0),2)
  lname=strcompress(string(abs(indgen((xlen_hurf/50) * 2 + 1)*50-xlen_hurf)),/remove_all)
  
  name01=replicate(' ',30)
  IF not keyword_set(min1) THEN min1 =min(data1) ;minimum value of spectral density to be plotted
  IF not keyword_set(max1) THEN max1=max(data1) ;maximum value of spectral density to be plotted
  
  if (keyword_set(min1)) or (min1 eq 0.0) then fmin=min(data1(*,*))
  if (keyword_set(max1)) then fmax=max(data1(*,*)) 
xrange=[fmin,fmax]
  
;data setting
  data2(*,*)=bytscl(congrid(data1(*,*),cxy(0),cxy(0)),min=fmin,max=fmax)
  Final_PhaseSpeed2=data1
;contour position(left bottom & right top)
  fpos3=[p1(0),p1(1),p1(0)+cxy(0),p1(1)+cxy(1)]
  
;colorbar position(left bottom & right top)
  bfpos3=[b1(0),b1(1),b1(0)+bxy(0),b1(1)+bxy(1)]
  
;bar setting
  fbar3=findgen(128,2) & fbar3(*,1)=fbar3(*,0)
  fbdata2=bytscl(congrid(fbar3,bxy(0),bxy(1)))
  fby3=fltarr(2) & fbx3=fmin+(findgen(128)*fmax*2)/127.0
;-----------------------------------------------------------------------------------
;draw contour
  loadct,bw,/silent
 
 tv,data2(*,*),p1(0),p1(1),xsize = 8000,ysize = 8000

;plot contour frames
  loadct,0,/silent
  contour,data2(*,*),ax1,ax1,/noerase,/device,/nodata,$
          yr=axr,xr=axr,position=fpos3,xs=1,ys=1,xtickname=name01,ytickname=name01,title=title1
  AXIS,YAxis=0,Vp_max * (-1.) - 30,0,ys=1,yr=axr, /data,yticks=(xlen_hurf/50)*2,yminor=(xlen_hurf/50) - 1,ytickname=lname,ytitle='phase speed [m/s]'
  
;plot circles
r3=(vp_max/10)-1
  for r2=0,r3 do $ 
    if ((r2+1) mod 5 eq 0) then oplot,xcir(r2,*),ycir(r2,*),linestyle=0 $
                           else oplot,xcir(r2,*),ycir(r2,*),linestyle=2
  oplot,lin,cent & oplot,cent,lin
  

;draw color bar
  loadct,bw,/silent
  tv,fbdata2,b1(0),b1(1),xsize = 8000,ysize = 500
  
;plot color bar frames
  loadct,0,/silent
  contour,fbar3,fbx3,fby3,/noerase,/nodata,/device,position=bfpos3,xrange=xrange,$
          xs=1,ys=1,xminor=1,xticks=ticknum,ytickname=replicate(' ',12),yminor=1,yticks=1$
          ,xtickformat='(f6.1)',xticklen=1.0;,xtitle='power spectral density'
          DEVICE,/close
  print,'plot end'
;================================================================================
 
 TOC



              ;save,final_PhaseSpeed2, filename='C:\Matsuda_FFT\7_24_0-59.sav'

end
