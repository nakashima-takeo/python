text_to_display = "Python Test"
display_line_length = 51
character_used = "="

padding = (display_line_length - len(text_to_display) - 2) // 2

separation_line = character_used * display_line_length
display_line = character_used + " " \
    * padding + text_to_display \
    + " " * padding + character_used

print(separation_line)
print(display_line)
print(separation_line)