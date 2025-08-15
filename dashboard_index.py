"""
Dashboard Index Generator
Israel-Palestine Conflict Analysis
"""
import os

# Create visualizations directory if it doesn't exist
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

# Define the visualization information
visualizations = [
    {
        "id": "1_event_types_bar",
        "title": "Top 10 Event Types",
        "description": "Bar chart showing the most frequent event types in the conflict.",
        "business_concept": "Data Aggregation & Ranking Analysis"
    },
    {
        "id": "2_actors_pie",
        "title": "Main Actors Involved",
        "description": "Pie chart showing the proportional contribution of different actors.",
        "business_concept": "Proportional Analysis & Stakeholder Identification"
    },
    {
        "id": "3_events_over_time",
        "title": "Event Types Over Time",
        "description": "Area chart showing how the mix of event types evolved monthly.",
        "business_concept": "Time Series Analysis & Compositional Trends"
    },
    {
        "id": "4_fatalities_line",
        "title": "Fatalities Over Time",
        "description": "Line chart showing the trend of total fatalities over time.",
        "business_concept": "Trend Analysis & Impact Measurement"
    },
    {
        "id": "5_geographic_scatter",
        "title": "Geographic Distribution",
        "description": "Map visualization of events using latitude and longitude.",
        "business_concept": "Geospatial Analysis & Pattern Recognition"
    },
    {
        "id": "6_location_heatmap",
        "title": "Event Types by Location",
        "description": "Heatmap showing relationship between event types and locations.",
        "business_concept": "Correlation Analysis & Concentration Identification"
    }
]

# Generate the HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Israel-Palestine Conflict Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .header {
            background-color: #333366;
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .intro {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .card-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        .card {
            background-color: white;
            border-radius: 5px;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .card img {
            width: 100%;
            height: 180px;
            object-fit: cover;
            border-bottom: 1px solid #eee;
        }
        .card-content {
            padding: 15px;
        }
        .card h3 {
            margin-top: 0;
            color: #333366;
        }
        .card p {
            color: #666;
            font-size: 14px;
            margin-bottom: 10px;
        }
        .badge {
            display: inline-block;
            background-color: #e6e6fa;
            color: #333366;
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: bold;
        }
        .button {
            display: block;
            background-color: #333366;
            color: white;
            text-align: center;
            padding: 10px;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 10px;
        }
        .button:hover {
            background-color: #252550;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            color: #666;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Israel-Palestine Conflict Analysis Dashboard</h1>
        <p>A Business Analytics Approach to Understanding Conflict Patterns</p>
    </div>
    
    <div class="intro">
        <h2>About This Analysis</h2>
        <p>This dashboard presents a data-driven analysis of the Israel-Palestine conflict using business analytics techniques. Through six complementary visualizations, we explore different aspects of the conflict data, from event frequencies and actor involvement to geographical patterns and temporal trends.</p>
        <p>Each visualization is designed to answer specific questions about the conflict and is accompanied by explanations of the business analytics concepts used in the analysis.</p>
    </div>
    
    <div class="card-container">
"""

# Add cards for each visualization
for viz in visualizations:
    html_content += f"""
        <div class="card">
            <img src="{viz['id']}.png" alt="{viz['title']}">
            <div class="card-content">
                <h3>{viz['title']}</h3>
                <p>{viz['description']}</p>
                <div class="badge">{viz['business_concept']}</div>
                <a href="{viz['id']}.html" class="button">View Details</a>
            </div>
        </div>
    """

# Complete the HTML content
html_content += """
    </div>
    
    <div class="intro">
        <h2>How to Use This Dashboard</h2>
        <p>Click on any visualization card to view a detailed explanation and analysis of that specific chart. Each page includes:</p>
        <ul>
            <li>A high-resolution visualization</li>
            <li>Explanation of what the chart shows</li>
            <li>Business analytics concepts applied</li>
        </ul>
        <p>The visualizations are designed to be viewed in sequence, but you can explore them in any order based on your interests.</p>
    </div>
    
    <div class="footer">
        <p>Israel-Palestine Conflict Analysis Dashboard | Created for Business Analytics Presentation</p>
    </div>
</body>
</html>
"""

# Save the HTML file
with open('visualizations/index.html', 'w') as f:
    f.write(html_content)

print("Dashboard index created at visualizations/index.html")
print("To view the dashboard, open this file in a web browser after running all visualization scripts.")
print("Done!") 