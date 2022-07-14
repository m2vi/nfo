class Helper:
    def exportMediaInfo(self, mediainfo, path):
        f = open(path, "w")
        f.write(mediainfo)
        f.close()

    def exportText(self, nfo, out):
        f = open(f"{out}{nfo['RELEASE']}.nfo", "w")
        f.write(self.__dictToText(nfo))
        f.close()

    def __dictToText(self, dict):
        rows = []

        for i in range(len(list(dict.items()))):
            key, value = list(dict.items())[i]

            rows.append(
                f"{self.__appendDots(key)} {value} {'🦜' if i in [1, 6] else ''}".replace("🦜", "\n"))

        return '\n'.join(rows)

    def __appendDots(self, key, length=13):
        key = f"{key} "

        while len(key) != length and not (len(key) > length):
            key += '.'

        return key


helper = Helper()
