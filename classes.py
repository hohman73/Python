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