fn summation(n: i32) -> i32 {
    let mut res: i32 = n;
    for p in 0..n {
        res = res + p;
    }
    res
}
