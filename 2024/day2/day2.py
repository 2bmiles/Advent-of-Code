import input

def parse_reports(reports):
    lines = reports.split("\n")
    report_list = []
    for line in lines:
        report = []
        report.extend(map(int, line.split(" ")))
        report_list.append(report)
    return report_list

def is_safe(report, level_to_remove = None):
    prev_level = report[0] + 1
    if level_to_remove is None:
        for level in report:
            if 3 < abs(level - prev_level) or level == prev_level:
                return False
            prev_level = level
        return (sorted(report) == report or sorted(report, reverse=True) == report)
    else:
        report = report[:level_to_remove] + report[level_to_remove + 1:]
        return is_safe(report)

def check_report(has_dampener = False):
    reports  = parse_reports(input.reports)
    safe_reports = []
    for report in reports:
        if is_safe(report):
            safe_reports.append(report)
        elif has_dampener:
            for i in range(len(report)):
                if is_safe(report, i):
                    safe_reports.append(report)
                    break
    return len(safe_reports)

print(check_report())