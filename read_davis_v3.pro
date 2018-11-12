;;;;;READ davis data
;;;;;

;data1 = image of I
;data2 = bining data of data1
;data3 = Imean
;data4 = I'/Imean
;dread is directly of data



PRO read_davis_v3, date1, data4, dread

TIC
;dread='E:\DATA\MCM ASI 2017_Processed\Jun18-19\SRCAUN'
dread='F:\MCM AMTM 2017\Jun18-19\Processed'
;dread="C:\Users\Kenneth\Desktop\AMTM_BANDOH Jun17-18"

;dread1 = FILE_SEARCH(dread + '\OH_srcaun????.tif') ;dt=10sec
dread1 = FILE_SEARCH(dread + '\BandOH_caun****.tif') ;dt=37sec
;dread1 = FILE_SEARCH(dread + '\TempOH_caun****.tif') ;dt=37sec
;dread1 = FILE_SEARCH(dread + '\P14_1_ff****.tif') ;dt=37sec


IPB=2.   ; 'Images Per Bin'

time = N_ELEMENTS(dread1)
data1 = FLTARR(256, 256, time)
data2 = FLTARR(256, 256, CEIL(time/IPB))
;data3 = FLTARR(256, 256)
data3 = FLTARR(256, 256, CEIL(time/IPB))
data4 = FLTARR(256, 256,  CEIL(time/IPB))
DI=FLTARR(CEIL(time/IPB))
FOR i = 0, time - 1 DO BEGIN
  tempo = ROTATE(READ_TIFF(dread1(i)), 7)
 ;Note!! The prosudure "READ_TIFF" reads the tiff file upside down.
;  STOP
  data1(*,*,i) = tempo(32:319 - 32, *)
;  data1(*,*,i) = tempo(64:319, *)
;  STOP
ENDFOR
;STOP
FOR i = 0, 256 - 1 DO BEGIN
  FOR ii = 0, 256 - 1 DO BEGIN
    data2(i,ii,*) = binning(data1(i,ii,*),IPB)+1.
    ;I changed the  INTERPOLATE(SMOOTH(data1(i,ii,*), 6),1,1, CEIL(time/6.))
    ;because the 'smooth' will use width + 1 (7), if width is even.
    ;And interpolate picks up arrays like bwlow
    ;Array number 0 1 2 3 4 5 6 7 8 9 10 11 12 13
    ;             *         *          * 

   ; data3(i,ii)=MEAN(data2(i,ii,*))

    FOR k = 0,  CEIL(time/IPB) - 1 DO BEGIN

    IF k lt 24 THEN BEGIN
      data3(i,ii,k) = MEAN(data2(i,ii,0:48))
    ENDIF ELSE BEGIN
    IF k gt 1118 THEN BEGIN
      data3(i,ii,k) = MEAN(data2(i,ii,CEIL(time/IPB)-50:CEIL(time/IPB) - 1))
    ENDIF ELSE BEGIN
      data3(i,ii,k) = MEAN(data2(i,ii,k-24:k+24))

    IF k lt 30 THEN BEGIN
      data3(i,ii,k) = MEAN(data2(i,ii,0:59))
    ENDIF ELSE BEGIN
    IF k gt CEIL(time/IPB)-40 THEN BEGIN
    data3(i,ii,k) = MEAN(data2(i,ii,CEIL(time/IPB)-61:CEIL(time/IPB) - 1))
    ENDIF ELSE BEGIN
    data3(i,ii,k) = MEAN(data2(i,ii,k-30:k+30))
   
    ENDELSE
    ENDELSE
    ENDELSE
    ENDELSE
ENDFOR
ENDFOR
ENDFOR
;STOP
;RETURN


FOR i = 0,  CEIL(time/IPB) - 1 DO BEGIN

  ;data4(*,*,i) = (data2(*,*,i) - data3(*,*))/data3(*,*)

  data4(*,*,i) = (data2(*,*,i) - data3(*,*,i))/data3(*,*,i) 
  ;data4(*,*,i) = -.1+0.2*(data4(*,*,i)-min(data4(128-20:128+20,128-20:128+20,i)))/(max(data4(128-20:128+20,128-20:128+20,i))-min(data4(128-20:128+20,128-20:128+20,i)))
 ;DI(i)=data4(128,128,i)
  ;DI(i)=(data2(128,128,i) - data3(128,128,i))/data3(128,128,i)
ENDFOR
print,min(data4)
print,max(data4)
;

;save,data4, filename='E:\DATA\MCM ASI 2017_Processed\MCM ASI 2017 Bin&IDLready\Jun18-19w2minBIN.sav'
save, data4, filename='C:\Users\Kenneth\Desktop\AMTM_BandOH_18-19.sav'
;WRITE_CSV,'C:/Users/Kenneth/Desktop/ASI(Norm)_70.csv',DI(*)




TOC
END