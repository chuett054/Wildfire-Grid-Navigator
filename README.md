# Wildlife-Grid-Navigator
Visualizes real-time NOAA wildfire perimeters vs. US power-grid assets and computer at-risk substations &amp; population; live demo integrates backend risk API with interactive map.

## Overview

The Wildfire Grid Navigator shows: 

- Active fire perimeters (in red)
- Electrical substations (as blue dots) filtered by minimum nearby population and proximity to nearby fires.

The demo runs on React + leaflet for the front end and FastAPI for the GeoJSON data. 

## Demo

1. **National Overview**
    
    Substations (blue) across the continental U.S., each within 50 miles of an active wildfire boundary (red) and serving ≥ 1,000 people.
    

![Screenshot 2025-07-08 at 10.31.31 AM.png](attachment:790d6347-8c01-4111-8ac8-d3b991ada519:Screenshot_2025-07-08_at_10.31.31_AM.png)

2.  **Central California** 

Substations meeting the population threshold positioned near the Carrizo Plain fire perimeter.

![Screenshot 2025-07-08 at 10.32.05 AM.png](attachment:f942168a-1596-40d8-88cd-6c79eb3b4a3c:Screenshot_2025-07-08_at_10.32.05_AM.png)

1. **Banning–Beaumont Detail**

I-10 corridor around Banning, CA: Substations within 50 miles of the nearby fire polygon, filtered for high-impact zones.

![Screenshot 2025-07-08 at 10.32.30 AM.png](attachment:96621aa1-2621-42d8-92b0-d223017fe1e0:Screenshot_2025-07-08_at_10.32.30_AM.png)

1. **Everglades & South Florida**
    
    Miami to Big Cypress: High-population substations (blue) located within a 50-mile buffer of Everglades wildfire perimeters (red).
    

![Screenshot 2025-07-08 at 10.33.06 AM.png](attachment:9342374a-36fa-4ca1-a25c-bbf06f353649:Screenshot_2025-07-08_at_10.33.06_AM.png)

## Key Features

1. **Fire Perimeters**
    - Loaded from NOAA GeoJSON and rendered with `react - leaflet’s <GeoJSON>` layer.
    - Semi-transparent red fill, not to be confused with government bases, filled with red and marked with slashes.
2. Substation Filtering
    1. Population: Only substations with a buffer population of ≥ 1000 are shown. 
    2. Proximity: Uses Turf.js to create a 50-mile buffer around each fire, then tests which substations fall inside the buffer. 
3. Performance
    1. Spatial buffers computed once on load. 
    2. filtering runs in `react.useMemo` to avoid recalculations on pan/zoom. 
4. Interactive popup (in progress)
    1. Clicking a substation or blue dot fetches risk data via fastAPI. 

## How to use

1. Clone repo and Install dependencies:

`git clone https://github.com/yourusername/wildlife-grid-navigator.git
cd wildlife-grid-navigator/frontend
npm install
npm start`

1. Backend (FastAPI): 

`cd ../backend
pip install -r requirements.txt
uvicorn main:app --reload`

1. Open local host. 

## End Note

I enjoyed building this project and defiantly see more like this coming in the future. I will continue to add features as time passes. Thanks for reading!
