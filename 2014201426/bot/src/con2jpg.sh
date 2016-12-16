#!/bin/sh

rm -rf ~/BOT/data/jpg
mkdir ~/BOT/data/jpg
find ~/BOT/data/pic -name "*.jpg" | xargs -i cp {} ~/BOT/data/jpg

rm -rf ~/BOT/data/jpeg
mkdir ~/BOT/data/jpeg
find ~/BOT/data/pic -name "*.jpeg" | xargs -i cp {} ~/BOT/data/jpeg

rm -rf ~/BOT/data/gif
mkdir ~/BOT/data/gif
find ~/BOT/data/pic -name "*.gif" | xargs -i cp {} ~/BOT/data/gif

rm -rf ~/BOT/data/png
mkdir ~/BOT/data/png
find ~/BOT/data/pic -name "*.png" | xargs -i cp {} ~/BOT/data/png

ls -l ~/BOT/data/jpg | wc -l 
ls -l ~/BOT/data/jpeg | wc -l 
ls -l ~/BOT/data/png | wc -l 
ls -l ~/BOT/data/gif | wc -l 

rm -rf ~/BOT/data/pictures
mkdir ~/BOT/data/pictures
cp -r ~/BOT/data/jpg/. ~/BOT/data/pictures
cd ~/BOT/data/jpeg
for file in *.jpeg; 
    do convert $file ~/BOT/data/pictures/${file%%.*}.jpg; 
done;
cd ~/BOT/data/gif
for file in *.gif; 
    do convert $file ~/BOT/data/pictures/${file%%.*}.jpg; 
done;
cd ~/BOT/data/png
for file in *.png; 
    do convert $file ~/BOT/data/pictures/${file%%.*}.jpg; 
done;


#cat dog giraffe hyena sikadeer weasel chipmunk fox guinea\ pig reindeer squirrel wolf 

