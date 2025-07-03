from django.core.management.base import BaseCommand
import pandas as pd
from jobs.models import InterestTag

class Command(BaseCommand):
    help = "01_관심사 태그 마스터 시트를 읽어 태그 데이터를 DB에 입력합니다."

    def handle(self, *args, **kwargs):
        df = pd.read_excel("STEM 관심사, 직무, 롤모델 연결.xlsx", sheet_name="01_관심사 태그 마스터")

        for _, row in df.iterrows():
            tag_id = int(row["tag_id"])
            tag_name = row["tag_name"]

            obj, created = InterestTag.objects.get_or_create(
                tag_id=tag_id,
                defaults={"name": tag_name}
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ 새 태그 등록: {tag_name}"))
            else:
                self.stdout.write(self.style.WARNING(f"ℹ️ 이미 존재하는 태그: {tag_name}"))

        self.stdout.write(self.style.SUCCESS("🎉 관심사 태그 입력 완료!"))
