fn to_alternating_case(s: &str) -> String {
    let mut alt = String::new();
    // B
    for char in s.chars() {
        if char.to_uppercase().to_string() != char.to_string() {
            alt.push_str(&char.to_uppercase().to_string());
        } else if char.to_lowercase().to_string() != char.to_string() {
            alt.push_str(&char.to_lowercase().to_string());
        } else {
            alt.push(char);
        }
    }
    alt
}
