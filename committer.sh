TIMESTAMP=$(date -d "today" +"%Y%m%d-%H%M%S")
OUTDIR=${2:-'./tmp/'}
OUTFILE="${OUTDIR}${TIMESTAMP}"
git --no-pager diff --staged --name-only | zip $OUTFILE.zip -@
git rev-parse --abbrev-ref HEAD >> $OUTFILE.txt
echo $1 >> $OUTFILE.txt
