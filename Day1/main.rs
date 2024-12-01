use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn readFile() -> str {
    // Create a path to the desired file
    let path = Path::new("example.txt");
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
        Ok(_) => print!("{} contains:\n{}", display, s),
    };
    return s;
}

fn main() {
    files = readFile();
}
