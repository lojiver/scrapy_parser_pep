from datetime import datetime

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    def __init__(self):
        self.status_count = {}

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = datetime.now()
        timestamp = now.strftime('%Y-%m-%dT%H-%M-%S')
        file_name = f'status_summary_{timestamp}.csv'
        file_path = results_dir / file_name
        total = sum(self.status_count.values())
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for key, value in self.status_count.items():
                f.write(f'{key},{value}\n')
            f.write(f'Total,{total}\n')

    def process_item(self, item, spider):
        status = item['status']
        self.status_count[status] = self.status_count.get(status, 0) + 1
        return item
