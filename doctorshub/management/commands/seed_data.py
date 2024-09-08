from django.core.management.base import BaseCommand
from doctorshub.models import Doctor, Specialization, Area


class Command(BaseCommand):
    help = 'Seeds the database with doctors, areas, and specializations relevant to Egypt'

    def handle(self, *args, **kwargs):
        specializations = [
            'أسنان', 'عيون', 'جراحة', 'قلب', 'أنف وأذن وحنجرة', 'جلدية', 'أطفال', 'نساء وتوليد', 'عظام'
        ]

        specialization_objects = []
        for spec in specializations:
            specialization, created = Specialization.objects.get_or_create(name=spec)
            specialization_objects.append(specialization)
            self.stdout.write(self.style.SUCCESS(f"Specialization '{spec}' added."))

        areas = ['مدينة نصر', 'المعادي', 'الزمالك', 'الدقي', 'الهرم', 'مصر الجديدة', 'الجيزة', 'التجمع الخامس']

        area_objects = []
        for area in areas:
            area, created = Area.objects.get_or_create(name=area)
            area_objects.append(area)
            self.stdout.write(self.style.SUCCESS(f"Area '{area}' added."))

        doctors = [
            {'name': 'د. محمد عبد الله', 'phone': '0123456789', 'address': 'شارع التحرير', 'specialization': 'أسنان',
             'area': 'مدينة نصر'},
            {'name': 'د. أحمد علي', 'phone': '0112345678', 'address': 'شارع النصر', 'specialization': 'قلب',
             'area': 'مصر الجديدة'},
            {'name': 'د. فاطمة سعيد', 'phone': '0102345678', 'address': 'شارع الثورة', 'specialization': 'جلدية',
             'area': 'المعادي'},
            {'name': 'د. خالد منصور', 'phone': '0153456789', 'address': 'شارع الهرم', 'specialization': 'جراحة',
             'area': 'الهرم'},
            {'name': 'د. إيمان عبد العزيز', 'phone': '0163456789', 'address': 'شارع التسعين', 'specialization': 'أطفال',
             'area': 'التجمع الخامس'},
        ]

        for doctor_data in doctors:
            specialization = Specialization.objects.get(name=doctor_data['specialization'])
            area = Area.objects.get(name=doctor_data['area'])

            doctor, created = Doctor.objects.get_or_create(
                name=doctor_data['name'],
                phone=doctor_data['phone'],
                address=doctor_data['address'],
                specialization=specialization,
                area=area
            )
            self.stdout.write(self.style.SUCCESS(f"Doctor '{doctor.name}' added."))
