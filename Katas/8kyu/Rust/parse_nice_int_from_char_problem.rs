fn get_age(age: &str) -> u32 {
    let a = age.chars().take(1).last().unwrap();
    return a.to_string().parse::<u32>().unwrap();
}
