## Service on AWS

This project demonstrates the design, implementation, and deployment of a scalable and resilient conference room booking system on AWS. Leveraging a microservices architecture, this solution prioritizes security, performance, and cost optimization, showcasing a strong understanding of service discovery and internal DNS management.

## Architecture

The system is built on a multi-tiered architecture using various AWS services, with a focus on secure and efficient inter-service communication:

* **Users:** Access the application through a web browser.
* **Application Load Balancer (ALB):** Distributes traffic across application instances in a public subnet.
* **Elastic Container Service (ECS):** Hosts the application's microservices for scalability and resilience.
* **Elastic Container Registry (ECR):** Stores Docker images for automated deployments.
* **Relational Database Service (RDS):**  A managed database (likely PostgreSQL) for persistent data storage.
* **ElastiCache:**  Improves performance by caching frequently accessed data.
* **Service Discovery (AWS Cloud Map):** Enables dynamic service registration and discovery.
* **Internal DNS (Route53 Private Hosted Zone):** Provides internal DNS resolution within the VPC.
* **Networking:** Public and private subnets enhance security; security groups control traffic flow.


## Key Features & Benefits

* **Scalability:** ECS and ALB enable horizontal scaling.
* **Resilience:** Multiple ECS instances ensure fault tolerance.
* **Security:** Private subnets, security groups, and IAM roles enhance security.
* **Performance:** ElastiCache optimizes data access; efficient service discovery minimizes latency.
* **Cost Optimization:** Managed services reduce overhead.
* **Automated Deployment:** ECR and CI/CD pipelines streamline deployments.
* **Simplified Service Communication:** Cloud Map and Route53 facilitate robust inter-service communication.


## Key Learnings and Skills Gained

This project provided valuable hands-on experience in:

* **Microservice Architecture:** Designing, developing, and deploying microservices on AWS.
* **Service Discovery & DNS:** Implementing Cloud Map and Route53 for robust service communication.
* **Security Best Practices:** Applying security best practices for cloud-native applications.
* **Performance Optimization:** Implementing caching strategies and database optimization techniques.
* **Monitoring and Logging:** Integrating CloudWatch for comprehensive monitoring.
* **CI/CD Pipeline Implementation:** Automating the build and deployment process.
