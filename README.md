This repo is to fuzzyfie and defuzzyfie ordinal data. Fuzzy ist comparable to bool logic but it has not only Fals = 0 and True = 1. 
It´s using anything in between to receive smooth transition.

For fuzzyfication you need a dectionary of the form DICT={"key": value}. fuzzyfied=fuzzyfication(DICT, some quantity). 
The class fuzzified fuzzyfies the given dict and applies some quantity on the reulting triangle functions.

with numpy logical links can be calculatet by:

`$`fuzzyfied1 \land fuzzyfied2 = `$ np.min([fuzzyfied1.fuzzy()["some key"], fuzzyfied2.fuzzy()["some key"]])`

`$` fuzzyfied1 \lor fuzzyfied2 = `$ np.max([fuzzyfied1.fuzzy()["some key"], fuzzyfied2.fuzzy()["some key"]])`

If exactly one result is required:

`fuzzyfied.defuzzification(DICT of results from reelevant conditions, list of corresponding values)`

See also the examples "smooth trader" and "kettle steering"
