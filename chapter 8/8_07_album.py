def make_album(artist_name, album_title, number_songs=''):
    album = {'artist': artist_name,
             'title': album_title
             }
    if number_songs:
        album['tracknumbers'] = number_songs
    return album


print(make_album('Kendrick Lamar', "To pimp a butterfly", number_songs=16))
print(make_album('Kanye West', "My Beautiful Dark Twisted Fantasy"))
print(make_album('Taylor Swift', "1889"))
print(make_album('Pink Floyd',
      'The Dark Side of the Moon', number_songs=10))
