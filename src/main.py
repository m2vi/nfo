import subprocess
import re
from .helper import helper
from .utils import utils


class Main:
    def __init__(self, release_name, imdb_id, media_info, out="./out/"):
        self.release_name = release_name
        self.imdb_id = imdb_id
        self.media_info = media_info
        self.out = out
        pass

    def create(self):
        release_name, imdb_id, media_info, out = self.release_name, self.imdb_id, self.media_info, self.out

        general = media_info.general_tracks[0].to_data()

        video = media_info.video_tracks[0].to_data()
        audio_tracks = media_info.audio_tracks
        text_tracks = media_info.text_tracks

        nfo = {
            "RELEASE": release_name,
            "SOURCE": "",


            "SIZE": utils.size(general),
            "DURATION": utils.duration(general),
            "VIDEO": utils.video(video),
            "AUDIO": utils.audio(audio_tracks),
            "SUBS": utils.subs(text_tracks),

            **utils.imdb(imdb_id),
        }

        info = subprocess.check_output(
            ["mediainfo", "--output=FMT", f"{out}/{release_name}.{general['file_extension']}", "> {out}/info.txt"], encoding='utf-8')

        info = re.sub(r"^Complete name.*\n", "", info, flags=re.MULTILINE)

        helper.exportMediaInfo(info, f"{out}/info.txt")

        helper.exportText(nfo, out)
