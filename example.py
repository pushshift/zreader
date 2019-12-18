#!/usr/bin/env python3

import zreader
import ujson as json



# Adjust chunk_size as necessary -- defaults to 16,384 if not specified
reader = zreader.Zreader("reddit_data.zst", chunk_size=8192)

# Read each line from the reader
for line in reader.readlines():
    obj = json.loads(line)
    print (obj['author'], obj['subreddit'], sep=",")

