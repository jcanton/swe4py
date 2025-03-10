# inspector.py

import sys

print("\n-------------------")
print(f"inspector.py:{__name__=}")
print(f"inspector.py:{__package__=}")
print(f"inspector.py:{sys.path=}")
print("-------------------\n")

# Import the `evidence` variable from `clue.py`
#
# You can try two ways:
#
# 1. Try with an absolute import
# import ....
#
# 2. Try with a relative import
# from ... import ....  #

# Note that wrong import will raise an ImportError that you can catch
# try:
#     import <something_wrong>
# except ImportError as e:
#     pass
#
# print("All good here!")

import detective.clue as clue
#import clue

found_evidence = clue.evidence
print(f"Found evidence: {found_evidence}")
