from sqlite3 import Cursor
from turtle import home
from flask import Flask, redirect, url_for, request, session, flash, render_template
from flask_mysqldb import MySQL, MySQLdb
import json

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'data_grafik'
mysql = MySQL(app)


@app.route('/')
def index():
    # Trend Ticket & SLA
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('''SELECT MONTHNAME(STR_TO_DATE(`StartMeasurement`,'%Y-%m-%d')) as bulan, count(case when RESOLVE_TIME_CHECK = 'Meet' then 1 else null end) as total_within_sla, count(case when RESOLVE_TIME_CHECK = 'Not Meet' then 1 else null end) as total_out_of_sla, count(RESOLVE_TIME_CHECK) as trend_ticket, count(case OLA_RESP_TIME when 'Meet' then 1 else null end) as ola_resp_meet, count(case OLA_RESP_TIME when 'Not Meet' then 1 else null end) as ola_resp_notmeet, count(case OLA_CEM_TIME_CHECK when 'Meet' then 1 else null end) as ola_cem_meet, count(case OLA_CEM_TIME_CHECK when 'Not Meet' then 1 else null end) as ola_cem_notmeet, count(case OLA_NETWORK_CHECK when 'Meet' then 1 else null end) as ola_no_meet, count(case OLA_NETWORK_CHECK when 'Not Meet' then 1 else null end) as ola_no_notmeet, count(case OLA_CCM_CHECK when 'Meet' then 1 else null end) as ola_ccm_meet, count(case OLA_CCM_CHECK when 'Not Meet' then 1 else null end) as ola_ccm_notmeet from remedy_cc  GROUP BY MONTHNAME(STR_TO_DATE(`StartMeasurement`,'%Y-%m-%d')) ORDER BY MONTH(STR_TO_DATE(`StartMeasurement`,'%Y-%m-%d')) asc''')
    sql = cursor.fetchall()
    cursor.close()

    # Trend Ticket And SLA Region
    cursor2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor2.execute("""SELECT Region ,count(case RESOLVE_TIME_CHECK when 'Meet' then 1 else null end) as total_within_sla_region, count(case RESOLVE_TIME_CHECK when 'Not Meet' then 1 else null end) as total_out_of_sla_region, count(RESOLVE_TIME_CHECK) as trend_ticket_region from remedy_cc GROUP BY Region ORDER BY Area_2 asc, Region asc""")
    sqlr = cursor2.fetchall()
    cursor2.close()

    # Total Interaction
    cursor3 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor3.execute(
        """SELECT count(KIP_Level_2) as total_interaction FROM data_interaksi where KIP_Level_2 ='Jaringan, Internet, dan Telephony'""")
    sqld = cursor3.fetchall()
    cursor3.close()

    # Total Network
    cursor4 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor4.execute("""
    SELECT count(Incident_Number) as total FROM remedy_cc
    """)
    sqlt = cursor4.fetchall()
    cursor4.close()

    # Dianose, Analyze FTR, Ticket Resolve
    cursor5 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor5.execute('''SELECT count(case when FTR_2 = 'CEM' and Status = 'Cancelled' and Status = 'Close' then 1 else null end) as total_cem,count(case STATUS when 'Cancelled' then 1 else null end) as total_cancelled, count(case FTR_2 when 'L4' then 1 else null end) as total_excalated, count(case Status_New when 'Closed' then 1 else null end) as total_resolved, count(case Status_New when 'Open' then 1 else null end) as total_inprog, count(case when ResCat = 'Coverage' and Status != 'Cancelled' then 1 else null end) as total_coverage, count(case when  ResCat =  'Availability' and Status != 'Cancelled' then 1 else null end) as total_avail, count(case when ResCat =  'Quality' and Status != 'Cancelled' then 1 else null end) as total_quality, count(case when  ResCat =  'Non Network Resolution' and Status != 'Cancelled' then 1 else null end) as total_nonr, count(case  when ResCat =  'Capacity' and Status != 'Cancelled' then 1 else null end) as total_capacity, count(case when ResCat = 'Others' and Status != 'Cancelled' then 1 else null end) as total_others from remedy_cc''')
    sqlftr = cursor5.fetchall()
    cursor5.close()

    # Get Area
    cursor6 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor6.execute(
        """select distinct Area_2 from remedy_cc order by Area_2 asc""")
    getArea = cursor6.fetchall()
    cursor6.close()

    # Get Region
    cursor7 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor7.execute(
        """select distinct Region from remedy_cc order by Region asc""")
    getRegion = cursor7.fetchall()
    cursor7.close()

    # WHY 1
    cursor9 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor9.execute("""SELECT WHY_1, count(WHY_1) as total_why1, count(case when WHY_1 = 'Data Service' then 1 else null end) as data_service, count(case when WHY_1 = 'Signal' then 1 else null end) as total_signal,  count(case when WHY_1 = 'Voice Service' then 1 else null end) as voice_service from remedy_cc ORDER BY WHY_1""")
    sqlwhy1 = cursor9.fetchall()
    cursor9.close()

    cursor10 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor10.execute(
        """SELECT * FROM remedy_cc where RESOLVE_TIME_CHECK = 'Not Meet'""")
    sqlrecon = cursor10.fetchall()
    cursor10.close()

    # WHY 2
    cursor11 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor11.execute("""SELECT WHY_2, Val_WHY_2, count(WHY_2) as total_why2, count(case when WHY_2 = 'Call Blocked' then 1 else null end) as call_blocked, count(case when WHY_2 = 'Low Coverage / Signal not Strength' then 1 else null end) as low_coverage, count(case when WHY_2 = 'No Signal' then 1 else null end) as no_signal, count(case when WHY_2 = 'Slow Connection' then 1 else null end) as slow_connection, count(case when WHY_2 = 'Unable to Connect' then 1 else null end) as unable_connect, count(case when WHY_2 = 'Voice Quality' then 1 else null end) as voice_quality,count(case when WHY_2 = 'Other' then 1 else null end) as other, count(case when WHY_2 = 'Need Check' and Val_WHY_2 = 'Call Blocked' then 1 else null end) as val_call_blocked, count(case when WHY_2 = 'Need Check' and Val_WHY_2 = 'No Signal' then 1 else null end) as val_no_signal, count(case when WHY_2 = 'Need Check' and Val_WHY_2 = 'Slow Connection' then 1 else null end) as val_slow_connection, count(case when WHY_2 = 'Need Check' and Val_WHY_2 = 'Unable to Connect' then 1 else null end) as val_unable_connect, count(case when WHY_2 = 'Need Check' and Val_WHY_2 = 'Voice Quality' then 1 else null end) as val_voice_quality, count(case when WHY_2 = 'Need Check' and Val_WHY_2 = 'Low Coverage / Signal not Strength' then 1 else null end) as val_low_coverage, count(case when WHY_2 = 'Need Check' and Val_WHY_2 = 'Other' then 1 else null end) as val_other from remedy_cc order by WHY_2 asc""")
    sqlwhy2 = cursor11.fetchall()
    cursor11.close()

    return render_template('home.html', sql=sql, sqlr=sqlr, sqld=sqld, sqlt=sqlt, sqlftr=sqlftr, getArea=getArea, getRegion=getRegion, sqlwhy1=sqlwhy1, sqlrecon=sqlrecon, sqlwhy2=sqlwhy2)


if __name__ == '__main__':
    app.run(debug=True)
