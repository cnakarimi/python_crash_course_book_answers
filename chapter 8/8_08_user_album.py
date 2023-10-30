def make_album(artist_name, album_title, number_songs=''):
    album = {'artist': artist_name,
             'title': album_title
             }
    if number_songs:
        album['tracknumbers'] = number_songs
    return album


while True:
    user_artist = input("who is the artist? ")
    user_album = input("what is the title of the album? ")
    print(make_album(user_artist, user_album))
    print('if you wanna make new album press 1')
    print('if you wanna quit press q')
    user_input = input('so what? ')
    if user_input == '1':
        continue
    if user_input == 'q':
        print("you exit from the app!")
        break
