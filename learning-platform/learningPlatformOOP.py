# AI-Powered Learning Platform → Music Streaming Platform → Game Tournament System
# AI-Powered Learning Platform – Intermediate/Advanced OOP Challenge
# Build a personalized learning system that adapts to user behavior, tracks progress, and recommends content.

# User Class
# Initialize with: username, email, learning_style ("visual", "auditory", "kinesthetic")
# Has enrolled_courses list (Course objects), completed_lessons list (Lesson objects)
# Has performance_history dict mapping lesson IDs to scores
# Has daily_streak integer, preferences dict tracking topic interest and engagement
# Has enroll(course) method
# Has complete_lesson(lesson, score) method
# Has get_learning_summary() method returning progress, strengths, weaknesses
# Has get_recommended_lessons(count=5) method using performance and preferences
# Has update_preferences(topic, engagement_score) method
# Has get_streak_status() method returning motivational message based on streak

# Course Class
# Initialize with: title, description, topic, difficulty_level ("beginner", "intermediate", "advanced")
# Has lessons list (ordered Lesson objects), enrolled_users list (User objects), ratings list (integers)
# Has add_lesson(lesson) method
# Has get_average_rating() method
# Has get_completion_rate() method (% of users who completed all lessons)
# Has get_most_engaging_lesson() method based on user scores and feedback

# Lesson Class
# Initialize with: title, content_type ("video", "text", "interactive"), duration_minutes, topic
# Has content string, quiz list (Question objects), view_count, completion_count
# Has feedback_scores list (integers)
# Has add_question(question) method
# Has get_engagement_score() method combining views, completions, feedback
# Has is_suitable_for(user) method matching user’s learning style

# Question Class
# Initialize with: prompt, options list, correct_answer
# Has difficulty ("easy", "medium", "hard"), tags list (e.g., ["math", "logic"])
# Has check_answer(user_answer) method
# Has get_hint() method (optional, based on difficulty)

# LearningPlatform Class
# Initialize with: platform_name
# Has users dict (username as key), courses dict (title as key), lessons list
# Has register_user(username, email, learning_style) method
# Has add_course(course) method
# Has search_courses(keyword) method
# Has get_average_quiz_score(lesson) method
# Has get_trending_lessons(limit=10) method based on engagement
# Has get_user_dashboard(user) method returning personalized summary
# Has generate_learning_path(user, topic) method creating adaptive lesson sequence
# Has get_platform_stats() method returning total users, lessons, engagement metrics

# LearningPlatform Class

# Has generate_learning_path(user, topic) method creating adaptive lesson sequence

