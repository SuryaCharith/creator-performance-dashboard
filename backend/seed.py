from database import get_connection

sample_data = [
    ("instagram", "2026-01-01", 1200, 140, 20, 15),
    ("instagram", "2026-01-02", 1800, 210, 35, 22),
    ("instagram", "2026-01-03", 1600, 190, 28, 18),
    ("youtube", "2026-01-01", 3000, 400, 60, 45),
    ("youtube", "2026-01-02", 2800, 370, 55, 38),
    ("youtube", "2026-01-03", 3500, 520, 80, 60)
]

def seed():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executemany("""
        INSERT INTO analytics (
            platform, date, impressions, likes, comments, followers_gained
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, sample_data)

    conn.commit()
    conn.close()
    print("✅ Sample analytics data inserted successfully")

if __name__ == "__main__":
    seed()
