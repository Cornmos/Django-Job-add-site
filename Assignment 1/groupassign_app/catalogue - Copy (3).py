
class SubjectModel():
    def __init__(self, subjectCode, subjectName, semester,discipline,description):

        self.subjectCode = subjectCode
        self.subjectName = subjectName
        self.semester = semester
        self.discipline = discipline
        self.description = description

hit237 = SubjectModel("HIT237", "Building Interactive Software", 1,"Information Technology","Using Django to build dynamic Websites")
hit137 = SubjectModel("HIT137", "Database-Driven Web Applications", 1,"Information Technology","Learn introductory coding skills in Python")
hit220 = SubjectModel("HIT220", "Algorithms and Complexity", 1,"Information Technology","This unit prepares students to explore and implement efficient algorithms in order to solve complex computing problems")
hit235 = SubjectModel("HIT235", "Digital Systems and Computer Architecture", 1,"Information Technology","Introduction to the basics of digital systems and their design")
hit372 = SubjectModel("HIT372", "Organisation Network Infrastructure", 1,"Information Technology","This unit introduces students to the advanced infrastructure of modern computer networks and associated client-server technologies.")
hit274 = SubjectModel("HIT274", "Network Engineering Applications", 1,"Information Technology","This unit covers a broad aspect of networking that includes the architectures, models, protocols and networking elements.")
hit374 = SubjectModel("HIT374", "Enterprise Network Engineering", 1,"Information Technology","This unit covers the architecture, components, and operations of routers and switches in larger and more complex networks.")
hit164 = SubjectModel("HIT164", "Computing Fundamentals", 1,"Information Technology","This unit provides an overview of the discipline of IT, the historical perspectives and fundamental concepts of computation.")
hit172 = SubjectModel("HIT172", "Operating Systems and Applications", 1,"Information Technology","This unit covers the fundamentals of multiple operating systems and their associated applications.")
pmo201 = SubjectModel("PMO201", "Project Management", 1,"Information Technology","The purpose of this unit is to introduce and apply fundamental concepts of and practices in project management. ")

subjectCatalogue = [hit237, hit137,hit220, hit235, hit372, hit274, hit374, hit164, hit172,pmo201]
