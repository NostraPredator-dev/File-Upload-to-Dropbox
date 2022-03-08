import dropbox
import os


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

    def upload_folders(self, local_dir, dropbox_dest):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(local_dir):
            for filename in files:

                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, local_dir)
                dropbox_path = os.path.join(dropbox_dest, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path)


def main():
    access_token = '8k2TAf5UpKgAAAAAAAAAAVrqNx06t7iceNzZvIdJulSyPlNGWPOyJcNEctZgGmcP'
    transfer_data = TransferData(access_token)

    file_from = input("Enter the path of file : ")
    file_to = input("Enter full path to upload to dropbox : ")  # The full path to upload the file to, including the file name

    # API v2
    transfer_data.upload_folders(file_from, file_to)
    print("File uploaded !!")


main()
