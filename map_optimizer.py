import osmnx as ox
import networkx as nx
import folium

class MapOptimizer:
    """Advanced Routing Engine for Smart City Logistics (OSMnx 2.0 Compatible)."""
    
    def __init__(self, city_name="Eindhoven, Netherlands"):
        print(f"🌍 Loading real-world map data for: {city_name}...")
        # تنظیمات جدید برای ورژن های جدید
        ox.settings.use_cache = True
        ox.settings.log_console = False
        self.G = ox.graph_from_place(city_name, network_type="drive")
        print("✅ Graph network constructed successfully.")

    def find_optimal_route(self, point_a, point_b):
        """Calculates the optimal route and creates a custom Folium map."""
        print("🛣️ Calculating the mathematically shortest path...")
        
        # پیدا کردن نزدیک‌ترین گره‌ها (Nodes)
        orig_node = ox.distance.nearest_nodes(self.G, point_a[1], point_a[0])
        dest_node = ox.distance.nearest_nodes(self.G, point_b[1], point_b[0])
        
        # اجرای الگوریتم دایجسترا
        route = nx.shortest_path(self.G, orig_node, dest_node, weight="length")
        
        # استخراج مختصات مسیر برای رسم در Folium (متد جدید و دستی)
        route_coords = []
        for node in route:
            y, x = self.G.nodes[node]['y'], self.G.nodes[node]['x']
            route_coords.append((y, x))

        # ساخت نقشه با فولیکوم
        m = folium.Map(location=point_a, zoom_start=14, tiles="cartodbpositron")
        
        # رسم خط مسیر روی نقشه
        folium.PolyLine(route_coords, color="blue", weight=5, opacity=0.8).add_to(m)
        
        # علامت‌گذاری شروع و پایان
        folium.Marker(location=point_a, popup="Start (TU/e)", icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=point_b, popup="Destination", icon=folium.Icon(color='red')).add_to(m)

        file_name = "optimized_route.html"
        m.save(file_name)
        print(f"🏁 Success! Interactive map saved as '{file_name}'.")

if __name__ == "__main__":
    # مختصات اطراف دانشگاه آیندهوون هلند (TU/e)
    loc_a = (51.4486, 5.4907) 
    loc_b = (51.4416, 5.4777) 
    
    engine = MapOptimizer()
    engine.find_optimal_route(loc_a, loc_b)