from data import *

Jackera.register_user("Jack", "jhohman@gmail.com", "Kinesthetic")
Jackera.register_user("Paige", "phohman@gmail.com", "Visual")

for c in (Algebra1, Biology, Chemistry, Spanish1, History1, Geometry, Calculus):
    Jackera.add_course(c)

for lesson in (Alg1_L1, Alg1_L2, Alg1_L3, Alg1_L4, Alg1_L5, Alg1_L6):
    Jackera.courses[Algebra1.title].add_lesson(lesson)

for lesson in (Bio_L1, Bio_L2, Bio_L3, Bio_L4, Bio_L5, Bio_L6):
    Jackera.courses[Biology.title].add_lesson(lesson)

for lesson in (Span1_L1, Span1_L2, Span1_L3):
    Jackera.courses[Spanish1.title].add_lesson(lesson)

for lesson in (Chem_L1, Chem_L2):
    Jackera.courses[Chemistry.title].add_lesson(lesson)

for lesson in (His1_L1, His1_L2, His1_L3):
    Jackera.courses[History1.title].add_lesson(lesson)

for lesson in (Geo_L1, Geo_L2, Geo_L3, Geo_L4, Geo_L5, Geo_L6, Geo_L7, Geo_L8, Geo_L9, Geo_L10):
    Jackera.courses[Geometry.title].add_lesson(lesson)

for lesson in (Calc_L1, Calc_L2, Calc_L3, Calc_L4, Calc_L5, Calc_L6, Calc_L7, Calc_L8, Calc_L9, Calc_L10):
    Jackera.courses[Calculus.title].add_lesson(lesson)


# Print all lessons
# for title, course in Jackera.courses.items():
#     for lesson in course.lessons:
#         print(lesson.title)

for course in (Algebra1, Biology, Chemistry, Spanish1, History1, Geometry, Calculus):
    Jackera.users["Jack"].enroll(course)

Jackera.users["Jack"].complete_lesson(Alg1_L1, 99)
Jackera.users["Jack"].complete_lesson(Alg1_L2, 86)
Jackera.users["Jack"].complete_lesson(Alg1_L3, 96)
Jackera.users["Jack"].complete_lesson(Bio_L1, 90)
Jackera.users["Jack"].complete_lesson(Bio_L2, 86)
Jackera.users["Jack"].complete_lesson(Chem_L1, 23)
Jackera.users["Jack"].complete_lesson(Span1_L1, 36)
Jackera.users["Jack"].complete_lesson(Span1_L2, 13)
Jackera.users["Jack"].complete_lesson(His1_L1, 99)


(course_progress, strengths, weaknesses), trending, recommended_lessons, streak = Jackera.get_user_dashboard("Jack")
print("Course Progress:", course_progress)
print("Strengths:", strengths)
print("Weaknesses:", weaknesses)
print("Trending Lessons:")
print("-----------------")
for lesson in trending:
    print(lesson.title)
print("Recommended Lessons:")
print("--------------------")
for lesson in recommended_lessons:
    print(lesson.title)
print(streak)

for lesson in Jackera.generate_learning_path(Jackera.users["Jack"], "Science"):
    print(lesson.title)