;Wrote by Kogure (2017/07/12)

FUNCTION binning, y, width

x = N_ELEMENTS(y)
bin_len = CEIL(FLOAT(x)/FLOAT(width))
;STOP
y_bin = FLTARR(bin_len)

FOR i = 0, bin_len - 1 DO BEGIN
  
  IF i ne bin_len - 1 THEN BEGIN
    y_bin(i) = mean(y(i*width : i *width + width - 1))
  ENDIF ELSE BEGIN
    y_bin(i) = mean(y(i*width : x - 1))
  ENDELSE
ENDFOR
;STOP
RETURN, y_bin

;example
;y = FINDGEN(10)
;y1 = binning(y,3)
;print,y1
;1.0000000       4.0000000       7.0000000       9.0000000



END




