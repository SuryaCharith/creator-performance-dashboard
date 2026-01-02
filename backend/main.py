from fastapi import FastAPI
from database import get_connection

app = FastAPI(title="Creator Performance Dashboard API")

@app.on_event("startup")
def startup():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analytics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            platform TEXT NOT NULL,
            date TEXT NOT NULL,
            impressions INTEGER NOT NULL,
            likes INTEGER NOT NULL,
            comments INTEGER NOT NULL,
            followers_gained INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()

@app.get("/")
def health_check():
    return {"status": "API is running"}
@app.get("/analytics/raw")
def get_raw_data():
    conn = get_connection()
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM analytics").fetchall()
    conn.close()
    return [dict(row) for row in rows]

from fastapi import Query, HTTPException

@app.get("/analytics")
def get_analytics(platform: str | None = Query(default=None)):
    conn = get_connection()
    cursor = conn.cursor()

    if platform:
        if platform not in ["instagram", "youtube"]:
            raise HTTPException(
                status_code=400,
                detail="Invalid platform. Use 'instagram' or 'youtube'."
            )

        rows = cursor.execute(
            "SELECT * FROM analytics WHERE platform = ?",
            (platform,)
        ).fetchall()
    else:
        rows = cursor.execute(
            "SELECT * FROM analytics"
        ).fetchall()

    conn.close()
    return [dict(row) for row in rows]
@app.get("/analytics/summary")
def get_analytics_summary(platform: str | None = Query(default=None)):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT impressions, likes, comments, followers_gained FROM analytics"
    params = ()

    if platform:
        if platform not in ["instagram", "youtube"]:
            raise HTTPException(
                status_code=400,
                detail="Invalid platform. Use 'instagram' or 'youtube'."
            )
        query += " WHERE platform = ?"
        params = (platform,)

    rows = cursor.execute(query, params).fetchall()
    conn.close()

    total_impressions = sum(row["impressions"] for row in rows)
    total_engagement = sum(row["likes"] + row["comments"] for row in rows)
    total_followers = sum(row["followers_gained"] for row in rows)

    return {
        "total_impressions": total_impressions,
        "total_engagement": total_engagement,
        "total_followers_gained": total_followers
    }
@app.get("/analytics/metrics")
def get_metrics(platform: str | None = Query(default=None)):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT
            SUM(impressions) as total_impressions,
            SUM(likes + comments) as total_engagement,
            SUM(followers_gained) as total_followers_gained
        FROM analytics
    """

    params = ()

    if platform:
        if platform not in ["instagram", "youtube"]:
            raise HTTPException(
                status_code=400,
                detail="Invalid platform. Use 'instagram' or 'youtube'."
            )
        query += " WHERE platform = ?"
        params = (platform,)

    result = cursor.execute(query, params).fetchone()
    conn.close()

    return {
        "total_impressions": result["total_impressions"] or 0,
        "total_engagement": result["total_engagement"] or 0,
        "total_followers_gained": result["total_followers_gained"] or 0
    }
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

