for /f "skip=1" %%x in ('wmic os get localdatetime') do if not defined mydate set mydate=%%x
echo %mydate%
set mydate=%mydate:+=-%
set mydate=%mydate:.=-%
echo %mydate%
python pprofile.py --format callgrind --out callgrind_%mydate%.cachegrind main.py