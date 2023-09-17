# Reddit API Project

This project is a collection of Python scripts that interact with the Reddit API to retrieve information about subreddits and their posts. Each script serves a specific purpose related to Reddit data extraction.

## Scripts

### 1. `0-subs.py`

This script retrieves the number of subscribers for a given subreddit using the Reddit API.

#### Usage:

```python
number_of_subscribers(subreddit)
```

### 2. `1-top_ten.py`

This script retrieves and displays the top 10 hot posts (sorted by upvotes) for a given subreddit using the Reddit API.

#### Usage:

```python
top_ten(subreddit)
```

### 3. `2-recurse.py`

This script recursively retrieves all hot post titles for a given subreddit. It continues fetching until there are no more posts to retrieve.

#### Usage:

```python
recurse(subreddit)
```

### 4. `3-count.py`

This script counts the occurrences of specified words in the titles of hot posts for a given subreddit using the Reddit API.

#### Usage:

```python
count_words(subreddit, word_list)
```

## How to Run

To run these scripts, make sure you have Python 3.x installed on your system. You also need the `requests` library, which can be installed using pip:

```bash
pip install requests
```

After installing the required libraries, you can run the scripts using Python in your terminal or IDE.

Example:

```bash
python 0-subs.py
```


# Ruby Regex Match Tool

A simple Ruby script for matching and extracting strings using regular expressions.

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Description

The Ruby Regex Match Tool is a command-line utility designed to match and extract strings from an input string using regular expressions. It provides several regex patterns and examples for matching different types of strings.

## Usage

Before running the script, make sure you have Ruby installed on your system.

To run the script, use the following command:

```bash
./regex_match.rb <string>
```

Replace `<string>` with the input string you want to match against. The script will then display the matched results based on various regular expressions.

## Examples

Here are some examples of how to use the script:

- Matching and printing the string "School":

```bash
./regex_match.rb "This is a School example. School is fun."
```

- Matching and printing strings using different regular expressions:

```bash
./regex_match.rb "hbttn hbtttn hbttttn hbtttttn"
```

- Extracting specific information from a string:

```bash
./regex_match.rb "[from: Alice][to: Bob][flags: important]"
```

## Contributing

If you would like to contribute to this project, feel free to open issues or pull requests on the [GitHub repository](https://github.com/yourusername/regex-match-ruby).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Make sure to replace `<string>` with your actual usage instructions, and update the "Contributing" section with a link to your project's GitHub repository if you have one. Additionally, if you choose to license your project differently, update the "License" section accordingly.

Save this content in a file named `README.md` in your project's root directory.

## Author

This project was created by **Telesphore Uwabera**.

## License

This project is open-source and available under the [License Name] license. See the [LICENSE](LICENSE) file for more details.
