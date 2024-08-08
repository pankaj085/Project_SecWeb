# SecWeb
SECURE LOGIN PAGE DEVELOPMENT

This project focuses on creating a secure login page designed to protect user credentials and manage sessions effectively. Use of best practices in authentication and session management, including encryption of sensitive data, prevention of common vulnerabilities such as SQL Injection and Cross-Site Scripting (XSS), and secure handling of session cookies. The project emphasizes the importance of cybersecurity measures in web development to safeguard against unauthorized access and data breaches.

The web application is built with Python Flask and leverages a range of technologies including SQLAlchemy, SQLite, Werkzeug's security features, Flask-WTF, HTML, SCSS, CSS, JavaScript, and Jinja2 templates. The application is designed with a strong focus on security, implementing measures to safeguard against SQL Injection and Cross-Site Scripting (XSS) attacks.

Flask's Jinja2 template engine is used to ensure automatic escaping of variables, preventing XSS by default. Additionally.

Flask-WTF is employed to enhance security by providing Cross-Site Request Forgery (CSRF) protection. It integrates a CSRF token into forms, thwarting potential attackers from forging malicious requests.

SQLAlchemy provides security against SQL injection attacks by using parameterized queries. This means that instead of directly embedding user input into SQL statements, SQLAlchemy uses placeholders and binds the values separately. This ensures that user input is treated as data and not executable code

Overall, the application combines robust security practices with modern web technologies to deliver a secure and efficient user experience.
