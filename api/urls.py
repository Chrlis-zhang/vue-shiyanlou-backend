from django.urls import path

from . import views

urlpatterns = [
    path('v2/courses/', views.courses, name='courses'),
    path('v2/courses/<int:courseId>/', views.course, name='course'),
    path('v2/courses/<int:courseId>/labs/', views.courseLabs, name='courseLabs'),
    path('v2/courses/categories/', views.categories, name='categories'),
    path('v2/courses/<int:courseId>/follow/', views.follow, name='follow'),
    path('v2/courses/userstatus/', views.courseUserStatus, name='courseUserStatus'),
    path('v2/courses/<int:courseId>/join/', views.join, name='joinCourse'),

    path('v2/index/categories/', views.indexCategories, name='indexCategories'),
    path('v2/index/banner-pictures/', views.indexBanner, name='indexBanner'),
    path('v2/index/louplus/', views.louplus, name='louplus'),
    path('v2/index/classfication-courses/', views.classficationCourses, name='classficationCourses'),
    path('v2/index/bootcamps/', views.indexBootcamps, name='indexBootcamps'),
    path('v2/index/paths/', views.indexPaths, name='indexPath'),

    path('v2/fringe/recent-activities/', views.recentActivities, name='recentActivities'),
    path('v2/fringe/recent-louplus-courses/', views.recentLouplus, name='recentLouplus'),    
    
    path('v2/questions/', views.questions, name='questions'),
    path('v2/questions/<int:questionId>/', views.question, name='question'),
    path('v2/questions/<int:questionId>/answers/', views.questionAnswers, name='questionAnswers'),
    path('v2/questions/<int:questionId>/related-questions/', views.relatedQuestions, name='relatedQuestions'),

    path('v2/paths', views.paths, name='paths'),
    path('v2/paths/<int:pathId>/', views.path, name='path'),
    path('v2/paths/<int:pathId>/stages/', views.stages, name='pathStages'),
    path('v2/paths/<int:pathId>/join/', views.pathJoin, name='pathJoinAndDelete'),
    path('v2/paths/userstatus/', views.pathUserstatus, name='pathUserstatus'),

    path('v2/comments/', views.comment, name='comments'),
    path('v2/comments/userstatus/', views.commentsUserstatus, name='commentsUserstatus'),
    path('v2/comments/<int:commentId>/', views.deleteComment, name='deleteComment'),

    path('v2/labreports/', views.labreports, name='labreports'),
    path('v2/labreports/<int:reportId>/', views.labreport, name='labreport'),
    path('v2/labreports/<int:reportId>/learn-data/', views.labreportLearnData, name='labreportLearnData'),
    path('v2/labreports/<int:reportId>/related/', views.labreportRelated, name='labreportRelated'),
    path('v2/auth/login', views.login, name='login'),

    path('v2/user/', views.userInfo, name='user'),
    path('v2/user/checkin/', views.checkin, name='checkin'),
    path('v2/user/change-email/', views.changeEmail, name='changeEmail'),
    path('v2/user/change-password/', views.changePassword, name='changePassword'),
    path('v2/user/mail-settings/', views.mailSettings, name='mailSettings'),

    path('v2/users/<int:userId>/', views.userInfoWithoutCookies, name='userWithoutCookies'),
    path('v2/users/<int:userId>/courses/', views.userStudiedCourses, name='userStudiedCourses'),
    path('v2/users/<int:userId>/questions/', views.userQuestionsForOneCourse, name='userQuestionsForOneCourse'),
    path('v2/users/<int:userId>/paths/', views.userPaths, name='userPath'),
    path('v2/users/<int:userId>/labreports/', views.userLabreports, name='userLabreports'),
    
    path('v2/library/', views.library, name='library'),
    path('v2/library/books/', views.libraryBooks, name='libraryBooks'),

    path('v2/live-courses/', views.liveCourses, name='liveCourses'),

    path('v2/challenges/', views.challenges, name='challenges'),
    path('v2/challenges/tags/', views.challengesTags, name='challengesTags'),
    path('v2/challenges/userstatus/', views.challengesUserStatus, name='challengesUserStatus'),

    path('v2/contests/', views.contests, name='contests'),
    path('v2/contests/<str:contestName>/rank/', views.contestRank, name='contestRank'),
    path('v2/contests/rank/', views.contestsRank, name='contestsRank'),

    path('v2/search/', views.search, name='search'),

    path('v2/services/qiniu/token/', views.getQiniuToken, name='qiniuToken')
]
