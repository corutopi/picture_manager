from pathlib import Path
import os


class MainModel:
    def __init__(self):
        self.folder_path = None  # folder path string
        self.picture_files: list = None  # picture file path string list

    def set_file(self, file_path):
        """Set folder and selected picture form file_path"""
        '''check file exists and file extension'''
        if not os.path.isfile(file_path):
            raise IOError
        # @todo implements check extension
        '''get parent folder path and set'''
        p = Path(file_path)
        self.set_folder(p.parent)
        pass

    def set_folder(self, folder_path):
        """Set folder and read picture files in the folder"""
        '''check folder exists'''
        # @todo implements
        '''set path'''
        self.folder_path = folder_path
        self.reload_folder()

    def reload_folder(self):
        p = Path(self.folder_path)
        print('local folder :' + str(p))
        print('parent folder:' + str(p.parent))
        self.picture_files = list(map(lambda x: str(x), p.glob('*.jpg')))

    def get_next(self, file_name):
        num = self.picture_files.index(file_name)
        if num == len(self.picture_files) - 1:
            return self.picture_files[0]
        else:
            return self.picture_files[num + 1]

    def get_prev(self, file_name):
        num = self.picture_files.index(file_name)
        if num == 0:
            return self.picture_files[-1]
        else:
            return self.picture_files[num - 1]

    def delete_file(self, file_name):
        """delete file from folder_path
        @todo implements 'file_name list' delete
        """
        import send2trash
        send2trash.send2trash(os.path.join(self.folder_path, file_name))
        self.reload_folder()


if __name__ == '__main__':
    import sys
    import pprint
    # pprint.pprint(sys.path[1])

    m = MainModel()
    m.set_folder(os.path.join(sys.path[1], 'SamplePicture'))
    pprint.pprint(list(map(lambda x: str(x), m.picture_files)))
    # l = list(map(lambda x: x.name, m.picture_files))
    # print(l)
    # for i in l:
    #     print(i)

