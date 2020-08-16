import plotly
import plotly.express as px
import os
import sqlite3
import shutil
import getpass
import pathlib
import pandas as pd
#comment
username = getpass.getuser()
print("Running the dashboard script")

con = sqlite3.connect("db.sqlite3")
c = con.cursor()
# Change this to your prefered queryresults = c.fetchall()
c.execute("select marks,student_id_id from courses_studentmarks")
results = c.fetchall()
# for r in results:
#  print(r)
#storing data for web app
db_df = pd.read_sql_query(
    "select marks,student_id_id from courses_studentmarks ", con)

pd.set_option('display.max_colwidth', 100)

fig = px.bar(db_df, x='marks', y='student_id_id',
             hover_data=['marks', 'student_id_id'], height=600)
plotly.offline.plot(fig, filename='bar_embed.html', auto_open=False)

con.close()
