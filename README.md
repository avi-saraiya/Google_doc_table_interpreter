# Google Doc Table Interpreter

## Overview

This Python program retrieves a webpage's content, extracts specific coordinate-based character data using regex, and reconstructs a grid-like structure based on the extracted information. The output is printed in an organized format, representing the original layout of the data.

## Features

Fetches text content from a given URL.

Extracts x-coordinates, y-coordinates, and corresponding characters using regex.

Sorts the extracted data to reconstruct a structured grid.

Prints the grid in a readable format.

## Requirements


Ensure you have Python 3.x installed on your system.

You also need to install the following dependencies:

pip install requests beautifulsoup4

## How It Works

### Retrieve Webpage Content

The get_page_content(url) function fetches the text content from the given URL using the requests library and parses it with BeautifulSoup.

Extract Data Using Regex

The parse_grid_data(content) function uses regex to find patterns in the text and extracts x-coordinates, y-coordinates, and characters.

### Sort and Print Grid

The print_grid_from_coordinates(url) function:

Combines x and y coordinates into tuples.

Maps coordinates to their corresponding characters.

Sorts the tuples to ensure correct grid alignment.

Prints characters in the correct order to visually represent the original structure.

## Usage

Run the script by executing:

![image](https://github.com/user-attachments/assets/2f1963f3-aa87-4695-8958-76c416eedc6a)

The script will fetch data from the predefined URL and print the structured grid.

### Example Output

The following is the output when the link in the code is used as input:

![image](https://github.com/user-attachments/assets/0afc9d34-c8c5-444b-9f50-589319eb8f0e)

(The actual output depends on the webpage data.)

## Notes

The script currently processes specific Unicode characters (░█▀). If the webpage content format changes, the regex pattern may need adjustments.

The URL used in the script should contain data in the expected format; otherwise, results may vary.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

