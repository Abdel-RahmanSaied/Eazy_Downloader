from pytube import Search

s = Search(' cairoke')
for v in s.results:
  print(f"{v.title}\n{v.watch_url}\n")

