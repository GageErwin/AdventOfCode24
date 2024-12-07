use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;
use std::time::Instant;

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

fn part1(rules: Vec<(i32, i32)>, checks: Vec<&str>) -> i32 {
    let mut result = 0;
    for check in checks {
        let nums: Vec<&str> = check.split(",").collect();
        let values: Vec<i32> = nums.iter().map(|&v| v.parse::<i32>().unwrap()).collect();
        let mut valid: bool = true;
        for (before, after) in &rules {
            if values.contains(before) || values.contains(after) {
                let mut before_index = 0;
                match &values.iter().position(|b| b == before) {
                    Some(index) => before_index = index.clone(),
                    None => continue,
                };
                let mut after_index: usize = 0;
                match &values.iter().position(|a| a == after) {
                    Some(index) => after_index = index.clone(),
                    None => continue,
                };
                if before_index > after_index {
                    valid = false;
                }
            }
        }
        if valid == true {
            result += values[values.len() / 2]
        }
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
    let mut rules: Vec<(i32, i32)> = Vec::new();
    let mut checks: Vec<&str> = Vec::new();
    for line in data.lines() {
        if line.contains("|") {
            let values: Vec<&str> = line.split("|").collect();
            let value1 = match values[0].parse::<i32>() {
                Err(_) => panic!("invalid number"),
                Ok(num) => num,
            };
            let value2 = match values[1].parse::<i32>() {
                Err(_) => panic!("invalid number"),
                Ok(num) => num,
            };
            rules.push((value1, value2))
        } else if line.contains(",") {
            checks.push(line);
        }
    }
    let part_1 = part1(rules, checks);
    let start = Instant::now();
    assert_eq!(part_1, 143);
    println!("Part 1 {}", part_1);
    let duration = start.elapsed();
    println!("TTC: {:?}ns", duration.as_nanos());
}
