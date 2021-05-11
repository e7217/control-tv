# from webdav3.client import Client
import webdav.client as wc
import option

client = wc.Client(option.options)
# client = Client(option.options)
print(client)
print(client.list(''))
client.pull(remote_directory='플레이리스트', local_directory='./temp')

# res1.write_async(local_path="~/Downloads/file1", callback)

