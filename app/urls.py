from framework.app import MiniFramework
from app.views import home, user_profile


app = MiniFramework()

app.route('/')(home)
app.route('/user/<int:user_id>')(user_profile)