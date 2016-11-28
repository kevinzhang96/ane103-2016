# resizes all files in a given folder to be at most 1024x1024 (aspect fit)
# usage: ./resize.sh folder

for i in "$1"/*
do
    if [ -d "$i" ]; then
        loop "$i"
    elif [ -e "$i" ]; then
        convert $i -resize 1024x1024 "$i"
    else
        echo "$i"" - Folder Empty"
    fi
done
