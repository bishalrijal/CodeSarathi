from django.test import TestCase

# Create your tests here.
from account.models import TechSkill,Languages
s_no= TechSkill.objects.all().count()
skill={}
skilllist=[]
languages=[]
for i in range (s_no):
    skill_element=TechSkill.objects.get(id=i+1)
    l_no=skill_element.languages.all().count()
    for i in range(l_no):
        languages.append(Languages.objects.get(id=i+1).name)
    skill[skill_element.skill_name]=languages
    skilllist.append(skill)

s_list=[]
Lang=[]
s_no=TechSkill.objects.all().count()
for i in range(s_no):
    t=TechSkill.objects.all()[i]
    s_list.append(t.skill_name)
    l_no=t.languages.all().count()
    l=[]
    for j in range(l_no):
        l.append(t.languages.all()[j].name)
    Lang.append(l)