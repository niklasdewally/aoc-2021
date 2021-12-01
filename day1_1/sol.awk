NR == 1 {prev = $1}
NR > 1 && $1>prev {count++}
NR > 1  {prev = $1}

END {print count}
