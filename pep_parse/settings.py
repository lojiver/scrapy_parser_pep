# from datetime import datetime
from pathlib import Path

# now = datetime.now()
# timestamp = now.strftime('%Y-%m-%dT%H-%M-%S')

BASE_DIR = Path(__file__).parent.parent
BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
        # 'encoding': 'utf-8'
    },
}


ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
