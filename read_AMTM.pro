;;;;;READ davis data
;;;;;

;data1 = image of I
;data2 = bining data of data1
;data3 = Imean
;data4 = I'/Imean
;dread is directly of data



PRO read_AMTM, date1, data4, dread

for m=0 , 1 DO BEGIN
p=17+m
q=18+m


z='Jun'+string(p)+'-'+string(p)

Date=z.compress()
dread='F:\MCM AMTM 2017\'+Date+'\Processed'

;dread=dread5.compress()

IPB=2.   ; 'Images Per Bin'


dread1 = FILE_SEARCH(dread + '\BandOH_????????.tif')
time = N_ELEMENTS(dread1)
;data1 = FLTARR(200, 200, time)
;
;data2 = FLTARR(200, 200,CEIL(time/IPB))
;data3 = FLTARR(200, 200)
;data4 = FLTARR(200, 200,CEIL(time/IPB))


data1 = FLTARR(200, 200, time)

data2 = FLTARR(200, 200,CEIL(time/IPB))
data3 = FLTARR(200, 200)
data4 = FLTARR(200, 200,CEIL(time/IPB))



FOR i = 0, time - 1 DO BEGIN
  tempo = ROTATE(READ_TIFF(dread1(i)), 7)
 ;Note!! The prosudure "READ_TIFF" reads the tiff file upside down.
;  data1(*,*,i) = tempo(60:319 - 60, 28:255 - 28)
  data1(*,*,i) = tempo(32:319 - 32, *)

  
;  data1(*,*,i) = tempo(64:319, *)
;  STOP
ENDFOR
FOR i = 0, 200 - 1 DO BEGIN
  FOR ii = 0, 200 - 1 DO BEGIN
    data2(i,ii,*) = binning(data1(i,ii,*),IPB)
    ;I changed the  INTERPOLATE(SMOOTH(data1(i,ii,*), 6),1,1, CEIL(time/6.))
    ;because the 'smooth' will use width + 1 (7), if width is even.
    ;And interpolate picks up arrays like bwlow
    ;Array number 0 1 2 3 4 5 6 7 8 9 10 11 12 13
    ;             *         *          * 
;    STOP
    data3(i,ii) = MEAN(data2(i,ii,*))
  ENDFOR
ENDFOR
;STOP
;RETURN

FOR i = 0, CEIL(time/IPB) - 1 DO BEGIN
  data4(*,*,i) = (data2(*,*,i) - data3)/data3 
  ;  STOP
ENDFOR
;filename=filename2.compress()
save,data4,filename='E:\DATA\MCM AMTM 2017 Binned\AMTM_BAND_'+Date+'.sav'

ENDFOR
END