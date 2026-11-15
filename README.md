# TerranceCloud Portfolio Website

Source code for [terrancecloud.com](https://terrancecloud.com), a personal cybersecurity and cloud security portfolio.

## Project Overview

This repository contains the source files for my personal portfolio website. The site serves as a central location to showcase my cybersecurity projects, cloud security work, technical development, and professional background.

## AWS Architecture

The website is hosted using AWS services:

- **Amazon S3:** Stores the website's static files.
- **Amazon CloudFront:** Distributes website content through a global content delivery network.
- **DNS:** Connects the custom domain to the hosted website.

## Repository Structure

| File | Purpose |
|---|---|
| `index.html` | Main portfolio website |
| `s3-lifecycle.json` | S3 lifecycle configuration for noncurrent object versions |
| `grc-python-lab/parse_config.py` | Python script that reads and evaluates simulated S3 configuration data |
| `grc-python-lab/s3_config.json` | Sample S3 security configuration used by the Python lab |
| `.gitignore` | Excludes local development files and sensitive configuration artifacts |

## Security and Configuration Practices

This project demonstrates practical exposure to:

- Static website hosting with AWS S3
- Content delivery with Amazon CloudFront
- Versioning and lifecycle management
- Basic Python-based configuration review
- Git version control and GitHub repository management
- Separation of simulated lab configurations from actual AWS resources

## Live Website

[https://terrancecloud.com](https://terrancecloud.com)

## Author

Terrance Scott

GitHub: [@tersco37](https://github.com/tersco37)