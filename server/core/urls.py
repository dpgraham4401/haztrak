"""URLs for the core app."""

from django.urls import include, path

from .views import GetCurrentTrakUserView, LaunchExampleTaskView, TaskStatusView

task_patterns = (
    [
        path("/example", LaunchExampleTaskView.as_view(), name="example"),
        path("/<str:task_id>", TaskStatusView.as_view(), name="status"),
    ],
    "task",
)

app_name = "core"
urlpatterns = [
    path("task", include(task_patterns)),
    path(
        "user/",
        include(
            [
                path("current-user", GetCurrentTrakUserView.as_view(), name="current_user"),
            ]
        ),
    ),
]
