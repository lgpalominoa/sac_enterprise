import requests

class MotorVentas:
    def __init__(self):
        self.headers = {
            "User-Agent": "SAC-Enterprise-Pro/1.0 (contacto@empresa.com)"
        }

    def geocode(self, query):
        r = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": query, "countrycodes": "co", "format": "json"},
            headers=self.headers,
            timeout=10
        )
        data = r.json()
        if not data:
            return None
        return float(data[0]["lat"]), float(data[0]["lon"])

    def search_business(self, lat, lon, radius=1500):
        query = f"""
        [out:json];
        (
          node(around:{radius},{lat},{lon})["name"];
          way(around:{radius},{lat},{lon})["name"];
        );
        out center tags;
        """
        r = requests.get(
            "https://overpass-api.de/api/interpreter",
            params={"data": query},
            timeout=20
        )

        results = []
        
        for e in r.json().get("elements", []):
            tags = e.get("tags", {})
            results.append({
                "Nombre": tags.get("name"),
                "Dirección": tags.get("addr:full") or tags.get("addr:street"),
                "Teléfono": tags.get("contact:phone") or tags.get("phone"),
                "Website": tags.get("website"),
                "Facebook": tags.get("contact:facebook"),
                "Instagram": tags.get("contact:instagram"),
                "Lat": e.get("lat") or e.get("center", {}).get("lat"),
                "Lon": e.get("lon") or e.get("center", {}).get("lon")
            })
            
            results.sort(key=lambda x: x['Nombre'].lower())
            
        return results
