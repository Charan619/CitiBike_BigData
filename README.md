# Bikenomics
The “Bikenomic - NYC Citibike Optimization” project explores using live and historical Citibike data to improve bike-sharing efficiency in New York City. By analyzing station usage patterns, the study identifies high and low utilization stations based on pickup and drop-off trends across different times and days. The goal is to balance demand by encouraging users to walk slightly farther to less busy stations through incentives like discounts and surge pricing. The project employs a machine learning model using PySpark to predict station demand, aiding in dynamic bike redistribution. The technology stack includes Flask for the web server, MongoDB for data storage, OpenMaps for visualization, and geopy for geolocation. The project demonstrates that strategic user redirection and dynamic pricing can reduce idle bike times and improve user experience. Future work involves enhancing the machine learning models, integrating real-time data streams via Kafka, and scaling the solution to other cities.

## Highlights
🚲 Utilization of live and historical Citibike data to optimize bike availability.

📊 Identification of high, normal, and low frequency stations using machine learning.

💡 Incentives proposed for users to use less congested stations (discounts and surge pricing).

⚙️ Use of PySpark ML for processing over 36 million data points and predicting station demand.

🌐 Integrated tech stack with Flask, MongoDB, geopy, and OpenMaps for a seamless user application.

📈 Data reveals ridership peaks in warmer months and high activity in Midtown Manhattan stations.

🔮 Future plans include real-time data integration and expansion to other urban areas.

## Key Insights

📉 Balancing Bike Distribution Reduces Idle Time:
The core challenge is uneven bike distribution, where some stations become empty or full, leading to idle bikes and frustrated users. By analyzing the ‘bike_availability_diff’ metric—measuring net bike inflow or outflow—the project identifies stations with persistent surpluses or shortages. This insight enables targeted interventions to redistribute bikes efficiently, improving overall system utilization.

🤖 Machine Learning Enables Predictive Optimization:
Deploying a Random Forest regression model on PySpark ML that ingests 36 million data points allows prediction of station demand based on day and time. This predictive capability helps anticipate demand surges and shortfalls, informing dynamic pricing and user incentives to alleviate congestion. The scale of data and complexity necessitate distributed computing, highlighting big data’s role in urban mobility solutions.

💰 Dynamic Pricing and Incentives Influence User Behavior:
Offering users a choice between high-frequency stations with surge pricing and low-frequency stations with discounts leverages economic incentives to guide user decisions. This approach encourages users to walk further to less busy stations, balancing supply and demand organically. The economic nudges align user convenience with system efficiency, a strategy that can be generalized to other shared mobility services.

🌍 Seasonal and Temporal Usage Patterns Inform Resource Allocation:
Ridership data reveals strong seasonal trends with higher usage in warmer months and lower in colder seasons, along with daily peaks in afternoon and evening hours. Weekend rides tend to be longer, indicating leisure use. Understanding these patterns allows for temporal adjustment of bike distribution and pricing strategies, optimizing resource allocation when and where demand is highest.

🗺️ Comprehensive Station Coverage Enables Flexible Routing:
With over 2200 stations spread uniformly across NYC and parts of New Jersey, users have multiple proximate options for pickups and drop-offs. This dense station network supports the feasibility of redirecting users to alternative stations without significant inconvenience, underpinning the incentive-based rerouting strategy.

💾 Scalability and Real-Time Data Processing Are Crucial:
The dataset size (over 4GB for 2023 alone) and the continuous influx of real-time trip data require horizontally scalable infrastructure. Technologies like Spark ML for distributed processing and proposed Kafka pipelines for streaming data ingestion are essential to maintain system responsiveness and provide timely, actionable insights for operational decisions.

📱 User-Centric Application Development Enhances Accessibility:
The integration of Flask, MongoDB, OpenMaps, and geopy creates a user-friendly platform that visualizes station availability and offers multiple bike station options based on real-time data. This practical implementation bridges complex backend analytics with front-end usability, promoting user engagement and satisfaction while supporting operational objectives.

### Read the Citibike_balancer_Report.pdf for more detailed analysis
