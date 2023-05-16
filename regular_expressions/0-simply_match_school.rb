#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.empty?
  puts "Usage: ./regex_match.rb <string>"
  exit
end

# Retrieve the argument
input_string = ARGV[0]

# Match the regular expression against the input string
match = input_string.match(/School/)

# Print the matched string or an empty string if no match
puts match ? match[0] : ""

