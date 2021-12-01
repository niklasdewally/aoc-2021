NR==1 {a = $1}
NR==2 {b = $1}
NR > 3 && ($1 + a + b) > prevWindow {count++}
NR > 2 {prevWindow = $1 + a + b ;a=b;b=$1}
END {print count}
