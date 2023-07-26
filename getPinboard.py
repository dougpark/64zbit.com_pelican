# https://github.com/lionheart/pinboard.py
import pinboard
import os.path
from urllib.parse import urlparse

exec(open('config/.token').read())

pb = pinboard.Pinboard(pinboard_token)

# most recent update
print('Most recent update: ' + str(pb.posts.update()))

# add search for Link tag
# Add search for public
results = pb.posts.all(tag=["link"])
#print("post="+str(results))
#print(results["date"])
#print(results["user"])
#print(results["posts"])
#posts = results["posts"]
for bookmarks in results:
    # print(bookmarks.url)
    # print(bookmarks.description)
    # print(bookmarks.extended)
    # print(bookmarks.tags)
    # print(bookmarks.shared)
    # print(bookmarks.toread)
    # print(bookmarks.time)
    # print('----------------')
    #print(result["posts"][2].url)
    #print(result["posts"][2])

    path_to_file = 'content/Link/link_'+str(bookmarks.time)+'.md'
    if not os.path.exists(path_to_file):
        print(path_to_file)
        with open(path_to_file, 'w') as f:
            f.write('Title: '+bookmarks.description+'\n')
            f.write('Date: '+str(bookmarks.time)+'\n')
            f.write('Author: Link\n')
            f.write('Category: Link\n')
            f.write('Tags: ')
            for tag in bookmarks.tags:
                f.write(tag+', ')
            f.write('\n')
            summary = bookmarks.extended.split('\n')
            f.write('Summary: '+ str(summary[0])+'\n')
            f.write('\n')

            domain = urlparse(bookmarks.url).netloc
            f.write('## [Read the full article at '+domain+']('+bookmarks.url+')\n')

            # Add markdown blockquote > to each line
            # https://ubuntuforums.org/showthread.php?t=1110854
            text = bookmarks.extended 
            joined_group = '\n'.join(["> %s" % line for line in text.split('\n')]) 
            f.write(joined_group+'\n')

            f.write('\n')
            #f.write('[Link to the original article ('+domain+')]('+bookmarks.url+')\n')

        # [JSON Feed](https://www.jsonfeed.org)
        # f.write('\n'.join(bookmarks.description))
        # f.write('\n'.join(bookmarks.extended))
        # f.write('\n'.join(bookmarks.tags))
        # f.write('\n'.join(bookmarks.time))
        # f.write('\n'.join(bookmarks.url))
        