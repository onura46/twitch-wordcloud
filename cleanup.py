import os

class Cleanup():
    def erase_save():
        if os.path.exists('save') == False:
            os.mkdir('save')
        dir = 'save'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
