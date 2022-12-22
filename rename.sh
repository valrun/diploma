#!/bin/bash
cd /Users/vryndina/study/d-dataset

for dir in * ;
  do
  let inc=1
  for i in $dir/* ;
    do mv "$i" "$dir/$dir-$inc.jpg"
    let inc=$inc+1
  done;
done
