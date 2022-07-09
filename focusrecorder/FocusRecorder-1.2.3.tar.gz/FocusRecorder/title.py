# Measure an app usage this week

from FocusRecorder import utls

def run(title):
    sqlserver = utls.sqlServer()
    result = sqlserver.run(
        f'''
        with tmp1 as
        (
            select  strftime('%Y-%m-%d', datetime(time, 'unixepoch', 'localtime')) date,
                    title,
                    time - lag(time, 1, 0) over (order by time) time
            from    focus
        ), tmp2 as
        (
            select  date,
                    min(title) title,
                    round(sum(time)/60/60, 2)||'h' time
            from    tmp1
            where   title = '{title}' and time < 100
            group by    date
        )
        select * from tmp2
        '''
    )