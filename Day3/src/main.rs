use regex::Regex;
use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn read_file(file_name: &String) -> String {
    // Create a path to the desired file
    let path = Path::new(&file_name);
    let display = path.display();

    // Open the path in read-only mode
    let mut file = match File::open(&path) {
        Err(why) => panic!("could not open {}: {}", display, why),
        Ok(file) => file,
    };

    // Read the file contents into a string
    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("could no open file {}: {}", display, why),
        Ok(_) => file,
    };
    return s;
}

fn part1(data: String) -> i32 {
    let mut result: i32 = 0;
    let re = Regex::new(r"mul\(\d+,\d+\)").unwrap();
    let num = Regex::new(r"\d+").unwrap();
    let values: Vec<&str> = re.find_iter(&data).map(|m| m.as_str()).collect();
    for n in values {
        let ints: Vec<&str> = num.find_iter(n).map(|m| m.as_str()).collect();
        let value1 = ints[0].parse::<i32>().unwrap();
        let value2 = ints[1].parse::<i32>().unwrap();
        result += value1 * value2;
    }
    result
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        panic!("File name is required")
    }
    let file_name = &args[1];
    let data = read_file(file_name);
    let part_1_result = part1(data);
    println!("Part 1: {}", part_1_result);
}
