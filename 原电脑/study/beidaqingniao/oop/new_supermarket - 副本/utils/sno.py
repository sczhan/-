class Sno:
    __number = 0

    @staticmethod
    def get_no():
        Sno.__number += 1
        return Sno.__number


