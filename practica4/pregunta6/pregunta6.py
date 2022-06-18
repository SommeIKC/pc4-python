import re
text =  '@robot9! @robot4& I have a good feeling that the show is going to be amazing! @robot9$ @robot7%'


regex = r'@robot\d\W'


print(re.findall(regex, text))