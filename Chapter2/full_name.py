first_name = "ada"
last_name = "lovelace"

# use f-strings. The f is for format because python formats
#  the string by replacing the name of any variable in braces with its values
full_name = f"{first_name} {last_name}"
print(full_name)
message = f"Hello, {full_name.title()}"
print(f"Hello, {full_name.title()}")
print(message)

# earlier format syntax
full_name = "{} {}".format(first_name, last_name)
print(full_name.title())

# add a tab
print("Python")
print("\tPython")
print("\nPython")
print("Languages:\nPython\nC\nJavaScript")

# stripping white space
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

not_favorite = '     C++ '

print(favorite_language.rstrip())
print(not_favorite.lstrip())
not_favorite = not_favorite.rstrip()
print(not_favorite.rstrip())
not_favorite = not_favorite.lstrip()
print(not_favorite)
