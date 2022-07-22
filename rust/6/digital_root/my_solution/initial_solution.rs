fn digital_root(n: i64) -> i64 {
    let mut sum = 0i64;
    let mut num = n;
    while num > 0 {
        sum = sum + (num % 10);
        num = num / 10;
        if num == 0 && sum >= 10 {
            num = sum;
            sum = 0;
        }
    }
    sum
}