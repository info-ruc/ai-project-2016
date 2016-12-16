#!/bin/sh


DATA=/root/BOT/data
rm -rf $DATA/train_lmdb
convert_imageset --shuffle \
--resize_height=32 --resize_width=32 \
/root/BOT/data/pictures/ $DATA/train.txt $DATA/train_lmdb

rm -rf $DATA/test_lmdb
convert_imageset --shuffle \
--resize_height=32 --resize_width=32 \
/root/BOT/data/pictures/ $DATA/test.txt $DATA/test_lmdb


