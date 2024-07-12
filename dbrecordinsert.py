# dbinsert.py

import sqlite3

def insert_day_records(username, day_records):
    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()
    
    # テーブルが存在しない場合は作成
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS day_records (
            username TEXT PRIMARY KEY,
            day1_record TEXT,
            day2_record TEXT,
            day3_record TEXT,
            day4_record TEXT,
            day5_record TEXT,
            day6_record TEXT,
            day7_record TEXT,
            day8_record TEXT,
            day9_record TEXT,
            day10_record TEXT,
            day11_record TEXT,
            day12_record TEXT,
            day13_record TEXT,
            day14_record TEXT,
            day15_record TEXT,
            day16_record TEXT,
            day17_record TEXT,
            day18_record TEXT,
            day19_record TEXT,
            day20_record TEXT,
            day21_record TEXT,
            day22_record TEXT,
            day23_record TEXT,
            day24_record TEXT,
            day25_record TEXT,
            day26_record TEXT,
            day27_record TEXT,
            day28_record TEXT,
            day29_record TEXT,
            day30_record TEXT,
            day31_record TEXT,
            day32_record TEXT
        )
    ''')
    
    # データを挿入または更新
    cursor.execute('''
        INSERT OR REPLACE INTO day_records (username, day1_record, day2_record, day3_record, day4_record, day5_record, day6_record, day7_record, day8_record, day9_record, day10_record, day11_record, day12_record, day13_record, day14_record, day15_record, day16_record, day17_record, day18_record, day19_record, day20_record, day21_record, day22_record, day23_record, day24_record, day25_record, day26_record, day27_record, day28_record, day29_record, day30_record, day31_record, day32_record)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', [username] + [day_records.get(f'day{i}_record') for i in range(1, 33)])

    conn.commit()
    conn.close()
