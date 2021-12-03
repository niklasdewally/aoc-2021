$1 ~ /forward/ {horizontal += $2;}
$1 ~ /down/    {depth += $2}
$1 ~ /up/      {depth -= $2}
END {print horizontal*depth}
