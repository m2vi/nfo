from pymediainfo import MediaInfo
from src.main import Main
import re


complete_path = input("Enter the path to the media file: ")

if (complete_path.find(".") == -1):
    print(f"Error: Invalid path ({complete_path})")
    exit(1)

imdb_id = input("Enter the IMDB ID: ")

if (not re.match(r"tt[0-9]*", imdb_id)):
    print(f"Error: Invalid IMDB ID ({imdb_id})")
    exit(1)

release_name = input("Enter the release name (optional): ")
if (release_name == ""):
    release_name = ".".join(complete_path.split("/")[-1].split(".")[0:-1])

media_info = MediaInfo.parse(complete_path)

nfo = Main(release_name, imdb_id, media_info,
           complete_path.replace(media_info.general_tracks[0].to_data()['file_name_extension'], ""))

nfo.create()
