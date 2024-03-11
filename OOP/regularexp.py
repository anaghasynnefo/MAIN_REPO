# import re
# str="hello team have a nice day"

# x=re.match("hello",str)

# if x:
#    print("match")

# else:
#    print("not match")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# import re
# str="team hello have a nice day"

# x=re.match("hello",str)

# if x:
#    print("match")

# else:
#    print("not match")


""""""""""""""""""""""""""""""""""""""""""""""""""""""

# import re
# str="hello team have a nice day"

# x=re.search("hello",str)

# if x:
#    print("match")

# else:
#    print("not match")


""""""""""""""""""""""""""""""""""""""""""""""""
# import re
# str="hello team have hello a good day"

# x=re.findall("hello",str)
# print(x)

""""""""""""""""""""""""""""""""""""""""""

# import re
# str="jinu@gmail.com"

# x=re.split("@",str)
# print(x[0])


""""""""""""""""""""""""
# import re

# str="SYNNEFO"
# x=re.match("[A-Z a-z]ynnefo",str)

# if x:
#     print("match")

# else:
#     print("not match")


""""""""""""""""""""""""
# import re

# str="2YNNEFO"
# x=re.match("[0-9]",str)

# if x:
#     print("match")

# else:
#     print("not match")


""""""""""""""""""""

# import re

# str="2YNNEFO"


# 0-9
# x=re.match("\dYNNEFO",str)

# if x:
#     print("match")

# else:
#     print("not match")


""""""""""""""""""""""""


# import re

# str="HELLO TEAM "


# 0-9
# x=re.search("^TEAM",str)

# if x:
#     print("match")

# else:
#     print("not match")

""""""""""""""""""""


# import re

# str="hello team"


# 0-9
# x=re.search("team$",str)

# if x:
#     print("match")

# else:
#     print("not match")

""""""""""""""""""

# import re

# str="hello team "


# 0-9
# x=re.search("^\dello.team$",str)

# if x:
#     print("match")

# else:
#     print("not match")


# """"""""""""""""""

# import re

# terms='^anagha*$'

# x=re.search(terms,"anagha")
# print("match")

# if x:
#     print("matched")

# else:
#    print("not match")


""""""""""""""""""

# import re
# terms="\d"
# x=re.match(terms,"9hello synnefo")
# if x:
#     print("match")
# else:
#     print("not match")

""""""""""""""""""


# import re
# terms="|d"
# x=re.match(terms,"9hello synnefo")
# if x:
#     print("match")
# else:
#     print("not match")


""""""""""""""


# import re
# terms="\D"
# x=re.match(terms,"hello synnefo")
# if x:
#     print("match")
# else:
#     print("not match")


# """"""""""""

# import re
# terms="^[^h]ello"
# x=re.search(terms,"pello synnefo")
# if x:
#     print("match")
# else:
#     print("not match")

# """"""""""""""

# import re
# terms="\W"
# x=re.search(terms,"pello synnefo")
# if x:
#     print("match")
# else:
#     print("not match")

# """"""""""""""

# import re
# terms="^[5-9]\d{9}$"
# x=re.search(terms,"9846636061")
# if x:
#     print("validate")
# else:
#     print("not validate")

""""""""""""





