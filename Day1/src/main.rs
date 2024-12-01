use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;
use std::time::{SystemTime, UNIX_EPOCH};

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

fn part1(a: &Vec<i32>, b: &Vec<i32>) -> i32 {
    let result: i32 = std::iter::zip(a, b).map(|(l, r)| (l - r).abs()).sum();
    result
}

fn part2(a: &Vec<i32>, b: &Vec<i32>) -> i32 {
    let mut result: i32 = 0;
    for value in a {
        let mut counter: i32 = 0;
        for num in b {
            if value == num {
                counter += 1
            }
        }
        result += value * counter
    }
    result
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        panic!("File name is required")
    }
    let file_name = &args[1];
    let files = read_file(file_name);
    let lines = files.lines();
    let mut data1: Vec<i32> = Vec::new();
    let mut data2: Vec<i32> = Vec::new();
    let start = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_nanos();
    for line in lines {
        let mut items = line.split_ascii_whitespace();
        data1.push(items.next().unwrap().parse::<i32>().unwrap());
        data2.push(items.next().unwrap().parse::<i32>().unwrap());
    }

    data1.sort();
    data2.sort();

    let part1_result = part1(&data1, &data2);
    let part_1_end = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_nanos();

    println!("Part 1: {}", part1_result.to_string());
    println!("Part 1 TTC: {}ns", part_1_end - start);

    let start_2 = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_nanos();
    let part2_result = part2(&data1, &data2);
    println!("Part 2: {}", part2_result.to_string());
    let end = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_nanos();
    println!("Part 2 TTC: {}ns", end - start_2);
    println!("\n");
    println!("TTC: {}ns", end - start)
}
