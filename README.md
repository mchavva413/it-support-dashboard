# IT Support Monitoring Dashboard

## Overview

A full-stack IT support system designed to monitor system health, manage tickets, and simulate real-world IT support operations.

## Features

* System monitoring (CPU, Memory, Disk usage)
* Ticket creation and tracking
* REST API using FastAPI
* Backend deployed on Render
* Frontend dashboard for visualization

## Tech Stack

* Backend: FastAPI (Python)
* Frontend: React
* Monitoring: psutil
* Deployment: Render
* Version Control: Git & GitHub

## API Endpoints

* GET / → Check API status
* GET /system → System metrics (CPU, memory, disk)
* GET /tickets → Fetch tickets
* POST /ticket → Create ticket

## Example Response

```json
{
  "cpu": 35,
  "memory": 60,
  "disk": 70
}
```

## Live Demo

https://it-support-dashboard-vrcl.onrender.com

## Purpose

This project demonstrates:

* IT support system design
* Backend API development
* System monitoring and troubleshooting
* Real-world DevOps deployment

## Future Improvements

* Add authentication
* Improve UI dashboard
* Add alerting system
* Database integration
