# compresses all images in a given folder; 85 quality, progressive compression, small gaussian, strip exif
# usage: ./resize.sh folder

for i in "$1"/*
do
    if [ -d "$i" ]; then
        loop "$i"
    elif [ -e "$i" ]; then
        convert -strip -interlace Plane -gaussian-blur 0.05 -quality 85% $i $i
    else
        echo "$i"" - Folder Empty"
    fi
done
