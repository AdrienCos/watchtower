# Watchtower sample period (in s)
sample_period: float = 1

# Output CSV file path (relative to the executable, or absolute)
csv_path = "out.csv"

# Info about all files to sample
files: list = [
    {"path": "/sys/kernel/sentinel/nb_cpus",
        "name": "Number of CPUs cores",
        "unit": "N/A"},
    {"path": "/sys/kernel/sentinel/CPU_0",
        "name": "CPU 0 freq",
        "unit": "kHz"},
    {"path": "/sys/kernel/sentinel/CPU_1",
        "name": "CPU 1 freq",
        "unit": "kHz"},
    {"path": "/sys/kernel/sentinel/CPU_2",
        "name": "CPU 2 freq",
        "unit": "kHz"},
    {"path": "/sys/kernel/sentinel/CPU_3",
        "name": "CPU 3 freq",
        "unit": "kHz"},
    {"path": "/sys/kernel/sentinel/free_ram",
        "name": "Free RAM",
        "unit": "kB"},
    {"path": "/sys/kernel/sentinel/used_ram",
        "name": "Used RAM",
        "unit": "kB"},
    {"path": "/sys/kernel/sentinel/total_ram",
        "name": "Total RAM",
        "unit": "kB"},
    {"path": "/sys/kernel/sentinel/free_swap",
        "name": "Free Swap",
        "unit": "kB"},
    {"path": "/sys/kernel/sentinel/used_swap",
        "name": "Used Swap",
        "unit": "kB"},
    {"path": "/sys/kernel/sentinel/total_swap",
        "name": "Total Swap",
        "unit": "kB"},
]