class User:
    def __init__(self, username, email, learning_style):
        self.username = username
        self.email = email
        self.learning_style = learning_style
        self.enrolled_courses = []
        self.completed_lessons = []
        self.performance_history = {}
        self.preferences = {}
        self.daily_streak = 0
    
    def enroll(self, course):
        self.enrolled_courses.append(course)
        course.enrolled_users.append(self)

        # Jack.enroll(Algebra)
        # for course in Jack.enrolled_courses:
        #     print(course.title)
    
    def complete_lesson(self, lesson, score):
        enrolled = False
        for course in self.enrolled_courses:
            if lesson in course.lessons:
                enrolled = True
                break
        if not enrolled:
            return
        if lesson not in self.completed_lessons:
            self.completed_lessons.append(lesson)
            self.performance_history[lesson] = score
        else:
            if score > self.performance_history[lesson]:
                self.performance_history[lesson] = score
        lesson.completion_amount += 1
        self.update_preferences(lesson.content_type, lesson.get_engagement_score())

        # Jack.complete_lesson(Alg1_L1, 99)
        # Jack.complete_lesson(Alg1_L1, 19)
        # Jack.complete_lesson(Alg1_L2, 23)
        # Jack.complete_lesson(Alg1_L2, 86)
        # for lesson in Jack.completed_lessons:
        #     print(f"{lesson.title} : {Jack.performance_history[lesson]}")

    def get_learning_summary(self):
        course_progress = {}
        topic_scores = {}
        weaknesses = []
        strengths = []
        for course in self.enrolled_courses:
            if course.topic not in topic_scores:
                topic_scores[course.topic] = []
            course_completed_lessons = []
            for lesson in course.lessons:
                if lesson in self.completed_lessons:
                    course_completed_lessons.append(lesson)
                if lesson in self.performance_history:
                        topic_scores[course.topic].append(self.performance_history[lesson])
            if len(course.lessons) == 0:
                continue
            else:
                course_progress[course.title] = f"{len(course_completed_lessons) / len(course.lessons) * 100:.0f}%"
        for topic in topic_scores:
            if len(topic_scores[topic]) == 0:
                continue
            else:
                avg_score = sum(topic_scores[topic]) / len(topic_scores[topic])
                topic_scores[topic] = avg_score
                if avg_score >= 90:
                    strengths.append(topic)
                elif avg_score <= 60:
                    weaknesses.append(topic)
        return course_progress, strengths, weaknesses

        # learning_summary = Jack.get_learning_summary()
        # print("Course Progress:", learning_summary[0])
        # print("Strengths:", learning_summary[1])
        # print("Weaknesses:", learning_summary[2])
    
    def get_recommended_lessons(self, limit=3):
        nonsuitable_lessons = []
        suitable_lessons = []
        strength_lessons = []
        neutral_lessons = []
        weakness_lessons = []
        for course in self.enrolled_courses:
            for lesson in course.lessons:
                if lesson not in self.completed_lessons:
                    if lesson.is_suitable_for(self):
                        suitable_lessons.append(lesson)
                    else:
                        nonsuitable_lessons.append(lesson)
        learning_summary = self.get_learning_summary()
        strengths = learning_summary[1]
        weaknessess = learning_summary[2]
        for lesson in nonsuitable_lessons:
            for course in self.enrolled_courses:
                if lesson in course.lessons:    
                    if course.topic in strengths:
                        strength_lessons.append(lesson)
                    elif course.topic in weaknessess:
                        weakness_lessons.append(lesson)
                    else:
                        neutral_lessons.append(lesson)
        lessons_to_take = suitable_lessons + strength_lessons + neutral_lessons + weakness_lessons
        return lessons_to_take[:limit]

        # for lesson in Jackera.users["Jack"].get_recommended_lessons():
        #     print(f"{lesson.title}: {lesson.content_type}")

        # print("--------")

        # learning_summary = Jackera.users["Jack"].get_learning_summary()
        # print("Strengths:", learning_summary[1])
        # print("Weaknesses:", learning_summary[2])
    
    def update_preferences(self, content_type, engagement_score):
        if content_type in self.preferences:
            self.preferences[content_type] += 1
        else:
            self.preferences.update({content_type:1})

        # Jackera.users["Jack"].update_preferences("video", 3)
        # print(Jackera.users["Jack"].preferences)
    
    def get_streak_status(self):
        match self.daily_streak:
            case 0:
                return "Day one is waiting. Ready?"
            case s if 1 <= s <= 2:
                return "You showed up today — that’s the hardest part."
            case s if 3 <= s <= 6:
                return "Consistency beats intensity. You’re proving it!"
            case s if 7 <= s <= 13:
                return "You’ve built a solid habit. Don’t stop now."
            case s if 14 <= s <= 29:
                return "Your streak is on fire. Stay locked in!"
            case s if s >= 30:
                return "Legend status unlocked. Nothing can stop you now."
        
        # Jack.daily_streak = 1
        # print(Jack.get_streak_status())
            
class Course:

    difficulty_dict = {"Beginner": 1, "Intermediate": 2, "Advanced": 3}

    def __init__(self, title, description, topic, difficulty_level):
        self.title = title
        self.description = description
        self.topic = topic
        self.difficulty_level = difficulty_level
        self.lessons = []
        self.enrolled_users = []
        self.ratings = []
    
    def add_lesson(self, lesson):
        self.lessons.append(lesson)

        # Algebra1.add_lesson(Alg1_L6)
        # for lesson in Algebra1.lessons:
        #     print(lesson.title)
    
    def get_average_rating(self):
        return sum(self.ratings) / len(self.ratings)

        # Chemistry.ratings.extend([5,4,3,2,1])
        # print(Chemistry.get_average_rating())
    
    def get_completion_rate(self):
        if len(self.enrolled_users) == 0:
            return 0.0
        counter = 0
        for user in self.enrolled_users:
            if set(self.lessons).issubset(set(user.completed_lessons)):
                counter += 1
        return counter / len(self.enrolled_users) * 100
    
        # print(Spanish1.get_completion_rate())
    
    def get_most_enganging_lesson(self):
        if not self.lessons:
            return None
        engaging_lessons = sorted(self.lessons, key=lambda x: x.get_engagement_score(), reverse=True)
        return engaging_lessons[0]

        # print(Algebra1.get_most_enganging_lesson().title)

