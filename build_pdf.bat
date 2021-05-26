rem Run this from a MikTeX prompt

rem PATH needs to include Python environment scripts, Python, and Perl
PATH=%PATH%;C:\Users\dsx\environments\OpenAgWA\;C:\Users\dsx\environments\OpenAgWA\Scripts;C:\StrawberryPerl\perl\bin

rem Make sphinx update the latex files first
make latexpdf

rem then build the PDF
build\latex\make.bat all-pdf

rem copy the PDF to the repo root
copy build\latex\openag.pdf openag_docs.pdf