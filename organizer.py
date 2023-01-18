from PIL import Image
import os

#path of folders
downloadsFolder = r'PATH\OF\DOWNLOADS\FOLDER'

#path of folders where files are moved
picturesFolder = r'PATH\OF\PICTURES'
musicsFolder = r'PATH\OF\MUSICS'
docsFolder = r'PATH\OF\DOCS'

if __name__ == '__main__':

    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in ['.jpg', '.jpeg', '.png']:
            picture =   Image.open(f'{downloadsFolder}\{filename}')
            picture.save(f'{picturesFolder}\{filename}', optimize=True, quality=60)
            os.remove(f'{downloadsFolder}\{filename}')

        if extension in ['.mp3']:
            os.rename(f'{downloadsFolder}\{filename}', f'{musicsFolder}\{filename}')

        if extension in ['.pdf', '.doc', '.docx', '.xlsx', '.xls', '.csv', '.pptx']:
            os.rename(f'{downloadsFolder}\{filename}', f'{docsFolder}\{filename}')