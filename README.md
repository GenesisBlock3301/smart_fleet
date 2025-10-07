# smart_fleet
A fleet management system for logistics companies. One service handles vehicles and their telemetry, another handles driver assignments and trips. They communicate via gRPC, and Kafka streams are used for event-driven updates (e.g., vehicle location updates, trip completion). Each microservice has its own PostgreSQL database
