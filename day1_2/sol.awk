{prevs[NR] = $1}
NR > 3 && (prevs[NR] + prevs[NR-1] + prevs[NR-2]) > prevWindow {count++}
NR > 2 {prevWindow = prevs[NR] + prevs[NR-1] + prevs[NR-2]}
END {print count}
