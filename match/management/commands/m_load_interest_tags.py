import csv
from django.core.management.base import BaseCommand
from match.models import InterestTag
from pathlib import Path

class Command(BaseCommand):
    help = 'CSV 파일에서 InterestTag 데이터를 불러와 DB에 저장'

    def handle(self, *args, **kwargs):
        base_dir = Path(__file__).resolve().parent.parent.parent
        csv_path = base_dir / 'interest_tags.csv'

        if not csv_path.exists():
            self.stdout.write(self.style.ERROR(f"CSV 파일이 존재하지 않습니다: {csv_path}"))
            return

        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                tag, created = InterestTag.objects.get_or_create(
                    tag_id=int(row['tag_id']),
                    defaults={
                        'tag_name': row['tag_name'].strip(),
                        'description': row['description'].strip(),
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"추가됨: {tag.tag_name}"))
                else:
                    self.stdout.write(f"이미 존재함: {tag.tag_name}")
