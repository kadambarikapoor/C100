import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f= open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AxJ80xHcvT8QddeMMQVF5dpkJ3DFrTiY6lTZ6UfOXvMtsTashRsxcUEDQeUElMrotU7UO7fHjxL6_UCFNSuVN4_ttWue-ScEW9T8CwT2WPTst9Pl6ctGB5NHkT6aYImd5xgxbb8'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer. ")
    file_to = input("Enter the full path to upload to dropbox. ")
    transferData.upload_file(file_from, file_to)

    print("Files have been moved.")
if __name__ == '__main__':
    main()