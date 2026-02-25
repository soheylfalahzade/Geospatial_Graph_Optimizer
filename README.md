# 🌍 Geospatial Graph Optimizer
**Smart City Routing & Infrastructure Analytics Engine**

This project provides an advanced Python framework for retrieving, modeling, and optimizing real-world urban road networks. By leveraging geospatial data from OpenStreetMap, it constructs complex mathematical graphs and applies state-of-the-art pathfinding algorithms to find the most efficient routes in a city environment.

## 🏛️ Case Study: Eindhoven, Netherlands
As a strategic demonstration, this engine was tested on the city of **Eindhoven**. It specifically optimizes routes between the **Eindhoven University of Technology (TU/e)** and the city center, showcasing its relevance for **Intelligent Transportation Systems (ITS)**.

## 🚀 Key Technical Features
- **Geospatial Data Modeling:** Utilizes `OSMnx 2.0` to fetch and process real-world topological data from OpenStreetMap.
- **Graph Theory Integration:** Converts urban infrastructure into weighted directed graphs using `NetworkX`.
- **Advanced Pathfinding:** Implements Dijkstra's and A* algorithms for travel distance and time minimization.
- **Interactive Visualization:** Generates dynamic HTML maps with custom route overlays using `Folium`.

## 🛠️ Tech Stack
- **Language:** Python 3.13+
- **Data Retrieval:** OSMnx
- **Graph Engine:** NetworkX
- **Mapping:** Folium / Leaflet.js
- **Computation:** NumPy, Scikit-learn

## 📊 Result Visualization
The output is an interactive map (`optimized_route.html`) that provides a visual proof of the algorithmic optimization.
- **Green Marker:** Start Point (TU/e Campus)
- **Red Marker:** Destination (City Center)
- **Blue Line:** Mathematically Optimized Path

## 💼 Ph.D. Research Relevance
This project serves as a modular component for my Master's research on **Traffic Flow Optimization** and **Autonomous Vehicle Navigation**, proving the scalability of my algorithmic approaches to real European urban networks.

---
*Developed by Soheyl Falahzade - Specialized in AI-Driven Logistics & Computational Geometry.*
