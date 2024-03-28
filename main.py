import requests
from bs4 import BeautifulSoup


def write_to_file(filename, data, mode='w'):
    try:
        with open(filename, mode, encoding='utf-8') as file:
            if isinstance(data, str):
                file.write(data)
            else:
                for line in data:
                    if "\n" in line:  # Remove new line characters
                        line = line.replace("\n", "")
                    print(line)
                    file.write(str(line) + '\n')
        print(f"Data written to '{filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_all_links(soup):
    links = []
    a_tags = soup.find_all('a')
    for a_tag in a_tags:
        href = a_tag.get('href')
        if href and '/product/' in href:
            links.append(href)
    return links


def main():
    links = None

    url = "https://140online.com/products.aspx?key=&Page=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        write_to_file("data.txt", data)
        soup = BeautifulSoup(data, 'html.parser')
        links = get_all_links(soup)
    else:
        print(f"Error: {response.status_code}")

    print(links)
    write_to_file("links.txt", links)


if __name__ == "__main__":
    main()
