import os
import glob
import logging

class EximCLeanup:

    def __init__(self):
        self.logger = logging
        self.logger.basicConfig(level=logging.INFO)
        self.base_path = '/nfs/mail'


    def get_files_from_directory(self, test_path=None):
        if test_path:
            self.base_path = test_path
        files = glob.glob(f"{self.base_path}/*")
        return files

    def update_permissions(self, files):
        self.logger.info(f"Updating permissions!")
        for path in files:
            self.logger.info(f"Updating {path}.")
            os.system(f'chmod u=rwx,g=rx+s,o=rx {path}')
            self.check_permissions(path)

    def check_permissions(self, path):
        read_check = os.access(path, os.R_OK)
        write_check = os.access(path, os.W_OK)
        self.logger.info(f"Read Permissions: {read_check}")
        self.logger.info(f"Write Permissions: {write_check}")

    def controller(self):
        self.logger.info(f"Starting Cleanup on {self.base_path}")
        files = self.get_files_from_directory()
        self.update_permissions(files)


if __name__ == '__main__':
    exim = EximCLeanup()
    exim.controller()
