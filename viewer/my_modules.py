import os
from .models import file_list, movie_name
from datetime import datetime
from django.db import IntegrityError
import subprocess
from .OpenSubtitlesDownload import opensubtitledownload

def file_lister(dir):
    manual_check = []
    for dirnames, dirpath, filenames in os.walk(dir):
        subtitle_Strings = (".srt", ".idx", ".sub")
        if dirpath:
            manual_check.append(dirnames)
        else:
            for file in filenames:
                m_name_only = dirnames.split('\\')[-1]
                f_path = os.path.join(dirnames, file)
                filesize = os.path.getsize(f_path)
                filedate = datetime.fromtimestamp(os.path.getmtime(f_path))
                try:
                    if any (s in file for s in subtitle_Strings):
                        m_name = movie_name(moviename = m_name_only,
                                            has_subtitle = True)
                        m_name.save()
                        f_info = file_list(m_name=movie_name.objects.get(moviename=m_name_only),
                                           file_name=file,
                                           file_path=f_path,
                                           file_size=filesize,
                                           file_date=filedate,
                                           is_subtitle=True)
                        f_info.save()
                    else:
                        m_name = movie_name(moviename = m_name_only,
                                            has_subtitle = False)
                        m_name.save()
                        f_info = file_list(m_name=movie_name.objects.get(moviename=m_name_only),
                                           file_name=file,
                                           file_path=f_path,
                                           file_size=filesize,
                                           file_date=filedate,
                                           is_subtitle=False)
                        f_info.save()
                except IntegrityError as e:
                    if 'UNIQUE constraint failed' in e.args[0]: # or e.args[0] from Django 1.10
                        try:
                            if any(s in file for s in subtitle_Strings):
                                existing_m_name = movie_name.objects.get(moviename=m_name_only)
                                existing_m_name.has_subtitle = True
                                existing_m_name.save()
                                f_info = file_list(m_name=movie_name.objects.get(moviename=m_name_only),
                                                   file_name=file,
                                                   file_path=f_path,
                                                   file_size=filesize,
                                                   file_date=filedate,
                                                   is_subtitle=True)
                                f_info.save()
                            else:
                                f_info = file_list(m_name=movie_name.objects.get(moviename=m_name_only),
                                                   file_name=file,
                                                   file_path=f_path,
                                                   file_size=filesize,
                                                   file_date=filedate,
                                                   is_subtitle=False)
                                f_info.save()
                        except IntegrityError as e:
                            if 'UNIQUE constraint failed' in e.args[0]:  # or e.args[0] from Django 1.10
                                print(file + 'already in database\n')
                                break

    return manual_check




def file_delete(file):
    obj = file_list.objects.get(file_name = file)
    try:
        os.remove(obj.file_path)
        obj.delete()
    except OSError:
        pass


def downloader(f_name):
    obj = file_list.objects.get(file_name=f_name)
    file = obj.file_path
    opensubtitledownload(file)





























"""

def file_lister(dir):
    subtitle_Strings = (".srt", ".idx", ".sub")
    for dirnames, dirpath, filenames in os.walk(dir):
        for file in filenames:
            m_name_only = dirnames.split('\\')[-1]
            f_path = os.path.join(dirnames, file)
            filesize = os.path.getsize(f_path)
            filedate = datetime.fromtimestamp(os.path.getmtime(f_path))
            try:

            
            
                m_name = movie_name(moviename=m_name_only)
                m_name.save()

                f_info = file_list(m_name=movie_name.objects.get(moviename=m_name_only),
                                   file_name=file,
                                   file_path=f_path,
                                   file_size=filesize,
                                   file_date=filedate)
                f_info.save()

            except IntegrityError as e:
                if 'UNIQUE constraint failed' in e.args[0]:  # or e.args[0] from Django 1.10
                    try:
                        print ('trying to add file\n')
                        f_info = file_list(m_name=movie_name.objects.get(moviename=m_name_only),
                                           file_name=file,
                                           file_path=f_path,
                                           file_size=filesize,
                                           file_date=filedate)
                        f_info.save()
                    except IntegrityError as e:
                        if 'UNIQUE constraint failed' in e.args[0]:  # or e.args[0] from Django 1.10
                            print('probably exists in database')
                            
                            
"""