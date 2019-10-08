class PeopleStatistics:
    def __init__(self, mean_year, men, fem, m_height, f_height):
        self.mean_year = mean_year
        self.men = men
        self.fem = fem
        self.m_height = m_height
        self.f_height = f_height
    def __str__(self):
        return str(self.__dict__)
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

def analyze(filename):
    stats = PeopleStatistics(0, 0, 0, 0, 0)
    sum_years = 0
    sum_m_height = 0
    sum_f_height = 0
    rows = 0
    source = open(filename)
    next(source)
    for line in source:
        rows += 1
        sum_years += int(line[:4])
        if line[5] == 'm':
            stats.men += 1
            sum_m_height += float(line[-5:])
        else:
            stats.fem += 1
            sum_f_height += float(line[-5:])
    stats.mean_year = int(sum_years / float(rows - 1))
    stats.m_height = round(sum_m_height / float(stats.men), 2)
    stats.f_height = round(sum_f_height / float(stats.fem), 2)
    return stats

CheckResult.check(analyze("code/A5/people.txt"), PeopleStatistics(1976, 494, 506, 1.79, 1.64))
