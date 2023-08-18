class Version:
    MAYOR = 0
    MINOR = 0
    PATCH = 1

    def current(self):
        return f"{self.MAYOR}.{self.MINOR}.{self.PATCH}"

    def correct_version(self, version):
        curr = self.current()
        return version == curr
