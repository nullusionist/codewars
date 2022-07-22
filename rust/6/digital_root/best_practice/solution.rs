fn digital_root(n: i64) -> i64 {
    if n/10==0 {n} else {digital_root(n%10 + n/10)}
}