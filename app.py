from flask import Flask, render_template

app = Flask(__name__)

# Product data (in-memory, replace with DB later)
_products_data = [
    {
        "id": 1,
        "name": "Product 1",
        "image": "/static/images/products/p1.png",
        "description": "Planter Mate Model No: JC-PM01-W-IT-US 1. 5V/2A  5W 2. Size: 110*110*(212-710)mm 3. Growth-Enhancing Full Spectrum 4. Build-in timer (16H on+8H off) 5. Include: 1.5M USB cable 6: US Adapter 5V/2A",
        "model_details": "1. Specifically designed for single – indoor planter use. 2. Lighting Feature: It is equipped with a DC 5V/5W white light, full spectrum LED grow light. This light is harmless to eyes and is more efficient and healthier for plant growth. 3. Adjustable Height: The telescoping legs can be adjusted according to the size of the planter. 4. Cost-effective",
        "price": 22.99
    },
    {
        "id": 2,
        "name": "Product 2",
        "image": "/static/images/products/p2.png",
        "description": "Planter Mate Model No:JC-PM03-SC-US 1: 5V/2A  5W 2. Size:110*110*(212-710)mm 3: Growth-Enhancing Full Spectrum 4: Three modes timer, 8H/12H/16H 5. Eco friendly PP, straw color 6. Include: 1.5M USB cable with in-line controller 7: US Adapter 5V/2A",
        "model_details": "1. Specifically designed for single – indoor planter use. 2. Lighting Feature: It is equipped with a DC 5V/5W white light, full spectrum LED grow light. This light is harmless to eyes and is more efficient and healthier for plant growth. 3. Adjustable Height: The telescoping legs can be adjusted according to the size of the planter. 4. Cost-effective 5. Eco-conscious design with sustainable materials – safe for your home and the planet.",
        "price": 29.99
    },
    {
        "id": 3,
        "name": "Product 3",
        "image": "/static/images/products/p3.png",
        "description": "Planter Mate Model No: JC-PM10-W-US 1: 5V/2A  7W 2. Size: 120*110*(195-718)mm 3. Growth-Enhancing Full Spectrum: Grow White 4000K + Red light 4. Three modes timer, 8H/12H/16H 5. Five levels dimming: 100%-80%-60%-40%-20% 6. Include: 1.7M USB cable with in-line controller 7: US Adapter 5V/2A",
        "model_details": "1. A perfect companion for Orchids, specifically designed to supplement light for their leaves, being low-key without spoiling the beauty of the flowers. 2. Effectively support photosynthesis, stimulates foliage growth, and encourages flowering in ornamental and edible plants. 3. The irradiation height can be adjusted. 4. Detachable Lamp Body, freight saved and easy Installation 5. Special design, also can be plant support stake",
        "price": 32.99
    },
    {
        "id": 4,
        "name": "Product 4",
        "image": "/static/images/products/p4.png",
        "description": "Planter Mate Model No: JC--PM21-W-US 1. 5V/2A  10W,PPE:1.2 2. Size:115.5*162.5*(310-750)mm 3. Growth-Enhancing Full Spectrum 4. Three modes timer, 8H/12H/16H 5. Five levels dimming: 100%-80%-60%-40%-20% 6. Unique design clip  2 ways: Plug into soil & Clip on pot 7. Include: 1.7M USB cable with in-line controller 8: US Adapter 5V2A",
        "model_details": "1. Specially designed for tropical plants such as Sansevieria trifasciata, Anthurium andraeanum, Monstera deliciosa. High power, high PPF. 2. Gear-timing mode and wire control, adjustable for different plants. 3. White-light full-spectrum LED grow light, harmless to eyes, efficient and healthy for plants. 4. Adjustable irradiation angle to meet plants' light needs. 5. Patented clip fits over 90% of indoor flower pots.",
        "price": 36.99
    },
    {
        "id": 5,
        "name": "Product 5",
        "image": "/static/images/products/p5.png",
        "description": "Grow Light BAR Model No:JC-BAR01-B-US 1: 24V/1A  22W,PPE:1.2 2. Size: 600*150*(225-623)mm 3:Seeding-Enhancing Full Spectrum 4: High PPFD design, Plus type 5: Three modes timer, 8H/12H/16H 6. Include: 24V/1A adapter with 1.8m cable and inline controller; Telescope rod *2 7. Multiple installation methods available",
        "model_details": "1. Versatile Application: Specifically designed for seedlings, microgreens and houseplants. 2. Lighting Feature: LED Gro-Bar, 22W, White light full spectrum LED grow light, no harm to eyes, healthier and more efficient. 3. Height Flexibility: Telescoping legs can be adjusted according to the growth of plants to meet different stage requirements. 4. Perfect Compatibility: Fits standard 10*20 seedling trays.",
        "price": 99.99
    },
    {
        "id": 6,
        "name": "Product 6",
        "image": "/static/images/products/p6.png",
        "description": "LED Grow Strip 2M kit Model No.: JC-SP01-US 1: 24V/1A, 24W 2. Size: 2000*12*5mm 3: Growth-Enhancing Full Spectrum 4: IP65 5: Three modes timer, 8H/12H/16H 6: Five levels dimming: 100%-80%-60%-40%-20% 7: Include: 24V/1A adapter with 1.8m cable, 6*clip, 12*screw, in-line controller",
        "model_details": "1. Flexible Strip Light, can be installed to any place you need. 2. In-line switch: 5 levels brightness dimming, 4 timer modes. 3. IP65 waterproof level, and can be used in damp location.",
        "price": 59.99
    },
    {
        "id": 7,
        "name": "Product 7",
        "image": "/static/images/products/p7.png",
        "description": "Floor Grow light Model No:JC-FLR01-B-US 1: 24V/1A, 22W,PPE:1.2 2. Size: 300x300x1645mm 3: Growth-Enhancing Full Spectrum 4: IP20 5: Three modes timer, 8H/12H/16H 6: Five levels dimming: 100%-80%-60%-40%-20% 7: Include: 24V/1A adapter with 1.8m cable, in-line controller",
        "model_details": "1. LED provides abundant light to plants. 2. Halo-shaped head pivots and tilts. 3. Integrated in-line timer and dimmer. 4. Tailored for lighting indoor large plants gracefully. 5. The direction of light can be adjusted as plants require. 6. With a classic design, it composes a charming home landscape along with large plants. 7. White light full spectrum LED grow light, no harm to eyes, healthier and more efficient.",
        "price": 139.99
    },
    {
        "id": 8,
        "name": "Product 8",
        "image": "/static/images/products/p8.png",
        "description": "Mini Garden Model No:JC-MG06-US-PP05*3 1: 24V/1A 14W 2. Size:324*174*(66-346)mm 3. Growth-Enhancing Full Spectrum 4: Three modes timer: 8H/12H/16H 5. Five levels dimming: 100%-80%-60%-40%-20% 6: Include: 24V/1A adapter with 1.8m cable and in-line controller 7: 3.5 inch Pot *3",
        "model_details": "1. Designed to combine indoor planting with home decor. 2. Growth-Enhancing Full Spectrum. 3. Foldable design for space-saving. 4. Friendly material: nature bamboo.",
        "price": 129.99
    },
    {
        "id": 9,
        "name": "Product 9",
        "image": "/static/images/products/p9.png",
        "description": "Sunlit Pot Model No: SP01(PM01-PP01) 1. 5V/2A  5W,PPE:1.2 2. Size: 110*110*(212-710)mm 3. Growth-Enhancing Full Spectrum 4. Build-in timer (16H on+8H off) 5. Include: US Adapter 5V2A with 1.5M USB cable 6: Unique Patent Design Pot: Self-watering and breathable, providing consistent moisture and airflow",
        "model_details": "1. Water Smart Pot and 5W Grow light: an ideal match. Together, they build an optimal micro-environment. 2. Light gives precise rays as plants require. 3. Pot has self-watering and breathable features, securing stable water and air. 4. Functional inline controller: Five levels brightness dimming, 20%/40%/60%/80%/100%. Four timer modes, Built-in Automatic Timer System.",
        "price": 52.99
    },
    {
        "id": 10,
        "name": "Product 10",
        "image": "/static/images/products/p10.png",
        "description": "Sunlit Pot Model No: SP02(PM21-PP01) 1. 5V/2A  5W,PPE:1.2 2. Size: 110*110*(212-710)mm 3. Growth-Enhancing Full Spectrum 4. Build-in timer (16H on+8H off) 5. Include: US Adapter 5V2A with 1.5M USB cable 6: Unique Patent Design Pot: Self-watering and breathable, providing consistent moisture and airflow",
        "model_details": "1. Water Smart Pot and 7W Grow light: an ideal match. Together, they build an optimal micro-environment. 2. Light gives precise rays as plants require. 3. Pot has self-watering and breathable features, securing stable water and air. 4. Functional inline controller: Five levels brightness dimming, 20%/40%/60%/80%/100%. Four timer modes, Built-in Automatic Timer System.",
        "price": 56.99
    },
    {
        "id": 11,
        "name": "Product 11",
        "image": "/static/images/products/p11.png",
        "description": "Sunlit Pot Model No: SP10(PM10-PP10) 1. 5V/2A  5W,PPE:1.2 2. Size: 110*110*(212-710)mm 3. Growth-Enhancing Full Spectrum 4. Build-in timer (16H on+8H off) 5. Off-white PP material 6. Include: US Adapter 5V2A with 1.5M USB cable 7: Unique Patent Design Pot: Self-watering and breathable, providing consistent moisture and airflow",
        "model_details": "1. Perfect for beautiful blooming. 2. Pot (Designed for orchids): controls humidity, has good permeability, enhances root vitality. 3. Grow Light (Designed for orchids): lights up leaves, safeguards the flower's beauty, guarantees photosynthesis. 4. Grow Light with adjustable height, fits different growth stages, prolongs the flowering time. 5. Functional inline controller: Five levels brightness dimming, 20%/40%/60%/80%/100%. Four timer modes, Built-in Automatic Timer System.",
        "price": 52.99
    },
    {
        "id": 12,
        "name": "Product 12",
        "image": "/static/images/products/p12.png",
        "description": "2 in 1 Smart Grow Box Seeding Sart + Micro-green box Model No: JC-SGB10-US 1. DC5V/2A, 8W 2. Size: 185*153*164mm 3. Seeding Enhancing full spectrum: 6500K 4: 3 modes timer: 8H/12H/16H 5: Include: Seeding sart box*1; 12 cell tray*1; Grow pad*2; 8W LED Bar*1; 1.5m Type-C to USB cable 6: US Adapter 5V2A",
        "model_details": "1. Seeding enhancing full spectrum, designed for both microgreens cultivation and seed starting. 2. Easy to Use: Simple setup and operation for effortless seeding. 3. High Germination Rate: Optimized design promotes faster and healthier seedling growth. 4. Heat & Humidity Retention: Maintains ideal conditions for seeding. 5. Ventilation Design: Promotes air circulation for healthier plant development. 6. Supports almost all types of microgreen seeds and allows harvesting in as little as 5 days. 7. Suitable for many different propagation methods, for example seed germination, seedling nurturing, succulent cuttings.",
        "price": 52.99
    }
]

# Data access functions
def get_all_products():
    return _products_data

def get_product_by_id(product_id):
    return next((p for p in _products_data if p["id"] == product_id), None)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/products")
def products():
    return render_template("products.html", products=get_all_products())

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = get_product_by_id(product_id)
    if product:
        return render_template("product_detail.html", product=product)
    return "Product not found", 404

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

