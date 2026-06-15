from django.core.management.base import BaseCommand
from chatbot.models import Category, FAQ

class Command(BaseCommand):
    help = 'Cleans old junk data and seeds pure SKASC data'

    def handle(self, *args, **kwargs):
        # 1. Clear all old FAQs to remove "dollar" fees and generic B.Tech mentions
        FAQ.objects.all().delete()
        
        # 2. Get/Create categories
        admin_cat, _ = Category.objects.get_or_create(name='Admission')
        course_cat, _ = Category.objects.get_or_create(name='Courses')
        placement_cat, _ = Category.objects.get_or_create(name='Placements')
        about_cat, _ = Category.objects.get_or_create(name='About SKASC')

        faqs = [
            # About SKASC
            {
                'category': about_cat,
                'question': 'Tell me about Sri Krishna Arts and Science College (SKASC)',
                'answer': 'Established in 1997 by the VLB Trust in Coimbatore, SKASC is an autonomous institution known for its "Vision to Wisdom" approach. It has a student strength of over 9,000 and has consistently ranked in the Top 50 of NIRF rankings.'
            },
            {
                'category': about_cat,
                'question': 'Where is SKASC located?',
                'answer': 'SKASC is located in Sugunapuram, Kuniamuthur, Coimbatore, Tamil Nadu, 641008. You can contact us at 0422–2678400.'
            },
            {
                'category': about_cat,
                'question': 'What are the rankings of SKASC?',
                'answer': 'SKASC is ranked #50 in NIRF 2025 (College category). It was also ranked 2nd best for Graduate Outcomes in NIRF 2023 and 1st in Swachh Campus Ranking 2019.'
            },

            # Courses
            {
                'category': course_cat,
                'question': 'What UG and PG courses are offered at SKASC?',
                'answer': 'SKASC offers 51 programs. UG includes B.A. English, B.Sc. (CS, IT, Data Science, AI & ML, Psychology), BCA, B.Com, and BBA. PG includes MSW, M.A. English, M.Sc. (CS, IT, Biotech), and M.Com.'
            },
            {
                'category': course_cat,
                'question': 'Does SKASC offer BCA or Computer Science?',
                'answer': 'Yes! SKASC offers B.Sc. Computer Science, BCA, B.Sc. IT, Computer Technology, Software Systems, Data Science, and AI & ML specializations.'
            },

            # Fees (Corrected for SKASC)
            {
                'category': admin_cat,
                'question': 'What is the fee structure at SKASC?',
                'answer': 'As an autonomous institution, SKASC offers competitive fee structures for all 51 programs. Fees vary by course (Arts, Science, or Commerce). For a detailed fee proforma and installment options, please visit the Administrative Office at the Kuniamuthur campus or contact admissions@skasc.ac.in.'
            },

            # Placements
            {
                'category': placement_cat,
                'question': 'What are the placement records for 2025-26?',
                'answer': 'For 2025-2026, SKASC has an 84.44% placement rate with 124+ companies visiting and a highest package of 13.72 LPA. Top recruiters include ZOHO, KGIS, and Zifo.'
            },

            # Admissions & Scholarships
            {
                'category': admin_cat,
                'question': 'How can I apply for admission to SKASC?',
                'answer': 'You can apply online via skasc.ac.in. The process involves online registration, document verification, and counseling. Scholarships like the Pudhumai Penn scheme and Management scholarships are available.'
            }
        ]

        for faq_data in faqs:
            FAQ.objects.create(
                question=faq_data['question'],
                category=faq_data['category'],
                answer=faq_data['answer']
            )

        self.stdout.write(self.style.SUCCESS('Database cleaned and updated with accurate SKASC data.'))
