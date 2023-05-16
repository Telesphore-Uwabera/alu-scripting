#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.empty?
  puts "Usage: ./regex_match.rb <string>"
  exit
end

# Retrieve the argument
input_string = ARGV[0]

# Match the regular expression
match = /School/.match(input_string)

# Print the matched string
puts match ? match[0] : ""

