# pylint: disable=C0114, E1121, R0204

# Third Party Library
import pandas as pd

# Pandas Tutorial #

# Pandas Getting Started
print(pd.__version__)
mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}
myvar = pd.DataFrame(mydataset)
print(myvar)
print()

# Pandas Series
