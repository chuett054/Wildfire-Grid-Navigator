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
    
<img width="1512" alt="Screenshot 2025-07-08 at 10 31 31 AM" src="https://github.com/user-attachments/assets/7b030244-fc08-4a41-8db2-7238bc4d1346" />


2.  **Central California** 

Substations meeting the population threshold positioned near the Carrizo Plain fire perimeter.

<img width="1512" alt="Screenshot 2025-07-08 at 10 32 05 AM" src="https://github.com/user-attachments/assets/f1941bab-dc7e-4d53-a2cd-1cde9ae48ddb" />


3. **Banning–Beaumont Detail**

I-10 corridor around Banning, CA: Substations within 50 miles of the nearby fire polygon, filtered for high-impact zones.

<img width="1512" alt="Screenshot 2025-07-08 at 10 32 30 AM" src="https://github.com/user-attachments/assets/d145cfe7-7755-4f8a-b13f-060b0c6b47d2" />


4. **Everglades & South Florida**
    
    Miami to Big Cypress: High-population substations (blue) located within a 50-mile buffer of Everglades wildfire perimeters (red).
    

<img width="1512" alt="Screenshot 2025-07-08 at 10 33 06 AM" src="https://github.com/user-attachments/assets/9b2d6dbf-dc74-41ff-a62d-e86fe1fe1241" />


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
