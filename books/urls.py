from django.urls import path
from .views import BookInputView, BookGetByID, LangChoicesView, TagChoicesView, BookGetByIDTeacher, BookGetByIDApproval,RankingStudentView

urlpatterns = [
    path('book/', BookInputView.as_view()),
    path('book/id=<str:id>/',BookGetByID.as_view()),
    path('book_teacher/id=<str:id>/', BookGetByIDTeacher.as_view()),
    path('book_teacher_approve/id=<str:id>/', BookGetByIDApproval.as_view()),
    path('tag/', TagChoicesView.as_view()),
    path('lang/', LangChoicesView.as_view()),
    path('students_ranking/', RankingStudentView.as_view())
]