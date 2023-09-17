## API ADVANCED

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

## Author

This project was created by **Telesphore Uwabera**.

## License

This project is open-source and available under the [License Name] license. See the [LICENSE](LICENSE) file for more details.
