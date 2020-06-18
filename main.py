from tbp import thepiratebay

def piratebay(book):
    TPB_TORRENTS = thepiratebay(book)
    for torrent in TPB_TORRENTS:
        print(f'THE PIRATE BAY: {torrent} \n')

def run():
    book = input('What book are you looking for?: ')
    piratebay(book)


if __name__ == '__main__':
    run()