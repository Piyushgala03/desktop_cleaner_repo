import os

def create():
    try:
        if os.path.exists('C:\\Users\\Admin\\Desktop\\All Files'):
            mov()
        else:
            os.mkdir('C:\\Users\\Admin\\Desktop\\All Files')
            mov()
    except Exception as e:
        print(e)


def mov():
    try:
        extensions=['.txt', '.mp4', '.mkv', '.jpg','.jpeg', '.png', '.mp3', '.zip', '.tar', '.java', '.py', '.cpp', '.pdf', '.doc','.docx', '.ppt','pptx', '.xls','.xlsx', '.ico','.csv','.gif','.heic','heif','.html','.htm','json']
        allfiles=os.listdir('C:\\Users\\Admin\\Desktop')
        for i in allfiles:
            for j in extensions:
                if i.endswith(j):
                    if os.path.exists(f'C:\\Users\\Admin\\Desktop\\All Files\\{(j.strip(".")).upper()}'):
                        os.rename(f'C:\\Users\\Admin\\Desktop\\{i}',f'C:\\Users\\Admin\\Desktop\\All Files\\{(j.strip(".")).upper()}\\{i}')
                    else:
                        os.mkdir(f'C:\\Users\\Admin\\Desktop\\All Files\\{(j.strip(".")).upper()}')
                        os.rename(f'C:\\Users\\Admin\\Desktop\\{i}',f'C:\\Users\\Admin\\Desktop\\All Files\\{(j.strip(".")).upper()}\\{i}')
    except Exception as e:
        print(e)

create()