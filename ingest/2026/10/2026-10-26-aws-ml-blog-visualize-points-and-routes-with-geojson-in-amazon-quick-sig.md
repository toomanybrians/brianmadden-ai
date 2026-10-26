---
title: Visualize points and routes with GeoJSON in Amazon Quick Sight layer maps
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/visualize-points-and-routes-with-geojson-in-amazon-quick-sight-layer-maps/
author: Amit Makashir
date_published: '2026-10-23'
date_captured: '2026-10-26'
ingest_method: feed
model: claude-sonnet-5
---

# Visualize points and routes with GeoJSON in Amazon Quick Sight layer maps

## Insights

- Amazon Quick Sight's layer maps now support Point and LineString GeoJSON geometries (previously only Polygon/custom shapes), letting users plot individual locations and routes alongside territory boundaries in the same visual framework.
- The feature requires a GeoJSON file (max 100MB) joined to a Quick Sight dataset via a shared key field; the join is value-based, not name-based, giving flexibility in field naming.
- Layer map points are explicitly positioned as a second, more rigid point-mapping option versus Quick Sight's existing native point map: layer maps lack geocoding and auto-refresh, requiring manual GeoJSON updates, but offer precise viewport locking (disabling pan/zoom) and uniform styling — suited to fixed/curated locations rather than frequently changing data.
- Multiple geometry types can be composited by stacking separate layer map visuals (free-form layout, matched bounds, hidden base layers) — up to five layer maps per sheet — enabling combined views like points-on-routes or points-within-polygons.
- Geometry updates are decoupled from standard data refresh (SPICE/Direct Query); changing map shapes requires replacing the GeoJSON file and republishing, with programmatic updates possible via S3 + Quick Sight APIs (UpdateDashboard, UpdateDashboardPublishedVersion) for automated/dynamic use cases.
- Viewport control (exact bounds, pan/zoom lock) is only configurable via the dashboard definition JSON/API, not exposed in the console UI — a notable gap between no-code and API-driven configuration.
