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
