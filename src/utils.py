import time
import imdb
from functools import reduce, cache


class Utils:
    def duration(self, general):
        return time.strftime('%H:%M:%S', time.gmtime(general['duration']/1000))

    def video(self, video):
        return f"{video['format']} {video['width']}x{video['height']} @ {video['frame_rate']}fps [{video['other_bit_rate'][0]}]"

    def size(self, general):
        return general['other_file_size'][0]

    def audio(self, audio_tracks):
        lt = []

        for audio_track in audio_tracks:
            data = audio_track.to_data()
            channels = reduce(lambda x, y: float(x) + float(y), data['other_channel_positions'][0].split(
                "/"))
            lt.append(
                f"{data['other_language'][0]} {data['format']} {channels}")

        return ", ".join(lt)

    def subs(self, text_tracks):
        lt = []

        for text_track in text_tracks:
            data = text_track.to_data()
            if (data['title']):
                lt.append(data['title'])
                continue

            lt.append(
                f"{data['other_language'][0]}{' Forced' if (data['forced'] == 'Yes') else ''}")

        return ", ".join(lt)

    @cache
    def imdb(self, imdb_id):
        ia = imdb.Cinemagoer()
        data = ia.get_movie(imdb_id.replace("tt", ""))

        return {
            "LINK": f"https://www.imdb.com/title/{imdb_id}/",
            "RATING": f"{data['rating']}/10",
            "GENRE": ", ".join(data['genres']),
            "PLOT": data['plot'][0],
        }


utils = Utils()
