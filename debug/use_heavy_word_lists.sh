#!/usr/bin/env bash

cp settings/additional_words.csv.bkp settings/additional_words.csv
cp settings/words_to_replace.csv.bkp settings/words_to_replace.csv
cp code/homophones.csv.bkp code/homophones.csv
notify-send.sh "Restored heavy .csv lists"
