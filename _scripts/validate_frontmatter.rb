#!/usr/bin/env ruby
require 'psych'
errors = []
Dir.glob('**/*.{md,html}').sort.each do |path|
  next if path.split('/').any? { |part| %w[.git _site vendor node_modules .bundle].include?(part) }
  text = File.read(path, encoding: 'UTF-8')
  next unless text.start_with?("---\n", "---\r\n")
  front = text.split(/^---\s*$\r?\n?/, 3)[1]
  begin
    raise 'Missing closing front matter delimiter' unless text.scan(/^---\s*$/).size >= 2
    Psych.parse_stream(front)
  rescue Psych::Exception, RuntimeError => e
    errors << "#{path}: #{e.message}"
  end
end
abort errors.join("\n") unless errors.empty?
puts 'All source front matter parses successfully.'
