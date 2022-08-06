import json

class MembersDB:
    def __init__(self):
        self.__data__ = None

    def Save_DB_Values(self, Data_File):
        with open(Data_File) as json_file:
            self.__data__= json.loads(json_file)

    def get_data(self, name):
        for member in self.__data__['members']:
            if member['Name'] == name:
                return member

    def close(self):
        pass

