;;;;;READ davis data
;;;;;

;data1 = image of I
;data2 = bining data of data1
;data3 = Imean
;data4 = I'/Imean
;dread is directly of data



PRO read_davis_v3_NOBIN, date1, data4, dread

dread='E:\DATA\MCM ASI 2017_Processed\Jun17-18'

dread1 = FILE_SEARCH(dread + '\OH_caun????.tif')
time = N_ELEMENTS(dread1)
data1 = FLTARR(256, 256, time)
data2 = FLTARR(256, 256, time)
data3 = FLTARR(256, 256)
data4 = FLTARR(256, 256, time)

FOR i = 0, time - 1 DO BEGIN
  tempo = ROTATE(READ_TIFF(dread1(i)), 7)
 ;Note!! The prosudure "READ_TIFF" reads the tiff file upside down.
;  STOP
  data1(*,*,i) = tempo(32:319 - 32, *)
;  data1(*,*,i) = tempo(64:319, *)
;  STOP
ENDFOR
  FOR i = 0, 256 - 1 DO BEGIN
  FOR ii = 0, 256 - 1 DO BEGIN

;    data2(i,ii,*) = binning(data1(i,ii,*),6)
;    ;I changed the  INTERPOLATE(SMOOTH(data1(i,ii,*), 6),1,1, CEIL(time/6.))
;    ;because the 'smooth' will use width + 1 (7), if width is even.
;    ;And interpolate picks up arrays like bwlow
;    ;Array number 0 1 2 3 4 5 6 7 8 9 10 11 12 13
;    ;             *         *          * 
;;    STOP
    data3(i,ii) = MEAN(data1(i,ii,*))
  ENDFOR
  ENDFOR
;STOP
;RETURN

data4 = data2
FOR i = 0,  time - 1 DO BEGIN
  data4(*,*,i) = (data1(*,*,i) - data3)/data3 
  ;  STOP
ENDFOR
print,max(data4(*,*,*))
print,min(data4(*,*,*))
save,data4, filename='C:\Users\Kenneth\Desktop\ASInoBIN.sav'
;STOP
END