#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.empty?
  puts "Usage: ./regex_match.rb <string>"
  exit
end

# Retrieve the argument
input_string = ARGV[0]

# Match the regular expression against the input string
matches = input_string.scan(/School/)

# Concatenate the matches
concatenated_string = matches.join

# Print the concatenated string and its length
#puts "#{concatenated_string} (#{concatenated_string.length} chars long)"
puts ARGV[0].scan(/hbt*n/).join
