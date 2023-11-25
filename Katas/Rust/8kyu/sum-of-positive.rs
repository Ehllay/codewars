fn positive_sum(slice: &[i32]) -> i32 {
    let mut result: i32 = 0;

    for i in slice {
        if i > &0 {
            result += i
        }
    }
    result
}
