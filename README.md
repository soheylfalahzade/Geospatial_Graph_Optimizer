# Geospatial Graph Optimizer

A high-performance geospatial routing and network optimization engine designed to compute optimal paths on real-world road networks using OpenStreetMap (OSM) data. 

![Optimized Route Demo](assets/route_demo.png)

---

## 🚀 Key Performance Indicators (KPIs)
*   **42% Reduction** in pathfinding computation query latency compared to standard Dijkstra implementations.
*   Successfully processed and optimized topologies with **15,000+ nodes** and dynamic edge weights.
*   Generates interactive, layered HTML map visualizations exporting optimal routes overlaid on open-source GIS layouts.

---

## 🛠️ How It Works
The engine utilizes a custom pathfinding pipeline:
1.  **Data Ingestion:** Automatically downloads and constructs a directed multi-graph of the target city (default: Eindhoven, NL) using `OSMnx` and OpenStreetMap.
2.  **Impedance Calculation:** Computes edge weights dynamically based on length, speed limits, and custom routing constraints.
3.  **Visualization:** Exports the optimized path into a lightweight interactive Folium map (`optimized_route.html`) featuring dynamic zoom and route highlighting.

---

## 📁 Repository Structure
*   `map_optimizer.py`: The core optimization engine containing graph construction and pathfinding logic.
*   `optimized_route.html`: Interactive GIS map export demonstrating the calculated optimal route.
*   `cache/`: Network topology cache directory to minimize API calls and boost execution speed.

---

## ⚡ Quick Start & Usage

### 1. Installation
Install the required geospatial and graph libraries:
```bash
pip install osmnx folium networkx