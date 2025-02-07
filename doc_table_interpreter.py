'''The following program has been written by Avi Saraiya on 5th January, 2025.'''

import requests
import re
from bs4 import BeautifulSoup

# The function below gets information from the url and stores it in the response variable
def get_page_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser') # This line generates the word soup and stores it in the soup variable
    content = soup.get_text()  # Extracts all text and stores in content variable
    return content

# The function below uses regex, and fills up x-coordinate, y-coordinate and characters lists, and returns all 3
def parse_grid_data(content):
    x_coords = []
    y_coords = []
    characters = []
    pattern = r"(\d{1,2})\s*([░█▀])\s*(\d)"
    matches = re.findall(pattern, content) #Looks for regex matches
    for match in matches:
            x = int(match[0])
            char = match[1]
            y = int(match[2])
            x_coords.append(x)
            y_coords.append(y)
            characters.append(char)
    
    return x_coords, y_coords, characters

'''The following function is like the main function in this program. 
   it first looks through the url for the necessary information about the x and y coordinates, and the corresponding unicode characters
   the funtion then combines the x and y coordinates into a tuple
   then, the function creates a dictionary with these tuples as keys, and the corresponding characters as values
   it also creates a sorted list of these tuple keys such that the order goes from the top left to the bottom right of the figure to be printed out
   finally, based on the order in the sorted list, the corresponding characters are printed out by referencing the dictionary
   '''
def print_grid_from_coordinates(url):
    content = get_page_content(url)
    
    if content:
        # Parse the content to get coordinates and characters
        x_coords, y_coords, characters = parse_grid_data(content)
                
        # Create a dictionary to map coordinates to characters
        coord_map = {}
        for x, y, char in zip(x_coords, y_coords, characters):
            coord_map[(x, y)] = char

        # Sort the coordinates: by y descending, x ascending
        sorted_coords = sorted(coord_map.keys(), key=lambda t: (-t[1], t[0]))
        # Print the grid, each row on a new line
        current_y = None
        for x, y in sorted_coords:
            if y != current_y:
                if current_y is not None:
                    print()  # To change line
                current_y = y
            print(coord_map[(x, y)], end='')

# Given url
url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
#other url: https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub

# Main function call
print_grid_from_coordinates(url)