class Lesson:
    def __init__(self, title, content_type, duration_minutes, topic):
        self.title = title
        self.content_type = content_type
        self.duration_minutes = duration_minutes
        self.topic = topic
        self.content = None
        self.quiz = []
        self.view_count = 0
        self.completion_amount = 0
        self.feedback_scores = []
    
    def add_question(self, question):
        self.quiz.append(question)

        # Bio_L1.add_question(Bio_L1_Q1)
        # for question in Bio_L1.quiz:
        #     print(question.prompt)
    
    def get_engagement_score(self):
        total_feedback_score = 0
        for score in self.feedback_scores:
            total_feedback_score += score
        return self.view_count + self.completion_amount + total_feedback_score

        # print(Alg1_L1.get_engagement_score())
    
    def is_suitable_for(self, user):
        if ((user.learning_style == "Visual" and self.content_type in ["Video", "Text"]) or
        (user.learning_style == "Auditory" and self.content_type == "Audio") or
        (user.learning_style == "Kinesthetic" and self.content_type == "Interactive")):
            return True
        return False

        # print(Alg1_L1.is_suitable_for(Paige))

class Question:
    def __init__(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer
        self.difficulty = None
        self.tags = []
    
    def check_answer(self, user_answer):
        return user_answer.strip().upper() == self.correct_answer

        # print(Bio_L1_Q1.check_answer("c"))
    
    def get_hint(self):
        if self.difficulty == "easy":
            return f"The answer is option {self.correct_answer}"
        elif self.difficulty == "medium":
            return f"Look for keywords related to {', '.join(self.tags)}"
        elif self.difficulty == "hard":
            return "Think carefully about each option"
        else:
            return "No hints for this question"
        
        # Bio_L1_Q1.difficulty = "medium"
        # Bio_L1_Q1.tags.extend(["life", "organisms"])
        # print(Bio_L1_Q1.get_hint())

class LearningPlatform:
    def __init__(self, platform_name):
        self.platform_name = platform_name
        self.users = {}
        self.courses = {}
        self.lessons = []
    
    def register_user(self, username, email, learning_style):
        self.users.update({username:User(username, email, learning_style)})
    
        # for user in Jackera.users.items():
        #     print(user)

    def add_course(self, course):
        self.courses.update({course.title:course})
    
        # for course in Jackera.courses.items():
        #     print(course)
    
    def search_courses(self, keyword):
        results = []
        for course in self.courses:
            if keyword.lower() in course.lower():
                results.append(course)
        return results

        # results = Jackera.search_courses("h")
        # for finding in results:
        #     print(finding)
    
    def get_average_quiz_score(self, lesson):
        quiz_scores = []
        for username, user in self.users.items():
            for user_lesson, score in user.performance_history.items():
                if lesson == user_lesson:
                    quiz_scores.append(score)
        if quiz_scores == []:
            return None
        return sum(quiz_scores) / len(quiz_scores)
                
        # Jackera.users["Jack"].complete_lesson(Bio_L1, 10)
        # Jackera.users["Paige"].complete_lesson(Bio_L1, 89)
        # print(Jackera.get_average_quiz_score(Bio_L1))
    
    def get_trending_lessons(self, limit=10):
        lessons = []
        for course in self.courses.items():
            for lesson in course[1].lessons:
                lessons.append(lesson)
        lessons.sort(key=lambda lesson: lesson.get_engagement_score(), reverse=True)
        return lessons[:limit]

        # for lesson in Jackera.get_trending_lessons(3):
        #     print(f"{lesson.title}: {lesson.get_engagement_score()}")
    
    def get_user_dashboard(self, user):
        learning_summary = self.users[user].get_learning_summary()
        trending = self.get_trending_lessons(3)
        streak = self.users[user].get_streak_status()
        recommended_lessons = (self.users[user].get_recommended_lessons())
        return learning_summary, trending, recommended_lessons, streak

        # (course_progress, strengths, weaknesses), trending, recommended_lessons, streak = Jackera.get_user_dashboard("Jack")
        # print("Course Progress:", course_progress)
        # print("Strengths:", strengths)
        # print("Weaknesses:", weaknesses)
        # print("Trending Lessons:")
        # for lesson in trending:
        #     print(lesson.title)
        # print("Recommended Lessons:")
        # for lesson in recommended_lessons:
        #     print(lesson.title)
        # print(streak)

    def generate_learning_path(self, user, topic):
        topic_courses = []
        learning_path = []
        for course in user.enrolled_courses:
            if course.topic == topic:
                topic_courses.append(course)
        topic_courses.sort(key=lambda course: Course.difficulty_dict[course.difficulty_level])
        for course in topic_courses:
            for lesson in course.lessons:
                if lesson not in user.completed_lessons:
                    learning_path.append(lesson)
        return learning_path

        # for lesson in Jackera.generate_learning_path(Jackera.users["Jack"], "Science"):
        # print(lesson.title)

    def get_platform_stats(self):
        total_lessons = 0
        total_engagement = 0
        for course_name, course in self.courses.items():
            for lesson in course.lessons:
                total_lessons += 1
                total_engagement += lesson.get_engagement_score()
        return len(self.users), total_lessons, total_engagement

        # platform_stats = Jackera.get_platform_stats()
        # print("Total Users:", platform_stats[0])
        # print("Total Lessons:", platform_stats[1])
        # print("Total Engagement:", platform_stats[2])

Jackera = LearningPlatform("Jackera")

Algebra1 = Course("Algebra 1", "Equations, functions, graphs, problem-solving.", "Math", "Beginner")
Biology = Course("Biology", "Life, cells, genetics, ecosystems, evolution.", "Science", "Intermediate")
Chemistry = Course("Chemistry", "Matter, atoms, reactions, periodic trends, bonding.", "Science", "Intermediate")
Spanish1 = Course("Spanish 1", "Language, culture, communication, grammar, conversation.", "Language", "Beginner")
History1 = Course("History 1", "Civilizations, cultures, events, leaders, revolutions.", "Social Studies", "Beginner")
Geometry = Course("Geometry", "Shapes, theorems, proofs, trigonometry, and measurement.", "Math", "Intermediate")
Calculus = Course("Calculus", "Limits, derivatives, integrals, and applications of continuous change.", "Math", "Advanced")

Alg1_L1 = Lesson("Algebra Foundations", "Video", 30, "Overview and History of Algebra")
Alg1_L2 = Lesson("Solving Equations & Inequalities", "Text", 60, "Algebraic Equations and Inequalities")
Alg1_L3 = Lesson("Working with Units", "Interactive", 60, "Rate Conversion")
Alg1_L4 = Lesson("Linear Equations & Graphs", "Text", 60, "Two-variable Linear Equations Intro")
Alg1_L5 = Lesson("Forms of Linear Equations", "Video", 60, "Intro to Linear Equation Forms")
Alg1_L6 = Lesson("Systems of Equations", "Text", 60, "Solving Systems of Equations")

Geo_L1 = Lesson("Introduction to Geometry", "Video", 30, "Points, Lines, Planes, and Angles")
Geo_L2 = Lesson("Triangles and Their Properties", "Text", 60, "Classifying Triangles and Angle Sums")
Geo_L3 = Lesson("Congruence and Similarity", "Interactive", 60, "Transformations and Proofs of Congruence")
Geo_L4 = Lesson("Polygons and Quadrilaterals", "Text", 60, "Properties of Parallelograms, Trapezoids, and Other Polygons")
Geo_L5 = Lesson("Circles", "Video", 60, "Chords, Tangents, Arcs, and Central Angles")
Geo_L6 = Lesson("Perimeter, Area, and Volume", "Text", 60, "Measuring 2D and 3D Shapes")
Geo_L7 = Lesson("Coordinate Geometry", "Interactive", 60, "Slopes, Midpoints, and Distance Formula")
Geo_L8 = Lesson("Trigonometry in Geometry", "Video", 60, "Right Triangles, Sine, Cosine, and Tangent")
Geo_L9 = Lesson("Geometric Proofs", "Text", 60, "Two-Column Proofs and Reasoning with Theorems")
Geo_L10 = Lesson("Transformations", "Interactive", 60, "Reflections, Rotations, Translations, and Dilations")

Calc_L1 = Lesson("Introduction to Calculus", "Video", 30, "Understanding Limits and the Concept of Change")
Calc_L2 = Lesson("Limits and Continuity", "Text", 60, "Evaluating Limits and Identifying Continuity")
Calc_L3 = Lesson("Derivatives Basics", "Interactive", 60, "Definition of the Derivative and First Principles")
Calc_L4 = Lesson("Rules of Differentiation", "Audio", 60, "Power Rule, Product Rule, Quotient Rule, and Chain Rule")
Calc_L5 = Lesson("Applications of Derivatives", "Video", 60, "Tangent Lines, Velocity, and Optimization Problems")
Calc_L6 = Lesson("Graphing with Derivatives", "Interactive", 60, "Concavity, Inflection Points, and Curve Sketching")
Calc_L7 = Lesson("Introduction to Integration", "Audio", 60, "Antiderivatives and the Indefinite Integral")
Calc_L8 = Lesson("Definite Integrals", "Text", 60, "Area Under Curves and the Fundamental Theorem of Calculus")
Calc_L9 = Lesson("Techniques of Integration", "Interactive", 60, "Substitution, Integration by Parts, and Partial Fractions")
Calc_L10 = Lesson("Applications of Integrals", "Video", 60, "Volumes, Work, and Accumulated Change in Context")

Bio_L1 = Lesson("Intro to Biology", "Video", 30, "The Science of Biology")
Bio_L2 = Lesson("Waters, Acids, and Bases", "Video", 60, "Adhesion and Cohesion")
Bio_L3 = Lesson("Macromolecules", "Video", 60, "Intro to Macromolecules")
Bio_L4 = Lesson("Energy and Enzymes", "Text", 60, "Laws of Thermodynamics")
Bio_L5 = Lesson("Structure of a Cell", "Video", 60, "Intro to Cells")
Bio_L6 = Lesson("Membranes and Transport", "Interactive", 60, "Cell Membranes")

Chem_L1 = Lesson("Introduction to Chemistry", "Video", 45, "Atoms and Elements Overview")
Chem_L2 = Lesson("The Periodic Table", "Text", 60, "Understanding groups, periods, and element properties")

Span1_L1 = Lesson("Introduction to Spanish", "Video", 30, "Spanish Alphabet and Pronunciation")
Span1_L2 = Lesson("Basic Greetings & Expressions", "Text", 45, "Common Phrases and Everyday Conversation")
Span1_L3 = Lesson("Numbers and Days", "Text", 45, "Counting and Calendar Basics")

His1_L1 = Lesson("Introduction to History", "Video", 30, "Understanding the study of history and its importance")
His1_L2 = Lesson("Ancient Civilizations", "Audio", 45, "Exploring Mesopotamia, Egypt, and early societies")
His1_L3 = Lesson("Classical Empires", "Interactive", 45, "Overview of Greece, Rome, and their lasting influence")


Bio_L1_Q1 = Question("Which of the following best describes the primary focus of biology?",
                    ["A) The study of chemical reactions in the lab", "B) The study of celestial objects and their movements", "C) The study of life and living organisms", "D) The study of physical forces like motion and energy"],
                    "C")

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

    
#def extra()


    # Advanced Recommendation System
    # 1. Performance-Based Filtering: Recommend lessons where user struggles
    # 2. Interest-Based Filtering: Use preferences to suggest topics
    # 3. Learning Style Matching: Prioritize content types that suit the user
    # 4. Hybrid Recommendation: Combine all three for personalized suggestions
    # Analytics Features
    # Track time spent per topic
    # Track quiz performance trends
    # Track engagement by content type
    # Identify drop-off points in courses
    # Gamification Features
    # Add badges for streaks, completions, quiz mastery
    # Add leaderboards for top learners
    # Add XP system for lesson completion
    # Social Learning Features
    # Users can share progress
    # Users can recommend lessons
    # Users can form study groups
    # Bonus Challenges
    # AI Tutor: Simulate hints, encouragement, feedback
    # Voice Mode: Add auditory content for auditory learners
    # Offline Mode: Track progress locally and sync later
    # Accessibility Features: Text-to-speech, dyslexia-friendly fonts, etc.

    # Personalized Recommendations The platform learns from each user’s performance, preferences, 
    # and learning style to suggest the most relevant lessons. That’s a form of machine learning-lite—even 
    # if you’re not training a neural net, you’re simulating intelligent behavior.

    # Behavior Tracking It monitors things like:

    # Time spent on topics

    # Quiz scores

    # Engagement with content types Then it adjusts what the user sees next. That’s data-driven adaptation, which is core to AI systems.

    # Hybrid Recommendation Engine You’re combining:

    # Performance-based filtering (what the user struggles with)

    # Interest-based filtering (what they enjoy)

    # Learning style matching (how they learn best) This mimics how real AI systems like Duolingo or Khan Academy personalize learning paths.
