import requests
from bs4 import BeautifulSoup
from colorama import Fore


print(Fore.YELLOW + '''
                                                                        Instagram: f8le
                                                                        Twitter or x: _f8le
.d88b.               8 w    8888                      8 w               888b.             
YPwww. .d88 8   8 .d88 w    8www .d8b. 8   8 8d8b. .d88 w 8d8b. .d88    8   8 .d88 Yb  dP 
    d8 8  8 8b d8 8  8 8    8    8' .8 8b d8 8P Y8 8  8 8 8P Y8 8  8    8   8 8  8  YbdP  
`Y88P' `Y88 `Y8P8 `Y88 8    8    `Y8P' `Y8P8 8   8 `Y88 8 8   8 `Y88    888P' `Y88   dP   
                                                                wwdP                dP    
                                                                                                                                                	—— ١١٣٩هـ / 1727م ——



''' + Fore.WHITE)


# Function to extract PHP files from a webpage
def extract_php_files(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all links on the page
        links = soup.find_all('a')
        
        # List to store PHP files
        php_files = []
        
        # Extract PHP files from links
        for link in links:
            href = link.get('href')
            if href.endswith('.php'):
                php_files.append(href)
        
        return php_files
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Failed to retrieve webpage:" + Fore.WHITE, e)
        return None

# Function to save PHP files to a text file
def save_to_file(php_files, filename):
    try:
        with open(filename, 'w') as file:
            for php_file in php_files:
                file.write(php_file + '\n')
        print(Fore.BLUE + "PHP files saved to" + Fore.WHITE, filename)
    except IOError as e:
        print(Fore.RED + "Error saving file:" + Fore.WHITE, e)

# Ask the user for the website URL
url = input(Fore.GREEN + "Enter the URL of the website: " + Fore.WHITE)

# Example usage
php_files = extract_php_files(url)

if php_files:
    print("PHP Files on", url+":")
    for php_file in php_files:
        print(php_file)

    
save_option = input(Fore.GREEN + "Do you want to save the PHP files to a text file? (yes/no): " + Fore.WHITE).lower()

if save_option == 'yes':
        filename = input(Fore.GREEN + "Enter the filename to save: " + Fore.WHITE)
        save_to_file(php_files, filename)
else:
    print(Fore.RED + "No PHP files found." + Fore.WHITE)
if php_files:
    print("PHP Files on", url+":")
    for php_file in php_files:
        print(php_file)
else:
    print(Fore.RED + "No PHP files found." + Fore.WHITE)
