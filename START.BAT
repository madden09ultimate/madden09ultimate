@ECHO OFF
ECHO Welcome to the MADDEN 09 ISO MOD CREATION TOOL
ECHO '
ECHO '
ECHO '
pause

:start
ECHO Checking if installation files are in the correct folder...
IF EXIST MOD\SLUS_217.70 GOTO :check2
ECHO The Installation Files are not in the correct folders. Please re-read the instructions and try again!
PAUSE
EXIT

:check2
IF EXIST *.ISO GOTO :check3
ECHO A copy of the MADDEN 09 Football ISO Game is missing.
PAUSE
EXIT

:check3
IF EXIST IMGBURN.EXE GOTO :install
ECHO IMGBURN is Missing.
PAUSE
EXIT

:install
ECHO Preparing and Extracting Original MADDEN 09 Files and Patching MADDEN 09 NEXT Files...
ECHO Please wait a moment...
ECHO '
ECHO '
pause
rename *.iso MADDEN09.iso
mkdir next
powershell -ExecutionPolicy Bypass -File powershell.ps1

ECHO Extraction of Madden NFL 09 original game completed.
PAUSE

cd next

ECHO '
ECHO '
ECHO Installation File Location: Correct.
echo Continuing Set-Up. Deleting QKL files...
del DATA\*.qkl
echo Deleting ONLINE files...
rmdir /S /Q NETGUI
rmdir /S /Q EACN
rmdir /S /Q ONLINE
del DATA\CAFE*.DAT
del DATA\ONLINE.DAT
del DATA\OSDKSTRN.DAT
del DATA\UIONLINE.DAT
PAUSE

ECHO Patching Complete!
ECHO '
ECHO '
ECHO '
ECHO Running IMGBURN to create MADDEN 09 MOD ISO!
ECHO This may take a few moments to load and run. If prompted by IMGBURN, press YES each time!
  cd ..
  PAUSE
  IF EXIST "next\SYSTEM.CNF" GOTO :burn
  ECHO The installation did not copy files over correctly. Please try again with Run as Administrator, or use the Manual Method.
  PAUSE
  EXIT

:burn
  ImgBurn /mode build /src "next" /dest "Madden 09 Mod.iso" /volumelabel "MADDEN 09 MOD" /rootfolder /noimagedetails /start /overwrite yes /close
  ECHO MADDEN 09 MOD ISO Game successfully created!
  PAUSE

