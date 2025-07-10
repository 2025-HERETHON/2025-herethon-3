import csv
from django.core.management.base import BaseCommand
from role.models import Role
from jobs.models import Job

class Command(BaseCommand):
    help = 'CSV 파일을 읽어 Role 테이블에 데이터를 입력합니다.'

    def handle(self, *args, **kwargs):
        with open('role/role_data.csv', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    job = Job.objects.get(job_id=int(row['job_id']))
                    Role.objects.update_or_create(
                        role_name=row['role_name'],
                        job=job,
                        defaults={
                            'role_title': row['role_title'],
                            'short_bio': row['short_bio'],
                            'quote': row['quote'],
                            'original_url': row['original_url'],
                        }
                    )
                    self.stdout.write(self.style.SUCCESS(f"✔ 등록됨: {row['role_name']}"))
                except Job.DoesNotExist:
                    self.stderr.write(f"❌ Job {row['job_id']} 없음 → {row['role_name']} 건너뜀")
                except Exception as e:
                    self.stderr.write(f"❗ 오류 발생: {e}")
