#!/usr/bin/env bash

cp settings/additional_words.csv settings/additional_words.bkp
cp settings/words_to_replace.csv settings/words_to_replace.csv.bkp
cp code/homophones.csv code/homophones.csv.bkp
notify-send.sh "Backed up existing lists"

if [ -f "settings/additional_words.csv.orig" ]; then
    cp settings/additional_words.csv.orig settings/additional_words.csv
    notify-send.sh "Restored original additional words list"
else
    echo> settings/additional_words.csv
    notify-send.sh "Nuke original additional words list"
fi
if [ -f "settings/words_to_replace.csv.orig" ]; then
    cp settings/words_to_replace.csv.orig settings/words_to_replace.csv
    notify-send.sh "Restored original words to replace list"
else
    echo> settings/words_to_replace.csv
    notify-send.sh "Nuked original words to replace list"
fi

echo >code/homophones.csv
notify-send.sh "Nuked homophones list"
