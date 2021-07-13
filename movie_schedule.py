current_movies = {
    'The Grinch': '11:00 AM',
    'Rudolph': '1:00 PM',
    'Frosty the Snowman': '3:00 PM',
    'Christmas Vacation': '5:00 PM'
}

print('We are showing the following movies:')
for key in current_movies:
    print(key)

movie = input('What movie do you want the showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
    print('the movie you selected is not currently showing')
else:
    print(movie, 'is showing at', showtime)
