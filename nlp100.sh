#!/bin/bash
set -eu

# ch2
curl -sS http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt -o ./ch2/hightemp.txt
cp -a ./ch2/hightemp.txt ./ch2/src/hightemp.txt

# ch3
curl -sS http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz -o ./ch3/jawiki-country.json.gz
gunzip -c ./ch3/jawiki-country.json.gz > ./ch3/jawiki-country.json
cp -a ./ch3/jawiki-country.json ./ch3/src/jawiki-country.json

# ch4
curl -sS http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt -o ./ch4/neko.txt
cp -a ./ch4/neko.txt ./ch4/src/neko.txt

# ch5
cp -a ./ch4/neko.txt ./ch5/neko.txt

# ch7
curl -sS http://www.cl.ecei.tohoku.ac.jp/nlp100/data/artist.json.gz -o ./ch7/src/artist.json.gz
gunzip -c ./ch7/src/artist.json.gz > ./ch7/src/artist.json
