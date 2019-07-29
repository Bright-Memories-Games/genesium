class Geo:
    def __init__(self, init_geo):
        self.locations = ['Albis', 'Hestir', 'Nox', 'Willaldan', 'Hostalikon', 'Galerenon', 'Fernlander']
        self.current_geo = init_geo
        self.default_geo = init_geo

    def current(self):
        return self.current_geo

    def reset(self):
        self.current_geo = self.default_geo

    def jump_to(self, new_geo):
        if new_geo in self.locations:
            self.current_geo = new_geo
        else:
            return 1

samuel = Geo('Hostalikon')
