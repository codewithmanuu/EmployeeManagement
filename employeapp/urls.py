from django.urls import path
from .views import *
urlpatterns=[
    path('',index,name='index'),
    path('log/',user_login,name='login'),
    path('emp/',create_employee,name='employee'),
    path('empdis/',display_emp,name='emp'),
    path('editemp/<int:id>',edit_emp,name='editemp'),
    path('empdelete/<int:id>',empdelete,name='empdelete'),
    path('createdes/',create_designation,name='createdes'),
    path('createteam/',create_team,name='createteam'),
    path('leave/<int:id>',Approveleave,name='leave'),
    path('leavedis/',leavedis,name='leavedis'),
    path('editleave/<int:id>',editleave,name='editleave'),
    path('deleteleave/<int:id>',deleteleave,name='deleteleave'),
    path('listdesi/',listdesignation,name='listdesi'),
    path('listteam/',listteam,name='listteam'),
    path('graph/',salary_graph,name='graph'),
    path('logout/',logout,name='logout')
    # path('editdes/',empdesedit,name='editdes'),
    # path('editteam/',empteamedit,name='editteam')
]