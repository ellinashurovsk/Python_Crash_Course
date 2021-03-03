favorite_languages = {
    'Benjamin': 'python',
    'sarah': 'c',
    'Amelia': '',
    'Emma': '',
    'Elijah': 'ruby',
    'Evelyn': '',
    'James': 'python'
}

for key, value in favorite_languages.items():
    if value == '':
        print(
            f'Please {key.title()} write down your favorite programming language.')
    else:
        print(f'{key.title()} thank you for the participation.')
