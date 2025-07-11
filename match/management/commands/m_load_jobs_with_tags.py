import csv
from django.core.management.base import BaseCommand
from match.models import Job, InterestTag

class Command(BaseCommand):
    help = 'CSV로 Job 생성 + related_tags 자동 연결'

    def handle(self, *args, **kwargs):
        with open('match/job_table.csv', newline='', encoding='utf-8') as csvfile:  # ✅ 경로 바뀜
            reader = csv.DictReader(csvfile)
            for row in reader:
                job, created = Job.objects.get_or_create(
                    job_id=row['job_id'],
                    defaults={
                        'job_name': row['job_name'],
                        'job_description': row['job_description'],
                        'emotive_copy': row['emotive_copy'],
                        'Soft_Skills': row['Soft_Skills'],
                        'related_majors' : row['related_majors'],
                        'entry_path': row['entry_path'],
                        'keyword_tags': row['keyword_tags'],
                        'recommend_reason': row['recommend_reason'],
                        'stem_category': row['stem_category'],
                        'field_id': row['field_id'],
                        'field_name': row.get('field_name', '')  # 있으면 쓰고 없으면 공백
                    }
                )

                # related_tags 연결
                job.related_tags.clear()

                tag_ids = row['related_tags'].split(',')
                for tag_id in tag_ids:
                    tag = InterestTag.objects.filter(tag_id=int(tag_id.strip())).first()
                    if tag:
                        job.related_tags.add(tag)

                self.stdout.write(self.style.SUCCESS(f'{job.job_name} 등록 완료'))
