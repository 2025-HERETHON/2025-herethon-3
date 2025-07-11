from django.core.management.base import BaseCommand
import pandas as pd
from jobs.models import Job, FieldCategory, InterestTag

class Command(BaseCommand):
    help = "직무 마스터 데이터를 엑셀에서 불러와 DB에 저장합니다."

    def handle(self, *args, **kwargs):
        df = pd.read_excel("STEM 관심사, 직무, 롤모델 연결.xlsx", sheet_name="02_직무 마스터")

        for _, row in df.iterrows():
            field_obj, _ = FieldCategory.objects.get_or_create(
                field_id=row["field_id"],
                defaults={"name": row["field_name"]}
            )

            job = Job.objects.create(
                job_id=row["job_id"],
                job_name=row["job_name"],
                job_description=row["job_description"],
                emotive_copy=row["emotive_copy"],
                Soft_Skills=row["Soft_Skills"],
                related_majors=row["related_majors"],
                entry_path=row["entry_path"],
                keyword_tags=row["keyword_tags"],
                recommend_reason=row["recommend_reason"],
                stem_category=row["STEM_category"],
                field=field_obj
            )

            # ✅ related_tags 연결 - 루프 안에서 tag 여러 개 추가
            tag_ids = str(row["related_tags"]).split(",")  # 예: "1,4"

            for tag_id in tag_ids:
                tag_id = tag_id.strip()
                if tag_id:
                    try:
                        tag_obj = InterestTag.objects.get(tag_id=int(tag_id))
                        job.related_tags.add(tag_obj)
                    except InterestTag.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f"❗️태그 ID {tag_id} 없음"))

        # ✅ 모든 행 처리 후에 완료 메시지 출력
        self.stdout.write(self.style.SUCCESS("✅ 직무 마스터 데이터 입력 완료"))
