from pcstore import Pcstore_crawler
import sys

if len(sys.argv) <= 1:
    print("Please input a keyword for searching.")
else:
    if len(sys.argv[1]) < 2:
        print("Please insert atleast two words for searching, because of PC store's policy.")
    else:
        test = Pcstore_crawler(sys.argv[1])
        print(test.get_item_title())