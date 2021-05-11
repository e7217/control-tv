# from webdav3.client import Client
import webdav.client as wc
import option

client = wc.Client(option.options)
# client = Client(option.options)
print(client)
print(client.list(''))
for i in client.list():
    if i == 'playlist/':
        continue
    print(i)
    client.download(i, './temp/'+i)

# res1.write_async(local_path="~/Downloads/file1", callback)

