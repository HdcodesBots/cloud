import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
        
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        
        f = open(file_from , 'rb')
        dbx.files_upload(f.read() , file_to) 
    
def main():
    access_token = 'sl.A9PAQZMBJ4lFk4ETWcMUCOUlUGxfLP-0mytsBLIc_LWsP0Oa5qqaSsW8S1adS59uaCi6tdDk9ItSJRQNZ_CnSmGkcuRzGLtcNLzakqauRl6SzOX9CGdLcBAEC0sLJvuMxhajsJA'
    transferData = TransferData(access_token)
    
    file_from = "C:\\Users\\busin\\Downloads\\os"
    file_to = "C:\\Users\\busin\\Dropbox\\Python test"
    
    
    transferData.upload_file(file_from , file_to)
    
    print("The upload was successfull")
    
main()