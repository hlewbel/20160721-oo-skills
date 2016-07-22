

class Student(object):

    def __init__(self, first_name, last_name, address):
        """ Initialize student attributes """
        
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init__(self, question, correct_answer):
        """ Initialize questions and answers attributes """
        
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """ Evaluate if user's answer to question matches correct_answer
        
        """
        print self.question, " "

        return raw_input() == self.correct_answer


class Exam(object):

    def __init__(self, exam_name):
        """ Initialize questions and answers attributes """

        self.questions = []
        self.exam_name = exam_name


    def add_question(self, question, correct_answer):
        """ Question and Correct Answer
        
        """

        self.questions.append(Question(question, correct_answer))

    def administer(self):
        """ keep score of right number of Q&Alberta

        """
        score = 0

        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1

        return score

class Quiz(Exam):

    def administer(self):

        quiz_score = super(Quiz, self).administer()
        print quiz_score
        print len(self.questions)
        return quiz_score >= len(self.questions)/2.0 #ensure float

def take_test(exam, student):
    """ Has a student take the test and provides the student's score

    """

    student.score = exam.administer()

def example():
    """ Creates an example exam

    creates an exam, adds questions, creates a student,
    administers the test
    """

    #instantiate exam
    exam = Exam("Midterm")
    exam.add_question("What is the capital of Alberta?", "Edmonton")
    student = Student("Hannah", "Lewbel", "101 Not Telling You Ave, Campbell, CA 95008")
    take_test(exam,student)
    print student.score

#print "let's take an exam"
#example()

def example_quiz():
    """ test out the quiz """

    quiz = Quiz("HQuiz")
    quiz.add_question("What is the capital of Alberta?", "Edmonton")
    quiz.add_question("How cool is Brian?", "Very")
    quiz.add_question("Who's on first?", "What")
    student = Student("Hannah", "Lewbel", "101 Not Telling You Ave, Campbell, CA 95008")
    take_test(quiz,student)
    print student.score

print "now let's take a quiz"
example_quiz()
