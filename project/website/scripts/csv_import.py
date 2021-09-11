import csv
from url_search.models import Url_list

def run():

    # All data in run method only will be executed 
    fhand = open('scripts/top-1m.csv')
    reader = csv.reader(fhand)

    for row in reader:
        id = row[0]
        name = row[1]
        item = Url_list.objects.create(id =id,name=name)
        item.save()
