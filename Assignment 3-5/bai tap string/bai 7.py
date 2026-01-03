def get_filename(path):
    return path.replace('/', '\\').split('\\')[-1]
def get_song_name(path):
    file = get_filename(path)
    return file.split('.')[0]
path = "d:\\music\\muabui.mp3"
print(get_filename(path))
print(get_song_name(path))
