class Version:
    MAYOR = 0
    MINOR = 0
    PATCH = 1

    def current(self):
        return "#{MAYOR}.#{MINOR}.#{PATCH}"
