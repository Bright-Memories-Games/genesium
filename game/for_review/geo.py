class Geo:
    def __init__(self, current_location):
        self.locations = ['Albis', 'Hestir', 'Nox', 'Willaldan', 'Hostalikon', 'Galerenon', 'Fernlander']
        self.current_location = current_location
        self.default_location = current_location

    def current(self):
        return self.current_location

    def reset(self):
        self.current_location = self.default_location

    def jump_to(self, new_location):
        self.current_location = new_location

samuel = Geo('Hostalikon')