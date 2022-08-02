from pytube import Search

s = Search(' apocalypse')
for v in s.results:
  print(f"{v.title}\n{v.watch_url}\n")

# get object keys
# keys = "\n".join([k for k in s.results[0].__dict__])
# print(keys)