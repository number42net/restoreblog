#!/bin/bash
mkdir -p "$@"/fullsize

date=$(echo $@ | awk '{ print $1 }')
name=$(echo $@ | awk '{for (i=2; i<NF; i++) printf $i " "; print $NF}')

cat > "$@"/project.yaml <<- EOM
project:
  published: false
  name: "$name"
  status: In progress
  start_date: "$date"
  thumbnail: img_001.jpg
  description: 
    - "Short description"
    - ""
    - "- List item 1"
EOM

cat > "$@"/index.md <<- EOM
# $name

Intro

##### Work done:

* Line item 1
* Line Item 2

##### Planned work:

* Line item 1
* Line Item 2

# Exterior inspection:
EOM