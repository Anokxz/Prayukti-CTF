use std::io::{self, Write};

const FLAG_NUMS: &str = "flag{rusTY_HAND";
const FLAG_END: &str = "$_iN_WOrk}";

fn main() {
    print!("Enter a number: ");
    io::stdout().flush().unwrap();

    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");

    let num: i32 = match input.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Invalid input. Please enter a number.");
            return;
        }
    };

    if num == 696969 {
        println!("Flag Found!");
        println!("Flag {}{}", FLAG_NUMS, FLAG_END);
    } else {
        println!("Creds Mismatch. Hehe...");
        println!("Try again Kiddo ;)");
    }
}
