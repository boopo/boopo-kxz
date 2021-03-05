from flask_restful import Api

from App.apis.jwxt.jwxt_api import  KB, Exams, Grades, SingleJd, AverageJd, EmptyRoom, SpecialCourse, MakeUpGrades

jwxt_api = Api(prefix='/jwxt')

jwxt_api.add_resource(KB, '/kb')
jwxt_api.add_resource(Exams, '/exam')
jwxt_api.add_resource(Grades, '/grade')
jwxt_api.add_resource(SingleJd, '/alljd')
jwxt_api.add_resource(AverageJd, '/avejd')
jwxt_api.add_resource(EmptyRoom, '/classroom')
jwxt_api.add_resource(SpecialCourse, '/course')
jwxt_api.add_resource(MakeUpGrades, '/grades')



