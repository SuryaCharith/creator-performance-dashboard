const BASE_URL = "http://127.0.0.1:8000";

export async function fetchAnalytics(platform = "") {
  let url = `${BASE_URL}/analytics`;
  if (platform) {
    url += `?platform=${platform}`;
  }

  const response = await fetch(url);
  if (!response.ok) {
    throw new Error("Failed to fetch analytics");
  }
  return response.json();
}

export async function fetchMetrics(platform = "") {
  let url = `${BASE_URL}/metrics`;
  if (platform) {
    url += `?platform=${platform}`;
  }

  const response = await fetch(url);
  if (!response.ok) {
    throw new Error("Failed to fetch metrics");
  }
  return response.json();
}
