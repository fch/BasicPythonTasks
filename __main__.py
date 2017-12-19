from lib import check as CheckResult

exec(open("./code/A2/format_me.py").read(), globals())
exec(open("./code/A2/overtime.py").read(), globals())
exec(open("./code/A2/truncate.py").read(), globals())

exec(open("./code/A3/sail.py").read(), globals())
exec(open("./code/A3/tempomat_control.py").read(), globals())

exec(open("./code/A4/text_statistics.py").read(), globals())
exec(open("./code/A4/animals.py").read(), globals())
exec(open("./code/A4/debug_me.py").read(), globals())

exec(open("./code/A5/people.py").read(), globals())
exec(open("./code/A5/fibonacci.py").read(), globals())

CheckResult.finish()
