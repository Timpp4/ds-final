import logging

# Error logging
logging.basicConfig(filename='', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

def finalPath(start, end, depthCounter, data):
    depth1 = []
    depth2 = []
    depth3 = []

    while True:
        if (depthCounter == 3):
            for art in data:
                for i in art.titles: 
                    if (art.depth == 3 and str(i).lower() == str(end).lower()):
                        print("Found: " + i + " in " + art.name + " (depth=" + str(art.depth) + ")")
                        depth3.append(art.name)
            for art in data:
                if art.depth == 2:
                    print("depth on 2")
                    print(art.name)
                    if art.name in depth3:
                        print(art.name in depth3)
                        depth2.append(art.name)
                        print(art.name + " nexti on depth2")
                        print(depth2)
            for art in data:
                if art.depth == 1:
                    print(art.titles)
                    for p in art.titles:
                        print(p)
                        if (p not in depth2):
                            print(p + " if p not in depth2")
                            print(depth2)
                            try:
                                depth2.remove(p)
                                print(depth2)
                            except Exception as err:
                                logger.error(err)
                #for i in art.titles:
                #    if (str(i).lower() == str(start).lower() and art.depth == 2):
                #        print(i + " " + art.name)
                #        if (i in depth3):
                #            print("Found: " + i + " in " + art.name + " (depth=" + str(art.depth) + ")")
                #            depth2.append(art.name)
            break
        if (depthCounter == 2):
            for art in data:
                for i in art.titles:
                    if (str(i).lower() == str(end).lower() and art.depth == 2):
                        print("Found: " + i + " in " + art.name + " (depth=" + str(art.depth) + ")")
                        depth2.append(art.name)
            break
        if (depthCounter == 1):
            break
        if (depthCounter == 0):
            break

    while True:
        if depthCounter == 3:
            depth2 = (list(set(depth2)))
            depth3 = (list(set(depth3)))
            print("['"+start+"']", end="\n-> ")
            print(depth2, end="\n-> ")
            print(depth3)
            print("['"+end+"']")
            break
        elif depthCounter == 2:
            depth2 = (list(set(depth2)))
            print("['"+start+"']", end="\n-> ")
            print(depth2)
            print("['"+end+"']")
            break
        elif depthCounter == 1:
            print("['"+start+"']")
            print("v")
            print("['"+end+"']")
            break
        else:
            print("No path between (" + start + ") and (" + end + ").")
            break