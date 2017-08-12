from bs4 import BeautifulSoup
from Model.xmlConetent import xmlContent
xml = xmlContent()


x="""<fono attribo>
   <bar>
      <type foobar="1"/>
      <type foobar="2"/>
   </bar>
</foo>"""

y=BeautifulSoup(xml.x , 'html.parser')
# z1 = y.foo.bar.type["foobar"]

z2 = y.findAll("ul")[0].findAll("li")[2].get_text()
z3 = y.findAll("h4")[5].string

# y.foo.bar.findAll("type")
# y.foo.bar.findAll("type")[0]["foobar"]
# z2 = y.foo.bar.findAll("type")[1]["foobar"]

print(z2)
