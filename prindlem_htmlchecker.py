import re

example_set = ['''<a><b><c></c></b></a>''',
 '''<foo>asd<bar>alksjd</bar><p>asldkj</p></foo>''',
 '''<foo><bar></bop></bar></foo>''',
 '''<foo><bar></bar></foo></foo>''',
 '''<foo><bar></foo></bar>''']

def valid_html(test_strings):
    valid_htmlList = []
    for item in test_strings:                                      #loop thru all test strings
        htmlRegex = re.compile(r'</?[a-z]+>')           #compile the regex
        tags = htmlRegex.findall(item)                      #find all tags in the string
        i = 0
        while i < len(tags):  #loop thru the tags
            if type(re.search(r'</[a-z]+>', tags[i])) == type(None):
                i += 1
                continue

            if len(tags) == 1:
                valid_htmlList.append((item, False))
                break

            if re.search(r'</[a-z]+>', tags[i])[0] == '</' + re.findall(r'[a-z]+>', tags[i-1])[0]:
                del tags[i]
                del tags[i-1]
                if tags == []:
                    valid_htmlList.append((item, True))
                i -= 1

            else:
                valid_htmlList.append((item, False))
                break

    return(valid_htmlList)

print(valid_html(example_set))

#print(re.findall('(?<=\<)(.*?)(?=\>)', re.findall('<[^/>][^>]*>', item))
#re.findall('(?<=\<)(.*?)(?=\>)',
#[('<a><b><c></c></b></a>', True),
#('<foo>asd<bar>alksjd</bar><p>asldkj</p></foo>', True),
#('<foo><bar></bop></bar></foo>', False),
#('<foo><bar></bar></foo></foo>', False),
#('<foo><bar></foo></bar>', False)
#]

