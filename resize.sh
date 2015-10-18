#/usr/bin/env sh

# Resize pictures to 2048px wide. Requires ImageMagick.

for i in $(cat pics.txt); do convert -monitor DSC_${i}.JPG -resize 2048 finished/DSC_${i}.JPG; done
