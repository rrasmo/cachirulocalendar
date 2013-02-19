from events.models import Event, Community
from datetime import datetime
import urllib
from lxml import html

def scrap_zgzactiva():
    print 'scrapping zgzactiva'
    community_id = 2

    URL = 'http://www.zaragoza.es/ciudad/sectores/activa/lista_Zactiva'
    XPATH = '//div[@id="rscont"]/table/tr'

    root = html.parse(URL).getroot()
    root.make_links_absolute()
    trs = root.xpath(XPATH)[1:]

    for tr in trs:
        td1, td2 = tr.getchildren()[:2]
        a = td1.getchildren()[0]
        name = a.text
        url = a.attrib['href']
        date_string = td2.text
        start_date = datetime.strptime(date_string, '%d-%m-%Y %H:%M')
        end_date = start_date

        event, created  = Event.objects.get_or_create(name=name, url=url, start_date=start_date, end_date=end_date, community_id=community_id)
        #print event, created

